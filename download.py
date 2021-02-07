import wget
import argparse
import os
import math
from glob import glob

def log(current, total, width=100):
    unit = 1000000
    avail_dots = width-2
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    percent_bar = '[' + '■'*shaded_dots + ' '*(avail_dots-shaded_dots) + ']'
    progress = "%d%% %s [%d mb/ %d mb]" % (current / total * 100, percent_bar, current/unit, total/unit)
    return progress

def download(path):
    os.makedirs(path, exist_ok=True)
    url_list = [
        'https://zenodo.org/record/1227121/files/DKITCHEN_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/DLIVING_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/DWASHING_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/NPARK_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/OHALLWAY_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/OMEETING_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/OOFFICE_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/PCAFETER_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/PRESTO_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/PSTATION_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/TBUS_16k.zip?download=1',
        'https://zenodo.org/record/1227121/files/TCAR_16k.zip?download=1',
    ]
    print('total noise dataset number: {}'.format(len(url_list)))
    for url in url_list:
        wget.download(url, out=path, bar=log)
    tmps = glob('./*.tmp')
    for tmp in tmps:
        os.remove(tmp)
        
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='End-to-End Speech Recognition Training')
    parser.add_argument('--path', default='./noise_dataset', type=str, help="destination to download noise dataset")
    args = parser.parse_args()
    
    download(args.path)