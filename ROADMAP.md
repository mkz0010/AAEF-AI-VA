# Roadmap

## Phase 0: Business and Safety Design

- Define project charter.
- Define MVP scope.
- Define AI data handling policy.
- Define credential_ref model.
- Define Tool Gateway and AAEF Authorization Gateway boundaries.
- Define NDA, AI use, and external AI handling assumptions.

## Phase 1: Technical Prototype

### credential_ref Flow Decision

- credential_ref is visible to AI as a reference only.
- Raw credentials remain AI-hidden and are resolved only by Tool Gateway after authorization.
- MVP may use a local mock Vault with fictitious credentials.
- Sanitization is required before tool output is returned to AI.


### MVP Scope Decision

- Initial MVP focuses on Web/API/NW assessment assistance.
- Initial tools are OWASP ZAP, Nmap, nuclei, and limited browser automation.
- Burp Suite and Nessus / Tenable are deferred until the core control model is stable.
- Fully autonomous penetration testing, destructive testing, exploit chaining, and lateral movement are out of scope.


- Build Scope Extraction Agent prototype.
- Build Authorization Gateway prototype.
- Build Tool Gateway prototype.
- Integrate ZAP / Nmap / nuclei.
- Generate evidence-linked report drafts.

## Phase 2: MVP

- Process small Web/API/NW assessment scenarios.
- Link authorization decisions, tool execution, evidence, findings, and human review.
- Prepare demo scenario and PoC materials.

## Phase 3: Commercial PoC

- Run controlled PoC with a vulnerability assessment company, MSSP, SIer, or security consulting partner.
- Measure effort reduction, report quality, false positive reduction, and evidence completeness.
