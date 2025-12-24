# RAG Application (Document-Based)

## Overview
This module implements a simple Retrieval-Augmented Generation (RAG) application
used as a **testbed for security evaluation** in this lab.

The application retrieves content from locally ingested documents and provides
that context to a language model for question answering. It is intentionally
kept minimal to make security behaviors observable.

This RAG app supports multiple assessments documented in the `/reports` directory,
including:
- baseline grounding and hallucination tests (Week 5)
- indirect prompt injection via poisoned documents (Week 6)

---

## Why This Exists in a Security Lab
RAG systems are often assumed to be safer because they ground responses in data.
This module exists to **challenge that assumption** by enabling controlled tests of:

- hallucination vs abstention behavior
- trust assumptions about retrieved documents
- indirect prompt injection via stored content

By keeping the implementation simple, the security impact of design decisions
is easier to observe and reason about.

---

## Application Structure

- `loader.py`  
  Handles document loading and chunking from `data/rag_docs/`.

- `vectorstore.py`  
  Creates embeddings and performs similarity-based retrieval.

- `rag_app.py`  
  Application entrypoint that:
  - accepts user questions
  - retrieves relevant document chunks
  - sends retrieved context to the language model

---

## How to Run (Local)
From the repository root:

```bash
python src/app_rag_docs/rag_app.py
