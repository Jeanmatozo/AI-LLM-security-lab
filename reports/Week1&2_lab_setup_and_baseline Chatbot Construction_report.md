# Week 1–2 — Lab Setup & Baseline Chatbot Construction  

---

## 1. Summary

Weeks 1 and 2 established the foundation of the AI-LLM Security Lab.

Week 1 focused on repository setup, documentation, and structural planning.  
Week 2 focused on building and running the first functional LLM application: a basic terminal chatbot.

These weeks did not involve adversarial testing yet. Instead, they created the **baseline system and workflow** that all later security assessments build upon.

**Key takeaway:** Before breaking AI systems, you must first understand how to build and run them end-to-end.

---

## 2. Scope

### In Scope
- GitHub repository setup
- README and roadmap creation
- Base folder structure:
  - `src/`
  - `attacks/`
  - `reports/`
  - `notes/`
- Baseline chatbot implementation:
  - `src/app_basic_chatbot/chatbot.py`
- Local development environment setup

### Out of Scope
- Prompt injection testing (Week 3)
- RAG systems (Week 5+)
- Agent tools (Week 7+)

---

## 3. Environment & Assumptions

- Development on local Windows machine  
- Python installed and configured correctly  
- Command Prompt used for navigation (`cd`, `dir`)  
- OpenAI API key stored in environment variable  
- `openai` Python package installed  

---

## 4. System Construction

### Week 1 — Lab Foundation

Actions completed:
- Created public GitHub repository: `AI-LLM-security-lab`
- Wrote initial README explaining:
  - Purpose of the lab  
  - Security focus  
  - Early roadmap  
- Created base folders:
  - `src/`
  - `attacks/`
  - `reports/`
  - `notes/`
- Added `.gitkeep` files so empty folders are tracked

**Goal:**  
Create a structure that mirrors real security engineering workflows:
Build → Test → Document → Govern.

---

### Week 2 — Baseline Chatbot

Actions completed:
- Created:
  - `src/app_basic_chatbot/`
  - `chatbot.py`
- Implemented a simple script that:
  - Sends a prompt to the OpenAI API  
  - Receives a response  
  - Prints output in terminal  

- Environment setup:
  - Installed Python correctly  
  - Learned basic terminal usage  
  - Installed `openai` package  
  - Created API key  
  - Set `OPENAI_API_KEY` environment variable  

- Tested real prompts:
  - “What is ISO 27001?”
  - Basic cybersecurity questions  

**Result:**  
Successfully ran personal code that called a real LLM and returned live responses.

---

## 5. Threat Model (Baseline)

At this stage, security testing was not yet active, but basic trust boundaries were identified.

### Assets
- API key  
- System prompt integrity  
- Output correctness  

### Trust Boundaries
- User input → Application code  
- Application code → LLM API  

### Early Risks Identified
- User input is untrusted  
- Model behavior is probabilistic  
- No logging or security controls yet  

---

## 6. Red Team Perspective

From a red-team perspective, Weeks 1–2 represent:

- Target construction phase  
- Reconnaissance preparation  
- Understanding normal behavior  

Before attacking:
- You must know how the system is built  
- How inputs flow  
- How outputs are generated  
- Where trust boundaries exist  

This phase defines “normal” so future attacks can show “abnormal.”

---

## 7. Evidence

- GitHub repository with:
  - README  
  - Base folders  
  - `src/app_basic_chatbot/chatbot.py`  
- Terminal output showing:
  - Successful API calls  
  - Correct model responses  

---

## 8. Business Impact

Organizations often skip foundational understanding and jump directly to “AI security.”

This phase proves:
- Teams must understand how AI systems are built before securing them  
- Developers need hands-on experience with:
  - APIs  
  - Prompts  
  - Environment variables  
  - Runtime behavior  

Without this foundation:
- Security controls will be theoretical  
- Audits will lack technical grounding  
- Risk decisions will be weak  

---

## 9. Residual Risk & Next Steps

### Residual Risk
- No security controls implemented yet  
- No logging  
- No input validation  
- No threat detection  

This is intentional: the system is still in its “naive” state.

### Next Steps (Week 3)
- Begin direct prompt injection testing  
- Observe how easily system behavior can be overridden  
- Establish first real security findings  

---

## 10. Conclusion

Weeks 1–2 established:

- A professional lab structure  
- A working LLM application  
- Developer confidence in running AI locally  

This phase answers:

> “Can I build and run an AI system myself?”

From Week 3 onward, the question becomes:

> “Now that I can build it — how do I break it, measure risk, and secure it?”
