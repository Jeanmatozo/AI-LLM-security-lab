# Week 6 — Security Assessment Report  
## Indirect Prompt Injection Against RAG System (Scenario 2)

**Author:** Jean Akingeneye  
**Project:** AI-LLM Security Lab  
**Date:** Week 6

---

## 1. Summary
This assessment demonstrates a successful **indirect prompt injection attack** against a custom Retrieval-Augmented Generation (RAG) system. Unlike direct prompt injection, the attack embeds adversarial instructions inside a document stored in the RAG corpus. When this document is retrieved during normal operation, the model executes the hidden instructions despite a benign user query.

This represents a **high-risk enterprise failure mode** for AI systems that ingest internal documents, vendor files, emails, or reports without sanitization or trust classification.

---

## 2. Scope
**In scope**
- Custom RAG application
- Document corpus: `data/rag_docs/`
- Vector store and retrieval logic
- Application logs and retrieved context

**Out of scope**
- Tool-enabled agents (Week 7)
- External web browsing
- Automated detection/classification pipelines (not implemented yet)

---

## 3. Environment & Assumptions
- The RAG system retrieves semantically similar document chunks based on user queries.
- Retrieved chunks are concatenated directly into the LLM prompt.
- Documents in the RAG corpus were implicitly trusted prior to this assessment.
- User queries are assumed benign for this scenario.

---

## 4. Threat Model
### Assets
- Integrity of system instructions
- Accuracy and safety of model outputs
- Trustworthiness of internal document ingestion pipeline

### Attacker
- A malicious insider or external party able to insert or modify documents in the RAG corpus.

### Trust Boundaries
- Document ingestion → vector store (previously assumed trusted)
- Retrieved context → LLM prompt (critical boundary)

### Security Properties Desired
- Stored content must not override system instructions.
- Retrieved documents should not be treated as executable instructions.
- Malicious content should be detectable or neutralized before model execution.

---

## 5. Attack Scenario
### Attack Vector
A malicious document was added to the RAG corpus and indexed normally.

**Malicious file:** `malicious_vendor_note.md`

**Embedded instructions (excerpt):**
