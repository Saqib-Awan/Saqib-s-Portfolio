# Self-Ask with Web Search (Groq + Tavily)

**Author:** Saqib  

## Overview  

This project implements a self-ask agent that uses Groq’s Llama 3.3 to decide whether a web search is needed. If the LLM determines external information is required, it generates a search query, fetches results via Tavily API, and then answers the user. This pattern mimics how advanced AI assistants (like perplexity.ai) work.

## Features  

- 🧠 **LLM decides** – Autonomous choice between internal knowledge and web search.  
- 🌐 **Real‑time search** – Integrates Tavily API for up‑to‑date information.  
- 💬 **Interactive** – Ask any factual or current question.  
- 🧪 **No framework overhead** – Pure Python + API calls.  

## Setup  

- Groq API key – free at [console.groq.com](https://console.groq.com)  
- Tavily API key – free at [tavily.com](https://tavily.com)  

## Example  

**User:** What is the current population of Japan?  
**Agent:** 🔍 Searching for "current population of Japan"  
**Bot:** As of 2025, Japan's population is approximately 124 million.  

**User:** Who wrote 'Romeo and Juliet'?  
**Agent:** 🧠 Used internal knowledge  
**Bot:** William Shakespeare.  

## Files  

- `Self_Ask_Web_Search.ipynb` – Full notebook.  
- `README.md` – This file.  

## License  

MIT – free to use and modify.  

---

**© 2026 Saqib – Self-asking web search agent.**