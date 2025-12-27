# Report 03 — Tool Abuse in Agentic Systems

---

## 1. Summary
This assessment evaluates whether an LLM-based agent can be coerced into
misusing legitimate tools through indirect or manipulative user prompts.
The focus is on confused-deputy behavior rather than direct policy violations.

---

## 2. Scope

### In Scope
- Agent routing logic
- File-reading tool
- Allowlist enforcement
- Audit logging

### Out of Scope
- Network tools
- Write or modify tools
- Multi-agent systems

---

## 3. Threat Model

### Assets
- Confidential sandbox files
- Tool execution privileges
- Audit logs

### Attacker
- Untrusted user attempting to extract sensitive data indirectly

---

## 4. Tool Abuse Scenario

Summarize Scenario 1 here and link to:
- `attacks/tool_abuse/scenario1.md`

---

## 5. Findings

### Finding 1 — Confused-Deputy Risk via Indirect Requests
**Severity:** Medium / High (depending on outcome)

Describe:
- what the agent attempted
- whether tools were invoked
- whether enforcement held

---

## 6. Impact Analysis
Explain:
- why tool abuse is dangerous
- how it scales with more tools
- why reasoning-based refusal is insufficient

---

## 7. Evidence
- `reports/evidence/week8_tool_abuse.md`

---

## 8. Mitigations & Recommendations

### Short-Term
- Intent classification before tool routing
- Explicit allowlisting of *intents*, not just filenames

### Medium-Term
- Tool-specific policy checks
- Refusal templates that avoid metadata leakage

### Long-Term
- Capability-based security for agents
- Human-in-the-loop for high-risk tool actions

---

## 9. Conclusion
Tool abuse represents a distinct and high-risk class of failures
in agentic systems that cannot be addressed by prompt design alone.
