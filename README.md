# AI & LLM Security Lab

## Table of Contents

- [Setup & Dependencies](#setup--dependencies)
- [Requirements](#requirements)
- [Lab Progression (High-Level)](#lab-progression-high-level)
- [Code Structure](#code-structure)
- [Governance Folder](#governance-folder)
  - [Red Team Perspective](#red-team-perspective)
- [Attack Scenarios in This Lab](#attack-scenarios-in-this-lab)
  - [Scenario 1 — Direct Prompt Injection (Basic Chatbot)](#scenario-1--direct-prompt-injection-basic-chatbot)
  - [Scenario 2 — Indirect Prompt Injection (RAG Attack)](#scenario-2--indirect-prompt-injection-rag-attack)
  - [Scenario 3 — Tool Abuse & Silent Exfiltration](#scenario-3--tool-abuse--silent-exfiltration)
- [Governance & Control Mapping](#governance--control-mapping)
- [Silent Data Exfiltration in AI Systems](#silent-data-exfiltration-in-ai-systems)
- [What This Lab Demonstrates](#what-this-lab-demonstrates)
- [Automation and Reproducibility Note](#automation-and-reproducibility-note)
- [Disclaimer](#disclaimer)
- [Status](#status)


This is a hands-on security lab exploring **real-world risks in AI-powered applications**, with a focus on how Large Language Models (LLMs) fail in practice — not just in theory.

This repository is designed as a **security engineer’s lab**, emphasizing adversarial evaluation, observation, logging, and governance mapping.

> **Note:** This repository is a research and experimentation lab.

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
## Lab Progression (High-Level)

This lab progresses from black-box probing to system-level abuse:

- Baseline LLM probing and prompt injection
- RAG construction and document-based attacks
- Agentic tool misuse and privilege boundaries
- Silent data exfiltration and residual risk analysis
- Governance and executive-level risk translation


---

## Code Structure
The repository is organized to reflect a professional security engineering workflow: Build → Probe → Document → Mitigate.
```bash
AI-LLM-security-lab/
├── src/                # Vulnerable AI Applications (The "Targets")
│   ├── app_basic_chatbot/
│   ├── app_rag_docs/
│   └── app_agent_tools/
├── attacks/            # Adversarial Test Cases & Evaluation Artifacts
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

This lab is approached from a red-team mindset: systems are built first, then probed
under adversarial conditions to understand real failure modes before mitigations are applied.

- **Early weeks**: Black-box probing and prompt abuse
- **Middle weeks**: RAG poisoning and agent tool misuse
- **Later weeks**: Silent data exfiltration, convergence attacks, and residual risk analysis

The goal is not to “secure the model,” but to translate offensive findings into defensible controls, audit evidence, and governance decisions.

---

## Attack Scenarios in This Lab

### Scenario 1 — Direct Prompt Injection (Basic Chatbot)

- **App:** `src/app_basic_chatbot/chatbot.py`
- **Analysis** `reports/week03_prompt_injection_report.md`
- **Focus** `Why system prompts alone are insufficient as a security control`
  ![Direct Prompt Injection — Observed Behavior](assets/screenshot_01_basic_chatbot_observed_behavior.jpeg)
  *Observed behavior: single-turn instruction override signal (`INJECTED_SUCCESS`). Behavior does not persist due to stateless design.*

### Scenario 2 — Indirect Prompt Injection (RAG Attack)
- **App** `src/app_rag_docs/rag_app.py`
- **Analysis** `reports/week06_indirect_prompt_injection_report.md`
- **Focus** `Treating retrieved documents as untrusted input`
![RAG Context Interference — Observed Behavior](assets/screenshot_02_rag_context_interference.jpeg)
*Observed behavior: retrieved context introduced instruction-shaped interference, resulting in unexpected output. Evidence captured via retrieval logs.*

### Scenario 3 — Tool Abuse & Silent Exfiltration
- **App** `src/app_agent_tools/agent.py`
- **Analysis** `reports/week08_tool_abuse_report.md`
- **Focus** `Preventing model-initiated tool misuse via deterministic routing`
![Agent Tool Boundary Enforcement — Observed Behavior](assets/screenshot_03_agent_boundary_enforcement.jpeg)
*Observed behavior: deterministic routing denied unauthorized tool invocation and logged the decision for auditability.*

---
### Governance & Control Mapping

Each scenario is evaluated against:
- **OWASP LLM Top 10** `(LLM01, LLM02, LLM06, LLM07)`
- **ISO/IEC 27001:2022**
  - Information access control
  - Secure system design
  - Logging and monitoring
  - Third-party and tool governance

---

### Silent Data Exfiltration in AI Systems

Silent data exfiltration is treated as a first-class risk in this lab.
Detailed analysis and examples are documented in the corresponding scenario reports.


---
### What This Lab Demonstrates
- How real-world AI systems fail under adversarial pressure
- Why prompt-based controls are insufficient as security boundaries
- How RAG systems expand attack surface through untrusted data
- How deterministic routing and least privilege reduce agent risk
- How silent data exfiltration can be tested and disproven with evidence
- How technical findings translate into enterprise governance decisions

---

## Automation and Reproducibility Note

This repository focuses on adversarial evaluation design, observed behavior, and
failure-mode analysis for AI-powered systems.

While test cases are documented conceptually to emphasize research intent and
evaluation framing, these scenarios are designed to be compatible with
automated execution frameworks.

A separate repository (`llm-red-team-toolkit`) demonstrates how similar test
cases can be executed programmatically, with structured result collection and
artifact generation (e.g., JSONL outputs and scoring signals).

This separation reflects a deliberate design choice:
- This lab emphasizes *what* is evaluated and *why*
- Automation frameworks emphasize *how* evaluations are executed at scale

---

### Disclaimer

This repository is for educational and defensive security research only.

All attack scenarios are demonstrated in controlled environments using
synthetic, non-sensitive data. No real credentials, personal data, or
proprietary information are used.

The techniques documented here are intended to improve the security of
AI-powered systems, not to enable misuse.

---

### Status

🚧 Actively evolving — new scenarios, mitigations, and reports added weekly.

