# Advanced Resume Screening System using NLP and ML (UpdatedResumeDataSet)

**Author:** Saqib   

## Overview

This project builds an **intelligent resume screening system** that automatically classifies resumes into job categories (e.g., Data Scientist, Software Engineer, HR, Marketing, etc.). Using natural language processing and machine learning, the system extracts relevant features from unstructured resume text and predicts the most suitable job role. This helps HR teams filter large volumes of applications efficiently.

The project uses the **UpdatedResumeDataSet** – a curated collection of resumes labeled with 20+ job categories.

## Features

- 📄 **Resume parsing** – Extracts text from PDF, DOC, DOCX, and TXT formats.
- 🧹 **Text preprocessing** – Removes emails, URLs, digits, stopwords, and performs lemmatization.
- 🔍 **TF‑IDF vectorisation** – Converts text into numerical features.
- 🤖 **Multi‑class classification** – Predicts one of 20+ job categories.
- 📊 **Model comparison** – Evaluates Logistic Regression, Random Forest, SVM, and XGBoost.
- 📈 **Visualisations** – Word clouds per category, confusion matrix, top features per class.
- 💾 **Model export** – Save the best model and vectorizer for deployment.

## Dataset

- **Source:** UpdatedResumeDataSet (from Kaggle).
- **Size:** ~2,500 resumes.
- **Categories:** 20+ job roles (Data Science, Java Developer, HR, Sales, DevOps, etc.).
- **Format:** CSV with columns: `Category`, `Resume`.

## Architecture

1. **Data loading** – Load CSV containing resume text and category labels.
2. **Text cleaning** – Remove noise (emails, URLs, numbers, stopwords), lemmatize.
3. **Feature extraction** – TF‑IDF with n‑gram range (1,2) and max features 5,000.
4. **Train/test split** – Stratified split (80/20).
5. **Model training** – Multiple classifiers (Logistic Regression, Random Forest, SVM, XGBoost).
6. **Evaluation** – Accuracy, precision, recall, F1, confusion matrix.
7. **Interpretability** – Top words per category (logistic regression coefficients).

## Setup

- Google Colab (GPU optional, CPU works).
- Libraries: `pandas`, `scikit-learn`, `pickle`, `matplotlib`, `seaborn`, `nltk`.

## How to Run

1. Open the notebook `Advanced_Resume_Screening_System_using_NLP_and_ML.ipynb` in Google Colab.
2. Run the installation cell.
3. Upload or mount the `UpdatedResumeDataSet.csv` file.
4. Run all cells sequentially:
   - Load and clean data.
   - Preprocess resume text.
   - Train and evaluate multiple models.
   - Visualise results.
5. Test the model on a new resume (upload a file or paste text).

## Example Interaction

**Input resume (excerpt):** *“Experienced data scientist with Python, SQL, and machine learning. Built predictive models using scikit-learn and TensorFlow.”*  
**Predicted category:** Data Science

**Input resume (excerpt):** *“HR generalist with 5 years of experience in recruitment, employee relations, and performance management.”*  
**Predicted category:** HR

## Why This Matters

Automated resume screening saves time and reduces bias in recruitment. This project demonstrates:

- Practical NLP for real‑world HR applications.
- Multi‑class text classification at scale.
- Comparing multiple ML algorithms.
- Extracting interpretable features (top words per role).
- Building a deployable system.

## Results (Expected)

- **Best model:** XGBoost or Random Forest.
- **Test accuracy:** ~85–95% depending on dataset size.
- **Top performing categories:** Data Science, Java Developer, DevOps.

## Files

- `Advanced_Resume_Screening_System_using_NLP_and_ML.ipynb` – Full notebook.
- `UpdatedResumeDataSet.csv` – Dataset (download from Kaggle).
- `resume_screening_model.pkl` – Saved best model.
- `tfidf_vectorizer.pkl` – Saved TF‑IDF vectorizer.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – AI‑powered resume screening system.**