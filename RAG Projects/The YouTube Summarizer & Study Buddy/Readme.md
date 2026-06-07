# The YouTube Summarizer & Study Buddy

**Author:** Saqib   

## Overview

This project builds an **interactive Q&A system** for any YouTube video. Given a video URL, it fetches the transcript (subtitles), splits it into chunks, creates embeddings, and uses a local LLM (or Groq) to answer questions based *only* on the video content. This is a perfect study tool for lectures, tutorials, or any video content – part of Saqib’s advanced RAG portfolio.

## Features

- 🎥 **YouTube transcript fetch** – Uses `youtube-transcript-api` to retrieve captions (supports manual and auto‑generated).
- 🔍 **Chunking & vectorisation** – Recursive text splitter + `all-MiniLM-L6-v2` embeddings.
- 🗃️ **FAISS vector store** – In‑memory index for fast similarity search.
- 🤖 **Flexible LLM** – Uses Groq’s Llama 3.3 70B (fast) or falls back to a free Hugging Face model.
- 📌 **Source attribution** – Shows which chunks were used to answer.
- 💻 **Interactive Q&A loop** – Ask any question about the video content.

## Architecture

1. **Extract video ID** from any YouTube URL format.
2. **Fetch transcript** – Uses `YouTubeTranscriptApi` with fallback to Whisper for videos without captions.
3. **Chunk text** – Splits transcript into overlapping chunks (~1000 chars, 100 overlap).
4. **Embed & index** – FAISS stores chunk vectors.
5. **Retrieve** – For a query, top‑k relevant chunks are fetched.
6. **Generate answer** – A prompt injects the chunks into the LLM, which answers based solely on the transcript.
7. **Interactive loop** – User can ask unlimited questions.

## Setup

- Google Colab (GPU optional)
- Groq API key (recommended; free at [console.groq.com](https://console.groq.com))
- Without an API key, the notebook uses a slower free Hugging Face model (`zephyr-7b-beta`).

## How to Run

1. Open the notebook `The_YouTube_Summarizer_&_Study_Buddy.ipynb` in Google Colab.
2. Run the installation cell.
3. When prompted, enter your **Groq API key** (or press Enter to use the free fallback).
4. Enter a **YouTube video URL** (must have English captions; e.g., a TED talk or educational video).
5. Run all cells sequentially – the system will fetch the transcript, chunk it, and build the index.
6. Use the interactive loop to ask questions about the video.

## Example Interaction

**User:** What is the main topic of this video?  
**System:**  
- **Answer:** The video discusses the fundamentals of artificial intelligence and its impact on society.  
- **Sources:** 3 chunks retrieved.

**User:** What are the three key points mentioned?  
**System:**  
- **Answer:** 1. AI can automate routine tasks. 2. Ethical considerations are crucial. 3. AI will create new job categories.

## Why This Matters

This project demonstrates real‑time RAG on dynamic, external data. Unlike static PDF Q&A, it ingests live content from the web and provides a study assistant for any video. It showcases:

- Fetching and processing data from external APIs (YouTube).
- Building a RAG pipeline entirely in Colab.
- Graceful fallback mechanisms (if no API key or missing captions).
- A practical tool for students, researchers, or content consumers.

## Files

- `The_YouTube_Summarizer_&_Study_Buddy.ipynb` – Full Colab notebook.
- `youtube_rag_index/` – (Optional) saved FAISS index to Google Drive.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – YouTube Q&A study assistant.**