# RAG Evaluation Pipeline with RAGAS

**Author:** Saqib  

## Overview

This notebook implements a **systematic evaluation framework** for Retrieval‑Augmented Generation (RAG) systems. It measures the quality of both retrieval and generation using four key metrics:

- **Faithfulness** – Is the generated answer grounded in the retrieved context? (Measures hallucination.)
- **Answer Relevancy** – How well does the answer address the user’s question?
- **Context Precision** – Among the retrieved chunks, what proportion is relevant to the question?
- **Context Recall** – Did the retrieval system fetch all necessary information to answer the question?

The evaluation can run using the **RAGAS** library (with OpenAI or Groq as the judge) or a **custom Groq‑based fallback** that implements the same logic with explicit prompts. This flexibility ensures the notebook works even with rate limits or compatibility issues.

## Features

- 📊 **Four core metrics** – Quantify RAG quality from multiple angles.
- 🔁 **Two evaluation backends** – RAGAS (if compatible) or custom Groq LLM‑as‑a‑judge.
- 📝 **Per‑question scoring** – Detailed breakdown for diagnostic insights.
- 📈 **Visualisation** – Bar chart of average metric scores.
- 💾 **Export results** – Save per‑question scores to CSV.
- ⚡ **Groq‑friendly** – Custom evaluation works perfectly with Groq’s free tier.

## Architecture

1. **Build/load a RAG pipeline** – Any retriever + LLM (e.g., FAISS + Groq).
2. **Create a test set** – Questions, retrieved contexts, generated answers.
3. **Evaluate** – For each metric, compare answers against contexts and questions using an LLM judge.
4. **Aggregate** – Compute average scores and generate visualisations.

## Setup

- Google Colab (CPU or T4 GPU)
- Groq API key (required for custom evaluation; free at [console.groq.com](https://console.groq.com))
- (Optional) OpenAI API key if using RAGAS directly

## How to Run

1. Open the notebook `RAG_Evaluation_Pipeline_with_RAGAS.ipynb` in Google Colab.
2. Run the installation cell.
3. Enter your **Groq API key** when prompted.
4. (Optional) Upload your own RAG pipeline or use the built‑in sample document.
5. Run all cells sequentially – the notebook will:
   - Build a sample RAG system.
   - Generate test questions and answers.
   - Compute faithfulness, relevancy, precision, recall.
   - Display per‑question scores and a summary bar chart.
6. Review the interpretation guide to understand what each metric means.

## Example Output
Faithfulness : 0.85 (higher = less hallucination)
Answer Relevancy : 0.92 (higher = more on‑topic)
Context Precision : 0.78 (higher = fewer irrelevant chunks)
Context Recall : 0.81 (higher = less missing information)

text

## Why This Matters

Evaluating RAG is essential for production systems. Without measurement, you cannot know whether changes to chunking, embedding, or prompt design improve performance. This project demonstrates:

- Implementing research‑grade evaluation metrics (faithfulness, relevancy, etc.).
- Using an LLM as an impartial judge.
- Interpreting metrics to guide iterative improvements.
- A reusable framework applicable to any RAG pipeline.

## Files

- `RAG_Evaluation_Pipeline_with_RAGAS.ipynb` – Full notebook.
- `ragas_results.csv` – Per‑question evaluation scores (generated).
- `ragas_evaluation_results.png` – Bar chart of metric averages (generated).
- `README.md` – This file.

## License

MIT – free to use and modify.

---

**© 2026 Saqib – Professional RAG evaluation pipeline.**