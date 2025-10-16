import numpy as np
import matplotlib.pyplot as plt
import wave, contextlib, json
from utils.loader import load_audio
from utils.features import rms_energy, spectral_centroid
from utils.viz import plot_amplitude_map, plot_frequency_map
from utils.export import save_feature_json

def analyze_audio(path):
    """Main feature extraction and visualization pipeline."""

    y, sr, duration = load_audio(path)

    # Compute features
    rms = rms_energy(y)
    spec = spectral_centroid(y, sr)

    # Normalize 
    norm_rms = rms / np.max(rms)
    norm_spec = spec / np.max(spec)

    # summary
    results = {
        "duration_sec": round(duration, 2),
        "sample_rate": sr,
        "rms_mean": float(np.mean(norm_rms)),
        "spec_mean": float(np.mean(norm_spec))
    }

    save_feature_json(results, "audio_features.json")

    # Visualize amplitude and frequency structure
    plot_amplitude_map(norm_rms, duration)
    plot_frequency_map(norm_spec, duration)

    print("Analysis complete.")
    return results


def compare_clips(path_a, path_b):
    """Compare two audio clips by mean feature similarity."""
    a = analyze_audio(path_a)
    b = analyze_audio(path_b)

    diff = abs(a["rms_mean"] - b["rms_mean"]) + abs(a["spec_mean"] - b["spec_mean"])
    score = max(0, 1 - diff)
    print(f"Similarity score: {score:.2f}")
    return score


def quick_visual_summary(path):
    """Lightweight plot for amplitude overview."""
    with contextlib.closing(wave.open(path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        dur = frames / float(rate)
        signal = np.frombuffer(f.readframes(frames), dtype=np.int16)
    amp = np.abs(signal[::2000])
    x = np.linspace(0, dur, len(amp))
    plt.plot(x, amp / np.max(amp))
    plt.title("Amplitude Overview")
    plt.xlabel("Seconds")
    plt.ylabel("Normalized Amplitude")
    plt.show()


def export_summary(results, out_path="summary.txt"):
    """Write key metrics to a text summary file."""
    with open(out_path, "w") as f:
        for k, v in results.items():
            f.write(f"{k}: {v}\n")
    print(f"Summary written to {out_path}")


if __name__ == "__main__":
    audio_file = "sample.wav"
    features = analyze_audio(audio_file)
    export_summary(features)
