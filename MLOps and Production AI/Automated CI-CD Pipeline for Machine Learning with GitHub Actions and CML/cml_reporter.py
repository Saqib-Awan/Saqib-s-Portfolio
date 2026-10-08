"""
CML Markdown Comment Generator
"""

def generate_cml_report(baseline_auc: float, new_auc: float) -> str:
    return (
        f"## Model Quality Gate\n"
        f"| Metric | Baseline | Candidate | Delta |\n"
        f"| :--- | :--- | :--- | :--- |\n"
        f"| ROC-AUC | {baseline_auc:.3f} | {new_auc:.3f} | +{new_auc-baseline_auc:.3f} |\n"
    )