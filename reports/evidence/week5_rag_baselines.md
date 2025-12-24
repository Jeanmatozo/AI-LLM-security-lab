
# Week 5 — RAG Baseline Evidence

## 1. Test Setup
- RAG application: `src/app_rag_docs/`
- Document corpus: `data/rag_docs/`
- Goal: validate grounding vs hallucination behavior

---

## 2. Transcripts

## Run 1 — Grounded answer (in-scope)

**Question**
> What is ISO 27001?

**Retrieved context**
- iso27001_overview.md (chunk 0)

**Model Answer**
- ISO/IEC 27001 is an international standard that describes how to build, operate, monitor, and continually improve an Information Security Management System (ISMS). An ISMS is a structured way for an organization to understand its information security risks, select and implement controls to manage those risks, and continually review and improve its security posture. The current version is ISO/IEC 27001:2022, which replaces the earlier 2013 version and aligns more closely with modern risk and governance practices.


## Run 2 — Abstention (out-of-scope)

**Question**
> What is the population of Rwanda?

**Retrieved context**
- None relevant (or irrelevant chunks)

Model Answer
- I am not sure
