# COVID-19 Global Trends Analysis (Time Series & Geospatial)

**Author:** Saqib   

## Overview

This project analyses global COVID-19 pandemic data using the Our World in Data dataset. It covers daily cases, deaths, mortality rates, per‑capita metrics, and regional trends across continents. The notebook produces 10 professional visualisations, including time series, bar charts, heatmaps, stacked area charts, and an interactive choropleth map.

## Dataset

- **Source:** Our World in Data – COVID-19 (public)
- **Rows:** ~100,000 daily observations
- **Columns:** date, location, total_cases, new_cases, total_deaths, new_deaths, population, continent, iso_code

## Visualisations Included

1. Global daily new cases (with 7‑day moving average)
2. Global daily new deaths (with 7‑day moving average)
3. Top 10 countries by total cases
4. Top 10 countries by total deaths
5. Daily new cases stacked by continent
6. Mortality rate vs total cases bubble chart
7. Cases per million population (top 20)
8. Weekly new cases heatmap (selected countries)
9. 7‑day rolling average major countries
10. Interactive choropleth map (cases per million)

## How to Run

1. Open the notebook in Google Colab.
2. Run all cells sequentially.
3. The dataset will be auto‑downloaded from Our World in Data (no manual upload needed).

## Requirements

- pandas, matplotlib, seaborn, plotly

## Files

- `COVID_19_Global_Analysis.ipynb` – Full notebook.
- `README.md` – This file.

## License

MIT – free to use and modify.

---

**© 2026 Saqib – Global pandemic trends analysis.**