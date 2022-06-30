import IPython.display as ipd
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa as lib
import scipy.signal as signal
from scipy.signal import butter,filtfilt
import scipy.signal as sig
from scipy.io.wavfile import write
from datetime import datetime


def plot_magnitude_spectrum_new(signal, sr, filename, f_ratio=1):
    X = np.fft.fft(signal)
    X_mag = np.absolute(X)
    title='FFT'
    plt.figure(figsize=(18, 5))
    
    f = np.linspace(0, sr, len(X_mag))
    f_bins = int(len(X_mag)*f_ratio)  
    
    plt.plot(f[:f_bins], X_mag[:f_bins])
    plt.xlabel('Frequency (Hz)')
    plt.title(title)
    plt.savefig('fft_graphs/'+filename +'.png')
    return 'fft_graphs/'+filename +'.png'