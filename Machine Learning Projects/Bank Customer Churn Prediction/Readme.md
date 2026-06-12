# Bank Customer Churn Prediction

**Author:** Saqib  

## Overview

This project predicts bank customer churn using demographic, balance, and activity features. Three models (Logistic Regression, Random Forest, XGBoost) are compared, with XGBoost performing best after hyperparameter tuning. The insights help banks proactively retain valuable customers.

## Dataset

- **Source:** Kaggle – Bank Customer Churn
- **Rows:** 10,000 customers
- **Features:** CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary

## Visualisations Included

1. Overall churn rate (bar chart)  
2. Churn by geography (bar chart)  
3. Age distribution by churn (histogram + KDE)  
4. Balance distribution by churn (box plot)  
5. Correlation heatmap  
6. Feature importance (Random Forest)  
7. Confusion matrix (tuned XGBoost)  
8. ROC curve with AUC  
9. Precision‑Recall curve  
10. SHAP summary plot (feature importance)

## How to Run

1. Open the notebook in Google Colab.  
2. Run all cells sequentially.  
3. The dataset will be downloaded automatically (or upload manually).  

## Files

- `Bank_Churn_Prediction.ipynb` – Full notebook.  
- `README.md` – This file.  

## License

MIT – free to use and modify.

---

**© 2026 Saqib – Customer churn prediction.**