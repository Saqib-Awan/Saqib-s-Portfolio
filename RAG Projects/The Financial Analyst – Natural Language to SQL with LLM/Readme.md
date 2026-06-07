# The Financial Analyst – Natural Language to SQL with LLM

**Author:** Saqib  

## Overview

This project implements a **Text‑to‑SQL** system that allows users to ask natural language questions about a structured database and receive answers in plain English. Using Groq’s Llama 3.3 70B model, the system translates a user’s question into a SQL query, executes it on a SQLite database, and then converts the query results into a human‑readable response. It effectively bridges the gap between unstructured language and structured data – a core capability for AI‑powered business intelligence.

## Features

- 🗣️ **Natural language interface** – Ask questions like “What is the total revenue from all sales?”
- 🧠 **LLM‑generated SQL** – Uses chain‑of‑thought‑style prompting for accurate query generation.
- 🗄️ **SQLite execution** – Queries run against a real in‑memory or persistent database.
- 📊 **Result summarisation** – The LLM converts tabular results into a concise English answer.
- 🛡️ **Safe execution** – Basic error handling prevents malformed queries from crashing the system.
- 🔁 **Interactive loop** – Test your own questions in real time.

## Architecture

1. **Database setup** – A sample SQLite table (`sales`) is created with product, quantity, price, and date columns.
2. **Schema extraction** – The table schema is fed into the prompt.
3. **SQL generation** – The user’s question + schema → Llama outputs a SQL query.
4. **Execution** – The query runs on SQLite; results are fetched.
5. **Answer generation** – A second LLM call takes the question, SQL, and results, producing a plain English answer.
6. **Interactive loop** – Users can ask repeated questions.

## Sample Database Schema

```sql
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    sale_date TEXT
);
Setup
Google Colab (CPU works, GPU not required)

Groq API key (free tier from console.groq.com)

How to Run
Open the notebook The_Financial_Analyst_–_Natural_Language_to_SQL_with_LLM.ipynb in Google Colab.

Run the installation cell.

When prompted, enter your Groq API key.

Run all cells sequentially – the sample database will be created.

Use the interactive loop to ask questions about the sales data.

Example Interactions
User: What is the total revenue from all sales?
System:

Generated SQL: SELECT SUM(quantity * price) FROM sales;

Answer: The total revenue from all sales is $4672.89.

User: Which product had the highest quantity sold?
System:

Generated SQL: SELECT product, MAX(quantity) FROM sales;

Answer: The product with the highest quantity sold is Notebook with 10 units.

User: Show me all products in the Electronics category.
System:

Generated SQL: SELECT product FROM sales WHERE category = 'Electronics';

Answer: The Electronics products are Laptop, Mouse, and Monitor.

Why This Matters
Text‑to‑SQL is a highly demanded real‑world application. It allows non‑technical users to query databases using plain English, drastically reducing the need for specialised SQL knowledge. This project proves you can:

Use an LLM to generate structured queries from natural language.

Execute generated code safely (SQLite sandbox).

Combine two LLM calls (query generation + result summarisation) into a seamless pipeline.

Build an interactive tool ready for integration into dashboards or chatbots.

Files
The_Financial_Analyst_–_Natural_Language_to_SQL_with_LLM.ipynb – Full Colab notebook.

finance.db – (Optional) saved SQLite database file.

README.md – This file.

License
MIT – free to use, modify, and share.

© 2026 Saqib – Natural language to SQL for business analytics.
