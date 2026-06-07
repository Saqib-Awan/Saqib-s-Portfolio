# Advanced Human vs AI Text Classifier using NLP and BERT

**Author:** Saqib  

## Overview

This project builds a **binary text classifier** that distinguishes between human‑written text and AI‑generated text (e.g., from ChatGPT, GPT‑4, or similar models). Using a fine‑tuned BERT model, the system achieves high accuracy on a diverse dataset of human and AI samples. It is part of Saqib’s advanced NLP portfolio.

## Features

- 🤖 **State‑of‑the‑art model** – Fine‑tunes BERT (`bert-base-uncased`) for sequence classification.
- 📚 **Balanced dataset** – Contains thousands of human‑written and AI‑generated passages.
- 📊 **Comprehensive evaluation** – Accuracy, precision, recall, F1, confusion matrix, ROC‑AUC.
- 📈 **Visualisations** – Training curves, confusion matrix, ROC curve, and word clouds.
- 💾 **Model export** – Save fine‑tuned model and tokenizer for deployment.

## Architecture

1. **Data loading** – Load human and AI text samples (CSV or Hugging Face dataset).
2. **Preprocessing** – Clean text (lowercase, remove special characters, etc.).
3. **Tokenisation** – BERT tokenizer with padding/truncation to fixed length.
4. **Model** – `bert-base-uncased` with a classification head (2 classes).
5. **Training** – Fine‑tune using AdamW with learning rate scheduling.
6. **Evaluation** – Hold‑out test set with detailed metrics.
7. **Inference** – Predict on new text snippets.

## Setup

- Google Colab (T4 GPU recommended for faster training).
- Hugging Face `transformers`, `datasets`, PyTorch.

## How to Run

1. Open the notebook `Advanced_Human_vs_AI_Text_Classifier_using_NLP_and_BERT.ipynb` in Google Colab.
2. Run the installation cell.
3. Mount Google Drive (optional, for dataset/model persistence).
4. Run all cells sequentially:
   - Load dataset (auto‑downloaded from Hugging Face or uploaded manually).
   - Preprocess and tokenise.
   - Fine‑tune BERT (10‑20 minutes on T4 GPU).
   - Evaluate on test set.
   - Visualise results.
5. Test the model on your own text samples.

## Example Interaction

**Input text:** *“The quick brown fox jumps over the lazy dog. This is a classic pangram used to demonstrate fonts.”*  
**Prediction:** Human‑written (confidence: 0.92)

**Input text:** *“As an AI language model, I can generate text based on patterns in the data I was trained on. Here is an example paragraph.”*  
**Prediction:** AI‑generated (confidence: 0.89)

## Why This Matters

With the proliferation of LLMs, detecting AI‑generated content is critical for education, journalism, and content moderation. This project demonstrates:

- Fine‑tuning a transformer for a real‑world binary classification task.
- Handling imbalanced or balanced datasets.
- Evaluating models using multiple metrics.
- Saving and deploying a production‑ready classifier.

## Files

- `Advanced_Human_vs_AI_Text_Classifier_using_NLP_and_BERT.ipynb` – Full notebook.
- `bert_human_ai_model/` – Saved fine‑tuned model and tokenizer (generated after training).
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Human vs AI text detection with BERT.**