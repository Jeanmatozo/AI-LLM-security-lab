# AI & LLM Security Lab

My personal lab exploring cybersecurity risks in AI-powered applications, with a focus on:

- Prompt injection and jailbreaks
- RAG (Retrieval-Augmented Generation) security
- Agentic systems and tool abuse
- Mapping AI risks to ISO/IEC 27001-style controls

## Who I Am

ISO/IEC 27001:2022 Lead Auditor and cybersecurity learner transitioning into AI & LLM security engineering.

## Lab Roadmap (First 10 Weeks)

1. Create this repo and basic structure (src/, attacks/, reports/, notes/)
2. Build a simple LLM chatbot
3. Run and document prompt injection experiments
4. Build a small RAG app over local documents
5. Test indirect prompt injection from malicious documents
6. Build a basic agent with tool access (files / dummy API)
7. Simulate tool abuse and data exfiltration scenarios
8. Implement mitigations and guardrails
9. Document threat models and risks
10. Map AI risks to ISO/IEC 27001-style controls

# AI-LLM-security-lab

---

## Attack Scenarios in This Lab

### Scenario 1 — Direct Prompt Injection (Basic Chatbot)

- Path: `attacks/prompt_injection/scenario1.md`
- App: `src/app_basic_chatbot/chatbot.py`

**What this demonstrates**
- How single-turn prompt injection works
- Why stateless chatbots are still vulnerable
- Why system prompts alone are insufficient

---

### Scenario 2 — Indirect Prompt Injection (RAG System Attack)

- Path: `attacks/Indirect Prompt Injection/Scenario 2 (RAG System Attack).md`
- App: `src/app_rag_docs/rag_app.py`
- Malicious doc: `data/rag_docs/malicious_vendor_note.md`

**Observed behavior**
- RAG retrieves a malicious internal document
- Model follows hidden instructions instead of system policy
- Logs capture query, retrieved chunks, and compromised output

**What this demonstrates**
- Indirect prompt injection via stored documents
- RAG documents must be treated as untrusted input
- Enterprise AI systems can be compromised via poisoned PDFs, notes, or emails

Full analysis:
- `reports/week6_indirect_injection_report.md`

---

## Code Structure
	•	src/app_basic_chatbot/
Minimal LLM chatbot app used for direct prompt injection experiments.
	•	src/app_rag_docs/
Simple RAG app over local markdown docs using embeddings + an in-memory vector store.
	•	data/rag_docs/
Local markdown documents used for RAG, including:
	•	ai_security_notes.md
	•	iso27001_overview.md
	•	malicious_vendor_note.md (used for indirect injection testing)
	•	attacks/
Writeups for prompt injection and RAG-based attack scenarios.
	•	reports/
Security-style reports, baseline evaluations, and threat/impact notes.
	•	notes/
Learning notes and future experiment ideas.

⸻

## What I Am Practicing Here
	•	Writing and running Python-based security experiments for LLMs
	•	Designing and executing AI attack scenarios (prompt injection, RAG abuse)
	•	Logging and analyzing model behavior like a security engineer
	•	Connecting AI security findings back to governance frameworks (ISO/IEC 27001)

---

## Indirect Prompt Injection (RAG System Attack)

In Week 6, I demonstrated an indirect prompt injection attack against a RAG system by embedding hidden instructions inside a retrieved document.

**Observed behavior:**
- The RAG system retrieves a malicious internal document
- The model follows hidden instructions instead of system policy
- Logging captures the query, retrieved context, and compromised output

**What this demonstrates:**
- RAG documents must be treated as untrusted input
- Indirect prompt injection can occur without malicious user queries
- Enterprise AI systems can be compromised via poisoned notes, PDFs, or emails

Full analysis:  
`reports/week6_indirect_injection_report.md`

