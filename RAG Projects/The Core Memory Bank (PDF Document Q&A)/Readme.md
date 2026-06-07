# The Core Memory Bank (PDF Document Q&A)

**Author:** Saqib  

## Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system that answers questions based on the content of uploaded PDF documents. Users can upload one or more PDF files, and the system will retrieve relevant chunks and generate accurate, grounded answers with source citations – no external internet search required. It is the foundational RAG project in Saqib’s portfolio.

## Features

- 📄 **PDF upload** – Supports one or multiple PDFs (via Colab’s file upload).
- 🔍 **Text extraction & chunking** – Splits documents into overlapping chunks.
- 🧠 **Embedding & vector store** – Uses `all-MiniLM-L6-v2` + FAISS for efficient similarity search.
- 🗣️ **Answer generation** – Uses Groq’s Llama 3.3 70B (or free local fallback) to produce grounded answers.
- 📌 **Source citations** – The answer includes references to the source PDF filenames.
- 💾 **Persistent index** – Optionally save the FAISS index to Google Drive for reuse.

## Architecture

1. **Upload PDFs** – User uploads files via Colab widget.
2. **Load & chunk** – `PyPDFLoader` extracts text; `RecursiveCharacterTextSplitter` creates chunks (~500 chars, 50 overlap).
3. **Embed** – Sentence‑Transformer `all-MiniLM-L6-v2` converts chunks to vectors.
4. **Store** – FAISS builds an in‑memory index.
5. **Retrieve** – For a user query, the top‑k most similar chunks are fetched.
6. **Generate** – A prompt injects the retrieved chunks into Groq Llama, which produces the final answer.
7. **Cite** – Source filenames are extracted from metadata and displayed.

## Setup

- Google Colab (GPU optional, CPU works).
- Groq API key (recommended for fast inference; free at [console.groq.com](https://console.groq.com)).
- Without an API key, the notebook falls back to a slower free Hugging Face model (`flan-t5-large`).

## How to Run

1. Open the notebook `The_Core_Memory_Bank_(PDF_Document_Q&A).ipynb` in Google Colab.
2. Run the installation cell.
3. When prompted, enter your **Groq API key** (or press Enter to use the free local fallback).
4. Upload one or more PDF files.
5. Run all cells sequentially – the system will process the PDFs and create the FAISS index.
6. Use the interactive loop to ask questions about your documents.

## Example Interaction

**User:** What is the main topic of the uploaded document?  
**System:**  
- **Answer:** The document discusses the fundamentals of machine learning, including supervised and unsupervised learning.  
- **Sources:** `ml_fundamentals.pdf`

**User:** Summarise the section about neural networks.  
**System:**  
- **Answer:** Neural networks consist of input, hidden, and output layers. They learn by adjusting weights through backpropagation.  
- **Sources:** `ml_fundamentals.pdf`

## Why This Matters

RAG is one of the most important techniques in modern NLP, allowing LLMs to incorporate private or up‑to‑date knowledge without retraining. This project demonstrates:

- End‑to‑end RAG pipeline using pure Python and LangChain.
- Document loading, chunking, embedding, and retrieval.
- Integration with Groq’s high‑speed inference.
- Production‑ready code with error handling and fallbacks.

## Files

- `The_Core_Memory_Bank_(PDF_Document_Q&A).ipynb` – Full notebook.
- `uploaded_pdfs/` – Temporary directory for PDF uploads.
- `faiss_index/` – Saved index (if exported to Drive).
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Production‑ready PDF Q&A RAG system.**