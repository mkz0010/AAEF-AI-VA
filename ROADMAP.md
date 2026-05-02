# Roadmap

## Phase 0: Business and Safety Design

- Define project charter.
- Define MVP scope.
- Define AI data handling policy.
- Define credential_ref model.
- Define Tool Gateway and AAEF Authorization Gateway boundaries.
- Define NDA, AI use, and external AI handling assumptions.

## Phase 1: Technical Prototype

### Concrete Preflight Check Implementation Scaffold

- Added v0.3.0 concrete preflight check implementation scaffold after the runtime transition checkpoint.
- Recorded implementation responsibility, evidence type, input sources, and fail-closed behavior for all preflight checks while keeping preflight unsatisfied and execution disabled.


### Runtime Transition Checkpoint

- Added v0.2.9 runtime transition checkpoint after the preflight validation scaffold.
- Confirmed that the project is ready for concrete preflight implementation work while runtime execution remains disabled.


### Preflight Validation Scaffold

- Added v0.2.8 preflight validation scaffold after the execution authorization gate scaffold.
- Recorded future preflight checks across runtime readiness, target binding, authorization, approvals, no-egress, timeout, kill-switch, evidence, and sanitizer boundaries while keeping execution disabled.


### Execution Authorization Gate Scaffold

- Added v0.2.7 execution authorization gate scaffold after runtime enforcement design.
- Recorded future authorization requirements while keeping execution authorization and runtime execution disabled.


### Runtime Enforcement Design Scaffold

- Added v0.2.6 runtime enforcement design scaffold after the no-egress, timeout, and kill-switch policy scaffold.
- Recorded future enforcement components and sequence while keeping runtime enforcement unimplemented and execution disabled.


### Runtime Safety Policy Scaffold

- Added v0.2.5 no-egress, timeout, and kill-switch policy scaffold after local-only execution plan review.
- Defined future local-only safety requirements while keeping process launch, network activity, scans, credential injection, and raw artifact capture disabled.


### Local-Only Execution Plan Review

- Added v0.2.4 local-only execution plan review after bounded execution transition candidate.
- Restricted plan operations to runtime_detection and health_check_plan_only while keeping ZAP start/stop/API calls, scans, network activity, credential injection, and raw artifact capture disabled.


### Bounded Execution Transition Candidate

- Added v0.2.3 bounded execution transition candidate after runtime destination binding.
- Structured no-egress, timeout, kill-switch, operation allowlist, human approval, sanitizer, evidence, and raw artifact boundary prerequisites while keeping execution disabled.


### Runtime Destination Binding

- Added v0.2.2 scope-registry-style binding between runtime readiness and local target lab profile.
- Kept scan execution, network activity, real execution, credential injection, raw artifact capture, customer targets, and external targets disabled.


### Local Target Lab Profile

- Added v0.2.1 local target lab profile before bounded execution work.
- Restricted future target consideration to localhost/Docker-internal intentionally vulnerable lab targets while keeping scan execution disabled.


### Controlled Local Runtime Readiness

- Added v0.2.0 controlled local ZAP runtime readiness.
- Runtime detection remains separate from execution authority, and real execution remains disabled.


### Lifecycle Integration Checkpoint

- Added v0.1.30 lifecycle integration checkpoint before controlled local runtime work.
- Summarized stable capabilities, explicit non-goals, safety invariants, and v0.2.x next-phase candidates.


### Delivery Authorization Gate

- Added delivery authorization gate for delivery authorization candidates.
- Added delivery package generation while keeping dispatch, customer delivery, and report-ready status disabled.


### Report Packet Review Gate

- Added report packet review gate for report packet candidates.
- Added delivery authorization candidate assembly while keeping delivery authorization required and customer delivery disabled.


### Report Review Gate

- Added report review gate for report findings.
- Added report packet candidate assembly while keeping packet review required and customer delivery disabled.


### Report Finding Promotion Gate

- Added promotion gate from confirmed finding review to report finding.
- Kept report findings review-required, not report-ready, and not customer-delivery-ready in the MVP.


### Finding Candidate Review Gate

- Added human review gate for sanitized finding candidates.
- Kept confirmed candidates eligible only for future report promotion review, not report-ready in the MVP.


### Sanitized Finding Candidate Model

- Added non-report-ready finding candidate model derived from sanitized artifacts.
- Required human review and conservative severity/confidence defaults before any report workflow.


### Sanitizer and Redaction Policy

- Added sanitizer/redaction policy scaffold before real tool output can become AI-visible.
- Added generated sanitized artifact demo and tests for common sensitive values.


### Evidence Reconstruction Report

- Added human-readable reconstruction report generated from evidence chain and review decision linkage.
- Included safety assertions, blockers, next actions, chain nodes, and review questions.


### Evidence Chain Review Linkage

- Added reconstruction chain across request, authorization, execution result, evidence, operator review, human approval, and approval gate records.
- Added generated private JSON and Markdown evidence chain artifacts.


### Human Approval Record and Gate

- Added explicit human approval records for operator review decisions.
- Added approval binding and expiration validation while preserving real-execution blocking.


### Operator Readiness Review

- Added operator-facing readiness review summary for real execution blockers.
- Added generated private Markdown and JSON review artifacts for do-not-execute decisions.


### Real Execution Readiness Gate

- Added a readiness gate for future real tool execution prerequisites.
- Kept real execution disabled by default while surfacing runtime, egress, sanitizer, timeout, evidence, target binding, credential injection, and approval blockers.


### Scope Registry and Target Alias Resolution

- Added Tool Gateway-controlled scope registry for target aliases.
- Added target binding to ZAP command plans and dry-run executor validation.
- Kept raw destinations out of committed registry data and command plans.


### Controlled Executor Policy

- Added dry-run-only executor policy for adapter command plans.
- Confirmed command plans are not execution authority and must pass executor validation before any future real tool execution.


### ZAP Adapter Command Plan

- Added a dry-run command plan for the ZAP adapter.
- Moved ZAP integration closer to real execution without invoking ZAP or constructing arbitrary shell commands.


### Internal Adapter Artifact Policy

- Documented that adapter output is internal/private by default.
- Clarified raw artifact, sanitized artifact, public result, evidence, and AI-visible boundaries before real tool integration.

### Tool Gateway Adapter Stubs

- Added adapter registry for ZAP, Nmap, nuclei, and browser automation.
- Completed mock actions now route through adapter stubs.
- Real tool execution remains deferred until the adapter boundary is proven.


### v0.1.10 Stability Checkpoint

- v0.1.10 is treated as the stable local checkpoint after v0.1.8/v0.1.9 remediation.
- Added a single local validation command before future commits, merges, and tags.
- Next implementation step can proceed to adapter stubs from this stable baseline.


### Mock Vault credential_ref Validation

- credential_ref is now validated against secretless mock Vault metadata.
- Tool Gateway fails closed for unknown, mismatched, revoked, expired, or disallowed credential_ref usage.
- Raw secrets remain outside Git and outside AI-visible records.


### Tool Gateway Fail-Closed Tests

- Added negative tests for request/authorization mismatches and unsafe constraints.
- Added generated output validation for the mock runner.
- Next step is schema validation for generated outputs and mock Vault metadata tests.


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
