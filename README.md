# AI & LLM Security Lab

This is a hands-on security lab exploring **real-world risks in AI-powered applications**, with a focus on how Large Language Models (LLMs) fail in practice — not just in theory.

This repository is designed as a **security engineer’s lab**, emphasizing attack execution, observation, logging, and governance mapping.

---
## Setup & Dependencies

This lab is designed to be reproducible.

### Requirements
- Python 3.10+
- OpenAI API key

Install dependencies:

```bash
git clone https://github.com/Jeanmatozo/AI-LLM-security-lab.git
cd AI-LLM-security-lab
pip install -r requirements.txt

```
## Focus Areas

This lab explores realistic attack paths against AI-powered systems, including:

- Prompt Injection & Jailbreaks: Direct and indirect manipulation of model behavior.
- RAG Security: Poisoning retrieval sources to compromise grounded outputs.
- Agentic Tool Abuse: Exploiting over-privileged tools and autonomous agents.
- Silent Data Exfiltration: Leaking sensitive data via model, UI, and tool-driven channels.
- Governance Mapping: Aligning technical risks to OWASP LLM Top 10 and ISO/IEC 27001:2022.

---

## Code Structure
The repository is organized to reflect a professional security engineering workflow: Build → Probe → Document → Mitigate.
```bash
AI-LLM-security-lab/
├── src/                # Vulnerable AI Applications (The "Targets" )
│   ├── app_basic_chatbot/
│   ├── app_rag_docs/
│   └── app_agent_tools/
├── attacks/            # Technical Walkthroughs & Exploit Payloads
│   ├── prompt_injection/
│   ├── indirect_prompt_injection/
│   └── tool_abuse/
├── reports/            # Formal Security Assessments & Findings
│   ├── week3_prompt_injection_report.md
│   ├── week6_indirect_prompt_injection_report.md
│   └── week8_tool_abuse_report.md
├── Governance/         # Risk Management & Control Mappings
├── data/               # Synthetic Datasets & Malicious Documents
└── logs/               # Audit Trails & Model Behavior Logs

```
---
### Red Team Perspective

This lab is approached from a red-team mindset: systems are built first, then probed,
abused, and broken to understand real failure modes before mitigations are applied.

- Early weeks: Focus on black-box probing and prompt abuse
- Middle weeks: Explore RAG poisoning and tool misuse
- Later weeks: Examine silent data exfiltration, guardrail bypasses, and residual risk

The goal is to translate offensive findings into defensible controls, audit evidence, and enterprise risk decisions.

---

## Lab Roadmap (First 10 Weeks)

1. Week 1-2: Lab setup and baseline chatbot construction.
2. Week 3: Direct prompt injection experiments.
3. Week 4-5: RAG application build and baseline hardening.
4. Week 6: Indirect prompt injection via malicious documents.
5. Week 7: Agentic systems and tool access implementation.
6. Week 8: Tool abuse and silent data exfiltration scenarios.
7. Week 9: Mitigation implementation (Guardrails & Deterministic Routing).
8. Week 10: Final governance mapping to ISO/IEC 27001:2022.

---

# Attack Scenarios in This Lab

## Scenario 1 — Direct Prompt Injection (Basic Chatbot)

- **App:** `src/app_basic_chatbot/chatbot.py`
- **Analysis** `reports/week3_prompt_injection_report.md`
- **Focus** `Why system prompts alone are insufficient as a security control`

## Scenario 2 — Indirect Prompt Injection (RAG Attack)
- **App** `src/app_rag_docs/rag_app.py`
- **Analysis** `reports/week6_indirect_prompt_injection_report.md`
- **Focus** `Treating retrieved documents as untrusted input`

## Scenario 3 — Tool Abuse & Silent Exfiltration
- **App** `src/app_agent_tools/agent.py`
- **Analysis** `reports/week8_tool_abuse_report.md`
- **Focus** `Preventing model-initiated tool misuse via deterministic routing`

---
## Governance & Control Mapping

Each scenario is evaluated against:
- **OWASP LLM Top 10** `(LLM01, LLM02, LLM06, LLM07)`
- **ISO/IEC 27001:2022**
  - Information access control
  - Secure system design
  - Logging and monitoring
  - Third-party and tool governance

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


## Who I am 
ISO/IEC 27001:2022 Lead Auditor and cybersecurity practitioner transitioning into AI & LLM security engineering. I focus on bridging the gap between technical AI exploits and enterprise-grade governance


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

