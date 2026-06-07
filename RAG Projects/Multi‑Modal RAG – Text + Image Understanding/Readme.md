# Multi‑Modal RAG – Text + Image Understanding

**Author:** Saqib   

## Overview

This project builds a **multi‑modal Retrieval‑Augmented Generation (RAG)** system that can answer questions about documents containing both **text and images**. It extracts text from PDF pages, generates descriptive captions for figures and diagrams (using BLIP), combines both modalities into a unified vector index, and performs retrieval‑augmented answering with Groq’s Llama 3.3 70B.

Unlike standard RAG (which only handles text), this system can reference charts, diagrams, and photographs alongside written content – a critical capability for many real‑world documents.

## Features

- 📄 **PDF text extraction** – Uses PyPDFLoader to extract raw text.
- 🖼️ **Image captioning** – BLIP (Bootstrapping Language‑Image Pre‑training) generates natural language descriptions of each page image.
- 🔗 **Unified vector store** – FAISS index combines text chunks and image captions.
- 🔍 **Multi‑modal retrieval** – Query retrieves relevant text *or* image descriptions.
- 🧠 **Groq LLM** – Generates answers citing both text and image sources.
- 📊 **Inference demo** – Ask questions about any uploaded PDF.

## Architecture

1. **Upload PDF** – User uploads one or more PDF files.
2. **Convert pages to images** – `pdf2image` converts each page to PNG.
3. **Extract text** – PyPDFLoader extracts all text (page‑wise).
4. **Generate captions** – BLIP‑base (or BLIP‑large) captions each page image.
5. **Chunk & embed** – Split text into chunks, embed with `all-MiniLM-L6-v2`.
6. **Combine** – Add image captions as separate documents with `type: image` metadata.
7. **FAISS index** – Store all embeddings.
8. **QA chain** – Retrieve relevant chunks (text + image) and answer with Groq.

## Setup

- Google Colab (T4 GPU recommended for faster captioning)
- Groq API key (required – get free at [console.groq.com](https://console.groq.com))
- Hugging Face dependencies (auto‑downloaded)

## How to Run

1. Open the notebook `Multi‑Modal_RAG_–_Text_+_Image_Understanding_.ipynb` in Google Colab.
2. Run the installation cell (includes `pdf2image`, `transformers`, `blip`, etc.).
3. When prompted, enter your **Groq API key**.
4. Upload a PDF file that contains both text and images (e.g., a research paper, report, or brochure).
5. Run all cells sequentially – the system will:
   - Convert PDF pages to images.
   - Extract text and generate image captions.
   - Build the multi‑modal FAISS index.
6. Use the interactive loop to ask questions like:
   - *“What does the bar chart on page 3 show?”*
   - *“What is the main conclusion in the text?”*
   - *“Describe the architecture diagram on page 5.”*

## Example Interaction

**User:** What does the bar chart on page 3 show?  
**System (retrieved image caption):** *“A bar chart comparing quarterly sales for four regions: North ($12M), South ($8M), East ($15M), West ($10M).”*  
**LLM Answer:** The bar chart on page 3 shows that the East region had the highest quarterly sales at $15 million, followed by North at $12 million.

## Why This Matters

Multi‑modal RAG is at the cutting edge of AI research. Most RAG systems only handle text; this project shows you can:
- Process visual information alongside text.
- Use image captioning as a bridge from vision to language.
- Build a single index for heterogeneous data.
- Answer questions that require understanding figures, diagrams, or photographs.

## Results & Limitations

- **Caption quality:** BLIP‑base works for simple figures but may produce repetitive captions. Using **BLIP‑large** or **InstructBLIP** improves quality (adds download time).
- **Retrieval accuracy:** Hybrid text‑image indexing works well when captions are descriptive.
- **Performance:** Generating captions for many pages takes time (~5–10 seconds per page on T4 GPU).

## Files

- `Multi‑Modal_RAG_–_Text_+_Image_Understanding_.ipynb` – Full notebook.
- `README.md` – This file.

## License

MIT – free to use and modify.

---

**© 2026 Saqib – Multi‑modal document Q&A.**