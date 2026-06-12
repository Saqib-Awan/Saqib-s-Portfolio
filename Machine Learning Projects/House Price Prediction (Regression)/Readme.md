# House Price Prediction (Regression)

**Author:** Saqib  

## Overview

This project predicts house sale prices using the Ames Housing dataset. It includes data cleaning, feature engineering, handling missing values, and training regression models (Linear Regression, Ridge, Lasso, Random Forest, XGBoost). The final tuned XGBoost model achieves strong R² and low MAE. The notebook contains 10 professional visualisations.

## Dataset

- **Source:** Kaggle – House Prices: Advanced Regression Techniques
- **Rows:** 1,460 training examples
- **Features:** 80 (numeric and categorical)

## Visualisations Included

1. SalePrice distribution (histogram + KDE)  
2. Log‑transformed SalePrice distribution  
3. Correlation heatmap (top 15 features)  
4. GrLivArea vs SalePrice (scatter + regression line)  
5. OverallQual vs SalePrice (box plot)  
6. YearBuilt vs SalePrice (scatter)  
7. Missing values bar chart  
8. Residual plot (predicted vs residuals)  
9. Actual vs Predicted scatter (back‑transformed)  
10. SHAP summary plot

## How to Run

1. Open the notebook in Google Colab.  
2. Run all cells sequentially.  
3. The dataset will be downloaded automatically (or upload `train.csv` manually).  

## Results

- **Best model:** Tuned XGBoost  
- **MAE (log scale):** ~0.15 (≈ $16,000 in original price)  
- **R²:** ~0.88

## Files

- `House_Price_Prediction.ipynb` – Full notebook.  
- `README.md` – This file.  

## License

MIT – free to use and modify.

---

**© 2026 Saqib – House price regression.**