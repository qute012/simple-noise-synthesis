import numpy as np

from transform import NoiseSynthesis

if __name__=='__main__':
    transform = NoiseSynthesis()
    transform(np.sin(np.arange(80)))
    transform(np.sin(np.arange(20800)))
    print("tested successfully")