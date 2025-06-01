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

## Audio Enhancement

- The project now uses automatic noise reduction to improve transcription quality.
- Before transcription, all audio (recorded or pre-recorded) is processed to reduce background noise using the `noisereduce` and `soundfile` libraries.
- To install all dependencies, make sure your `requirements.txt` includes:
  ```
  noisereduce
  soundfile
  ```
- No extra steps are needed; enhancement is applied automatically in the workflow.

## Audio Recording

- The project supports recording audio directly from your microphone for transcription.
- To record audio, run the STT module and choose the "Record and transcribe" option when prompted.
- The recorded audio will be saved as a WAV file in the `samples/` directory and automatically enhanced for noise reduction before transcription.

**Example usage:**
```sh
python -m src.stt.whisper_stt
# Choose [2] Record and transcribe when prompted
```

- Make sure your microphone is connected and configured as the default input device on your system.
- The recording duration can be adjusted in the code (default is 5 seconds).