# Multilingual Translator

A modular Python project for speech-to-text, translation, and text-to-speech workflows. 

## Structure
- `src/`: Main source code (STT, translation, TTS modules)
- `data/`: Datasets and audio files
- `models/`: Model checkpoints
- `tests/`: Unit and integration tests

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python src/app.py`

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

## Audio Transcription Setup & Usage

### 1. Environment Setup
- Install [Anaconda](https://www.anaconda.com/products/distribution) and create a new environment:
  ```sh
  conda create -n translator python=3.10
  conda activate translator
  ```
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```
- Install FFmpeg (required for audio processing):
  ```sh
  conda install -c conda-forge ffmpeg
  ```

### 2. Preparing Audio Files
- Place your sample audio files in the `samples/` folder (e.g., `samples/0704.mp3`).
- Supported formats: `.wav`, `.mp3`, `.m4a`, `.flac`, `.aac`, `.ogg`.
- Ensure the file extension matches the actual audio format.

### 3. Recording Audio
- Use the provided script to record audio from your microphone:
  ```python
  from src.stt.record_audio import record_audio
  record_audio(filename="samples/recorded_audio.wav", duration=5)
  ```
- This will save a new recording to the `samples/` folder.

### 4. Transcribing Audio
- Update `src/stt/whisper_stt.py` to point to your desired audio file:
  ```python
  sample_audio = "samples/0704.mp3"
  ```
- Run the transcription script:
  ```sh
  python src/stt/whisper_stt.py
  ```
- The script will print the detected language and transcription.

### 5. Troubleshooting
- If you see a "Permission denied" error, ensure the audio file is not open in another program and that you have read permissions.
- If using OneDrive, try moving your audio file to a local folder outside OneDrive.
- If you get a "file format not supported" warning, check that FFmpeg is installed and the file extension matches the actual format.

---

**Tip:**  
Keep your audio files organized in the `samples/` or `data/raw/` folders for easy access and reproducibility.
