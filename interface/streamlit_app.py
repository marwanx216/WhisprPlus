# interface/streamlit_app.py

import sys
import os
import streamlit as st

# ✅ Fix for "No module named 'app'"
current_dir = os.path.dirname(os.path.abspath(__file__))             # -> /WhisprPlus/interface
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))        # -> /WhisprPlus
sys.path.insert(0, parent_dir)

from app import (
    transcribe_audio,
    preprocess_audio,
    fake_diarization,
    summarize_text,
    save_temp_file,
    get_transcription_stats
)

# --- Page Setup ---
st.set_page_config(
    page_title="WhisprPlus - Transcription Tool",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom Style ---
custom_css = """
    <style>
        .footer {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            color: gray;
            font-size: 0.85rem;
        }
        .footer a {
            margin: 0 10px;
            color: #999;
            text-decoration: none;
        }
        .stTextArea textarea {
            font-family: monospace;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("🎛️ Settings")
language = st.sidebar.selectbox("Language", ["auto", "en", "es", "fr", "de", "ar"])

# --- Main UI ---
st.title("🎙️ WhisprPlus")
st.caption("Custom AI-Powered Transcription Tool")

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file:
    st.success("File uploaded successfully.")
    temp_path = save_temp_file(uploaded_file)

    with st.spinner("🔊 Preprocessing audio..."):
        clean_audio = preprocess_audio(temp_path)

    with st.spinner("🧠 Transcribing with Whisper..."):
        transcript, segments = transcribe_audio(clean_audio, language)

    duration = segments[-1]['end'] if segments else 0
    stats = get_transcription_stats(transcript, duration)

    # --- Tabs ---
    tab1, tab2, tab3, tab4 = st.tabs(["📝 Transcript", "🧍 Diarization", "📊 Analytics", "🧠 Summary"])

    with tab1:
        st.download_button("Download Transcript (.txt)", transcript, file_name="transcript.txt")
        st.text_area("Transcript", transcript, height=350)

    with tab2:
        diarized = fake_diarization(transcript)
        st.download_button("Download Diarized (.txt)", diarized, file_name="diarized.txt")
        st.text_area("Diarized Output", diarized, height=300)

    with tab3:
        st.write(stats)

    with tab4:
        summary = summarize_text(transcript)
        st.download_button("Download Summary", summary, file_name="summary.txt")
        st.success(summary)

# --- Footer ---
st.markdown("""
    <div class="footer">
        Made by Marwan Ashraf | 
        <a href="https://github.com/marwanashraf0" target="_blank">GitHub</a> |
        <a href="https://linkedin.com/in/marwanashraf0" target="_blank">LinkedIn</a>
    </div>
""", unsafe_allow_html=True)
