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



def butter_lowpass_filter(data, cutoff, fs, order,nq):
    
    normal_cutoff = cutoff / nq
    # Get the filter coefficients 
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y
