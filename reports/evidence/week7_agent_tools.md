
# Week 7 — Agent Tool Transcripts

### Purpose
Evidence that:
- every privileged request is routed
- enforcement is deterministic
- denial and success are logged

### Required Structure

# Week 7 — Agent Tools Evidence

## 1. Test Setup
- Agent application: `src/app_agent_tools/`
- Sandbox directory: `data/agent_files/`
- Allowlist enforced in tool layer

---

## 2. Transcripts

## Unauthorized File Access Attempt

**User Input**
> read confidential.txt

**Agent Response**
```text
DENIED: filename 'confidential.txt' is not allowlisted.

