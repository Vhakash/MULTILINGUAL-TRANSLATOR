# MarianMT translation code
from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self, source_lang="en", target_lang="fr"):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
        print(f"🔁 Loading translation model: {self.model_name}")
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)

    def translate(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        translated = self.model.generate(**inputs)
        output = self.tokenizer.batch_decode(translated, skip_special_tokens=True)
        return output[0]
