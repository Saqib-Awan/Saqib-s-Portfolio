# Semantic Search & Re‑ranking with Embeddings + Groq

**Author:** Saqib    

## Overview

This project implements a hybrid semantic search engine:
1. **Fast retrieval** – Sentence‑transformers + FAISS to find candidate documents.
2. **LLM re‑ranking** – Groq’s Llama reorders candidates by relevance to the query.

Combining vector search with an LLM judge gives the speed of embeddings and the precision of large language models.

## Features

- 🔍 **Embedding‑based retrieval** – `all‑MiniLM‑L6‑v2` + FAISS.
- 🧠 **LLM re‑ranking** – Groq evaluates and reorders top‑k documents.
- 📚 **Sample corpus** – Built‑in news and facts.
- 💻 **Interactive** – Try any query.

## How It Works

1. User enters a query.
2. Query embedding is computed and FAISS returns the top‑K documents (by L2 distance).
3. Candidates are sent to Groq with an instruction to output the reordered indices.
4. The final list is displayed.

## Setup

- Groq API key – free at [console.groq.com](https://console.groq.com)
- Google Colab (GPU optional)

## Example

**Query:** *“Tell me about Paris.”*

**Retrieved candidates:** (embedding‑based)
1. “The capital of France is Paris. It is known for the Eiffel Tower.”
2. “Paris is also famous for its croissants and art museums.”
3. “In 2024, the Olympic Games will be held in Paris.”

**Re‑ranking order:** `0 2 1`  
**Final order:** most relevant → least.

## Files

- `Semantic_Search.ipynb` – Full notebook.
- `README.md` – This file.

## License

MIT – free to use and modify.

---

**© 2026 Saqib – Hybrid semantic search with LLM re‑ranking.**