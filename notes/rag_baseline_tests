# Week 5 – RAG Baseline Tests

## Goal
Evaluate the normal, expected behavior of the RAG application before performing adversarial or red-team testing.

---

## Test 1 – "What is ISO 27001?"
**Expected behavior:**  
- Retrieve content from `iso27001_overview.md`  
- Produce an answer grounded in the retrieved text  
- No hallucinations  

**Actual behavior:**  
- The model retrieved the correct chunk  
- Answer matched the ISO 27001 document  
- No hallucination  

**Result:** PASS

---

## Test 2 – "What is a prompt injection attack?"
**Expected behavior:**  
- Retrieve context from `ai_security_notes.md`  
- Provide the definition of prompt injection  
- No hallucinations  

**Actual behavior:**  
- Correct chunk was retrieved  
- Answer described prompt injection accurately  
- No hallucination  

**Result:** PASS

---

## Test 3 – "How does RAG reduce hallucinations?"
**Expected behavior:**  
- This information does not exist in the indexed documents  
- Model should respond with “not sure”  
- No hallucinated explanation  

**Actual behavior:**  
- Model responded: “I am not sure.”  
- No hallucinations or fabricated content  

**Result:** PASS

---

## Summary
The RAG pipeline demonstrates:
- Correct retrieval and embedding behavior  
- No hallucinations when information is missing  
- Reliable grounding in provided documents  
- Proper adherence to the instruction: *“If the answer is not in the context, say you are not sure.”*

Baseline RAG functionality is stable and ready for Week 6 red-team tests.
