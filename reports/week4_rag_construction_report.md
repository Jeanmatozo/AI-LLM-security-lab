# Week 4 — RAG Construction and Initial Hardening  

---

## 1. Summary

This phase focused on building the first Retrieval-Augmented Generation (RAG) application
used throughout the lab.

The goal was not to secure the system yet, but to:
- Implement a realistic RAG pipeline
- Observe how data flows from documents to model output
- Establish the baseline architecture that would later be attacked

**One-sentence takeaway:**  
I built a functional RAG system that retrieves local documents and injects them into an
LLM prompt, creating the foundation for later indirect prompt injection and trust-boundary testing.

---

## 2. Scope

### In Scope
- Application: `src/app_rag_docs/rag_app.py`
- Document corpus: `data/rag_docs/`
- Basic retrieval + prompt construction logic
- Manual testing via terminal

### Out of Scope
- Prompt injection testing (Week 3)
- Indirect prompt injection (Week 6)
- Tool-enabled agents (Week 7+)
- Automated evaluation harnesses

---

## 3. Environment & Assumptions
- The RAG app runs locally via:
  ```bash
  python -m src.app_rag_docs.rag_app

  ```
- Documents are loaded from data/rag_docs/
- Chunks are embedded and stored in a simple in-memory vector store
- Retrieved chunks are passed directly into the model prompt
- API access is controlled through the OPENAI_API_KEY environment variable

---
## 4. System Design Overview
### Functional Outcome
The system correctly answered questions like:
- “What is ISO 27001?”
- “What is an ISMS?”

Answers were grounded in locally ingested documents rather than general model knowledge
---

## 5. Threat Model (Baseline View)

### Assets
- Integrity of retrieved document content
- Accuracy of generated answers
- User trust in system outputs

### Attacker / Failure Mode
- At this stage, the main risk is accidental misuse:
  - irrelevant retrieval
  - hallucination when context is weak
  - over-trust in retrieved content

### Trust Boundaries
1. Documents → Vector store
2. Vector store → Retrieved context
3. Retrieved context → LLM prompt
4. LLM output → User

At this stage, documents and retrieval were implicitly trusted
---

## 6. Engineering Learnings

### Technical Skills Gained

- Running Python modules using the `-m` flag:

  ```bash
  python -m src.app_rag_docs.rag_app
  
  ```
- Understanding how __init__.py files affect Python package imports and module resolution.
- Using environment variables (such as OPENAI_API_KEY) to securely connect local code to external APIs.
- Building a complete Retrieval-Augmented Generation (RAG) pipeline without external frameworks.
- Understanding how vector embeddings enable semantic search over documents.

### Conceptual Learnings
- A simple in-memory vector store is enough to build a powerful RAG system.
- RAG systems are easy to build — and therefore easy to misuse.
- Prompt injection risks become significantly more dangerous when documents are involved, not just user input.

---

## 7. Red Team Signal

Although this week focused primarily on construction, early adversarial thinking was introduced.

### Vector Store Probing

High-entropy and exploratory questions were used to infer:

- What topics existed in the corpus  
- What kind of documents had been ingested  
- Where retrieval boundaries were  

This simulates reconnaissance behavior where an attacker:

- Does not control documents yet  
- But tries to map internal knowledge by querying creatively  

This phase mirrors real-world red team behavior:

> First understand the terrain. Then exploit it.

---

## 8. Security Observations

Documents are treated as trusted input:

- Retrieved text is injected directly into the model prompt.  
- There is no separation between “data” and “instructions.”  
- There is no validation or sanitization of retrieved content.  

These are not yet active vulnerabilities — but they define future attack surfaces.

---

## Next Steps (Week 5)

Establish a formal RAG baseline:

- Grounded answers  
- Proper abstention when context is missing  

Measure hallucination versus grounding behavior.  
Prepare for indirect prompt injection testing in later weeks.











