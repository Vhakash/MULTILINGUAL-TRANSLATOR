import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(filename = "samples/recorded_audio.wav", duration  = 5, fs = 44100):
    os.makedirs(os.path.dirname(filename),exist_ok = True)
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate = fs, channels = 1)
    sd.wait()  # Wait until recording is finished
    write(filename,fs,audio)  # Save as WAV file
    print(f"Saved recording to {filename}")
    return filename