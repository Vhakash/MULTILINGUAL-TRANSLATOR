# Interface to TTS (gTTS / Coqui etc.)
from gtts import gTTS
from playsound import playsound
import os

def text_to_speech(text, lang = "en", filename = "samples/0704.mp3", autoplay = True):
    tts = gTTS(text = text, lang = lang)
    os.makedirs(os.path.dirname(filename), exist_ok = True)
    tts.save(filename)
    print(f"✅ Saved TTS output to {filename}")
    if autoplay:
        playsound(filename)