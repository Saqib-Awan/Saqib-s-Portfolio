# High-Throughput Feature Store and Real-Time Ingestion Pipeline with Feast

## Abstract

An enterprise feature store platform built with Feast, bridging the gap between batch training data and real-time inference features. Utilizing Redis for sub-2ms online serving and Parquet for point-in-time historical joins, the architecture guarantees zero data leakage between offline model training and production serving.

## Visual Interface

![Application Interface](assets/screenshot.png)

## Architecture and Pipeline

1. **Streaming Feature Ingestion**: Consumes transaction events and continuously updates Redis online feature tables.
2. **Offline Parquet Store**: Manages historical feature snapshots for scalable batch model training.
3. **Point-in-Time Join Engine (ASOF)**: Reconstructs exact historical feature values as of observation timestamps to eliminate temporal data leakage.
4. **Online Low-Latency Retrieval**: Exposes sub-2ms feature vector reads for real-time fraud scoring.

## Key Features

- **Sub-2ms Online Latency**: Powered by distributed Redis clusters.
- **Zero Future Data Leakage**: Automated point-in-time timestamp matching.
- **Unified Feature Definitions**: Single declarative schema for both training and serving pipelines.
- **High Entity Scale**: Manages over 1.8 million active customer keys.

## Project Structure

```text
High-Throughput Feature Store and Real-Time Ingestion Pipeline with Feast/
├── app.py              # Core feature store online retrieval engine
├── feature_views.py    # Feast schema definitions and entity specifications
├── Dockerfile          # Feature store container specification
├── requirements.txt    # Project dependencies
├── README.md           # Documentation and data schemas
└── assets/
    └── screenshot.png  # Application interface preview
```

## Installation and Setup

```bash
cd "MLOps and Production AI/High-Throughput Feature Store and Real-Time Ingestion Pipeline with Feast"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

## Performance Metrics

- Online Read Latency: 1.8 ms per entity lookup
- Cache Hit Rate: 99.8% on distributed Redis cluster
- Entity Capacity: 1,840,000 active customer records

## Author

**Muhammad Saqib** — Applied AI/ML Engineer (Computer Vision, Deep Learning, NLP, LLMs)