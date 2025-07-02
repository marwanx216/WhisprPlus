# 🎙️ WhisprPlus

**WhisprPlus** is a professional, customizable voice-to-text transcription tool built with OpenAI's Whisper model. It includes speaker diarization, summarization, and transcription analytics — all in a clean, interactive Streamlit interface.

---

## 🚀 Features

- 🔊 Upload MP3, WAV, or M4A files
- 🧠 Whisper-based transcription (multilingual)
- 🧍 Speaker diarization (mocked, ready for WhisperX)
- 📊 Analytics: word count, WPM, duration
- 📃 AI-powered text summarization
- 💡 Dark/light theme support
- 📥 Download .txt versions of transcript, diarized output, and summary
- ⚡ Clean and responsive UI built with Streamlit

---

## 📂 Project Structure

```
WhisprPlus/
├── app/                   # Backend logic
│   ├── core.py            # AI functions (transcribe, summarize, etc.)
│   ├── helpers.py         # Utilities and stats
│   └── __init__.py
│
├── interface/
│   └── streamlit_app.py   # Streamlit frontend
│
├── assets/                # Sample audio, outputs, visuals
├── requirements.txt
├── README.md
└── setup.sh               # (Optional) Dev environment setup
```

---

## 💻 Installation

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/WhisprPlus.git
cd WhisprPlus
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg (if not installed)
- [FFmpeg download link](https://ffmpeg.org/download.html)
- Add FFmpeg to your system PATH

---

## 🧪 Run the App

```bash
streamlit run interface/streamlit_app.py
```

Then open in your browser: [http://localhost:8501](http://localhost:8501)

---

## 👨‍💻 Developer
**Made by [Marwan Ashraf](https://linkedin.com/in/marwanashraf0)**

- 🔗 [GitHub](https://github.com/marwanashraf0)
- 🔗 [LinkedIn](https://linkedin.com/in/marwanashraf0)

---

## 📜 License
This project is open source and free to use under the MIT License.

---

Enjoy your transcription journey! 🎧
