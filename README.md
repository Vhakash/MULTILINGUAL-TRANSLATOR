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

- The project uses automatic noise reduction to improve transcription quality.
- All audio (recorded or pre-recorded) is processed to reduce background noise using the `noisereduce` and `soundfile` libraries.
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

## Transcription and Translation

- You can transcribe from a pre-recorded audio file or record new audio.
- After transcription, you will be prompted to translate the output to a target language of your choice.
- The translation uses MarianMT models from Hugging Face. Ensure you have internet access and, if needed, a valid Hugging Face token for private/gated models.

**Example usage:**
```sh
python -m src.stt.whisper_stt
# Choose [1] Transcribe from file when prompted
# Enter the path to your audio file
```

- If you want to translate, enter `y` when prompted and provide the target language code (e.g., `fr` for French, `de` for German, `hi` for Hindi).

---

**Note:**  
If you need to use private or gated Hugging Face models, generate a token from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) and log in using:
```sh
huggingface-cli login
```
Paste your token when prompted.