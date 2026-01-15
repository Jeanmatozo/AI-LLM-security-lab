# Week 8 — Tool Abuse & Guardrail Evaluation

## 1. Summary  
This assessment evaluates the resilience of an agentic AI system against Tool Abuse and Confused Deputy attacks. Building on the Week 7 findings regarding audit gaps, this week focuses on testing the effectiveness of Deterministic Routing and Parameter Validation as primary defense mechanisms.

---

## 2. Scope  

**Application:**  
- `src/app_agent_tools/agent.py`  

**Tools:**  
- File-reading tool with allowlist enforcement  

**Attack Vectors:**  
- Indirect coercion  
- Parameter tampering  
- Allowlist probing  

---

## 3. Findings  

### Finding 1 — Confused-Deputy Risk via Indirect Requests  
**Severity:** Informational (Mitigated)  

The agent was subjected to socially engineered prompts designed to trick it into using the file-reading tool without an explicit user command.  

**Result:**  
The system successfully ignored inferred intent. Because tool invocation is gated behind deterministic routing, the “Confused Deputy” path was blocked at the application layer.

---

### Finding 2 — Allowlist Disclosure as Capability Signal  
**Severity:** Low  

The command `what files can you read` discloses the allowlist. While intentional, this provides an attacker with a verified list of targets, reducing the cost of reconnaissance.

---

## 4. Red Team Analysis  

From an adversarial perspective, the transition to Deterministic Routing has fundamentally changed the attack surface.

**Intent Decoupling:**  
By removing the LLM’s ability to “decide” when to use a tool based on natural language, we have eliminated a broad class of prompt injection attacks. The attacker can no longer use “polite coercion” to bypass security logic.

**Reconnaissance Shift:**  
Since direct tool abuse is blocked, the red team focus shifts to Parameter Tampering. We attempted to bypass the allowlist using path traversal (`../../etc/passwd`) and encoding tricks. However, because the validation happens in the Trusted Tool Layer (Python code) rather than the Untrusted Model Layer, these attempts were caught by standard string validation.

---

## 5. Mitigations & Recommendations  

### Implemented Controls  

- **Deterministic Routing:**  
  Privileged actions are mapped to specific regex patterns, ensuring the LLM cannot be “convinced” to run a tool outside of defined parameters.  

- **Hardcoded Allowlists:**  
  The tool layer maintains a “Source of Truth” for accessible files that the LLM cannot modify.  

### Recommended Improvements  

- **Output Filtering:**  
  Implement a secondary check on the content returned by tools to prevent sensitive data from being leaked even if a tool is legitimately invoked.  

- **Rate Limiting:**  
  Add per-user limits on tool calls to prevent automated allowlist probing and “denial of wallet” attacks.  

---

## 6. Business Impact

Failure to secure tool access in agentic systems leads to:

- Unauthorized data exfiltration  
- System integrity loss  
- Undetectable misuse disguised as “legitimate” operations  

By moving enforcement from the **probabilistic model layer** to the **deterministic code layer**, the organization gains:

- Verifiable access control  
- Forensic auditability  
- Alignment with ISO/IEC 27001 requirements for access control and monitoring  

This is not just a technical improvement—it is a governance upgrade.

---

## 7. Conclusion

Week 8 demonstrates that:

- Tool abuse is primarily an **intent-control problem**, not a tooling problem  
- Deterministic routing is a critical security boundary  
- LLM refusals are not security controls  
- Governance-grade security requires:
  - enforcement in code  
  - logging as evidence  
  - explicit trust boundaries  

This week establishes the foundation for Week 9:  
**Silent data exfiltration through legitimate channels.**
