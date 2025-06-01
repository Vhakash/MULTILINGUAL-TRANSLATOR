# Wrapper for Whisper model inference
import whisper
import os
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import noisereduce as nr
import soundfile as sf

SUPPORTED_EXTENSIONS = [".wav", ".mp3", ".m4a", ".flac", ".aac", ".ogg"]

def record_audio(filename="samples/recorded.wav", duration=5, fs=44100):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    print(f"🎙️ Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    # Convert float32 audio to int16 for WAV
    audio = audio.flatten()
    if np.max(np.abs(audio)) > 0:
        audio_int16 = np.int16(audio / np.max(np.abs(audio)) * 32767)
    else:
        audio_int16 = np.int16(audio)
    write(filename, fs, audio_int16)
    print(f"✅ Saved to {filename}")
    return filename

def enhance_audio(input_path, output_path=None):
    """Reduce noise in the audio and overwrite or save as new file."""
    if output_path is None:
        output_path = input_path
    data, rate = sf.read(input_path)
    # Reduce noise
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    sf.write(output_path, reduced_noise, rate)
    return output_path

def transcribe_audio(audio_path):
    ext = os.path.splitext(audio_path)[1].lower()
    if ext not in SUPPORTED_EXTENSIONS:
        print(f"⚠️ Warning: File format '{ext}' may not be supported. Make sure ffmpeg is installed.")

    # Enhance audio before transcription
    enhanced_path = enhance_audio(audio_path)

    print("Loading Whisper model...")
    model = whisper.load_model("medium")  # Options: tiny, base, small, medium, large

    print(f"Transcribing: {enhanced_path}")
    options = {"task": "transcribe"}  # No language specified: auto-detect
    try:
        result = model.transcribe(enhanced_path, **options)
        print(f"Raw result: {result}")  # Debug: print the full result object
        print(f"🗣️  Detected Language: {result.get('language', 'unknown')}")
        print(f"📝 Transcription:\n{result.get('text', '')}")
        return result.get("text", ""), result.get("language", "")
    except Exception as e:
        print(f"❌ Error during transcription: {e}")
        return "", ""

if __name__ == "__main__":
    print("Choose input type:")
    print("[1] Transcribe from file")
    print("[2] Record and transcribe")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "2":
        path = record_audio()
    else:
        path = input("Enter path to audio file: ").strip()
        if not os.path.exists(path):
            print("❌ File not found.")
            exit()
    transcribe_audio(path)

