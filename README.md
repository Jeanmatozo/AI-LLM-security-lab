# AI & LLM Security Lab

This is a hands-on security lab exploring **real-world risks in AI-powered applications**, with a focus on how Large Language Models (LLMs) fail in practice — not just in theory.

This repository is designed as a **security engineer’s lab**, emphasizing attack execution, observation, logging, and governance mapping.

---
## Setup & Dependencies

This lab is designed to be reproducible.

### Requirements
- Python 3.10+
- OpenAI API key

Clone the repo:

```bash
git clone https://github.com/Jeanmatozo/AI-LLM-security-lab.git
cd AI-LLM-security-lab

```
## Focus Areas

This lab explores realistic attack paths against AI-powered systems, including:
- **Prompt Injection & Jailbreaks**: Direct and indirect manipulation of model behavior.
- **RAG Security**: Poisoning retrieval sources to compromise grounded outputs.
- **Agentic Tool Abuse**: Exploiting over-privileged tools and autonomous agents.
- **Silent Data Exfiltration**: Leaking sensitive data through model outputs, structured responses, and indirect channels.
- **Governance Mapping**: Translating technical findings into enterprise risk language using OWASP LLM Top 10, ISO/IEC 27001:2022, and NIST AI RMF.

---

## Code Structure
The repository is organized to reflect a professional security engineering workflow: Build → Probe → Document → Mitigate.
```bash
AI-LLM-security-lab/
├── src/                # Vulnerable AI Applications (The "Targets")
│   ├── app_basic_chatbot/
│   ├── app_rag_docs/
│   └── app_agent_tools/
├── attacks/            # Technical Walkthroughs & Exploit Payloads
│   ├── prompt_injection/
│   ├── indirect_prompt_injection/
│   └── tool_abuse/
├── reports/            # Formal Security Assessments & Findings
│   ├── week01_2_lab_setup_report.md
│   ├── week03_prompt_injection_report.md
│   ├── week04_rag_construction_report.md
│   ├── week05_rag_baseline_report.md
│   ├── week06_indirect_prompt_injection_report.md
│   ├── week07_ai_red_team_report.md
│   ├── week08_tool_abuse_report.md
│   ├── week09_silent_data_exfiltration_report.md
│   └── week10_red_team_summary_report.md
├── Governance/         # Risk models, control mappings, and governance frameworks
│                       # (ISO/IEC 27001, OWASP LLM Top 10, NIST AI RMF)
└── data/               # Synthetic datasets & malicious documents

```
---

## Governance Folder

The `Governance/` directory contains non-technical artifacts that translate
attack findings into enterprise language, including:

- ISO/IEC 27001 control mappings  
- OWASP LLM Top 10 mappings  
- NIST AI RMF alignment  
- Risk statements, control gaps, and residual risk assessments  

This separates:
- **Attacks** → how systems fail
- **Governance** → how organizations manage and accept risk
---
### Red Team Perspective

This lab is approached from a red-team mindset: systems are built first, then probed,
abused, and broken to understand real failure modes before mitigations are applied.

- **Early weeks**: Black-box probing and prompt abuse
- **Middle weeks**: RAG poisoning and agent tool misuse
- **Later weeks**: Silent data exfiltration, convergence attacks, and residual risk analysis

The goal is not to “secure the model,” but to translate offensive findings into defensible controls, audit evidence, and governance decisions.

---

## Lab Roadmap (Week1- 9)


**Week 1–2**: Lab setup and baseline chatbot construction  
**Week 3**: Direct prompt injection experiments  
**Week 4–5**: RAG application build and baseline hardening  
**Week 6**: Indirect prompt injection via malicious documents  
**Week 7**: Agentic systems, tool access, least privilege, auditability  
**Week 8**: Tool abuse and confused-deputy testing  
**Week 9**: Silent data exfiltration testing and residual risk analysis 
**Week 10**: Executive and governance-level summary (no new attack surface introduced)

---

# Attack Scenarios in This Lab

## Scenario 1 — Direct Prompt Injection (Basic Chatbot)

- **App:** `src/app_basic_chatbot/chatbot.py`
- **Analysis** `reports/week03_prompt_injection_report.md`
- **Focus** `Why system prompts alone are insufficient as a security control`

## Scenario 2 — Indirect Prompt Injection (RAG Attack)
- **App** `src/app_rag_docs/rag_app.py`
- **Analysis** `reports/week06_indirect_prompt_injection_report.md`
- **Focus** `Treating retrieved documents as untrusted input`

## Scenario 3 — Tool Abuse & Silent Exfiltration
- **App** `src/app_agent_tools/agent.py`
- **Analysis** `reports/week08_tool_abuse_report.md`
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
## What This Lab Demonstrates
- How real-world AI systems fail under adversarial pressure
- Why prompt-based controls are insufficient as security boundaries
- How RAG systems expand attack surface through untrusted data
- How deterministic routing and least privilege reduce agent risk
- How silent data exfiltration can be tested and disproven with evidence
- How technical findings translate into enterprise governance decisions

---

## Who I Am

Cybersecurity practitioner with hands-on experience mapping AI and LLM security risks to enterprise governance frameworks, including ISO/IEC 27001:2022, OWASP LLM Top 10, and NIST AI Risk Management Framework. I focus on bridging technical AI exploit research with audit-ready risk, control, and governance analysis.


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

