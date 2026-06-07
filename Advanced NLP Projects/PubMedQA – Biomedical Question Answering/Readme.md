# PubMedQA – Biomedical Question Answering

**Author:** Saqib  

## Overview

This notebook implements a **biomedical question‑answering system** that answers clinical questions based on PubMed abstracts. Using a fine‑tuned BERT model, it classifies the question + abstract pair into **YES**, **NO**, or **MAYBE** – a task from the PubMedQA benchmark. This demonstrates how domain‑specific language models can support evidence‑based medicine and clinical decision support.

## Features

- 🩺 **Biomedical domain** – Trained on real PubMed question‑abstract pairs.
- 🎯 **3‑way classification** – YES / NO / MAYBE.
- 🧠 **Fine‑tuned BERT** – Uses `bert-base-uncased` with a classification head.
- 📚 **Dataset** – `bigbio/pubmed_qa` (Hugging Face).
- 📊 **Evaluation** – Accuracy, classification report (precision/recall/F1), confusion matrix.
- 💾 **Model export** – Save fine‑tuned model and tokenizer for inference.

## Dataset

- **Source:** `bigbio/pubmed_qa` on Hugging Face (subset of the original PubMedQA).
- **Splits:**  
  - Train: 450 samples  
  - Validation: 50 samples  
  - Test: 500 samples  
- **Format:** Each sample contains a `question`, a `context` (PubMed abstract), and a `label` (YES/NO/MAYBE).

## Architecture

1. **Model** – `bert-base-uncased` with a sequence classification head (3 classes).
2. **Preprocessing** – Combine `question` and `context` into a single text, truncate to 384 tokens.
3. **Fine‑tuning** – 3 epochs, learning rate 2e‑5, batch size 16.
4. **Evaluation** – Accuracy, per‑class precision/recall/F1.
5. **Inference** – Predict on new `(question, context)` pairs.

## Setup

- Google Colab (T4 GPU recommended for faster training).
- Libraries: `transformers`, `datasets`, `torch`, `scikit-learn`, `pandas`.

## How to Run

1. Open the notebook `PubMedQA_–_Biomedical_Question_Answering.ipynb` in Google Colab.
2. Run the installation cell (if any).
3. Run all cells sequentially:
   - Load PubMedQA dataset (auto‑download from Hugging Face).
   - Tokenise inputs.
   - Fine‑tune BERT (3 epochs, ~5–10 minutes on T4 GPU).
   - Evaluate on test set.
   - Display classification report and confusion matrix.
   - Save the fine‑tuned model (optional).
   - Test inference on a custom example.

## Example Interaction

**Question:** Does smoking cause lung cancer?  
**Context:** *[PubMed abstract summarising evidence on smoking and lung cancer]*  
**Prediction:** YES (confidence: 0.94)

**Question:** Is coffee consumption associated with reduced mortality?  
**Context:** *[Relevant abstract from PubMed]*  
**Prediction:** MAYBE (confidence: 0.67)

## Why This Matters

Biomedical QA has direct real‑world impact, helping clinicians and researchers quickly extract evidence from scientific literature. This project demonstrates:

- Fine‑tuning a transformer for a specialised domain (medicine).
- Working with a small, high‑quality dataset.
- Interpreting three‑way classification results.
- Building a reusable biomedical QA model.

## Results (Expected)

- **Test accuracy:** ~70–75% (on the 500‑sample test set).
- Better performance for `YES` and `NO` answers; `MAYBE` is often harder.
- Fine‑tuning significantly improves over zero‑shot baselines.

## Files

- `PubMedQA_–_Biomedical_Question_Answering.ipynb` – Full notebook.
- `pubmedqa_model/` – Saved fine‑tuned model and tokenizer.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Biomedical QA with BERT.**