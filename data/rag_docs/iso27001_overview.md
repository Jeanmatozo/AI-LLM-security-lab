# ISO/IEC 27001 Overview

These notes give a high-level overview of ISO/IEC 27001, the core international standard for information security management systems (ISMS).

---

## 1. What is ISO/IEC 27001?

ISO/IEC 27001 is an international standard that describes how to build, operate, monitor, and continually improve an **Information Security Management System (ISMS)**.

An ISMS is a structured way for an organization to:

- Understand its information security risks  
- Select and implement controls to manage those risks  
- Continually review and improve its security posture  

The current version is ISO/IEC 27001:2022. It replaces the earlier 2013 version and aligns more closely with modern risk and governance practices.

---

## 2. Scope and objectives

The main objectives of ISO 27001 are to help organizations:

- Protect the **confidentiality, integrity, and availability (CIA)** of information  
- Use a **risk-based approach** to security  
- Define clear **roles, responsibilities, and processes**  
- Demonstrate due diligence and compliance to customers, regulators, and partners  

The standard is **industry-neutral**: it can be applied to banks, hospitals, SaaS startups, universities, governments, etc.

---

## 3. ISMS core concepts

ISO 27001 revolves around a few core ideas:

### 3.1 Context of the organization

- Understand internal and external issues that affect information security  
- Identify interested parties (customers, regulators, partners) and their requirements  

### 3.2 Leadership and planning

- Top management must support and approve the ISMS  
- Define an information security policy and clear objectives  
- Plan how to address risks and opportunities

### 3.3 Support and operation

- Ensure there are resources, competence, and awareness  
- Establish documented procedures where needed  
- Operate processes to manage and control information security risks  

### 3.4 Performance evaluation and improvement

- Monitor and measure security performance  
- Conduct internal audits and management reviews  
- Handle nonconformities and continuously improve the ISMS  

---

## 4. Annex A controls (high-level)

Annex A of ISO 27001:2022 lists a catalogue of security controls. They are grouped into four main themes:

1. **Organizational controls**  
   - Policies, roles and responsibilities  
   - Risk management, supplier management  
   - Information classification, acceptable use  
   - Privacy, compliance, and secure project management  

2. **People controls**  
   - Background checks  
   - Security awareness and training  
   - Disciplinary process and responsibilities after termination  

3. **Physical controls**  
   - Secure areas and physical entry controls  
   - Protection of equipment and facilities  
   - Clear desk / clear screen, secure disposal  

4. **Technological controls**  
   - Access control and authentication  
   - Cryptography and key management  
   - Logging and monitoring  
   - Backup, operations security, network security  
   - Secure development and change management  

An organization does **not** need to implement every control. Instead, it must:

- Perform a risk assessment  
- Decide which controls are applicable  
- Justify exclusions in the Statement of Applicability (SoA)

---

## 5. Certification

Organizations can choose to have their ISMS **certified** by an independent auditor.

Typical steps:

1. Define the **scope** of the ISMS (e.g., a specific business unit, product, or the whole company).  
2. Implement the required processes and controls.  
3. Perform internal audits and a management review.  
4. Undergo a certification audit by an accredited certification body.  
5. Maintain and improve the ISMS through surveillance audits (usually annually).

Certification shows external parties that the organization has a **formal, audited approach** to managing information security.

---

## 6. How this connects to AI and LLM security

ISO 27001 is **not** an AI-specific standard, but it provides the governance layer for AI and LLM security:

- Risk assessments can include:
  - LLM-related threats (prompt injection, data leakage, model misuse)  
  - Risks from training data, APIs, and third-party models  

- Annex A controls map to AI systems, for example:
  - **Access control:** who can query models and view logs  
  - **Cryptography:** protecting training data, embeddings, and model artifacts  
  - **Operations security:** logging, monitoring, and incident response for AI services  
  - **Supplier relationships:** managing risks from external model providers or APIs  

In your AI & LLM Security Lab, ISO 27001 acts as the **governance and control framework** that sits above the technical experiments (prompt injection, RAG security, agents, etc.).

---

## 7. Key takeaways

- ISO/IEC 27001 defines how to build and run an ISMS using a risk-based approach.  
- Annex A provides a catalogue of controls that can be tailored to the organization’s needs.  
- Certification is optional but widely used to show trust and compliance.  
- For AI and LLM security, ISO 27001 provides the **management and control structure** that complements technical defenses and red-teaming work.
