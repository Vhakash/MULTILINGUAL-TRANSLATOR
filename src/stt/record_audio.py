import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(filename="samples/recorded.wav", duration=5, fs=44100):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    print(f"🎙️ Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print(f"✅ Saved to {filename}")
    return filename
