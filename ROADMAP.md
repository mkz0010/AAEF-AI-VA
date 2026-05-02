# Roadmap

## Phase 0: Business and Safety Design

- Define project charter.
- Define MVP scope.
- Define AI data handling policy.
- Define credential_ref model.
- Define Tool Gateway and AAEF Authorization Gateway boundaries.
- Define NDA, AI use, and external AI handling assumptions.

## Phase 1: Technical Prototype

### Tool Gateway Mock Runner

- Added a standard-library-only mock runner before real tool integration.
- The runner validates request and authorization binding and emits generated execution/evidence records.
- Generated outputs are written under ignored local private paths.


### Tool Gateway Prototype Scaffold

- Added prototype examples for allowed, denied, and human-approval-required flows.
- Added example validation before implementing real tool execution.
- Next step is a minimal Tool Gateway runner that consumes these examples.


### MVP Schema Contract Decision

- Tool Gateway implementation will use explicit JSON schema contracts.
- MVP schemas cover tool_action_request, authorization_decision, tool_execution_result, and evidence_record.
- Initial schemas constrain tools and operations to the MVP scope.


### Tool Gateway MVP Decision

- Tool Gateway is the trusted execution boundary between AI requests and real diagnostic tools.
- Tool Gateway must not execute arbitrary AI-generated shell commands.
- MVP adapters are ZAP, Nmap, nuclei, and limited browser automation where necessary.
- Tool Gateway must fail closed on missing, denied, expired, or mismatched authorization.


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
