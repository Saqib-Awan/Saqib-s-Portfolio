# MLOps and Production AI

An enterprise collection of production machine learning engineering, MLOps infrastructure, and deployment pipelines developed by Muhammad Saqib. The repositories feature containerized REST microservices (FastAPI/Docker), real-time model monitoring and data drift auditing (Evidently AI), experiment tracking and model registries (MLflow), ultra-low-latency feature stores (Feast/Redis), streaming anomaly detection (Kafka/Faust), distributed inference servers (ONNX/Triton), automated CI/CD workflows (GitHub Actions/CML), multi-armed bandit traffic routing, post-training edge quantization (AWQ/GGUF), serverless LLM gateways with circuit breakers, and Kubernetes autoscaling suites (HPA/Locust).

## Project Index

1. `A-B Testing and Multi-Armed Bandit Dynamic Model Routing Service/` - Bayesian Thompson Sampling traffic allocation maximizing conversions and minimizing regret between competing model variants.
2. `Automated CI-CD Pipeline for Machine Learning with GitHub Actions and CML/` - Automated PR regression testing, DVC dataset versioning, and continuous model performance reporting.
3. `Automated MLflow Experiment Tracking and Model Registry Platform/` - Centralized lifecycle tracking, parameter auditing, and staging-to-production promotion gates.
4. `Continuous Model Monitoring and Data Drift Detection Engine with Evidently AI/` - Real-time feature distribution monitoring utilizing Kolmogorov-Smirnov tests and Population Stability Index (PSI).
5. `Distributed Model Inference Server with Triton and ONNX Runtime/` - Multi-worker high-throughput inference server with dynamic batching and CUDA FP16 tensor core acceleration.
6. `Enterprise Credit Scoring and Default Prediction API with FastAPI and Docker/` - High-throughput containerized underwriting API with Pydantic v2 schemas and sub-15ms inference latency.
7. `High-Throughput Feature Store and Real-Time Ingestion Pipeline with Feast/` - Dual-store architecture pairing Redis online caching with offline Parquet stores for point-in-time joins.
8. `Kubernetes Model Autoscaling and Load Testing Suite with Locust/` - Horizontal Pod Autoscaler (HPA) stress testing validating 2,000 RPS concurrency with zero dropped requests.
9. `Model Quantization and Edge Optimization Suite (GGUF, AWQ, ONNX)/` - 4-bit and 8-bit post-training quantization reducing VRAM by 72% for edge deployments.
10. `Real-Time Streaming Anomaly Detection Pipeline with Kafka and Faust/` - Asynchronous event stream processor scoring 10,000 transactions/second with an online Isolation Forest.
11. `Serverless LLM Inference Gateway with Token Rate-Limiting and Fallback/` - Multi-provider API gateway with token-bucket rate limiting, semantic caching, and automated circuit breaker failover.

## Tech Stack

Python, FastAPI, Docker, MLflow, Evidently AI, Feast, Redis, Apache Kafka, Faust, ONNX Runtime, Triton, GitHub Actions, CML, Locust, Scikit-Learn, LightGBM, PyTorch

## Author

Muhammad Saqib - Applied AI/ML Engineer (Computer Vision, Deep Learning, NLP, LLMs, RAG, Machine Learning)
