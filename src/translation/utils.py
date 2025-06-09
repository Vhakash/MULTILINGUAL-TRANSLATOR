import csv
import os
from datetime import datetime

LOG_FILE = "samples/translation_log.csv"

def log_translation(input_text, translated_text, source_lang, target_lang):
    os.makedirs("samples", exist_ok=True)
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Source Lang", "Target Lang", "Input", "Translation"])
        writer.writerow([datetime.now().isoformat(), source_lang, target_lang, input_text, translated_text])