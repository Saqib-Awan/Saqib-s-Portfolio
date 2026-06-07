# Jigsaw Toxic Comment Classifier

**Author:** Saqib  

## Overview

This project implements a **multi‑label toxicity detection system** that identifies different types of toxic content in online comments. The model predicts six distinct toxicity attributes:  
`toxic`, `severe_toxic`, `obscene`, `threat`, `insult`, and `identity_hate`.  

It uses a **multi‑output logistic regression** model with TF‑IDF features, trained on the Jigsaw Toxic Comment Classification Challenge dataset (Wikipedia talk page edits). The system is designed for content moderation platforms to flag harmful comments automatically.

## Features

- 🧹 **Multi‑label classification** – One binary prediction per toxicity type.
- 📊 **TF‑IDF vectorisation** – Unigrams + bigrams with 10,000 features.
- 🤖 **Multi‑output Logistic Regression** – Fast, interpretable, well‑suited for sparse text.
- 📈 **Evaluation** – ROC‑AUC per label, confusion matrices, classification reports.
- 🎨 **Visualisations** – Label distribution, correlation heatmap, word clouds, ROC curves.
- 💾 **Model export** – Save trained model, vectorizer, and label columns for deployment.
- 📝 **Kaggle submission** – Generates probability predictions in the required format.

## Dataset

- **Source:** Jigsaw Toxic Comment Classification Challenge (Kaggle).
- **Files:** `train.csv`, `test.csv`, `test_labels.csv`, `sample_submission.csv`.
- **Training size:** ~160,000 comments.
- **Test size:** ~153,000 comments.
- **Labels:** 6 binary columns (`toxic`, `severe_toxic`, `obscene`, `threat`, `insult`, `identity_hate`).
- **Comments:** Wikipedia talk page edits, anonymised.

## Architecture

1. **Data loading** – Upload the four CSV files (via Colab file upload).
2. **Exploratory Data Analysis** – Check label frequency, correlations, and clean vs toxic word clouds.
3. **Text cleaning** – Lowercase, remove URLs, special characters, extra spaces.
4. **TF‑IDF vectorisation** – `max_features=10000`, `ngram_range=(1,2)`, `stop_words='english'`.
5. **Model training** – `MultiOutputClassifier(LogisticRegression(class_weight='balanced'))`.
6. **Evaluation** – ROC‑AUC per label, confusion matrices for top labels.
7. **Inference** – Predict probabilities for test set (with –1 filtering).
8. **Kaggle submission** – Export `submission.csv`.

## Setup

- Google Colab (CPU works, GPU optional).
- Libraries: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `wordcloud`, `joblib`.

## How to Run

1. Open the notebook `Jigsaw_Toxic_Comment_Classifier.ipynb` in Google Colab.
2. Run the installation cell (if any).
3. Run the cell to upload the four zip files (`train.csv.zip`, `test.csv.zip`, `test_labels.csv.zip`, `sample_submission.csv.zip`).
4. The notebook will automatically unzip and load the data.
5. Run all cells sequentially:
   - Explore data (label distribution, correlation, word clouds).
   - Clean text and vectorise.
   - Train the model (2–3 minutes on CPU).
   - Evaluate on test set (ROC‑AUC, confusion matrix).
   - Generate submission file.
6. Download `submission.csv` and upload to Kaggle for leaderboard score.

## Example Output (Scores)
ROC-AUC per label:
toxic : 0.98
severe_toxic : 0.97
obscene : 0.98
threat : 0.95
insult : 0.97
identity_hate : 0.96

Average ROC-AUC: 0.97

text

## Why This Matters

Online platforms need automated moderation to scale. This project demonstrates:

- Multi‑label text classification in a production context.
- Handling imbalanced labels with `class_weight`.
- Using TF‑IDF effectively for large‑scale text.
- Creating Kaggle‑compatible predictions.
- Visualising model performance for each toxicity type.

## Files

- `Jigsaw_Toxic_Comment_Classifier.ipynb` – Full notebook.
- `toxic_model.pkl` – Trained multi‑output model.
- `tfidf_vectorizer.pkl` – Fitted TF‑IDF transformer.
- `label_columns.pkl` – List of target label names.
- `submission.csv` – Predictions for Kaggle leaderboard.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Multi‑label toxicity classification.**