# Financial News Sentiment Classification using NLP and ML

**Author:** Saqib  

## Overview

This project builds a **sentiment classification system** for financial news headlines. Given a news headline about a company, stock, or economic event, the model predicts whether the sentiment is **positive**, **negative**, or **neutral**. This is a critical tool for algorithmic trading, market analysis, and risk management. The system uses traditional NLP (TF‑IDF) and machine learning (Logistic Regression, Random Forest) to achieve high accuracy on financial text data.

## Features

- 📊 **Multi‑class classification** – Positive, Negative, Neutral.
- 📰 **Financial domain focus** – Trained on real‑world financial news headlines.
- 🔍 **TF‑IDF vectorisation** – Converts text to numerical features (unigrams + bigrams).
- 🤖 **Multiple classifiers** – Logistic Regression, Random Forest, and XGBoost (optional).
- 📈 **Professional evaluation** – Accuracy, precision, recall, F1‑score, confusion matrix.
- 📉 **Visualisations** – Confusion matrix heatmap, class distribution bar chart, top features per class.
- 💾 **Model export** – Save the best model and vectorizer for deployment.

## Dataset

- **Source:** Financial News Headlines dataset (commonly from Kaggle – `all-data.csv`).
- **Size:** ~5,000 financial news headlines.
- **Classes:** Positive (~1,500), Neutral (~2,000), Negative (~1,500).
- **Format:** CSV with columns: `sentiment` (positive/negative/neutral) and `headline` (text).
- **Domain:** News about stocks, earnings, economic indicators, company announcements.

## Architecture

1. **Data loading** – Load CSV, map sentiment strings to numeric labels (0=negative, 1=neutral, 2=positive).
2. **Preprocessing** – Lowercase, remove punctuation, numbers, special characters, and stopwords (optional).
3. **Exploratory Data Analysis** – Class balance, headline length distribution, word clouds per sentiment.
4. **Feature extraction** – TF‑IDF with max features 10,000, n‑gram range (1,2).
5. **Model training** – Train/test split (80/20), train Logistic Regression (baseline) and Random Forest.
6. **Evaluation** – Accuracy, precision, recall, F1, confusion matrix.
7. **Interpretability** – Display top words per sentiment class using model coefficients (Logistic Regression).

## Setup

- Google Colab (CPU works, GPU optional).
- Libraries: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `wordcloud`, `joblib`.

## How to Run

1. Open the notebook `Financial_News_Sentiment_Classification_using_NLP_and_ML.ipynb` in Google Colab.
2. Run the installation cell.
3. Upload or mount the `all-data.csv` file (or the dataset provided).
4. Run all cells sequentially:
   - Load and clean data.
   - Perform EDA (class balance, word clouds).
   - Vectorise headlines.
   - Train and evaluate models.
   - Visualise confusion matrix and top features.
5. Test the model on new financial headlines.

## Example Interaction

**Input headline:** *“Apple stock surges after record quarterly earnings”*  
**Prediction:** Positive (confidence: 0.94)

**Input headline:** *“Company reports layoffs amid slowing demand”*  
**Prediction:** Negative (confidence: 0.89)

**Input headline:** *“Federal Reserve announces interest rate decision”*  
**Prediction:** Neutral (confidence: 0.76)

## Why This Matters

Sentiment analysis of financial news is widely used in quantitative finance and algorithmic trading. This project demonstrates:

- Domain‑specific text classification (finance is a specialised language domain).
- Handling multi‑class imbalance (neutral can be the majority class).
- Building interpretable models (top words per sentiment).
- Creating a deployable tool for market sentiment monitoring.

## Results (Expected)

- **Logistic Regression:** Accuracy ~90%, macro F1 ~0.88.
- **Random Forest:** Accuracy ~92%, macro F1 ~0.90.
- Top positive indicators: “surge”, “record”, “profit”, “upgrade”, “beat”.
- Top negative indicators: “drop”, “loss”, “layoff”, “decline”, “warning”.
- Top neutral indicators: “announcement”, “meeting”, “report”, “updated”, “forecast”.

## Files

- `Financial_News_Sentiment_Classification_using_NLP_and_ML.ipynb` – Full notebook.
- `all-data.csv` – Dataset (not included; download from Kaggle or provided data folder).
- `sentiment_model.pkl` – Saved best model.
- `tfidf_vectorizer.pkl` – Saved TF‑IDF vectorizer.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Financial news sentiment classification.**