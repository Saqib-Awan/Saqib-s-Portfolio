# LangChain Projects

A curated collection of LangChain / LLM applications and utilities by **Muhammad Saqib**. Each subproject is self contained with its own `README.md` or notebook and focuses on a single capability (chat, retrieval, summarization, SQL, PDFs, audio, code generation, etc.).

## Quick Start

- Use per project `README.md` files for setup and run instructions
- Common prerequisites: Python 3.9+, virtual environments, API keys where required
- Typical run command for apps: `streamlit run app.py` inside the project folder

## Project Index

- `Audio To Text Transcription/` — Whisper transcription with optional post processing via chat models
- `Basic PDF QA/` — RetrievalQA over a single PDF using an in memory doc store
- `Blog Generation/` — Streamlit app generating short blogs via local Llama 2 (`ctransformers`)
- `Calories Health Advisor/` — Gemini Vision nutrition analyzer from food images; optional SQL demo
- `Chat With Multiple Documents/` — Chat over multiple PDFs with FAISS + Gemini
- `Codebasics FAQ Chatbot/` — CSV FAQs → FAISS + Instructor embeddings → PaLM Q&A
- `Conversational Q&A Chatbot/` — ChatOpenAI conversational demo with simple memory
- `Invoice Data Extractor/` — Extract structured JSON from invoices using LangChain parsers
- `LLM Generic App/` — Notebook pipeline: PDFs → OpenAI embeddings → Pinecone → QA
- `News Research Tool/` — RockyBot: URLs → FAISS index → QA with sources
- `Q&A Chatbot Using LLM/` — Minimal single turn Q&A with OpenAI completions
- `SQL Database QA/` — MySQL inventory Q&A via SQLDatabaseChain and few shot prompts
- `Text Summarization/` — Notebook based summarization for text and PDFs
- `Web Page Summarization/` — Web page summarization using `stuff`, `map_reduce`, and `refine` chains
- `WordPress Code Assistant/` — Generate WordPress PHP code with QA cross check

## Notes

- API keys: many apps require keys (OpenAI, Google Generative AI, etc.). See individual project READMEs
- OS specifics: some projects include Windows specific dependencies (e.g., `python-magic-bin` for `unstructured`)
- Notebooks: open with Jupyter or VS Code and run cells sequentially

## Author

**Muhammad Saqib** — Applied AI/ML Engineering: NLP, deep learning, large language models, RAG pipelines, machine learning, and data analysis.


## License

Each app uses third party APIs and models subject to their terms. Ensure you have rights to any data you process and comply with applicable licenses and policies.
