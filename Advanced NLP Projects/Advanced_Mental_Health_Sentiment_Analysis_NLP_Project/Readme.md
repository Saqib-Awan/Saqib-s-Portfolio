# Advanced Mental Health Sentiment Analysis NLP Project (Combined Data)

**Author:** Saqib  

## Overview

This project performs **sentiment analysis** on mental health‑related text data (e.g., social media posts, therapy transcripts, or self‑reported statements). Using a combination of traditional machine learning (TF‑IDF + Logistic Regression) and a fine‑tuned BERT model, it classifies text into categories such as *anxiety*, *depression*, *normal*, *suicidal ideation*, or *stress*. The “Combined Data” refers to merging multiple public datasets to create a robust, generalised classifier.

## Features

- 🧠 **Multi‑class classification** – Detects various mental health conditions (4–6 classes).
- 📚 **Combined dataset** – Aggregates data from sources like Reddit, Twitter, and clinical transcripts.
- ⚖️ **Class balancing** – Handles imbalanced data using oversampling or class weights.
- 🤖 **Two‑model approach** – Fast TF‑IDF + Logistic Regression baseline and high‑accuracy BERT fine‑tuned model.
- 📊 **Professional evaluation** – Accuracy, precision, recall, F1, confusion matrix, ROC‑AUC (macro/micro).
- 📈 **Visualisations** – Word clouds, class distribution bar chart, confusion matrix heatmap, ROC curves.

## Architecture

1. **Data loading & cleaning** – Load CSV/JSON files, combine them, clean text (remove URLs, special characters, lowercasing).
2. **Exploratory Data Analysis** – Class distribution, text length analysis, word clouds per class.
3. **Baseline model** – TF‑IDF vectorisation + Logistic Regression (fast, interpretable).
4. **Advanced model** – Fine‑tune `bert-base-uncased` for sequence classification.
5. **Evaluation** – Compare both models on a held‑out test set.
6. **Inference** – Predict sentiment of any new text snippet.

## Combined Data Sources (Examples)

- **Reddit Mental Health Dataset** (r/depression, r/anxiety, r/SuicideWatch)
- **CLPsych** shared task data
- **Twitter mental health** corpus
- **DAIC‑WOZ** (clinical interviews)

The final combined dataset contains thousands of labelled examples across mental health categories.

## Setup

- Google Colab (T4 GPU recommended for BERT fine‑tuning).
- Hugging Face `transformers`, `datasets`, `scikit-learn`, `pandas`, `matplotlib`, `seaborn`.

## How to Run

1. Open the notebook `Advanced_Mental_Health_Sentiment_Analysis_NLP_Project.ipynb` in Google Colab.
2. Run the installation cell.
3. Mount Google Drive (if dataset is stored there) or upload the combined CSV file.
4. Run all cells sequentially:
   - Load and combine data.
   - Clean and preprocess.
   - Train baseline model.
   - Fine‑tune BERT (10–20 minutes on T4 GPU).
   - Evaluate both models.
   - Visualise results.
5. Test the model on custom text input.

## Example Interaction

**Input text:** *“I feel so hopeless and tired all the time. Nothing brings me joy anymore.”*  
**Prediction:** Depression (confidence: 0.94)

**Input text:** *“My heart is racing and I can’t stop worrying about the presentation tomorrow.”*  
**Prediction:** Anxiety (confidence: 0.89)

**Input text:** *“I had a great day at the park with friends. Feeling grateful.”*  
**Prediction:** Normal / Healthy (confidence: 0.91)

## Why This Matters

Mental health sentiment analysis is a socially impactful NLP application. This project demonstrates:

- Combining multiple messy real‑world datasets.
- Handling multi‑class imbalance.
- Building both baseline and state‑of‑the‑art models.
- Evaluating performance using clinically meaningful metrics.
- Creating a tool that could assist therapists, moderators, or early warning systems.

## Files

- `Advanced_Mental_Health_Sentiment_Analysis_NLP_Project.ipynb` – Full notebook.
- `combined_mental_health_data.csv` – Aggregated dataset (not included, but instructions to build it are in the notebook).
- `bert_mental_health_model/` – Saved fine‑tuned model and tokenizer.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Mental health sentiment analysis with combined data.**