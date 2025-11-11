# 🎬 YouTube Video Summarizer using LangChain + OpenAI

Summarize any YouTube video instantly using **LangChain**, **GPT-4**, and **Streamlit**!  
Just paste a YouTube link, and this app automatically fetches the transcript, processes it, and generates a clean, concise summary — powered by OpenAI’s GPT models 💡.

---

## ✨ Features

✅ **Automatic Transcript Extraction** – Uses `youtube-transcript-api` to fetch subtitles directly from the video.  
✅ **GPT-4 Summarization** – Uses LangChain’s prompt pipeline to create intelligent summaries.  
✅ **Streamlit Interface** – Simple, interactive web app to paste YouTube links and view results.  
✅ **Custom Prompt Template Support** – You can modify the summarization prompt in `yt_template.json`.  
✅ **Clean Output** – Transcript stored locally in `firstpost.txt` and summarized into human-readable content.  

---

## 🧠 Tech Stack

| Component | Description |
|------------|-------------|
| 🐍 Python 3.10+ | Core programming language |
| 🌐 Streamlit | Web-based UI |
| 🧩 LangChain | Prompt orchestration for GPT models |
| 🤖 OpenAI GPT-4 | Summarization engine |
| 🎥 youtube-transcript-api | Fetches video transcripts |
| 🔐 python-dotenv | Manages environment variables |

---

