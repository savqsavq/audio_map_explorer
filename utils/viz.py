import matplotlib.pyplot as plt
import numpy as np

def plot_amplitude_map(norm_rms, dur):
    x = np.linspace(0, dur, len(norm_rms))
    plt.figure(figsize=(8,3))
    plt.plot(x, norm_rms, color="#b64dff", lw=1)
    plt.title("Amplitude Envelope")
    plt.xlabel("seconds")
    plt.ylabel("normalized rms")
    plt.tight_layout()
    plt.savefig("amplitude_map.png")
    plt.close()

def plot_frequency_map(norm_spec, dur):
    x = np.linspace(0, dur, len(norm_spec))
    plt.figure(figsize=(8,3))
    plt.plot(x, norm_spec, color="#ffb64d", lw=1)
    plt.title("Spectral Centroid")
    plt.xlabel("seconds")
    plt.ylabel("normalized freq weight")
    plt.tight_layout()
    plt.savefig("frequency_map.png")
    plt.close()