# Simple Noise Synthesis
This is noise synthesis tool. It is automatically downloaded noise in diverse environments  in [DEMAND] datasets. It provided various noise environments in contrast to limited the AURORA-2 corpus and the CHiME background noise data. You can use for learning in a Pytorch simply as transforms.

## Requirements
You can download belows using pip.
- wget
- librosa
- numpy

```
pip install wget librosa numpy
```

When training
- Pytorch

You can install [pytorch] depending on environments.

## Usage
Default path is automatically created as noise_dataset directory.
```
python download.py [--path]
```

## Aspect
You can check each noise detailed aspect in [paper].

[DEMAND]: https://zenodo.org/record/1227121#.YBu28egzbZR
[pytorch]: https://pytorch.org/
[paper]: https://asa.scitation.org/doi/pdf/10.1121/1.4799597
