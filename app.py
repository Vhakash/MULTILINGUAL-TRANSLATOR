import streamlit as st
from stt.whisper_stt_cloud import transcribe_audio
from translation.marian_translator import Translator
from tts.tts_engine import text_to_speech
import tempfile
import os
import warnings
from translation.utils import log_translation


warnings.filterwarnings("ignore")

st.set_page_config(page_title="AI Translator", page_icon="🗣️")

st.title("🎙️ Multilingual Speech Translator")

# 1. Upload audio
st.header("1. Upload Audio")
audio_file = st.file_uploader("Upload audio (mp3, wav, m4a, etc)", type=["mp3", "wav", "m4a", "flac", "aac", "ogg"])

# 2. Translation settings
st.header("2. Translation Settings")
target_lang = st.text_input("Target language code (e.g., 'en', 'fr', 'hi')", value="hi")

if audio_file:
    # Save uploaded file to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio_file.name)[1]) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    st.success("Audio uploaded successfully!")

    if st.button("🔍 Transcribe & Translate"):
        # Transcription
        with st.spinner("Transcribing..."):
            try:
                text, detected_lang = transcribe_audio(tmp_path)
                st.subheader("📝 Transcription")
                st.write(text)
                st.subheader("🌍 Detected Language")
                st.write(detected_lang)
            except Exception as e:
                st.error(f"❌ Transcription failed: {e}")
                text, detected_lang = None, None

        # Translation
        with st.spinner("Translating..."):
            try:
                translator = Translator(source_lang=detected_lang, target_lang=target_lang)
                translated_text = translator.translate(text)
                st.subheader(f"🈯 Translation ({detected_lang} ➡ {target_lang})")
                st.write(translated_text)
            except Exception as e:
                st.error(f"❌ Translation failed: {e}")
                translated_text = None

        # Ensure the directory exists
        os.makedirs("samples", exist_ok=True)  
        # Log translation
        log_translation(text,translated_text, detected_lang, target_lang)

        # TTS
        if translated_text:
            with st.spinner("Generating Speech..."):
                tts_path = text_to_speech(translated_text, lang=target_lang, filename=None, autoplay=False)
                st.subheader("🔈 Translated Speech")
                st.audio(tts_path)

        st.success("✅ Done!")

    # Show uploaded audio for reference
    st.subheader("🔊 Uploaded Audio")
    st.audio(tmp_path)
else:
    st.info("Please upload an audio file to begin.")

st.markdown("---")
st.header("🧠 Download Translation Log as Flashcards")
if os.path.exists("samples/translation_log.csv"):
    with open("samples/translation_log.csv", "rb") as f:
        st.download_button("📥 Download Flashcards (CSV)", f, file_name="flashcards.csv")
