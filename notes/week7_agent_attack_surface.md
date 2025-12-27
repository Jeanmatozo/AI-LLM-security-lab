# Week 7 — Agent with Tool Access  
## Attack Surface Notes

---

## Overview

Week 7 introduced an agentic AI system with explicit tool access.
Unlike earlier chatbot and RAG designs, this agent can take actions
(read files) rather than only generate text.

This significantly expands the attack surface.

---

## New Capabilities Introduced

- File-reading tool with allowlist enforcement
- Deterministic routing for privileged commands
- Audit logging for tool usage

Each capability introduces new security considerations.

---

## Primary Attack Surfaces

### 1. Tool Invocation Boundary

The agent can invoke tools that interact with system resources.

Risks:
- Unintended tool invocation
- Tool invocation without sufficient intent validation
- Abuse of legitimate tools for illegitimate purposes

---

### 2. Intent Interpretation

Even with deterministic routing, the agent must interpret
natural-language intent.

Risks:
- Confused-deputy scenarios
- Indirect coercion (summarize, review, check)
- Ambiguous prompts that bypass explicit command patterns

---

### 3. Parameter Handling

The file-reading tool accepts a filename parameter.

Risks:
- Filename guessing
- Enumeration attempts
- Encoded or obfuscated filenames
- Path traversal strings (even if blocked)

---

### 4. Metadata Leakage

Even when access is denied, responses may reveal:
- Existence of files
- Allowlist contents
- Naming conventions

Risks:
- Incremental reconnaissance
- Attack chaining

---

### 5. Audit & Logging Integrity

Logs are the final line of defense for detection and response.

Risks:
- Silent failures (no tool invocation)
- Partial logging
- Inconsistent event naming
- Missing correlation between prompt and action

---

## Security Assumptions Being Tested

- User input is untrusted
- Tools must enforce security, not the LLM
- Refusals are not equivalent to enforcement
- Every privileged attempt must be logged

---

## Key Question for Week 8

> Can an attacker manipulate the agent’s interpretation of intent
> to cause legitimate tools to be used in unintended or unsafe ways,
> even when allowlists and routing exist?

---

## Transition to Week 8

Week 8 will focus on **tool abuse**, including:
- indirect coercion
- confused-deputy attacks
- intent manipulation
- metadata leakage

The goal is to validate whether Week 7 controls
are sufficient under adversarial pressure.
