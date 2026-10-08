# Enterprise LLM Security Guardrails and Red-Teaming Suite

## Abstract

A security evaluation and real-time inference firewall for Large Language Models. Built on the principles of Llama-Guard 3, NeMo Guardrails, and Microsoft Presidio, the suite intercepts inputs and outputs to neutralize direct prompt injections, jailbreaks, system prompt extractions, and PII leaks with minimal latency overhead.

## Visual Interface

![Application Interface](assets/screenshot.png)

## Architecture and Pipeline

1. **Adversarial Input Interception**: Inspects incoming prompt strings against 1,500+ curated adversarial attack payloads (OWASP Top 10 for LLMs).
2. **PII Sanitization Hook**: Detects and anonymizes Social Security Numbers, API keys, passwords, and clinical records via regex and NER analyzers.
3. **Safety Classification (Llama-Guard 3)**: Evaluates prompts against strict taxonomy policies (Cybersecurity Threats, Malicious Content, System Exploits).
4. **Output Hallucination & Leak Filter**: Validates generated model completions to ensure internal system instructions are never revealed.

## Key Features

- **Adversarial Defense**: 98.8% defense rate against sophisticated jailbreak prompts.
- **Ultra-Low Latency Overhead**: Adds just 14.2ms to overall model inference times.
- **Custom Policy Rules**: Configurable security policies tailored to enterprise compliance requirements.
- **Red-Teaming Benchmark Runner**: Built-in test suite to evaluate third-party LLMs against known exploit patterns.

## Tech Stack

- Python 3.10+
- Hugging Face Transformers (Llama-Guard-3)
- PyTorch
- Microsoft Presidio
- Pydantic

## Installation and Setup

```bash
cd "LLM Projects/Enterprise LLM Security Guardrails and Red-Teaming Suite"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

## Performance Metrics

- Overall Attack Neutralization Rate: 98.8% (1,488 / 1,500 adversarial probes blocked)
- False Positive Rate: < 0.6% on benign enterprise queries
- Interception Latency: 14.2 ms

## Author

**Muhammad Saqib** — Applied AI/ML Engineer (Computer Vision, Deep Learning, NLP, LLMs)