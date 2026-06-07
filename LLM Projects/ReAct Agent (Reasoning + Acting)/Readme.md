# Manual ReAct Agent with Groq

**Author:** Saqib  

## Overview

This project implements a **ReAct (Reasoning + Acting) agent** from scratch using only the Groq API. The agent interleaves **Thought**, **Action**, **Observation** steps to solve multi‑step problems. It demonstrates the core of agentic AI without relying on any high‑level framework – pure Python and API calls.

## Features

- 🧠 **Manual ReAct loop** – No LangChain, no dependencies beyond Groq.
- 🔧 **Two tools** – Weather (mock) and Calculator.
- 🔁 **Multi‑step reasoning** – The agent can chain tool calls.
- 💻 **Interactive** – Ask any question that requires tool use.

## How It Works

1. User asks a question.
2. The agent (prompted with the ReAct format) generates:
   - **Thought**: what to do next.
   - **Action**: tool name.
   - **Action Input**: parameters.
3. The Python script executes the tool and inserts **Observation**.
4. The loop repeats until a **Final Answer** is produced.

## Setup

- Groq API key – free at [console.groq.com](https://console.groq.com)
- Python 3.9+ (Google Colab works)

## Example

**User:** What is the weather in Paris? Then add 5 to that temperature.

**Agent output:**
Thought: I need the temperature in Paris.
Action: Weather
Action Input: Paris
Observation: The weather in Paris is 22°C.
Thought: Now I add 5.
Action: Calculator
Action Input: 22 + 5
Observation: 27
Thought: I know the final answer.
Final Answer: The weather in Paris is 22°C. Adding 5 gives 27°C.

text

## Files

- `Manual_ReAct_Agent.ipynb` – Full notebook.
- `README.md` – This file.

## License

MIT – free to use and modify.

---

**© 2026 Saqib – Pure Python ReAct agent.**