# app/__init__.py

# Optional: import core functions for quick access
from .core import (
    transcribe_audio,
    preprocess_audio,
    fake_diarization,
    summarize_text,
)

from .helpers import (
    save_temp_file,
    get_transcription_stats,
)
