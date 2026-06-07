# LLM as a Judge – Automated Evaluation of Responses

**Author:** Saqib   

## Overview

This project implements an **LLM‑as‑a‑judge** system using Groq’s Llama 3.3 70B. Given a question, a reference (ground truth) answer, and a candidate answer, the judge outputs numerical scores (1–5) for correctness, relevance, clarity, and conciseness, plus a short explanation. This technique is used in modern LLM evaluation frameworks like AlpacaEval and RAGAS.

## Features

- ⚖️ **Multi‑criteria scoring** – Four dimensions of quality.
- 📝 **Structured JSON output** – Easy to parse and store.
- 🔄 **Batch evaluation** – Score multiple test cases at once.
- 💻 **Interactive** – Judge any candidate answer you provide.

## How It Works

1. User provides question, reference answer, candidate answer.
2. Prompt instructs the judge LLM to output JSON scores.
3. Result is parsed and displayed.

## Setup

- Groq API key – free at [console.groq.com](https://console.groq.com)
- Google Colab or any Python environment.

## Example

**Question:** What is the capital of France?  
**Reference:** Paris  
**Candidate:** Paris is the capital of France.  

**Judge output:**
```json
{
  "correctness": 5,
  "relevance": 5,
  "clarity": 5,
  "conciseness": 4,
  "explanation": "Correct, relevant, clear, slightly longer than needed."
}

Files
LLM_as_Judge.ipynb – Full notebook.

README.md – This file.

License
MIT – free to use and modify.

© 2026 Saqib – Automated evaluation with LLM judge.