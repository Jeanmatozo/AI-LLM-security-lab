# AI & LLM Security Lab

A personal, hands-on security lab exploring **real-world risks in AI-powered applications**, with a focus on how Large Language Models (LLMs) fail in practice — not just in theory.

This repository is designed as a **security engineer’s lab**, emphasizing attack execution, observation, logging, and governance mapping.

---
## Setup & Dependencies

This lab is designed to be reproducible.

### Requirements
- Python 3.10+
- OpenAI API key

Install dependencies:

```bash
pip install -r requirements.txt

```
## Focus Areas

This lab explores realistic attack paths against AI-powered systems, including:

- Prompt injection and jailbreaks
- Indirect prompt injection via RAG (Retrieval-Augmented Generation)
- Agentic systems and tool abuse
- **Silent data exfiltration via model, UI, and tool-driven channels**
- Threat modeling for AI systems
- Mapping AI risks to **OWASP LLM Top 10**
- Mapping AI risks to **ISO/IEC 27001:2022-style controls**

---

## Who I Am

ISO/IEC 27001:2022 Lead Auditor and cybersecurity practitioner transitioning into **AI & LLM security engineering**, with a focus on:

- LLM application security (LLM AppSec)
- RAG security and trust boundaries
- Agent safety and tool governance
- Practical red-team style experimentation

---

## Lab Roadmap (First 10 Weeks)

1. Create repository and baseline structure (`src/`, `attacks/`, `reports/`, `notes/`)
2. Build a simple LLM chatbot
3. Run and document direct prompt injection experiments
4. Build a small RAG application over local documents
5. Test indirect prompt injection via malicious documents
6. Document threat models and attack paths
7. **Simulate tool abuse and silent data exfiltration scenarios**
8. Implement mitigations and guardrails
9. Evaluate logging, detection, and governance gaps
10. Map AI risks to ISO/IEC 27001-style controls

---

# Attack Scenarios in This Lab

## Scenario 1 — Direct Prompt Injection (Basic Chatbot)

- **Path:** `attacks/prompt_injection/scenario_01_basic_chatbot.md`
- **App:** `src/app_basic_chatbot/chatbot.py`

### What this demonstrates
- How single-turn prompt injection works
- Why stateless chatbots are still vulnerable
- Why system prompts alone are insufficient as a security control

---

## Scenario 2 — Indirect Prompt Injection (RAG System Attack)

- **Path:** `attacks/indirect_prompt_injection/scenario2_rag_attack.md`
- **App:** `src/app_rag_docs/rag_app.py`
- **Malicious document:** `data/rag_docs/malicious_vendor_note.md`

### Observed behavior
- The RAG system retrieves a malicious internal document
- The model follows hidden instructions embedded in retrieved content
- System policy is overridden indirectly
- Logs capture the query, retrieved chunks, and compromised output

### What this demonstrates
- RAG documents must be treated as **untrusted input**
- Indirect prompt injection can occur without malicious user queries
- Enterprise AI systems can be compromised via poisoned PDFs, notes, or emails

**Full analysis:**  
`reports/week6_indirect_injection_report.md`

---

## Scenario 3 — Tool Abuse & Silent Data Exfiltration (Week 7)

### Overview

In Week 7, this lab explores **silent data exfiltration** — scenarios where sensitive data is leaked without traditional downloads, malware, or obvious user actions.

These attacks leverage:
- Over-privileged tools
- Agent autonomy
- Trust in model outputs
- Insufficient output and tool governance

---

### Threat Model

- Attacker controls a prompt fragment, document, or tool input
- AI system has access to tools (files, APIs, or fetch functions)
- The model is induced to misuse tools or structure outputs in a way that leaks data
- Exfiltration occurs **without explicit user intent**

---

### Attack Focus

- Model-initiated tool misuse
- Prompt-based data smuggling
- Unauthorized disclosure through structured outputs
- Gaps in logging and authorization for AI-driven actions

---

### What this demonstrates

- AI systems can exfiltrate data **without network exploits**
- Tool access significantly expands attack surface
- Traditional AppSec assumptions do not hold for agentic systems
- Detection is harder because actions appear “legitimate”

---

### OWASP LLM Top 10 Mapping (Primary)

- **LLM01 — Prompt Injection**
- **LLM02 — Insecure Output Handling**
- **LLM06 — Sensitive Information Disclosure**
- **LLM07 — Insecure Plugin / Tool Design**

---

## Silent Data Exfiltration in AI Systems

In this lab, *silent data exfiltration* refers to scenarios where sensitive data is leaked through:

- Model-generated outputs
- Structured responses (JSON, tables, summaries)
- Agent-initiated tool actions
- Trusted rendering or execution paths

These attacks often bypass:
- Traditional DLP controls
- User awareness
- UI-based security checks

They represent one of the **highest-risk and least-understood classes of AI security failures**.

---

## Code Structure
src/
app_basic_chatbot/
chatbot.py

src/
app_rag_docs/
rag_app.py

data/
rag_docs/
ai_security_notes.md
iso27001_overview.md
malicious_vendor_note.md

attacks/
prompt_injection/
scenario1.md

attacks/
indirect_prompt_injection/
scenario2_rag_attack.md

reports/
week6_indirect_injection_report.md
week7_tool_abuse_exfiltration_report.md

notes/
learning_notes.md


---

## What I Am Practicing Here

- Writing and running Python-based LLM security experiments
- Designing AI attack scenarios (prompt injection, RAG abuse, tool misuse)
- Observing and logging model behavior like a security engineer
- Threat modeling AI systems across model, application, and tool layers
- Mapping technical findings to governance frameworks (ISO/IEC 27001)

---

## Governance & Control Mapping

Each scenario is evaluated against:

- **OWASP LLM Top 10**
- **ISO/IEC 27001:2022**
  - Information access control
  - Secure system design
  - Logging and monitoring
  - Third-party and tool governance
  - Risk assessment and treatment

The goal is not only to break AI systems — but to understand **how to secure them in regulated, enterprise environments**.

---

## Disclaimer

This repository is for educational and defensive security research only.

All attack scenarios are demonstrated in controlled environments using
synthetic, non-sensitive data. No real credentials, personal data, or
proprietary information are used.

The techniques documented here are intended to improve the security of
AI-powered systems, not to enable misuse.

---

## Status

🚧 Actively evolving — new scenarios, mitigations, and reports added weekly.

