# Conversational Memory with Summarization (Groq)

**Author:** Saqib  

## Overview  

Standard chatbots forget previous messages once the context window fills up. This project solves that problem by periodically compressing the conversation into a summary that is then used as memory. The summarisation is performed by Groq’s Llama, allowing long conversations to stay coherent without exceeding token limits.  

## Features  

- 💬 Multi‑turn dialogue with recall of past topics.  
- 🔄 Automatic summarisation after every N exchanges.  
- 🧠 Uses Groq’s fast LLM for both chat and summarisation.  
- 💾 Summary persists and can be saved or reloaded.  
- 🧪 Interactive console with a `summary` command to inspect memory.  

## How It Works  

1. User sends a message.  
2. The assistant replies, storing the exchange in a short‑term history.  
3. After every N turns, the entire conversation is summarised by the LLM.  
4. The summary becomes the long‑term memory, and the short‑term history is trimmed.  
5. Future replies use the summary + recent messages as context.  

## Setup  

- Groq API key – free at [console.groq.com](https://console.groq.com)  
- Google Colab or any Python environment.  

## Example  

**User:** My name is Alice.  
**Bot:** Nice to meet you, Alice!  

**User:** I work as a data scientist.  
**Bot:** That’s exciting! Data science is a great field.  

*After 2 turns, the conversation is summarised:*  
**Summary:** Alice introduced herself and mentioned she works as a data scientist.  

Later questions can refer back to that information without the bot forgetting.  

## Files  

- `Conversational_Memory_with_Summarization.ipynb` – Full notebook.  
- `README.md` – This file.  

## License  

MIT – free to use and modify.  

---

**© 2026 Saqib – Long‑memory chatbot using summarisation.**