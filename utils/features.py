import numpy as np
from scipy.signal import spectrogram

def rms_energy(y, frame=2048):
    # root mean square per frame
    return np.sqrt(np.mean(y.reshape(-1, frame)**2, axis=1))

def spectral_centroid(y, sr, frame=2048):
    # rough estimate of energy-weighted mean frequency
    f, t, Sxx = spectrogram(y, sr, nperseg=frame)
    centroid = np.sum(f * Sxx, axis=0) / np.sum(Sxx, axis=0)
    return np.nan_to_num(centroid)