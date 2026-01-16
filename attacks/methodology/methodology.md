
# How to design, run, measure, and report AI security attacks in this lab

## Philosophy

This lab treats AI security as an engineering and governance problem, not a prompt trick.

Principles:
- LLM behavior is not a security control.
- Enforcement must live in trusted code.
- Auditability is as important as prevention.
- Every technical finding must map to business risk.

## Attack Lifecycle

1. Threat Modeling  
   - Identify assets, actors, and trust boundaries.
2. Scenario Design  
   - Define goal, method, and success condition.
3. Execution  
   - Run controlled attacks with logging enabled.
4. Evidence Capture  
   - Save transcripts, logs, and outputs.
5. Analysis  
   - Interpret what happened and why.
6. Mitigation Design  
   - Propose immediate, short-term, and long-term fixes.
7. Governance Mapping  
   - Map to ISO 27001, OWASP LLM Top 10, enterprise risk language.

## Scenario Structure

Every scenario contains:

- Context  
- Attack Goal  
- Attack Method  
- Prompts / Inputs  
- Observations  
- Interpretation  
- Mitigation Strategy  
- Severity  
- Business Impact  
- Control Mapping  
- Red Team Perspective

## Evidence Standards

Every attack must produce:

- Raw prompts
- Model responses
- Tool logs (if used)
- File access logs
- Screenshots or transcripts

Evidence lives in:
reports/evidence/weekX_*.md

## Risk Rating

Severity is based on:

- Confidentiality impact
- Integrity impact
- Availability impact
- Ease of exploitation
- Detectability

Ratings:
- Informational
- Low
- Medium
- High
- Critical

## Business Translation

Every finding must answer:

- What data or system is at risk?
- Who could be harmed?
- What regulation or contract is affected?
- What financial or reputational impact could occur?

## Red Team Progression

Week 3–4: Baseline & recon  
Week 5: RAG grounding & abstention  
Week 6: Indirect prompt injection  
Week 7: Agent tools & privilege probing  
Week 8: Tool abuse  
Week 9: Silent data exfiltration  

Red team posture increases as system complexity increases.


