# Text‑to‑SQL with Llama (Groq)

**Author:** Saqib  

## Overview
This project implements a **Text‑to‑SQL** system using Groq's Llama 3.3 70B model. Users ask questions in plain English about a sample sales database, and the LLM generates a SQL query, executes it, and returns a natural language answer.

## Features
- 🔍 **Natural language interface** – Ask questions like “What is the total revenue?”
- 🧠 **LLM‑generated SQL** – Uses chain‑of‑thought‑style prompting for accuracy.
- 🗄️ **SQLite execution** – Runs queries against a real in‑memory database.
- 📊 **Result summarisation** – Converts tabular results into plain English.
- 🖥️ **Interactive loop** – Test your own questions.

## How It Works
1. User question → Llama generates a SQL query.
2. Query executed on SQLite database.
3. Results (columns + rows) passed back to Llama.
4. Llama produces a human‑readable answer.

## Setup
- **Groq API key** – Get one free at [console.groq.com](https://console.groq.com)
- **Python 3.9+** (Google Colab recommended)

## Running the Notebook
1. Open the provided `.ipynb` file in Colab.
2. Run the first cell to install dependencies.
3. Enter your Groq API key when prompted.
4. Execute all cells sequentially.
5. Test with the built‑in examples or type your own questions in the interactive loop.

## Example Interaction

❓ Question: What is the total revenue from all sales?  
📝 Generated SQL: `SELECT SUM(quantity * price) FROM sales;`  
✅ Answer: The total revenue from all sales is $4672.89.

❓ Question: Which product had the highest quantity sold?  
📝 Generated SQL: `SELECT product, MAX(quantity) FROM sales;`  
✅ Answer: The product with the highest quantity sold is Notebook with 10 units.

## Extending the Project
- Replace the sample database with your own schema (just change the `CREATE TABLE` and `INSERT` statements).
- Add more complex tables (customers, orders) and queries (JOINs, GROUP BY).
- Use a persistent database file instead of `:memory:`.

## Why This Is Portfolio‑Worthy
Text‑to‑SQL is a highly demanded skill in data engineering and AI‑assisted analytics. This project demonstrates:
- Prompt engineering for structured output.
- Safe code execution (SQL queries).
- Two‑stage LLM pipeline (SQL generation + result explanation).
- Production‑ready interactive interface.

## Files
- `llm_text_to_sql.ipynb` – Full Colab notebook.
- `README.md` – This file.

## License
MIT – free to use and modify.

---

**© 2026 Saqib – Natural language to SQL with Llama.**