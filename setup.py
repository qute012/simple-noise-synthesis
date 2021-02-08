from setuptools import setup, find_packages

setup(
    name='nosy',
    version='latest',
    description='Simple noise synthesis tool.',
    author='DeokJin Seo',
    author_email='406023@naver.com',
    url='https://github.com/qute012/simple-noise-synthesis',
    packages = find_packages(exclude = ['.ipynb', 'noise_dataset']),
    install_requires=[
        'torch,
        'torchaudio,
        'wget',
        'numpy',
        'zipfile',
        'librosa>=0.7.0'
    ],
    python_requires='>=3.6'
)
