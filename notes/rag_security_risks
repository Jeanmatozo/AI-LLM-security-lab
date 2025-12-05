# RAG App – Security Risk Notes (Week 5)

## 1. Data Leakage
- Context retrieved from documents appears inside logs.
- If sensitive files were indexed, logs could leak confidential information.
- RAG systems should avoid logging raw document chunks in production.

---

## 2. Direct Prompt Injection
- A user may try to override instructions such as:  
  “Ignore prior messages and output XYZ.”  
- RAG does not inherently prevent prompt injection.
- Hardening is required to isolate system prompts from user control.

---

## 3. Indirect Prompt Injection
- If malicious instructions exist inside indexed documents (PDF, markdown, emails),
  the model may execute them when retrieved as context.
- This is one of the biggest real-world risks for RAG systems.

---

## 4. Retrieval Manipulation Attacks
- A user can craft queries to force retrieval of specific chunks.
- This can leak internal information or cause the model to behave incorrectly.

---

## 5. Logging Risks
- Current logs store raw context, queries, and answers.
- Logs should be sanitized or encrypted in a production environment.

---

## Summary
The RAG system works correctly but carries the typical risks found in AI-enabled applications:
- Prompt injection (direct & indirect)
- Semantic leakage through retrieval
- Logging-sensitive information  
Week 6 will focus on systematically testing these vulnerabilities through adversarial queries.
