# whisper_stt_cloud.py (Streamlit-compatible)

import whisper
import os

SUPPORTED_EXTENSIONS = [".wav", ".mp3", ".m4a", ".flac", ".aac", ".ogg"]

def transcribe_audio(audio_path):
    ext = os.path.splitext(audio_path)[1].lower()
    if ext not in SUPPORTED_EXTENSIONS:
        print(f"⚠️ Warning: File format '{ext}' may not be supported. Make sure ffmpeg is installed.")

    print("Loading Whisper model...")
    model = whisper.load_model("medium")

    print(f"Transcribing: {audio_path}")
    try:
        result = model.transcribe(audio_path)
        return result.get("text", ""), result.get("language", "")
    except Exception as e:
        print(f"❌ Error during transcription: {e}")
        return "", ""
