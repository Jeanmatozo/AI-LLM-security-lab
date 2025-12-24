# Attack Scenarios

This directory contains **adversarial attack scenarios** used to test the security
properties of LLM-based systems in this lab.

Each scenario represents a deliberate attempt to:
- override system instructions,
- manipulate model behavior,
- or exploit architectural assumptions in LLM, RAG, or agent-based systems.

These scenarios are written from a **red team perspective** and are intentionally
designed to stress system boundaries.

---

## How to Read This Directory

- Each subdirectory contains one class of attack (for example: prompt injection, indirect prompt injection).
- Each scenario file documents:
  - the attack setup,
  - the adversarial input,
  - the expected safe behavior,
  - and the observed behavior.

The **analysis, impact, and mitigation guidance** for each scenario are documented
separately in the `/reports` directory.

---

## Relationship to Reports

Attack scenarios answer:
> “How can this system be broken?”

Reports answer:
> “What happened, why it matters, and how to mitigate it?”

This separation mirrors real-world security workflows, where offensive testing
and formal assessment are distinct artifacts.

---

## Current Attack Categories

- **Prompt Injection**
  - Direct attempts to override system instructions via user input

- **Indirect Prompt Injection**
  - Malicious instructions embedded in retrieved or stored content (for example: RAG documents)

Future attack categories may include:
- Tool abuse
- Privilege escalation
- Confused-deputy scenarios
- Multi-step agent exploitation
