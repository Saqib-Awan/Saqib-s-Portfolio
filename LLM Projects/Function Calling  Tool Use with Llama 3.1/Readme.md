# Function Calling / Tool Use with Llama (Groq)

**Author:** Saqib   

## Overview

This project demonstrates **function calling (tool use)** – a core capability for building agentic AI systems. Using Groq’s Llama 3.3 70B model, the assistant autonomously decides when to call external tools, extracts parameters from natural language, and incorporates the results into its final answer.

Unlike simple chatbots, this system can:
- Fetch weather information for any location.
- Perform mathematical calculations.
- Extend easily to any API or custom function.

## Features

- 🧠 **Autonomous tool selection** – The model decides which tool (if any) to call.
- 🔧 **Two built‑in tools**:
  - `get_current_weather` – Returns mock weather data (easily replaceable with a real API).
  - `calculate` – Safely evaluates mathematical expressions.
- 🔌 **Extensible design** – Add your own tools (database queries, web search, etc.) by defining the function schema and implementation.
- 📦 **Uses Groq’s native function calling API** – Fast inference on free tier.

## Architecture

1. **User query** → sent to Llama 3.3 70B with a list of available tools.
2. **Model decides** – if a tool is needed, it returns a structured `tool_call` with the function name and arguments.
3. **Executes tool** – the Python code runs the requested function.
4. **Second LLM call** – the model uses the tool’s output to generate a final natural language answer.

## Setup & Requirements

- Google Colab (free tier works, GPU not required)
- Groq API key – get one at [console.groq.com](https://console.groq.com)

## How to Run

1. Open the provided Colab notebook.
2. Run the installation cell.
3. When prompted, enter your Groq API key.
4. Execute the remaining cells.
5. Interact with the assistant by typing questions such as:
   - *"What is the weather in London?"*
   - *"Calculate 25 * 14 + 8"*
   - *"What is the weather in Tokyo in fahrenheit?"*

## Example Interaction
🔍 Your question: What is the weather in Paris?

🔧 Calling tool: get_current_weather with args {'location': 'Paris', 'unit': 'celsius'}

🤖 The current weather in Paris is 22°C and sunny.

text
🔍 Your question: Compute the square root of 144 plus 10

🔧 Calling tool: calculate with args {'expression': 'sqrt(144) + 10'}

🤖 The result of sqrt(144) + 10 is 22.0.

text

## Extending the Project

To add a new tool:

1. Define its JSON schema in the `tools` list.
2. Write a Python function that implements the logic.
3. Add the function to `available_functions` dictionary.

Example: adding a real‑time news API or a SQL query executor.

## Why This Matters for Your Portfolio

Function calling is the backbone of **agentic AI** – systems that can take actions, use APIs, and reason with external tools. This project proves you can move beyond simple text generation to building LLM applications that interact with the real world.

## Files

- `llm_function_calling.ipynb` – Complete Colab notebook.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Production‑ready LLM tool use.**