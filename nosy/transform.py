import numpy as np
import os

class NoiseSynthesis(object):
    def __init__(self, sr=16000, method='static', backend='torch'):
        self.sr = sr
        self.method = method
        self.backend = backend
        self.noises = self._process_noise_dataset()
        
    def __call__(self, sig):
        
    def _process_noise_dataset(self, path='noise_dataset'):
        