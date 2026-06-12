# Credit Card Fraud Detection

**Author:** Saqib   

## Overview

This project detects fraudulent credit card transactions using machine learning. The dataset is highly imbalanced (0.17% fraud). Techniques include SMOTE oversampling, scaling, and training multiple classifiers (Logistic Regression, Random Forest, XGBoost). Evaluation focuses on precision‑recall curves and AUC‑PR, which are more meaningful than accuracy for imbalanced problems.

## Dataset

- **Source:** Kaggle – Credit Card Fraud Detection
- **Rows:** 284,807 transactions
- **Features:** Time, V1…V28 (PCA), Amount
- **Target:** 0 = legitimate, 1 = fraud

## Visualisations Included

1. Class distribution (bar chart)  
2. Amount distribution by class (box plot)  
3. Transaction time distribution (histogram)  
4. Correlation heatmap (top features)  
5. Feature importance (Random Forest)  
6. Confusion matrix  
7. ROC curve with AUC  
8. Precision‑Recall curve with AUC‑PR  
9. SHAP summary plot  
10. Threshold analysis (precision/recall vs threshold)

## How to Run

1. Open the notebook in Google Colab.  
2. Run all cells sequentially.  
3. The dataset will be downloaded automatically (or upload `creditcard.csv`).  

## Results

- **Best model:** Tuned XGBoost  
- **ROC-AUC:** > 0.97  
- **PR-AUC:** ~ 0.80  
- Optimal threshold balances false positives and missed fraud.

## Files

- `Credit_Card_Fraud_Detection.ipynb` – Full notebook.  
- `README.md` – This file.  

## License

MIT – free to use and modify.

---

**© 2026 Saqib – Fraud detection system.**