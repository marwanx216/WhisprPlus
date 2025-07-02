# WhisprPlus 🎙️  
**Custom AI-Powered Transcription Tool**

WhisprPlus is an AI-powered transcription web app built with **OpenAI Whisper**, **HuggingFace Transformers**, and **Streamlit**. It transcribes audio, assigns fake speakers (placeholder), summarizes speech, and analyzes basic stats — all within a clean web interface.

---

## 🚀 Features

- 🔊 **Audio Preprocessing** – Silence removal and normalization (via Librosa)
- 🧠 **Transcription** – Powered by OpenAI Whisper (`base` model)
- 👥 **Speaker Diarization (Fake)** – Alternating speaker formatting
- ✍️ **Text Summarization** – Using HuggingFace `t5-small` model
- 📊 **Speech Analytics** – Word count, duration, and WPM
- 📥 **Downloadable Outputs** – Export transcript, diarization, and summary as `.txt`

---

## 🧠 Technologies Used

- 🧊 [OpenAI Whisper](https://github.com/openai/whisper)
- 🤗 [HuggingFace Transformers](https://huggingface.co/)
- 🧼 [Librosa](https://librosa.org/)
- 🟢 [Streamlit](https://streamlit.io/)
- 🐍 Python 3.10+

## App Overview

### App Initial Start
![Screenshot 2025-07-02 170325](https://github.com/user-attachments/assets/011476c5-59b6-435b-95fd-a6f0e34de00a)

### After Applying Transcript
![Screenshot (259)](https://github.com/user-attachments/assets/975867bf-a432-4762-a25c-e46527a04dde)

### Diarization
![Screenshot (256)](https://github.com/user-attachments/assets/4e385353-4eb0-4052-835c-d1a5b461526d)

### Analytics
![Screenshot (257)](https://github.com/user-attachments/assets/ca119c5b-0b70-4656-860a-ba2372b50365)

### Summary
![Screenshot (258)](https://github.com/user-attachments/assets/10dc8d37-b149-41e5-859b-da35fd8a0ee2)

## 📂 Folder Structure

```
WhisprPlus/
│
├── app/                # Core logic for transcription & processing
│   └── core.py
│
├── interface/          # Streamlit front-end
│   └── streamlit_app.py
│
├── temp/               # Temporary storage for uploaded/processed files
│   └── .gitignore
│
├── requirements.txt    # All Python dependencies
├── README.md           # Project overview (this file)
```

> ⚠️ The `temp/` folder is used to store temporary audio files and is excluded from version control via `.gitignore`.

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/WhisprPlus.git
cd WhisprPlus
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate it

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit app

```bash
streamlit run interface/streamlit_app.py
```

---

## 💡 How to Use the App

1. Upload an audio file (`.mp3`, `.wav`, or `.m4a`)
2. The app will:
   - Preprocess and normalize the audio
   - Transcribe the speech using Whisper
   - Add fake speaker tags
   - Summarize the transcription
   - Provide analytics like word count and duration
3. Use download buttons to save `.txt` files

---

## 🧪 Limitations

- ⚙️ Whisper’s `load_audio()` still uses `ffmpeg` under the hood (via subprocess).
- 🧍 Diarization is simulated by alternating speakers — not real speaker detection (WhisperX to be added later).

---

## 📌 Future Improvements

- ✅ Replace Whisper's dependency on `ffmpeg`
- 🧍‍♀️ Integrate real diarization (e.g. WhisperX or pyannote.audio)
- 🌍 Deploy to HuggingFace Spaces or Streamlit Cloud
- 💬 Real-time audio transcription

---

## 👨‍💻 Author

**Marwan Ashraf**  
🔗 [LinkedIn](https://linkedin.com/in/marwanax216)  
💻 [GitHub](https://github.com/marwan-ashraf-8a503b20a)

---

## 📄 License

This project is free to use.
