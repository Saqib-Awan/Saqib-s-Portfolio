# Customer Churn Prediction & Exploratory Analysis (Telco Dataset)

**Author:** Saqib  

## Overview

This project analyses customer churn for a telecommunications company. It uses the IBM Telco Customer Churn dataset to identify key factors leading to churn (e.g., contract type, monthly charges, payment method) and builds a logistic regression model to predict churn. The notebook contains 10 professional visualisations and a complete machine learning pipeline.

## Dataset

- **Source:** IBM Telco Customer Churn (Kaggle)
- **Records:** 7,043 customers
- **Features:** Tenure, MonthlyCharges, TotalCharges, ContractType, InternetService, PaymentMethod, Churn (target)

## Visualisations Included

1. Churn rate (overall and by contract type)
2. Tenure distribution by churn
3. Monthly charges box plot
4. Correlation heatmap
5. Churn by payment method (stacked bar)
6. Churn by internet service type
7. Total vs monthly charges scatter
8. Tenure vs monthly charges scatter
9. Feature importance from logistic regression
10. Confusion matrix

## How to Run

1. Open the notebook in Google Colab.
2. Run all cells sequentially.
3. The dataset will be loaded from a public URL (or upload manually if needed).

## Results

- **Test accuracy:** ~80%  
- **Top churn drivers:** Month‑to‑month contracts, high monthly charges, electronic check payment, fibre optic internet.  
- Low tenure strongly correlates with churn.

## Files

- `Telco_Churn_Analysis.ipynb` – Full notebook.
- `README.md` – This file.

## License

MIT – free to use and modify.

---

**© 2026 Saqib – Telco churn prediction and insights.**