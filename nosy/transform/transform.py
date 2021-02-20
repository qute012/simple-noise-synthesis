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
        
        print(noise)
        sig_len = len(sig)
        noise_len = len(noise)
        
        start_time = 0.0
        interval = abs(sig_len-noise_len)
        if sig_len>noise_len:
            np.random.uniform(0,interval)
        #elif noise_len>sig_len:
        
        
    def _process_noise_dataset(self, path='../noise_dataset'):
        noise_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                noise_files.append(os.path.join(root,file))
                
        noise_data = []
        for file in noise_files:
            noise_data.append(self._load_audio(file))
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
        
    def _rms(self, sig):
    """Calculate root mean square"""
        return np.sqrt(np.mean(np.square(sig)), ais=-1)

    def _rate(self, sig, snr):
        """Calculate noise rms rate"""
        snr = snr/self.max_snr
        rate = sig / (10**snr)
        return rate

    def _norm(self, sig, sr=16000):
        return sig/((1<<(sr//1000-1))-1)
        
    def _pre_emphasis(signal_batch, emph_coeff=0.95):
        return signal.lfilter([1, -emph_coeff], [1], signal_batch)

    def _de_emphasis(signal_batch, emph_coeff=0.95):
        return signal.lfilter([1], [1, -emph_coeff], signal_batch)