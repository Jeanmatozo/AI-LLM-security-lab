# Week 5 Security Report — RAG App Hardening & Baseline Evaluation
**Author:** Jean Akingeneye  
**Date:** Week 5  
**Application Tested:** `src/app_rag_docs/rag_app.py`  
**Focus Areas:** Retrieval quality, logging, baseline behavior, security risks

---

## 1. Executive Summary

In Week 5, I enhanced the RAG (Retrieval-Augmented Generation) application by adding structured logging, running baseline evaluations, and documenting early security risks. These improvements helped transform the RAG app from a simple prototype into a system suitable for deeper security testing in later weeks.

The major accomplishment was implementing **query-level logging**—a critical capability for AI security engineering that allows visibility into how the model behaves under different retrieval conditions.

---

## 2. What Was Built This Week

###  1. Logging System Added
Implemented structured logging to:

- Capture every user query  
- Save retrieved context chunks  
- Record the final model answer  

**Log file created:**  
`logs/week5_rag_log.txt` *(excluded from GitHub via .gitignore)*

Logging now enables:

- Traceability of model failures  
- Repeatable test cases  
- Evidence collection during red-teaming  
- Security analysis for prompt manipulation or unexpected outputs  

---

###  2. Baseline Behavior Tests
I ran a set of “normal operation” queries to understand expected RAG behavior.

**Queries tested:**

- *“What is ISO 27001?”*  
- *“What is a prompt injection attack?”*  
- *“How does RAG reduce hallucinations?”*

**Results:**

- The system correctly answered questions when the information existed in the RAG documents.
- When information was not found, the model obeyed my instruction to respond with:
  > **“I am not sure.”**  
  instead of hallucinating.

This is important:  
**A well-designed RAG system can reduce hallucinations if the prompt explicitly restricts unsupported answers.**

---

###  3. Security Notes & Risk Documentation

Created two markdown notes summarizing security findings:

1. Baseline behavior summary  
2. RAG security risk notes, including:

- Direct prompt injection  
- Indirect prompt injection (tested in Week 6)  
- Retrieval manipulation  
- Data leakage via context windows  
- Logging sensitivity concerns  

This prepared the foundation for Week 6 and beyond.

---

## 3. Key Learnings

### Logging is essential for AI security
With logs, I can now:

- Inspect context poisoning  
- Spot unexpected behavior  
- Reproduce attacks  
- Write professional-style security reports  

This mirrors enterprise AI security engineering practices.

---

### RAG can reduce hallucinations — when designed correctly
By enforcing:
If the answer is not in the context, say "I am not sure."


…my system refused to hallucinate during baseline testing.

This shows how **RAG + strict prompting** can improve reliability.

---

###  Prompt injection cannot be fully prevented
One of the most important insights this week:

**It is unrealistic to assume prompt injection can always be prevented.**  
Attackers are adaptive, creative, and constantly evolving techniques.

A safer mindset is:

###  “Assume prompt injection will eventually happen.”  
Then design to contain its impact through:

- Access control  
- Least privilege  
- Output validation  
- Tool restrictions  
- Context sanitization  

This insight shaped Week 6’s indirect prompt injection testing.

---

###  Git & Environment Setup Mastery
This week I also:

- Learned to use `.gitignore` properly  
- Avoided committing logs and cache files  
- Set permanent Windows environment variables (OPENAI_API_KEY)  
- Cleaned up repo structure with correct folder organization  

These are foundational skills for engineering workflows.

---

## 4. What Blocked Me

Some challenges included:

- Confusion around Git local vs remote sync  
- Cache/log folders repeatedly appearing in `git status`  
- Having to re-set the API key every terminal session before learning environment variables  
- Deciding which files belong in GitHub vs local-only security artifacts  

All of these were resolved step-by-step.

---

## 5. Next Steps (Lead-in to Week 6)

With the RAG system hardened and logging enabled, the next focus becomes:

###  Week 6 — Attack the RAG App  
Specifically:

- Indirect prompt injection  
- Stored attacks inside documents  
- Context poisoning  
- Logging attack evidence  
- Writing a professional security report (Week 6)

This sets the stage for more advanced AI red-teaming and agent security work in later weeks.

---

## 6. Files Added / Updated in Week 5



src/app_rag_docs/rag_app.py (logging + improvements)
logs/week5_rag_log.txt (local only, gitignored)
reports/ (baseline notes + security notes)
.gitignore (added logs/, pycache/ rules)
data/rag_docs/*.md (documents for retrieval)


---

## 7. Conclusion

Week 5 marks a turning point:  
I moved from **building** the RAG system to **analyzing and securing it**.

I now have:

- A functioning RAG app  
- Proper logging  
- A baseline behavior profile  
- A first set of documented risks  
- The mindset of an AI security engineer preparing for adversarial testing  

This foundation made Week 6’s indirect prompt injection attack possible—and successful.
