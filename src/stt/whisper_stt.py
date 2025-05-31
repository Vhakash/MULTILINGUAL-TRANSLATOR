# Wrapper for Whisper model inference
import whisper

def transcribe_audio(audio_path, language=None):
    print("Loading Whisper model...")
    model = whisper.load_model("small")  # tiny, base, small, medium, large available
    options = {"task": "transcribe"}
    if language:
        options["language"] = language

    print(f"Transcribing audio: {audio_path}")
    result = model.transcribe(audio_path, **options)

    print(f"Detected language: {result['language']}")
    print(f"Transcription:\n{result['text']}")
    return result["text"], result["language"]

if __name__ == "__main__":
    sample_audio = "samples/0704.mp3"  # Use the relative path to your mp3 in samples
    transcribe_audio(sample_audio)
