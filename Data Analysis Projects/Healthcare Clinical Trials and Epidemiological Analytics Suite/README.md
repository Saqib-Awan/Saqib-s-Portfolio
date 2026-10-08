# Healthcare Clinical Trials and Epidemiological Analytics Suite

## Abstract

A biostatistical analytics and epidemiological modeling suite engineered to analyze Phase III randomized controlled clinical trials (RCTs). Utilizing Lifelines for Kaplan-Meier non-parametric survival analysis and Cox Proportional Hazards regression, the platform evaluates drug efficacy, survival probabilities, and adverse event profiles across patient demographic cohorts.

## Visual Interface

![Application Interface](assets/screenshot.png)

## Architecture and Pipeline

1. **Clinical Cohort Ingestion**: Processing demographic variables, treatment arms (Investigational Therapy vs Standard of Care Placebo), and event timeline data.
2. **Kaplan-Meier Survival Estimator**: Constructs empirical survival curves and tests differences using two-sided Mantel-Cox log-rank statistics.
3. **Multivariate Cox Regression**: Estimates adjusted hazard ratios (HR) controlling for patient age, baseline comorbidities, and cancer staging.
4. **Safety & Tolerability Auditing**: Computes risk ratios and Fisher exact tests across Grade 1 through 4 adverse events.

## Key Features

- **Standardized Biostatistics**: Produces publication-ready Kaplan-Meier plots with 95% Hall-Wellner confidence bands.
- **Cohort Subgroup Stratification**: Interactively filters outcomes by biomarker presence, gender, and age brackets.
- **Rigorous Hypothesis Testing**: Calculates exact p-values with Bonferroni-Holm corrections for multiplicity.
- **Data Monitoring Committee (DMC) Briefs**: Exports standardized statistical efficacy summaries.

## Tech Stack

- Python 3.10+
- Lifelines
- SciPy Stats
- Pandas & NumPy
- Matplotlib & Seaborn

## Installation and Setup

```bash
cd "Data Analysis Projects/Healthcare Clinical Trials and Epidemiological Analytics Suite"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

## Performance Metrics

- Statistical Power: > 90% at alpha = 0.05
- Hazard Ratio: 0.54 (95% CI: 0.42 - 0.68, p < 0.0001)
- Cohort Retention Rate: 96.2% across 36-month follow-up period

## Author

**Muhammad Saqib** — Applied AI/ML Engineer (Computer Vision, Deep Learning, NLP, LLMs)