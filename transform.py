import numpy as np
import os

from utils import load_audio

class NoiseSynthesis(object):
    def __init__(self, sr=16000, backend='torch'):
        self.sr = sr
        self.method = method
        self.backend = backend
        self.noise_dataset = self._process_noise_dataset()
        
    def __call__(self, sig):
        
    def _process_noise_dataset(self, path='noise_dataset'):
        