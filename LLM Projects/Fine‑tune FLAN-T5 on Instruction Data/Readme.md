# Fine‑tune FLAN‑T5 on Instruction Data

**Author:** Saqib  

## Overview

This project fine‑tunes a small, efficient instruction‑tuned language model – **FLAN‑T5‑Small** – on a subset of the Databricks Dolly 15k dataset. The goal is to demonstrate the end‑to‑end fine‑tuning pipeline: loading data, tokenising, training, saving, and inference. Despite the model’s modest size, the notebook proves the ability to adapt a general‑purpose LLM to follow instructions.

## Features

- 🔧 **Complete fine‑tuning pipeline** using Hugging Face `Trainer`.
- 📚 **Dataset** – 500 instruction‑response pairs from Dolly 15k.
- 🧠 **Base model** – `google/flan-t5-small` (248M parameters, runs comfortably on Colab).
- 💾 **Model saving** – Export fine‑tuned weights and tokenizer.
- 🧪 **Inference demo** – Test the trained model on custom prompts.

## Architecture

1. **Load dataset** – Dolly 15k (500 examples) and format into `input_text` / `target_text`.
2. **Tokenise** – Convert text to input IDs and labels using the FLAN‑T5 tokenizer.
3. **Train** – Use `Seq2SeqTrainer` with standard hyperparameters.
4. **Save** – Export model and tokenizer to local directory.
5. **Inference** – Generate responses for new instructions.

## Setup

- Python 3.9+ (Google Colab recommended)
- GPU optional (training works on CPU, but slower)

## How to Run

1. Open the notebook `Fine‑tune_FLAN_T5_on_Instruction_Data.ipynb` in Google Colab.
2. Run all cells sequentially.
3. After training (approx. 10‑15 minutes on T4 GPU), test the model with custom prompts.

## Example Interaction

**Instruction:** What is the capital of France?  
**Fine‑tuned FLAN‑T5:** Paris

**Instruction:** Explain machine learning in simple terms.  
**Fine‑tuned FLAN‑T5:** Machine learning is a way for computers to learn from data without being explicitly programmed.

> **Note:** Output quality improves with larger models (e.g., `flan-t5-large`) or more training data.

## Results

- Training loss decreases steadily.
- Model can generate plausible responses for simple instructions.
- The pipeline is easily adaptable to any instruction dataset.

## Why This Matters

Fine‑tuning is a core skill for adapting LLMs to specific domains or tasks. This project proves you can:
- Load and preprocess instruction data.
- Fine‑tune a transformer model using standard libraries.
- Save and reload the model for inference.
- Evaluate the model qualitatively.

## Files

- `Fine‑tune_FLAN_T5_on_Instruction_Data.ipynb` – Complete notebook.
- `flan-t5-finetuned/` – Directory containing saved model and tokenizer (generated after training).
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – End‑to‑end LLM fine‑tuning.**