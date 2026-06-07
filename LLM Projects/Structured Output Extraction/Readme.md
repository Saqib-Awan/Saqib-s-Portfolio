# Structured Output Extraction – JSON Mode with Groq

**Author:** Saqib  

## Overview

This project demonstrates how to extract structured JSON data from unstructured text using Groq’s Llama 3.3 70B. You provide a JSON schema (fields and descriptions), and the model returns a clean JSON object. This technique is fundamental for converting free‑form documents, emails, or logs into structured records for databases, dashboards, or APIs.

## Features

- 🧩 **Custom JSON schemas** – Define exactly what fields to extract.
- ✅ **Automatic validation** – Handles malformed JSON gracefully.
- 📄 **Example use cases** – Invoice extraction, resume parsing, customer feedback analysis.
- 💻 **Interactive mode** – Try your own text and schema.

## How It Works

1. User provides unstructured text and a JSON schema description.
2. The LLM is prompted to output only valid JSON following the schema.
3. The Python code parses the JSON and returns a Python dictionary.

## Setup

- Groq API key – free at [console.groq.com](https://console.groq.com)
- Google Colab or any Python environment

## Example

**Input text:** *“INVOICE #12345, Date: 2025-05-01, Customer: Apple Inc., Total: $500”*

**Schema:**
```json
{
  "invoice_number": "string",
  "date": "string",
  "customer": "string",
  "total": "number"
}
Output JSON:

json
{
  "invoice_number": "12345",
  "date": "2025-05-01",
  "customer": "Apple Inc.",
  "total": 500
}
Files
JSON_Extraction.ipynb – Full notebook.

README.md – This file.

License
MIT – free to use and modify.

© 2026 Saqib – Structured data extraction from text.