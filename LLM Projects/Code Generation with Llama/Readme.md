# Code Generation with Llama (Groq)

**Author:** Saqib  

## Overview

This project uses Groq’s Llama 3.3 70B to generate code from natural language descriptions. It supports multiple languages (Python, JavaScript, SQL, Bash) and includes optional syntax validation and sandboxed execution for Python. The system acts as an AI programming assistant, translating user requests into executable code.

## Features

- 🧠 **Multi‑language code generation** – Python, JavaScript, SQL, Bash.
- 🔍 **Syntax validation** – Checks Python code validity.
- 🏃 **Sandboxed execution** – Runs Python code safely in a restricted environment.
- 📝 **Clean output** – Removes markdown code fences.
- 💻 **Interactive loop** – Try your own coding problems.

## How It Works

1. User describes a coding task (e.g., “write a function to reverse a string”).
2. Llama generates the code.
3. (Optional) Python code is syntax-checked and executed.
4. The generated code is displayed.

## Setup

- Groq API key – free at [console.groq.com](https://console.groq.com)
- Google Colab or any Python environment

## Example

**User:** Write a Python function to compute the factorial of a number.

**Generated Code:**
```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
Execution output: Executed successfully.

Files
Code_Generation.ipynb – Full notebook.

README.md – This file.

License
MIT – free to use and modify.

© 2026 Saqib – Code generation assistant.