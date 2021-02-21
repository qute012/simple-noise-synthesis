import os
import random
import numpy as np
import soundfile as sf
from scipy import signal

class NoiseSynthesis(object):
    def __init__(self, max_snr=20):
        self.max_snr = max_snr
        self.noise_dataset = self._process_noise_dataset()
        
    def __call__(self, sig, snr=10, sr=16000):
        noise = random.choice(self.noise_dataset)
        
        clean, noise = self._cut_noise(sig, noise)
        synthesized = self._synthesis(clean, noise, snr)
        return clean, synthesized
        
    def _process_noise_dataset(self, path='./noise_dataset'):
        noise_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                noise_files.append(os.path.join(root,file))
                
        noise_data = []
        for file in noise_files:
            noise_data.append(self._load_audio(file)[0])
        return noise_data
        
    def _load_audio(self, path, sr=16000):
        ext = path.split('.')[-1]

        if ext=='pcm':
            try:
                sig, sr = np.memmap(path, dtype='h', mode='r').astype('float32'), sr
            except:
                with open (path, 'rb') as f:
                    buf = f.read()
                    if len(buf)%2==1:
                        buf = buf[:-1]
                sig, sr = np.frombuffer(buf, dtype='int16'), sr
        else:
            sig, sr = sf.read(path, sr)
        return sig, sr
    
    def _cut_noise(self, clean, noise):
        clean_len = len(clean)
        noise_len = len(noise)
        
        if clean_len>noise_len:
            r = round(clean_len/noise_len)
            noise = np.repeat(noise, r+1)
            noise_len = len(noise)
            
        if noise_len>clean_len:
            t = np.random.randint(0,noise_len-clean_len)
            noise = noise[t:t+clean_len]
        return clean, noise
    
    def _rms(self, sig):
        """Calculate root mean square"""
        return np.sqrt(np.mean(np.square(sig), axis=-1))

    def _rate(self, sig, snr):
        """Calculate noise rms rate"""
        snr = snr/self.max_snr
        rate = sig / (10**snr)
        return rate

    def _norm(self, sig, sr=16000):
        return sig/((1<<(sr//1000-1))-1)
    
    def _synthesis(self, clean, noise, snr):
        clean_rms = self._rms(clean)
        noise_rms = self._rms(noise)
        amp = self._rate(clean_rms, snr)/noise_rms
        return clean+noise*amp
        
        
    def _pre_emphasis(signal_batch, emph_coeff=0.95):
        return signal.lfilter([1, -emph_coeff], [1], signal_batch)

    def _de_emphasis(signal_batch, emph_coeff=0.95):
        return signal.lfilter([1], [1, -emph_coeff], signal_batch)