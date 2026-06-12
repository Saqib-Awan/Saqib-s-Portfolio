# Wine Quality Prediction – EDA & Classification

**Author:** Saqib   

## Overview

This project analyses physicochemical properties of red and white wine to predict quality scores. Using random forest classification, it identifies which chemical features (alcohol, volatile acidity, sulphates) most influence perceived quality. The insights help winemakers focus on key attributes.

## Dataset

- **Source:** UCI Wine Quality Dataset  
- **Rows:** 6,497 samples (red + white)  
- **Features:** fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, quality (0-10)

## Visualisations Included

1. Quality score distribution (bar chart)  
2. Quality by wine type (violin plot)  
3. Alcohol vs quality (scatter with trend)  
4. Volatile acidity vs quality (box plot)  
5. Citric acid distribution by quality (histogram)  
6. pH vs quality (box plot)  
7. Correlation heatmap  
8. Feature importance (random forest)  
9. Confusion matrix  
10. Pairplot of top 4 features

## How to Run

1. Open the notebook in Google Colab.  
2. Run all cells sequentially.  
3. The dataset will be downloaded automatically from UCI.  

## Results

- **Best predictor:** Alcohol content (correlation 0.48 with quality)  
- **Random forest accuracy:** ~75% for binary classification (good vs poor)  
- **Top features:** alcohol, volatile acidity, sulphates, citric acid

## Files

- `Wine_Quality_Analysis.ipynb` – Full notebook.  
- `README.md` – This file.  

## License

MIT – free to use and modify.

---

**© 2026 Saqib – Wine quality prediction.**