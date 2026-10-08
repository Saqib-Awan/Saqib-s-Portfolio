"""
Plotly Chart Builders and Anomaly Scoring Functions
"""

def compute_z_score_anomalies(values: list) -> list:
    return [i for i, v in enumerate(values) if v > 2.5]