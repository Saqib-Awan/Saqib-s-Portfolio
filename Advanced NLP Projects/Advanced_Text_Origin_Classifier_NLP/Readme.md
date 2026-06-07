# Advanced Text Origin Classifier NLP (AI vs Human Text)

**Author:** Saqib  

## Overview

This project builds a **binary text classifier** that distinguishes between human‑written text and AI‑generated text (e.g., from GPT models, ChatGPT, or other LLMs). Using advanced NLP techniques including TF‑IDF with character n‑grams, stylometric features, and a fine‑tuned transformer model (BERT, RoBERTa, or DistilBERT), it achieves high accuracy on a diverse dataset of AI vs human examples.

The project uses the **ai_vs_human_text** dataset – a balanced collection of human‑authored passages and AI‑generated samples sourced from multiple domains (news, essays, creative writing, social media).

## Features

- 🧠 **Dual approach** – Classical ML (TF‑IDF + Logistic Regression) and fine‑tuned BERT.
- 🔍 **Stylometric features** – Includes punctuation, sentence length, word diversity, perplexity, and character n‑grams.
- ⚖️ **Balanced dataset** – Equal number of human and AI samples (typically 10,000+ each).
- 📊 **Comprehensive evaluation** – Accuracy, precision, recall, F1, ROC‑AUC, confusion matrix.
- 📈 **Visualisations** – Word clouds for human vs AI, feature importance, confusion matrix, ROC curve.
- 💾 **Model export** – Save the best model and vectorizer for deployment.

## Dataset

- **Source:** AI vs Human Text dataset (publicly available on Kaggle or Hugging Face).
- **Size:** ~20,000 examples (10,000 human, 10,000 AI).
- **Domains:** News articles, Reddit posts, essays, creative fiction, technical documentation.
- **AI models:** GPT‑2, GPT‑3, ChatGPT, Llama, or a mix.
- **Human sources:** Crowdsourced, Wikipedia, public domain literature.

## Architecture

### Baseline Model (ML)
1. **Text cleaning** – Lowercase, remove special characters and extra spaces.
2. **Feature extraction** – Character‑based TF‑IDF (ngram_range=(2,5)) to capture subtle stylistic patterns.
3. **Classifier** – Logistic Regression (fast, interpretable).

### Advanced Model (Transformer)
1. **Tokenisation** – BERT tokenizer (or RoBERTa) with max length 256.
2. **Model** – Fine‑tune `bert-base-uncased` for binary classification.
3. **Training** – 3 epochs, learning rate 2e-5, batch size 16.
4. **Evaluation** – Held‑out test set.

## Setup

- Google Colab (T4 GPU recommended for BERT fine‑tuning).
- Libraries: `transformers`, `datasets`, `scikit-learn`, `pandas`, `matplotlib`, `seaborn`, `wordcloud`.

## How to Run

1. Open the notebook `Advanced_Text_Origin_Classifier_NLP.ipynb` in Google Colab.
2. Run the installation cell.
3. Mount Google Drive or upload the `ai_vs_human_text.csv` dataset.
4. Run all cells sequentially:
   - Load and explore data.
   - Preprocess and clean text.
   - Train baseline model.
   - Fine‑tune BERT (10–20 minutes on T4 GPU).
   - Compare both models.
   - Visualise results.
5. Test the model on any custom text.

## Example Interaction

**Input text:** *“The quick brown fox jumps over the lazy dog. This is a classic pangram.”*  
**Prediction:** Human‑written (confidence: 0.87)

**Input text:** *“As an AI language model, I generate text based on patterns in my training data. The sky is blue because of Rayleigh scattering.”*  
**Prediction:** AI‑generated (confidence: 0.94)

## Why This Matters

With the rise of LLMs, detecting AI‑generated content is critical for education, journalism, content moderation, and preventing misinformation. This project demonstrates:

- Building classifiers that go beyond simple keyword matching.
- Using character n‑grams to capture AI‑specific quirks (e.g., repetitive patterns, unusual punctuation).
- Fine‑tuning a transformer for a real‑world binary classification task.
- Comparing classical ML vs deep learning for text origin detection.

## Results (Expected)

- **Logistic Regression (char TF‑IDF):** Accuracy ~92%, ROC‑AUC ~0.97.
- **Fine‑tuned BERT:** Accuracy ~97%, ROC‑AUC ~0.99.
- Top indicators of AI text: excessive use of “the”, “it”, “is”, “as”, “to” (high frequency function words), lower lexical diversity.

## Files

- `Advanced_Text_Origin_Classifier_NLP.ipynb` – Full notebook.
- `ai_vs_human_text.csv` – Dataset (not included; download separately).
- `bert_origin_classifier/` – Saved fine‑tuned model and tokenizer.
- `tfidf_vectorizer.pkl` – Saved TF‑IDF vectorizer.
- `idf_logreg_model.pkl` – Saved logistic regression model.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Advanced text origin detection (AI vs human).**