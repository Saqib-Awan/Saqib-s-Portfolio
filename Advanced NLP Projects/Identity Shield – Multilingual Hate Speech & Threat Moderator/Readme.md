# Identity Shield – Multilingual Hate Speech & Threat Moderator

**Author:** Saqib  

## Overview

This project builds a **multilingual hate speech detection system** that classifies text as **hate speech** or **non‑hate** across multiple languages. Using a combination of character‑based TF‑IDF vectorisation and logistic regression, the model is trained on a diverse dataset containing examples in English, Spanish, German, Italian, and other languages. The system is designed for real‑time content moderation on global platforms, helping to identify and flag harmful content regardless of language.

## Features

- 🌐 **Multilingual support** – Works on text in English, Spanish, German, Italian, and more.
- ⚖️ **Binary classification** – Hate speech vs non‑hate (labels: 1 = hate, 0 = non‑hate).
- 🔍 **Character‑level TF‑IDF** – Uses n‑grams of characters (n=1..3) to capture language‑agnostic patterns.
- 🤖 **Logistic Regression** – Fast, interpretable, and effective for this task.
- 📊 **Comprehensive evaluation** – Accuracy, precision, recall, F1, ROC‑AUC, confusion matrix.
- 📈 **Visualisations** – Word clouds for hate vs non‑hate, confusion matrix, ROC curve, top features.
- 💾 **Model export** – Save model and vectorizer for deployment on moderation APIs.

## Dataset

- **Source:** ISHate (Implicit Hate Speech) or similar multilingual hate speech corpus (e.g., HateBenchSet, HASOC, OffensEval).
- **Size:** Thousands of labeled examples across languages.
- **Labels:** Binary (0 = non‑hate / 1 = hate).
- **Languages:** English, Spanish, German, Italian, Arabic, etc. (varies by dataset).
- **Domain:** Social media comments, forum posts, tweets.

## Architecture

1. **Data loading** – Load multilingual text and labels (CSV or Parquet).
2. **Preprocessing** – Lowercase, remove URLs, special characters, digits (keeps letters and spaces).
3. **Exploratory Analysis** – Class distribution, text length by language, word clouds.
4. **Vectorisation** – Character‑based `TfidfVectorizer` (`analyzer='char_wb'`, ngram_range=(1,3)) to capture cross‑lingual patterns.
5. **Model** – Logistic Regression with `class_weight='balanced'` to handle potential class imbalance.
6. **Evaluation** – Standard metrics plus ROC‑AUC and per‑language breakdown if available.
7. **Interpretability** – Top character n‑grams that strongly indicate hate speech.

## Setup

- Google Colab (CPU works, GPU optional).
- Libraries: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `wordcloud`, `joblib`, `requests`.

## How to Run

1. Open the notebook `Identity_Shield_–_Multilingual_Hate_Speech_&_Threat_Moderator.ipynb` in Google Colab.
2. Run the installation cell.
3. The dataset loads automatically from Hugging Face / URL (no manual upload). If required, upload the dataset when prompted.
4. Run all cells sequentially:
   - Load and clean data.
   - Perform EDA (class distribution, word clouds).
   - Split into train/test.
   - Train logistic regression model.
   - Evaluate on test set.
   - Visualise confusion matrix and ROC curve.
5. Use the interactive inference cell to test custom text in various languages.

## Example Interaction

**Input (English):** *“You are a worthless piece of garbage, go die.”*  
**Prediction:** Hate speech (confidence: 0.92)

**Input (English):** *“I love learning new languages and meeting people.”*  
**Prediction:** Non‑hate (confidence: 0.96)

**Input (Spanish):** *“Eres un inútil, nadie te quiere.”*  
**Prediction:** Hate speech (confidence: 0.88)

**Input (German):** *“Der Kaffee ist köstlich, wirklich.”*  
**Prediction:** Non‑hate (confidence: 0.94)

## Why This Matters

Hate speech moderation on global platforms requires systems that work across languages. This project demonstrates:

- Language‑agnostic feature engineering using character n‑grams.
- Building a lightweight, fast model suitable for real‑time moderation.
- Handling multilingual data without requiring separate models per language.
- Creating a deployable tool for social media, forums, and chat applications.

## Results (Expected)

- **Test accuracy:** >85%
- **ROC‑AUC:** >0.92
- Precision/recall balanced across languages.
- Top indicators of hate speech: aggressive character patterns (e.g., “die”, “hate”, profanity n‑grams) across languages.

## Files

- `Identity_Shield_–_Multilingual_Hate_Speech_&_Threat_Moderator.ipynb` – Full notebook.
- `hate_speech_model.pkl` – Saved logistic regression model.
- `tfidf_vectorizer_hate.pkl` – Saved TF‑IDF vectorizer.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Multilingual hate speech detection.**