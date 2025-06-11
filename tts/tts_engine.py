# Interface to TTS (gTTS / Coqui etc.)

def text_to_speech(text, lang="en", filename=None, autoplay=True):
    from gtts import gTTS
    from playsound import playsound
    import os

    #Set default filename if not provided
    if filename is None:
        filename = f"samples/tts_{lang}.mp3"
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    print(f"✅ Saved TTS output to {filename}")
    if autoplay:
        playsound(filename)
    return filename #returns the filename in the streamlit to play the audio    