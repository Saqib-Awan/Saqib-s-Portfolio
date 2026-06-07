# Agentic RAG with LangGraph

**Author:** Saqib    

## Overview

This project implements an **agentic Retrieval‑Augmented Generation (RAG)** system using **LangGraph**. Unlike simple linear RAG pipelines, this agent can reason about user queries and decide which actions to take: retrieve from a local vector store, rewrite the query for better retrieval, fall back to a web search (via Tavily API), or answer directly from its own knowledge.

The agent is built as a **stateful graph** where each node performs a specific action, and conditional edges route the flow based on the agent’s decisions.

## Features

- 🧠 **Stateful agent** – Maintains conversation history and intermediate steps.
- 🔍 **Multi‑source retrieval** – Internal FAISS index (PDF documents) + optional web search.
- ✍️ **Query rewriting** – Automatically reformulates user questions to improve retrieval.
- 🌐 **Web search fallback** – Uses Tavily API when local documents lack the answer.
- 📊 **Step‑by‑step trace** – Prints every action taken (rewrite, retrieve, web search, generate).
- ⚡ **Fast LLM** – Powered by Groq’s Llama 3.3 70B.

## Architecture (LangGraph)
User Input → Rewrite → Retrieve → Conditional Edge
├─→ Web Search (if needed) → Generate → Answer
└─→ Generate (directly)

text

**Nodes:**
- `rewrite` – Improves the user query.
- `retrieve` – Fetches relevant chunks from FAISS index.
- `web_search` – Calls Tavily API.
- `generate` – Produces final answer using retrieved context.

**Edges:** Conditional routing based on whether local documents are sufficient.

## Setup

- Google Colab (T4 GPU optional, CPU works)
- Groq API key (required – get free at [console.groq.com](https://console.groq.com))
- Tavily API key (optional – for web search; free tier at [tavily.com](https://tavily.com))

## How to Run

1. Open the notebook `Agentic_RAG_with_LangGraph.ipynb` in Google Colab.
2. Run the installation cell.
3. Enter your **Groq API key** when prompted (required).
4. (Optional) Enter your **Tavily API key** to enable web search.
5. Upload one or more PDF files (or skip – agent will rely on web search + LLM knowledge).
6. Run all cells sequentially.
7. Ask questions in the interactive loop. The agent will show each step it takes.

## Example Interaction
🔍 Your question: What is the capital of France?
📋 Steps taken: rewrote_query → retrieved_local → generated_answer
💡 Answer: The capital of France is Paris. (source: local documents)

🔍 Your question: What is the latest news about AI?
📋 Steps taken: rewrote_query → retrieved_local → web_search → generated_answer
💡 Answer: [Retrieved real‑time news results via Tavily]

text

## Why This Matters

Agentic RAG represents the frontier of AI systems – LLMs that can reason, use tools, and decide what actions to take. This project demonstrates:
- Building a cyclic, stateful workflow with LangGraph.
- Integrating multiple tools (retriever, query rewriter, web search).
- Making autonomous decisions based on retrieved content.
- A production‑ready pattern for complex assistant applications.

## Files

- `Agentic_RAG_with_LangGraph.ipynb` – Full Colab notebook.
- `agent_graph.png` – Visualisation of the graph (optional, generated).
- `README.md` – This file.

## License

MIT – free to use and adapt.

---

**© 2026 Saqib – Agentic RAG with LangGraph.**