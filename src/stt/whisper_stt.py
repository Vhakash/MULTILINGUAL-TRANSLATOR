# Wrapper for Whisper model inference
import whisper
import os

SUPPORTED_EXTENSIONS = [".wav", ".mp3", ".m4a", ".flac", ".aac", ".ogg"]

def transcribe_audio(audio_path, language=None):
    ext = os.path.splitext(audio_path)[1].lower()
    if ext not in SUPPORTED_EXTENSIONS:
        print(f"⚠️ Warning: File format '{ext}' may not be supported. Make sure ffmpeg is installed.")

    print("Loading Whisper model...")
    model = whisper.load_model("small")  # Options: tiny, base, small, medium, large

    print(f"Transcribing: {audio_path}")
    options = {"task": "transcribe"}
    if language:
        options["language"] = language

    try:
        result = model.transcribe(audio_path, **options)
        print(f"Raw result: {result}")  # Debug: print the full result object
        print(f"🗣️  Detected Language: {result.get('language', 'unknown')}")
        print(f"📝 Transcription:\n{result.get('text', '')}")
        return result.get("text", ""), result.get("language", "")
    except Exception as e:
        print(f"❌ Error during transcription: {e}")
        return "", ""

if __name__ == "__main__":
    path = input("Enter path to pre-recorded audio file: ").strip()
    if not os.path.exists(path):
        print("❌ File not found.")
        exit()
    transcribe_audio(path)

