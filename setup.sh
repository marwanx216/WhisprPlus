#!/bin/bash

# setup.sh — Quick setup script for WhisprPlus

# Step 1: Create virtual environment
echo "🔧 Creating virtual environment..."
python -m venv .venv

# Step 2: Activate virtual environment
echo "⚡ Activating virtual environment..."
source .venv/bin/activate || source .venv/Scripts/activate

# Step 3: Upgrade pip & install requirements
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 4: Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "❗ FFmpeg not found. Please install it: https://ffmpeg.org/download.html"\else
    echo "✅ FFmpeg is installed."
fi

# Step 5: Run Streamlit app
echo "🚀 Launching WhisprPlus..."
streamlit run interface/streamlit_app.py
