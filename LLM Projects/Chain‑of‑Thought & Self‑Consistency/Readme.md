# Chain‑of‑Thought & Self‑Consistency with Groq

**Author:** Saqib  

## Overview

This project implements two advanced LLM reasoning techniques:
- **Chain‑of‑Thought (CoT)** – Prompt the model to "think step by step" before answering.
- **Self‑Consistency** – Generate multiple reasoning paths (via sampling) and take a majority vote on the final answer.

These methods dramatically improve performance on arithmetic, logic puzzles, and multi‑hop questions.

## Features

- 🧠 **CoT prompting** – Explicit reasoning traces.
- 🔁 **Self‑consistency** – 5–10 samples + majority voting.
- 📊 **Evaluation** – Compare direct, CoT, and self‑consistency accuracy.
- 📈 **Visualisation** – Accuracy bar chart automatically saved.

## Architecture

1. User question → sent to Llama 3.3 70B with CoT instruction.
2. Model outputs reasoning steps + final answer.
3. Repeat multiple times with temperature >0.
4. Aggregate final answers using `Counter` → majority vote.
5. Compare baseline (direct answer) and CoT.

## Setup

- Python 3.9+ (Colab works out‑of‑the‑box)
- Groq API key (free at [console.groq.com](https://console.groq.com))

## How to Run

1. Open the provided Colab notebook.
2. Enter your Groq API key.
3. Run all cells sequentially.
4. View the accuracy comparison chart and sample outputs.

## Example Output

**Question:** Roger has 5 tennis balls. He buys 2 cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?

**CoT reasoning:**  
Roger starts with 5. Each can has 3 balls, so 2 cans give 6 balls. Total = 5 + 6 = 11.  
**Final answer:** 11

**Self‑consistency** (5 samples) → majority answer: 11

## Results

On a set of grade‑school math problems:
- Direct: ~60%
- CoT: ~80%
- Self‑consistency: ~90%

## Why This Matters

Chain‑of‑thought and self‑consistency are used by top labs (Google DeepMind, OpenAI) to make LLMs reliable reasoners. This project proves you can implement research‑grade techniques and integrate them into production systems.

## Files

- `llm_cot_selfconsistency.ipynb` – Full Colab notebook.
- `reasoning_accuracy.png` – Generated accuracy bar chart.
- `README.md` – This file.

## License

MIT – use freely, attribution appreciated.

---

**© 2026 Saqib – Advanced LLM reasoning portfolio piece.**