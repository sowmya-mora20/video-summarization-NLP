# 🎥 Video Summarization using NLP

This project aims to automatically summarize YouTube video transcripts using Natural Language Processing (NLP) and Machine Learning techniques. It helps users save time by generating short summaries from long video content.

## 📌 Project Objective
To build a system that extracts transcripts from YouTube videos and provides concise summaries based on the user’s preferred language and summary length.

## 🔧 Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Libraries**: 
  - `youtube-transcript-api`
  - Hugging Face `transformers`
  - `summa` for text summarization
  - `googletrans` for language translation
- **Framework**: Streamlit for web UI

## ⚙️ How It Works
1. User enters a YouTube video URL.
2. The system extracts the transcript using YouTube Transcript API.
3. The transcript is summarized using NLP models.
4. The summary is translated to the chosen language.
5. Output is displayed on the web UI.

## 🚀 How to Run
```bash
pip install -r requirements.txt
python app.py
Visit http://localhost:5000 in your browser and try it out!

📂 Modules
Transcript Extraction: Gets video text using youtube-transcript-api

Summarization: Generates summaries using summa or Transformer models

Translation: Uses Google Translate to support multiple languages

UI Interaction: Simple interface to input URL and choose options

✅ Features
Input: YouTube URL

Output: Summarized transcript

Customizable: Language & summary length

Fast and efficient

👩‍💻 Team Members
Mora Sowmya (2456-21-737-108)

Dharmavarapu Lakshmi Jhansi Rani (2456-21-737-086)

Bharatha Bhargavi (2456-21-737-071)

Guide: Mr. M. Bapiraju, Assistant Professor

📜 Future Enhancements
Support for summarizing video audio directly

Real-time summarization for live content

Chrome extension for quick summaries




