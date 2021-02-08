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