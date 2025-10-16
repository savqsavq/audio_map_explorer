import numpy as np
import matplotlib.pyplot as plt
import wave, contextlib

def extract_features(path):
    with contextlib.closing(wave.open(path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        dur = frames / float(rate)
        signal = np.frombuffer(f.readframes(frames), dtype=np.int16)
    amp = np.abs(signal[::2000])  # downsample amplitude
    norm = amp / max(amp)
    return norm, dur

def visualize(path):
    data, dur = extract_features(path)
    x = np.linspace(0, dur, len(data))
    colors = plt.cm.magma(data)
    plt.scatter(x, data, c=colors, s=2)
    plt.title("audio structure visualization")
    plt.xlabel("seconds")
    plt.ylabel("normalized amplitude")
    plt.savefig("audio_structure.png")

if __name__ == "__main__":
    visualize("sample.wav")