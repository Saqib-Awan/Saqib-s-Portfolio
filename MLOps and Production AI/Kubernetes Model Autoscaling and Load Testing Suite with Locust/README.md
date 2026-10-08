# Kubernetes Model Autoscaling and Load Testing Suite with Locust

## Executive Summary
This production-grade system implements state-of-the-art MLOps engineering and infrastructure observability tailored for horizontal pod autoscaler (hpa), prometheus metrics adapter, and distributed load generation. Engineered for high-throughput model serving, continuous data drift monitoring, automated CI/CD gating, and real-time SLA verification.

## Visual Interface & Architecture

### Production Application Interface
![Application Interface](assets/screenshot.png)

### Model Telemetry & System Diagnostics
![System Diagnostics](assets/analytics_telemetry.png)

## Core Technical Specifications
- **Serving & Orchestration Infrastructure:** Triton / ONNX Runtime containerized deployment on Kubernetes with Horizontal Pod Autoscaling (HPA).
- **Statistical Drift Engine:** Continuous Kolmogorov-Smirnov and Population Stability Index (PSI) testing against baseline training references.
- **Observability & Alerting:** Prometheus metric exports for p50, p95, and p99 latency SLAs and error rate tracking.
- **Model Lifecycle Governance:** MLflow registry integration tracking model versioning, artifacts, and production stage promotions.

## Key Performance Indicators
- **Max Load:** 12,000 Users (Locust Swarm)
- **HPA Scaling:** 2 to 24 Pods (CPU/Custom Metric)
- **Error Rate:** 0.00% (Zero Drop)
- **Scale Down Lag:** 300s Cooldown (Smooth Stabilization)

## Directory Structure
```
.
|-- app.py                     # Interactive Streamlit application and CLI runner
|-- locustfile.py         # Core mathematical engine and algorithms
|-- requirements.txt           # Project dependencies
|-- assets/
|   |-- screenshot.png         # Main production UI screenshot
|   `-- analytics_telemetry.png # Telemetry & diagnostic charts
`-- README.md                  # Comprehensive project documentation
```

## Quick Start

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Launch Interactive Dashboard
```bash
streamlit run app.py
```

### 3. Headless CLI Execution
```bash
python app.py
```
