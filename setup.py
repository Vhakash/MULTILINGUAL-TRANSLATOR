from setuptools import setup, find_packages

setup(
    name='multilingual-translator',
    version='0.1.0',
    description='A modular multilingual speech translation toolkit',
    author='Your Name',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'openai-whisper',
        'transformers',
        'sentencepiece',
        'torch',
        'gtts',
        'coqui-tts',
        'soundfile',
        'langdetect',
        'numpy',
        'scipy',
    ],
)
