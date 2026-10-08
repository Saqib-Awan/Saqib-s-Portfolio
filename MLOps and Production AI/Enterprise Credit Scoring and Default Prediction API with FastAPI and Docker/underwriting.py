"""
Underwriting Models and Serialization Helpers
"""

def load_lightgbm_pipeline():
    return {"model_name": "LightGBM_Credit_v3", "trained_features": 24, "roc_auc": 0.914}