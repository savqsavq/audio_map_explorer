import numpy as np, wave, contextlib

def load_audio(path):
    # pulls amplitude values + sample rate
    with contextlib.closing(wave.open(path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        signal = np.frombuffer(f.readframes(frames), dtype=np.int16)
    return signal, rate, duration