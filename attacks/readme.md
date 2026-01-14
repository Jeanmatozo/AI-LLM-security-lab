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

### Prompt Injection
- Direct attempts to override system instructions via user input
- Examples:
  - “Ignore previous instructions”
  - Role or identity redefinition
  - Output-format manipulation

### Indirect Prompt Injection
- Malicious instructions embedded in retrieved or stored content  
  (for example: RAG documents, notes, PDFs, emails)
- The user query itself is benign, but retrieved context is adversarial

### Tool Abuse
- Coercing an LLM or agent to misuse legitimate tools in illegitimate ways
- The tool itself is not broken — the *intent* driving it is manipulated


## Future Attack Categories

As the lab evolves, additional categories may include:

- Privilege escalation
- Multi-step agent exploitation
- Cross-tool chaining attacks
- Memory and state manipulation
- Silent data exfiltration channels

These will be added only when the system design supports meaningful testing.

---

## Design Philosophy

This lab follows a progression:

1. Break behavior
2. Measure risk
3. Enforce controls
4. Assess residual exposure

Attack scenarios exist to answer the first question:

> “Where does this system fail under pressure?”

Everything else; risk, controls, governance, is built on top of that truth.
