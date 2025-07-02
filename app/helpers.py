import os


# Save uploaded file to /temp/
def save_temp_file(uploaded_file):
    os.makedirs("temp", exist_ok=True)
    file_path = os.path.join("temp", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path


# Basic transcription stats
def get_transcription_stats(text, duration_sec):
    words = len(text.split())
    wpm = round(words / (duration_sec / 60), 2) if duration_sec > 0 else 0
    return {
        "words": words,
        "duration_sec": round(duration_sec, 2),
        "words_per_minute": wpm
    }
