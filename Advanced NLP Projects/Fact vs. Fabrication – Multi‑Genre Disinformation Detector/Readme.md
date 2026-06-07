# Fact vs Fabrication – Multi‑Genre Disinformation Detector

**Author:** Saqib   

## Overview

This project builds a **fake news detection system** that classifies news articles as either **FAKE** or **REAL**. Using natural language processing and machine learning, the system analyses article text and predicts its veracity. It serves as a tool to combat misinformation across multiple news genres (politics, entertainment, science, etc.). The project uses a balanced dataset of labelled fake and real news articles.

## Features

- 📰 **Binary classification** – FAKE (0) vs REAL (1).
- 🔍 **TF‑IDF vectorisation** – Converts text to numerical features (unigrams + bigrams).
- 🤖 **Logistic Regression model** – Fast, interpretable, high‑accuracy baseline.
- 📊 **Comprehensive evaluation** – Accuracy, precision, recall, F1, ROC‑AUC, confusion matrix.
- 📈 **Visualisations** – Word clouds for fake vs real, confusion matrix, ROC curve, top predictive features.
- 💾 **Model export** – Save model and vectorizer for deployment.

## Dataset

- **Source:** Fake vs Real News Dataset (Kaggle).
- **Files:** `Fake.csv` (fake news), `True.csv` (real news).
- **Size:** ~4,500 fake articles, ~4,500 real articles (total ~9,000).
- **Columns:** `title`, `text`, `subject`, `date`, `label` (added after merging).
- **Genres:** Politics, world news, entertainment, technology, etc.

## Architecture

1. **Data loading** – Load both CSV files, add label column (0 for fake, 1 for real), concatenate.
2. **Data cleaning** – Combine title + text, remove special characters, lowercase, strip extra spaces.
3. **Exploratory Analysis** – Class balance, text length distribution, word clouds.
4. **Train/test split** – 80/20 stratified split.
5. **Vectorisation** – TF‑IDF with max 10,000 features, (1,2) n‑grams.
6. **Model training** – Logistic Regression (`liblinear` solver, class_weight='balanced').
7. **Evaluation** – Test set metrics, confusion matrix, ROC curve.
8. **Interpretability** – Top 20 words indicative of fake vs real news.

## Setup

- Google Colab (CPU works, GPU not required).
- Libraries: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `wordcloud`, `joblib`.

## How to Run

1. Open the notebook `Fact_vs_Fabrication_–_Multi‑Genre_Disinformation_Detector.ipynb` in Google Colab.
2. Run the installation cell.
3. Upload or mount the `Fake.csv` and `True.csv` files.
4. Run all cells sequentially:
   - Load and combine datasets.
   - Clean and preprocess text.
   - Perform EDA (word clouds, length analysis).
   - Train logistic regression model.
   - Evaluate on test set.
   - Display top predictive features.
5. Test the model on new article text.

## Example Interaction

**Input headline:** *“Breaking: Scientists discover cure for all cancers – clinical trials starting next month.”*  
**Prediction:** REAL (confidence: 0.92)

**Input headline:** *“SHOCKING: Government hiding alien evidence from public, whistleblower reveals.”*  
**Prediction:** FAKE (confidence: 0.88)

## Why This Matters

Misinformation spreads rapidly online, causing real‑world harm. Automated fake news detection helps:

- Flag suspicious articles for human fact‑checkers.
- Integrate with browser extensions or social media filters.
- Understand linguistic patterns of deceptive news.

This project demonstrates:
- End‑to‑end classical NLP pipeline.
- Model interpretability (top words per class).
- Deployment‑ready binary classifier.

## Results (Expected)

- **Test accuracy:** ~95%
- **ROC‑AUC:** ~0.98
- Top fake indicators: words like “shocking”, “exposed”, “alert”, “must read”.
- Top real indicators: proper nouns, “said”, “reported”, quotes.

## Files

- `Fact_vs_Fabrication_–_Multi‑Genre_Disinformation_Detector.ipynb` – Full notebook.
- `Fake.csv` / `True.csv` – Dataset files.
- `fake_news_model.pkl` – Saved logistic regression model.
- `tfidf_vectorizer_fake.pkl` – Saved TF‑IDF vectorizer.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Fake news detection.**