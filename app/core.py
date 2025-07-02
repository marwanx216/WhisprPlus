# app/core.py

import whisper
import librosa
import soundfile as sf
import numpy as np
from transformers import pipeline

# Load Whisper and Summarizer once
_whisper_model = whisper.load_model("base")
_summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")


# --- Transcription (no ffmpeg dependency) ---
def transcribe_audio(audio_path, language=None):
    import torch
    from whisper.audio import log_mel_spectrogram, pad_or_trim

    # Load audio using librosa (instead of whisper.audio.load_audio)
    audio, _ = librosa.load(audio_path, sr=16000)
    audio = pad_or_trim(audio)

    mel = log_mel_spectrogram(audio).to(_whisper_model.device)

    options = {"task": "transcribe", "fp16": False}
    if language and language != "auto":
        options["language"] = language

    result = _whisper_model.decode(mel, whisper.DecodingOptions(**options))
    segments = [{"start": 0, "end": 0, "text": result.text}]
    return result.text, segments


# --- Audio Preprocessing (No ffmpeg) ---
def preprocess_audio(input_path, target_sr=16000):
    # Load with librosa
    y, sr = librosa.load(input_path, sr=target_sr)

    # Normalize
    y = y / np.max(np.abs(y))

    # Trim silence
    y_trimmed, _ = librosa.effects.trim(y, top_db=30)

    # Save as WAV
    output_path = "temp/processed.wav"
    sf.write(output_path, y_trimmed, target_sr)

    return output_path


# --- Fake Diarization (Placeholder for WhisperX) ---
def fake_diarization(transcript):
    lines = transcript.split(". ")
    speaker_transcript = ""
    for i, line in enumerate(lines):
        speaker = f"Speaker {i % 2 + 1}"
        speaker_transcript += f"{speaker}: {line.strip()}.\n"
    return speaker_transcript


# --- Summarization ---
def summarize_text(text, max_len=130):
    summary = _summarizer(text, max_length=max_len, min_length=30, do_sample=False)
    return summary[0]['summary_text']
