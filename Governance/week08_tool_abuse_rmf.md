# Week 08 — Tool Abuse Governance Mapping  
## NIST AI Risk Management Framework (AI RMF)

---

## 1. Purpose

This document translates the Week 08 technical findings on **tool abuse in agentic systems**
into governance language using the **NIST AI Risk Management Framework (AI RMF)**.

The goal is to show how:
- red-team findings become risk statements,
- risks map to governance functions,
- and technical controls support enterprise risk management.

This is not a technical exploit report.  
It is a **risk and governance translation layer.**

---

## 2. Scenario Summary (Technical Recap)

Week 08 tested whether an agent with legitimate tool access could be coerced into:

- invoking tools indirectly,
- misusing tools via intent manipulation,
- leaking capability metadata,
- or bypassing intent boundaries.

Key findings:
- Deterministic routing prevented indirect tool invocation.
- Confused-deputy attacks failed due to explicit command gating.
- Allowlist disclosure reduced attacker guesswork but exposed no sensitive files.
- No silent tool misuse occurred under tested conditions.

---

## 3. Risk Statement

### Primary Risk

If an LLM or agent can be coerced into misusing legitimate tools through indirect or manipulative intent, then:

- Confidential data may be accessed or exfiltrated,
- Unauthorized actions may be executed,
- Auditability and accountability may fail,
- Regulatory and contractual obligations may be violated.

This is a **governance risk**, not just a technical bug.

---

## 4. NIST AI RMF Mapping

### GOVERN Function  
Establish organizational policies, roles, and accountability.

Relevant Subcategories:
- GOV-1: Policies for AI risk management exist
- GOV-2: Roles and responsibilities defined
- GOV-3: Oversight and accountability enforced

Week 08 Alignment:
- Tool usage policies are enforced at the application layer.
- Deterministic routing establishes clear authority boundaries.
- Logging creates accountability for privileged actions.

---

### MAP Function  
Understand system context, assets, and risk environment.

Relevant Subcategories:
- MAP-1: Context of AI system is documented
- MAP-2: Assets and impact are identified
- MAP-3: Risk scenarios are defined

Week 08 Alignment:
- Assets: sandbox files, tool privileges, logs
- Risk scenario: confused-deputy tool abuse
- Trust boundaries documented between:
  - user → agent
  - agent → tools
  - tools → filesystem

---

### MEASURE Function  
Analyze, assess, and track risks.

Relevant Subcategories:
- MEA-1: Risk identified and assessed
- MEA-2: Threat modeling performed
- MEA-3: Monitoring defined

Week 08 Alignment:
- Red-team prompts tested indirect coercion
- Tool invocation attempts logged
- Audit gap discovered and fixed (Week 07 carryover)
- Risk severity classified (Informational to Low)

---

### MANAGE Function  
Mitigate and respond to risk.

Relevant Subcategories:
- MAN-1: Risk response implemented
- MAN-2: Controls enforced
- MAN-3: Residual risk accepted or mitigated

Week 08 Alignment:
- Deterministic routing prevents inferred-intent execution
- Strict filename validation prevents parameter abuse
- Logging ensures traceability
- Allowlist disclosure risk accepted intentionally

---

## 5. Control Mapping

| Control Area | Technical Control | Governance Purpose |
|---------------|------------------|--------------------|
| Access Control | Allowlisted filenames | Prevent unauthorized access |
| Least Privilege | Tool gating | Limit blast radius |
| Audit Logging | Tool-level logs | Accountability |
| Intent Control | Deterministic routing | Remove LLM discretion |
| Validation | Filename regex | Prevent injection |

These controls support:
- Confidentiality
- Integrity
- Accountability
- Regulatory defensibility

---

## 6. Business Impact Translation

### If This Failed in Production:

- Sensitive files could be leaked without malware
- Actions would appear “legitimate”
- Traditional DLP would miss it
- Forensics would lack evidence if logs failed

### Business Consequences:

- Regulatory exposure (privacy, data protection)
- Contractual violations
- Loss of customer trust
- Audit failures
- Legal liability

---

## 7. Residual Risk

Even with deterministic routing:

- New tools introduce new risk
- Intent classification errors remain possible
- Indirect prompt injection may still influence outputs
- Multi-tool chaining increases attack surface

Residual risk must be:
- documented,
- monitored,
- and accepted explicitly by leadership.

---

## 8. Governance Takeaway

Week 08 shows:

- Tool abuse is not just a technical problem  
- It is a governance problem

Strong AI governance requires:

- Technical enforcement
- Policy clarity
- Logging and evidence
- Risk ownership
- Executive awareness

This is the bridge between:
> “Here is how I broke it”  
and  
> “Here is how the organization manages that risk.”


