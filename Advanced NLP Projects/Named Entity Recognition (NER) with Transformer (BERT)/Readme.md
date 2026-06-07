# Named Entity Recognition (NER) with Transformer (BERT)

**Author:** Saqib  

## Overview

This project implements a **Named Entity Recognition (NER) system** using a fine‑tuned transformer model (DistilBERT). NER is the task of extracting entities like persons, locations, organisations, and miscellaneous names from text. It is a fundamental building block for information extraction, search engines, and knowledge graph construction.

The model is trained on the **WikiANN** dataset (English), a standard benchmark for multilingual NER. After fine‑tuning, the system achieves high F1 scores on test data and can be used to annotate any English text.

## Features

- 🧠 **Token‑level classification** – Assigns an entity label (B‑PER, I‑LOC, O, etc.) to each token.
- 🤖 **Transformer‑based** – Fine‑tunes `distilbert-base-uncased` (fast, memory‑efficient).
- 📚 **Standard dataset** – WikiANN (English) – ~20k training sentences.
- 🏷️ **BIO tagging scheme** – Supports 7 entity classes (PER, LOC, ORG, etc.) plus O (outside).
- 📊 **Professional evaluation** – Per‑entity precision, recall, F1, overall accuracy, confusion matrix.
- 💾 **Model export** – Save fine‑tuned model and tokenizer for production inference.
- 🧪 **Live inference** – Test on custom text and see detected entities.

## Dataset

- **Source:** WikiANN (Hugging Face) – `wikiann` with language 'en'.
- **Size:**  
  - Train: ~20,000 sentences  
  - Validation: ~3,000 sentences  
  - Test: ~3,000 sentences  
- **Entity types:** PER (person), LOC (location), ORG (organisation), etc. (7 classes including O).
- **Format:** Tokenised sentences with integer labels mapped to BIO tags.

## Architecture

1. **Model** – `distilbert-base-uncased` (a smaller, faster BERT variant).
2. **Tokenisation** – Aligns subword tokens with original word labels using word IDs.
3. **Training** – 3 epochs, learning rate 2e‑5, batch size 16.
4. **Evaluation** – Uses `seqeval` for entity‑level metrics (strictly matching entities).
5. **Inference** – Decodes logits to BIO tags and extracts named entities.

## Setup

- Google Colab (T4 GPU recommended for faster training).
- Libraries: `transformers`, `datasets`, `seqeval`, `torch`, `scikit-learn`.

## How to Run

1. Open the notebook `Named_Entity_Recognition_(NER)_with_Transformer_(BERT).ipynb` in Google Colab.
2. Run the installation cell.
3. Run all cells sequentially:
   - Load WikiANN dataset.
   - Tokenise and align labels.
   - Load DistilBERT model for token classification.
   - Train for 3 epochs (15–20 minutes on T4 GPU).
   - Evaluate on validation and test sets.
   - Generate confusion matrix and classification report.
   - Test inference on custom sentences.
4. Save the fine‑tuned model (optional, to Google Drive).

## Example Interaction

**Input text:** *“Google CEO Sundar Pichai announced a new AI project in New York.”*

**Detected entities:**
- **Google** → ORG (Organisation)
- **Sundar Pichai** → PER (Person)
- **New York** → LOC (Location)

**Code output:**
Entities found:
Google - ORG
Sundar Pichai - PER
New York - LOC

text

## Why This Matters

NER is a core NLP task used in:
- Information extraction from legal/medical documents.
- Search engine query understanding.
- Conversational AI (extracting dates, places, people).
- Knowledge graph population.

This project demonstrates:
- Fine‑tuning a transformer for token classification.
- Handling word‑to‑subword alignment.
- Evaluating entity recognition using strict metrics.
- Building a deployable entity extractor.

## Results (Expected)

- **Overall F1‑score (test set):** ~0.88 – 0.92
- Best performing entity types: PER, LOC
- Confusion matrix shows occasional misclassification between ORG and MISC.

## Files

- `Named_Entity_Recognition_(NER)_with_Transformer_(BERT).ipynb` – Full notebook.
- `ner_model/` – Saved fine‑tuned model and tokenizer.
- `README.md` – This file.

## License

MIT – free to use, modify, and share.

---

**© 2026 Saqib – Transformer‑based named entity recognition.**