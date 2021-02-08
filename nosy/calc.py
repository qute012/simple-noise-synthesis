import numpy as np
from enum import Enum

class Constant(Enum):
    MAX_SNR = 20

def _rms(sig):
    """Calculate root mean square"""
    return np.sqrt(np.mean(np.square(sig)), ais=-1)

def _rate(sig, snr):
    """Calculate noise rms rate"""
    snr = snr/Constant.MAX_SNR
    rate = sig / (10**snr)
    return rate

def _norm(sig, sr=16000):
    max_bit = (1<<(sr//1000-1))-1
    if sig.max(axis=0)>max_bit:
        return sig*(max_bit/sig.max(axis=0))
    else:
        return sig