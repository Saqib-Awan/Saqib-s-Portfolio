# Predictive Maintenance – Machine Failure Classification

**Author:** Saqib   

## Overview

This project predicts machine failure using sensor data (temperatures, rotational speed, torque, tool wear). By identifying failure precursors, manufacturers can reduce unplanned downtime. The notebook includes feature engineering (temperature difference, power), model comparison (Logistic Regression, Random Forest, XGBoost), hyperparameter tuning, and SHAP interpretation.

## Dataset

- **Source:** AI4I 2020 Predictive Maintenance Dataset (UCI)
- **Rows:** 10,000 sensor readings
- **Features:** Type (L/M/H), Air temperature, Process temperature, Rotational speed, Torque, Tool wear
- **Target:** Machine failure (binary)

## Visualisations Included

1. Overall failure rate (bar chart)  
2. Failure by machine type (bar chart)  
3. Temperature distributions (histogram)  
4. Rotational speed vs torque (scatter, coloured by failure)  
5. Tool wear vs failure (box plot)  
6. Correlation heatmap  
7. Feature importance (Random Forest)  
8. Confusion matrix (tuned XGBoost)  
9. ROC curve with AUC  
10. SHAP summary plot

## How to Run

1. Open the notebook in Google Colab.  
2. Run all cells sequentially.  
3. The dataset will be downloaded automatically from UCI.  

## Files

- `Predictive_Maintenance.ipynb` – Full notebook.  
- `README.md` – This file.  

## License

MIT – free to use and modify.

---

**© 2026 Saqib – Predictive maintenance classification.**