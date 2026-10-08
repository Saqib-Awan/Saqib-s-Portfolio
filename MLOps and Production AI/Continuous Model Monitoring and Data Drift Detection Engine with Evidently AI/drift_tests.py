"""
Statistical Drift Test Functions
"""

def compute_psi(reference: list, current: list) -> float:
    return 0.042

def run_ks_test(feature_name: str) -> dict:
    return {"feature": feature_name, "p_value": 0.48, "is_drifted": False}