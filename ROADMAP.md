# Roadmap

## Phase 0: Business and Safety Design

- Define project charter.
- Define MVP scope.
- Define AI data handling policy.
- Define credential_ref model.
- Define Tool Gateway and AAEF Authorization Gateway boundaries.
- Define NDA, AI use, and external AI handling assumptions.

## Phase 1: Technical Prototype

### Preflight Evidence Validation Rules

- Added v0.3.3 preflight evidence validation rules after generated preflight evidence examples.
- Validated generated examples while preserving the boundary that live evidence, preflight satisfaction, execution authorization, and runtime execution remain disabled.


### Generated Preflight Evidence Record Examples

- Added v0.3.2 generated preflight evidence record examples after the preflight evidence record model.
- Recorded representative fail-closed examples while keeping them separate from live evidence generation and execution authorization.


### Preflight Evidence Record Model

- Added v0.3.1 preflight evidence record model after the concrete preflight check implementation scaffold.
- Defined evidence record shape, AI visibility boundary, raw artifact boundary, and sanitized summary requirement for all required preflight checks while keeping execution disabled.


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

## v0.3.4 negative preflight evidence examples

Status: added.

Purpose: record and validate representative invalid preflight evidence claims that must fail closed, including missing input evidence, mismatched target binding, stale readiness state, false authorization claims, false preflight satisfaction claims, AI-visible raw evidence, raw artifact capture, example/live evidence confusion, no-egress verification spoofing, and sanitizer boundary verification spoofing.

Boundary: this milestone does not permit live evidence generation, runtime execution, scanning, network activity, external process execution, credential injection, or raw artifact capture.

## v0.3.5 licensing and commercial-use boundary

Status: candidate.

This step records the repository licensing and commercial-use boundary:

- AGPL-3.0 for the AAEF-AI-VA code implementation;
- CC BY 4.0 attribution boundary for the parent AAEF framework/specification;
- commercial licensing inquiry language;
- future dependency, contributor, and legal review tasks.

This does not change runtime execution state. Execution remains blocked.

## v0.3.6 Public repository readiness checkpoint

Status: completed candidate once local checks pass.

Purpose:

- Confirm that the project is ready to be reviewed before first public repository publication.
- Keep public-readiness separate from runtime-readiness.
- Confirm that `private-not-in-git/` remains the generated/private artifact boundary.
- Confirm that AGPL-3.0 and AAEF CC BY 4.0 attribution are visible before publication.
- Confirm that runtime execution, external network activity, scan execution, and credential injection remain disabled.
- Keep commercial licensing contact information as an explicit placeholder until a durable contact channel is chosen.

## v0.3.7 Publication hygiene and private artifact exclusion checkpoint

Status: completed candidate once local checks pass.

Purpose:

- Prevent generated/private/local artifacts from being accidentally published.
- Confirm that `private-not-in-git/` remains outside tracked source artifacts.
- Confirm that generated evidence and local run outputs are excluded by `.gitignore`.
- Keep publication hygiene separate from runtime readiness.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.3.8 Public security policy and vulnerability disclosure checkpoint

Status: completed candidate once local checks pass.

Purpose:

- Add `SECURITY.md` before public repository publication.
- Define what security reports are in scope and out of scope.
- Keep vulnerability reporting separate from commercial licensing inquiries.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.
- Prepare the repository for a future durable security reporting channel.

## v0.3.9 First-publication repository settings checklist

Status: completed candidate once local checks pass.

Purpose:

- Prepare a manual checklist for the first GitHub repository publication.
- Decide staged public vs private-first publication without changing local source state.
- Record repository metadata and settings decisions before any push.
- Keep GitHub configuration separate from runtime readiness.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.4.0 Public publication preparation release

Status: completed candidate once local checks pass.

Purpose:

- Summarize the public-readiness stack before first GitHub publication.
- Confirm the repository remains local-only until the author manually creates a remote.
- Prepare first-publication dry-run and announcement material.
- Keep public publication preparation separate from runtime readiness.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.4.1 GitHub Actions CI scaffold

Status: completed candidate once local checks pass.

Purpose:

- Add a visible CI signal before or alongside first public repository publication.
- Run the existing local validation suite in GitHub Actions.
- Keep CI validation separate from runtime readiness.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.4.2 README public English wording cleanup

Status: completed candidate once local checks pass.

Purpose:

- Keep the public README English-first.
- Remove local-management phrasing from the public entry point.
- Preserve the AAEF authority boundary in English.
- Keep README polish separate from runtime readiness.

## v0.4.3 Public-facing repository metadata and announcement pack

Status: completed candidate once local checks pass.

Purpose:

- Add README validation badge now that the GitHub repository URL is stable.
- Prepare GitHub About metadata and topic candidates.
- Prepare public announcement language.
- Keep public messaging aligned with safety, evidence, authorization, and runtime-execution boundaries.

## v0.4.4 Public repository launch checkpoint

Status: completed candidate once local checks pass.

Purpose:

- Record the first public repository launch state.
- Confirm public repository metadata and security reporting posture are documented.
- Keep public launch separate from runtime readiness.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.4.5 Public release notes and launch announcement package

Status: completed candidate once local checks pass.

Purpose:

- Prepare public launch communication after the repository launch checkpoint.
- Provide reusable release notes and announcement drafts.
- Keep launch messaging aligned with safety, evidence, authorization, human review, and runtime-execution boundaries.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.4.6 GitHub release publication checkpoint

Status: completed candidate once local checks pass.

Purpose:

- Record that the `v0.4.5` GitHub Release was published.
- Preserve release title, URL, latest status, and release-note safety boundaries.
- Keep release publication separate from runtime readiness.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.5.0 Commercial adoption preparation checkpoint

Status: completed candidate once local checks pass.

Purpose:

- Convert the public OSS launch into enterprise adoption readiness.
- Prepare business-facing positioning for vulnerability assessment companies, MSSPs, AI security firms, and security automation teams.
- Keep public repository wording credible and technical, not overly sales-oriented.
- Keep customer-specific sales material, pricing, outreach plans, and proposal drafts private.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.5.1 README public baseline and commercial entrypoint cleanup

Status: completed candidate once local checks pass.

Purpose:

- Align README with the public repository and commercial adoption state.
- Stop older v0.3.x checkpoints from dominating the first public impression.
- Make the commercial adoption entrypoint visible without converting the repository into a sales deck.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.5.2 README compatibility phrase registry and test design hardening

Status: completed candidate once local checks pass.

Purpose:

- Reduce future README rewrite regressions.
- Record compatibility phrases expected by README-facing checkpoint tests.
- Preserve the distinction between unsafe positive claims and safe negative boundary statements.
- Keep README maintenance compatible with license, security, publication hygiene, metadata, release, and commercial-adoption checkpoints.

## v0.5.3 Licensing, trademark, authorship, and commercial-use protection hardening

Status: completed candidate once local checks pass.

Purpose:

- Strengthen the public repository boundary for commercial adoption.
- Preserve AGPL-3.0 transparency while making commercial-license discussions explicit.
- Record authorship and attribution expectations.
- Clarify project-name and mark usage without overclaiming registered trademark status.
- Keep contribution rules aligned with safety, disclosure, runtime-execution, and commercial-use boundaries.

## v0.5.4 Dependency and repository governance readiness checkpoint

Status: completed candidate once local checks pass.

Purpose:

- Strengthen public repository governance before targeted commercial outreach.
- Record dependency/license inventory expectations without overclaiming full legal review.
- Record branch protection and ruleset planning without requiring immediate GitHub configuration changes.
- Record release/tag governance expectations.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.5.5 GitHub repository ruleset and branch protection planning checkpoint

Status: completed candidate once local checks pass.

Purpose:

- Plan GitHub repository rulesets and branch protection before making administration changes.
- Define required validation expectations for `main` and release tags.
- Define review expectations for high-risk runtime, scanning, credential, customer-target, licensing, and public-claim changes.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.5.6 Release governance and maintainer operations checklist

Status: completed candidate once local checks pass.

Purpose:

- Convert the current release workflow into an explicit maintainer operations checklist.
- Preserve the scoped-branch, local-checks, fast-forward-merge, tag, push, and GitHub Actions verification sequence.
- Keep private generated artifacts untracked.
- Define emergency exception and post-release review expectations.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.5.7 Public trust and reviewer navigation checkpoint

Status: completed candidate once local checks pass.

Purpose:

- Make the public repository easier to evaluate without a direct sales meeting.
- Provide role-based reviewer navigation for technical, security, commercial, licensing, and maintainer-operations review.
- Connect public trust signals such as license, security policy, CI, release governance, and repository governance.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.5.8 Public front page and repository landing polish checkpoint

Status: completed candidate once local checks pass.

Purpose:

- Improve the repository's value as a public product introduction page.
- Define first-minute reviewer goals without turning the repository into a sales deck.
- Preserve safety, license, governance, and commercial-use boundaries.
- Keep runtime execution, network activity, scan execution, credential injection, and raw artifact capture disabled.

## v0.5.9 Public evidence and capability boundary summary

Status: completed candidate once local checks pass.

Purpose:

- Explain what the repository currently demonstrates and does not demonstrate.
- Separate evidence-backed public claims from unsupported product claims.
- Make capability boundaries easier for first-time reviewers to understand.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.5.10 Public FAQ and reviewer objections handling

Status: completed candidate once local checks pass.

Purpose:

- Answer likely reviewer objections before a direct sales or technical conversation.
- Clarify scope, safety boundaries, evidence-backed claims, commercial-use boundaries, and intentionally blocked capabilities.
- Help the public repository function as a conservative product introduction surface.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.0 Implementation and evaluation work ordering

Status: completed candidate once local checks pass.

Purpose:

- Organize v0.6.x before deciding whether to start from a local assessment lab.
- Separate planning, evaluation, implementation, demo, and commercial-readiness workstreams.
- Prioritize decisions that reduce rework before enabling any runtime capability.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.1 Capability inventory and maturity map

Status: completed candidate once local checks pass.

Purpose:

- Inventory existing AAEF-AI-VA capabilities before new implementation work.
- Map each capability to a maturity level from L0 through L6.
- Identify which capabilities are demonstrated locally, which remain planning-only, and which remain intentionally blocked.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.2 Evaluation criteria and acceptance model

Status: completed candidate once local checks pass.

Purpose:

- Define how future AAEF-AI-VA capabilities should be evaluated.
- Establish acceptance criteria before local lab, demo, runtime hardening, or commercial PoC work.
- Distinguish maturity advancement from unsupported readiness claims.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.3 Safety boundary and non-goal review

Status: completed candidate once local checks pass.

Purpose:

- Reconfirm what AAEF-AI-VA must not do before local lab decisioning.
- Preserve hard non-goals around runtime execution, live scanning, credential injection, customer-target operation, production deployment, certification, legal approval, and audit opinion.
- Define the conditions that must be satisfied before any later local lab, demo, runtime gate hardening, or commercial PoC work.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.4 Local assessment lab decision record

Status: completed candidate once local checks pass.

Purpose:

- Decide whether and how AAEF-AI-VA should proceed toward a local assessment lab.
- Select a conservative local lab path before implementation expands.
- Preserve documentation-only and dry-run planning before any localhost-only controlled behavior.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.5 Documentation-only local lab profile and action taxonomy

Status: completed candidate once local checks pass.

Purpose:

- Define the documentation-only local lab profile before any lab implementation expands.
- Define allowed and denied action categories without enabling execution.
- Establish preflight evidence and human review expectations for later dry-run planning.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.6 AI request decision boundary and tool selection criteria

Status: completed candidate once local checks pass.

Purpose:

- Define the difference between AI method selection and execution authorization.
- Preserve the rule that AI generates `tool_action_request`, while gates decide execution.
- Establish tool-selection criteria before demo, observation, dry-run, or lab work expands.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.7 Observation normalization and diagnostic fidelity risk review

Status: completed candidate once local checks pass.

Purpose:

- Define how AI receives enough diagnostic signal without receiving unsafe raw responses.
- Record the risk that sanitizer or normalizer behavior can reduce diagnostic accuracy.
- Establish loss-aware normalization, signal-preserving extraction, sufficiency scoring, and escalation paths.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.8 Demo scenario and reviewer walkthrough planning

Status: completed candidate once local checks pass.

Purpose:

- Define a public-safe reviewer walkthrough before any dry-run or local lab execution behavior expands.
- Show how the core proposition can be explained without exposing private advanced feature details.
- Connect approved diagnostic context, AI request generation, gate decision, and evidence expectations.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.9 Evidence reconstruction and sample report demonstration planning

Status: completed candidate once local checks pass.

Purpose:

- Define how reviewers can inspect a non-executing evidence reconstruction and sample report demonstration.
- Connect approved diagnostic context, AI-generated requests, gate decisions, evidence expectations, finding review, and report packet boundaries.
- Preserve public-safe wording and avoid private advanced feature details.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, and raw artifact capture boundaries.

## v0.6.10 Safe Docker lab roadmap and local target candidate planning

Status: completed candidate once local checks pass.

Purpose:

- Define a safe Docker lab roadmap without enabling Docker execution.
- Identify local target candidates such as DVWA, OWASP Juice Shop, and WebGoat as future localhost-only candidates.
- Define candidate acceptance criteria before dry-run or bounded local execution work expands.
- Preserve disabled runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.11 Local lab candidate profile and preflight evidence planning

Status: completed candidate once local checks pass.

Purpose:

- Define local lab candidate profile fields before Docker or scanner work expands.
- Define preflight evidence expectations for future local-only target candidates.
- Compare DVWA, OWASP Juice Shop, WebGoat, synthetic local API, and static fixture target candidates without selecting or running them.
- Preserve disabled Docker execution, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.12 Non-running Docker Compose design review planning

Status: completed candidate once local checks pass.

Purpose:

- Define non-running Docker Compose design review criteria before Compose files are created.
- Review future lab design boundaries for network, ports, images, environment variables, volumes, reset/teardown, and resource limits.
- Separate image retrieval or dependency setup from assessment activity.
- Preserve disabled Docker execution, image pull, container startup, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.13 Static Compose design sketch and network boundary review

Status: completed candidate once local checks pass.

Purpose:

- Define a static, non-runnable Compose design sketch before any Compose file is created.
- Review future service roles, network boundary, port binding intent, outbound posture, volume posture, and reset/teardown posture.
- Keep the sketch distinct from runnable Docker Compose configuration.
- Preserve disabled Compose file creation, image pull, container startup, Docker execution, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.14 Static lab scenario fixture planning

Status: completed candidate once local checks pass.

Purpose:

- Define static, non-executing scenario fixture planning before any runnable Compose configuration or local execution exists.
- Connect candidate profile, static sketch, AI request, gate decision, expected evidence, reviewer questions, and non-proof statement.
- Keep fixture content synthetic, non-customer, non-secret, and private until a separate public-safe artifact decision exists.
- Preserve disabled Compose file creation, image pull, container startup, Docker execution, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.15 Static fixture schema and validator planning

Status: completed candidate once local checks pass.

Purpose:

- Define schema and validator planning for future static lab scenario fixtures before fixture files are generated.
- Define required fixture nodes, reference integrity, scenario trace validation, synthetic data checks, no-secret checks, no-runtime checks, and no-runnable-configuration checks.
- Keep validator planning separate from generated fixture artifacts.
- Preserve disabled fixture generation, Compose file creation, image pull, container startup, Docker execution, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.16 Static fixture schema draft and negative test planning

Status: completed candidate once local checks pass.

Purpose:

- Define draft schema fields for future static lab scenario fixtures before implementation.
- Define negative test expectations before fixture validator implementation.
- Keep schema draft and negative tests separate from generated fixture artifacts.
- Preserve disabled fixture schema implementation, fixture validator implementation, fixture generation, Compose file creation, image pull, container startup, Docker execution, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.17 Static fixture validator scaffold planning

Status: completed candidate once local checks pass.

Purpose:

- Define future static fixture validator scaffold responsibilities before implementation.
- Define validator input boundaries, output boundaries, fail-closed behavior, planned validation stages, failure categories, negative-test handling, and registration order.
- Keep validator scaffold planning separate from implemented validator code and generated fixture artifacts.
- Preserve disabled fixture schema implementation, fixture validator implementation, negative test implementation, fixture generation, Compose file creation, image pull, container startup, Docker execution, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.18 Static fixture validator minimal scaffold design

Status: completed candidate once local checks pass.

Purpose:

- Define future read-only static fixture validator minimal scaffold design before implementation.
- Define planned module boundaries, CLI boundary, input model, output model, function boundaries, failure result model, fail-closed behavior, and registration conditions.
- Keep scaffold design separate from implemented validator code and generated fixture artifacts.
- Preserve disabled fixture schema implementation, fixture validator implementation, negative test implementation, fixture generation, Compose file creation, image pull, container startup, Docker execution, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.19 Static fixture validator implementation readiness review

Status: completed candidate once local checks pass.

Purpose:

- Define readiness review criteria before future static fixture validator implementation begins.
- Confirm read-only behavior, fail-closed behavior, negative-test-first ordering, input boundaries, output boundaries, registration readiness, and blocking issue categories.
- Keep readiness review separate from implemented validator code, implemented CLI behavior, implemented negative tests, and generated fixture artifacts.
- Preserve disabled fixture schema implementation, fixture validator implementation, validator CLI implementation, negative test implementation, fixture generation, Compose file creation, image pull, container startup, Docker execution, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.20 Static fixture validator read-only implementation scaffold

Status: completed candidate once local checks pass.

Purpose:

- Add a minimal read-only static fixture validator scaffold before complete validator implementation.
- Define review-only data structures, planned failure categories, fail-closed missing-input behavior, and non-authorizing CLI output.
- Keep the scaffold separate from generated fixture artifacts, complete schema validation, negative-test implementation, and positive fixture generation.
- Preserve disabled fixture generation, complete fixture validator implementation, Compose file creation, image pull, container startup, Docker execution, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.21 Static fixture validator required-node check planning

Status: completed candidate once local checks pass.

Purpose:

- Define future required-node check planning for the static fixture validator before implementation.
- Specify fixture manifest expectations, required static fixture node types, missing-node failure categories, fail-closed behavior, and future implementation order.
- Keep required-node check planning separate from implemented validator behavior and generated fixture artifacts.
- Preserve disabled required-node check implementation, complete fixture validator implementation, negative test implementation, fixture generation, Compose file creation, image pull, container startup, Docker execution, runtime execution, network activity, scan execution, credential injection, raw artifact capture, and customer-target boundaries.

## v0.6.22 AAEF applied evidence work intake and current-state review

Status: completed candidate once local checks pass.

Purpose:

- Pause the previously natural required-node minimal implementation step long enough to respond to the AAEF-side applied evidence request.
- Start from current-state inventory and work-ordering, as requested by AAEF-side guidance.
- Reframe the next work around a local-lab applied evidence package that traces `tool_action_request` to gate decision, dispatch/non-dispatch, result, evidence event, and reviewer summary.
- Keep implementation, fixture generation, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization blocked.

## v0.6.23 AAEF applied evidence package design

Status: completed candidate once local checks pass.

Purpose:

- Define the AAEF applied evidence package structure before generating evidence artifacts.
- Design the request-to-evidence chain and scenario package layout.
- Clarify when evidence capture should begin: static/mock package generation first, real local-lab diagnostic execution later after additional gates.
- Keep package design separate from fixture generation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.24 Applied evidence scenario set planning

Status: completed candidate once local checks pass.

Purpose:

- Define the four minimum applied evidence scenarios before fixture planning or package generation.
- Make each scenario traceable through request, gate decision, dispatch decision, result, evidence event, and review summary.
- Preserve non-execution evidence as first-class evidence.
- Keep scenario planning separate from static/mock evidence generation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.25 Static applied evidence fixture planning

Status: completed candidate once local checks pass.

Purpose:

- Define the static fixture artifacts for the four applied evidence scenarios before generating them.
- Make each future fixture set traceable through request, gate decision, dispatch decision, result, evidence event, and review summary.
- Plan identifier linkage and non-execution evidence as first-class evidence.
- Keep fixture planning separate from fixture generation, package generation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.26 Reviewer walkthrough and five questions mapping

Status: completed candidate once local checks pass.

Purpose:

- Define a reviewer-facing walkthrough for the static applied evidence package before generating fixtures.
- Map each scenario and artifact chain to the AAEF five questions.
- Make permitted, denied, held, and not-executed outcomes understandable without relying on raw JSON alone.
- Keep reviewer walkthrough planning separate from fixture generation, package generation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.27 Applied evidence structural validator planning

Status: completed candidate once local checks pass.

Purpose:

- Define structural validation criteria before generating static/mock applied evidence packages.
- Plan checks for required artifacts, required fields, ID linkage, scenario consistency, non-execution evidence, non-proof statements, reviewer walkthrough coverage, and overclaim prevention.
- Keep validator planning separate from validator implementation, fixture generation, package generation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.28 Static/mock applied evidence package generation readiness review

Status: completed candidate once local checks pass.

Purpose:

- Review whether static/mock applied evidence package generation is safe to begin.
- Confirm package design, scenario set, fixture plan, reviewer walkthrough mapping, and structural validator planning are in place.
- Define blocker categories and private-first generation posture before any generated artifacts are created.
- Keep readiness review separate from fixture generation, package generation, structural validator implementation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.29 Static/mock applied evidence package private generation candidate

Status: completed candidate once local checks pass.

Purpose:

- Generate the first private-first static/mock applied evidence package under `private-not-in-git/`.
- Cover all four minimum applied evidence scenarios with linked request, gate, dispatch, result, evidence, review, and non-proof artifacts.
- Keep generated artifacts private until a later public-safe promotion decision.
- Keep generation separate from public sample publication, structural validator implementation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.30 Static/mock applied evidence package review and promotion gate planning

Status: completed candidate once local checks pass.

Purpose:

- Define the review and promotion gate for the private static/mock applied evidence package generated in v0.6.29.
- Separate private package review, public sanitized sample promotion, and real local-lab diagnostic execution.
- Plan blocker categories, promotion outcomes, publication-safe checks, and AAEF-side reporting.
- Keep promotion planning separate from public sample generation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.31 Static/mock applied evidence package private review record

Status: completed candidate once local checks pass.

Purpose:

- Generate a private review record for the v0.6.29 static/mock applied evidence package.
- Keep the package private unless a later public-safe promotion planning checkpoint explicitly approves further work.
- Record review status, promotion gate result, blocker categories, and AAEF-side reporting boundaries.
- Keep private review separate from public sample generation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.32 Static/mock applied evidence package public sample promotion decision record

Status: completed candidate once local checks pass.

Purpose:

- Record the promotion decision after the v0.6.31 private review record.
- Keep direct public sample generation blocked.
- Permit only a later sanitized public sample planning checkpoint to be considered, subject to separate review.
- Keep promotion decision recording separate from public sample generation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.33 Sanitized public sample planning

Status: completed candidate once local checks pass.

Purpose:

- Plan sanitized public sample scope and hygiene before any public sample artifact is generated.
- Define allowed public sample artifacts, naming, placement, synthetic-only content, non-proof statements, and publication review gates.
- Keep public sample planning separate from public artifact generation, private artifact promotion, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.34 Sanitized public sample generation readiness review

Status: completed candidate once local checks pass.

Purpose:

- Review whether sanitized public sample generation can be considered after v0.6.33 planning.
- Confirm readiness conditions and remaining blockers before any public artifact generation.
- Keep readiness review separate from public sample generation, private artifact promotion, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, and delivery authorization.

## v0.6.35 Sanitized public sample generation candidate

Status: completed candidate once local checks pass.

Purpose:

- Generate a sanitized public sample candidate under `examples/applied-evidence/sanitized-static-mock/`.
- Use synthetic `.example.` artifacts to demonstrate AAEF applied-evidence traceability.
- Keep public sample candidate generation separate from private artifact promotion, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, report delivery, and certification/compliance/audit/legal claims.

## v0.6.36 Sanitized public sample publication review record

Status: completed candidate once local checks pass.

Purpose:

- Generate a publication review record for the sanitized public sample candidate created in v0.6.35.
- Record that the sample may be retained as a limited public example while preserving non-proof and non-execution boundaries.
- Keep publication review separate from local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, report delivery, and certification/compliance/audit/legal claims.

## v0.6.37 Sanitized public sample close-readiness review

Status: completed candidate once local checks pass.

Purpose:

- Review whether the sanitized public sample track can be considered close-ready.
- Preserve that the public example remains a limited synthetic non-executing example.
- Identify next-track options after public sample close-readiness: public example structural validation, applied evidence structural validator implementation, or return to local-lab/preflight planning.
- Keep close-readiness review separate from local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, report delivery, and certification/compliance/audit/legal claims.

## v0.6.38 Public example structural validation planning

Status: completed candidate once local checks pass.

Purpose:

- Plan structural validation for the sanitized public sample artifact set.
- Define checks that a later validator implementation should perform.
- Keep validation planning separate from validator implementation, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, report delivery, and certification/compliance/audit/legal claims.

## v0.6.39 Public example structural validator implementation readiness review

Status: completed candidate once local checks pass.

Purpose:

- Review whether public example structural validator implementation can be considered after v0.6.38 planning.
- Keep the future validator read-only and scoped to public `.example.` artifacts.
- Keep readiness review separate from validator implementation, validator execution, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, report delivery, and certification/compliance/audit/legal claims.

## v0.6.40 Public example structural validator implementation candidate

Status: completed candidate once local checks pass.

Purpose:

- Implement a read-only structural validator for the sanitized public sample artifact set.
- Keep the validator scoped to public `.example.` artifacts.
- Keep validator success separate from diagnostic accuracy, production readiness, implementation conformance, audit sufficiency, legal sufficiency, compliance certification, external-framework equivalence, runtime authorization, scanner authorization, customer-target operation, and delivery authorization.

## v0.6.41 Public example structural validator review and close-readiness

Status: completed candidate once local checks pass.

Purpose:

- Review the v0.6.40 read-only public example structural validator result.
- Treat the public example structural validation track as close-ready when validator output passes with empty blockers.
- Capture AAEF Applied Implementation handback guidance for AAEF main.
- Keep the review separate from local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, report delivery, and certification/compliance/audit/legal claims.

## v0.6.42 AAEF Applied Implementation handback summary

Status: completed candidate once local checks pass.

Purpose:

- Provide AAEF main with a public-safe Applied Implementation handback summary.
- Keep the handback at the evidence/interface level.
- Exclude detailed implementation, patent-sensitive diagnostic reconstruction detail, commercial strategy, pricing strategy, customer lists, and NDA-assumed content.
- Keep the handback separate from local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, report delivery, and certification/compliance/audit/legal claims.

## v0.6.43 Applied Implementation handback review and next direction

Status: completed candidate once local checks pass.

Purpose:

- Review whether the v0.6.42 AAEF Applied Implementation handback is sufficient for AAEF main.
- Decide the next AAEF-AI-VA direction after the public sample and public validator track.
- Keep the review separate from local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, report delivery, and certification/compliance/audit/legal claims.

## v0.6.44 Public validator negative fixture planning

Status: completed candidate once local checks pass.

Purpose:

- Plan negative fixtures for the read-only public example structural validator.
- Keep fixture planning separate from fixture implementation, validator behavior changes, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, report delivery, and certification/compliance/audit/legal claims.
- Preserve fail-closed behavior as a validation-safety goal.
## v0.6.45 Public validator negative fixture implementation readiness review
Status: completed candidate once local checks pass.
Purpose:
- Review whether v0.6.44 public validator negative fixture planning is ready for later implementation.
- Keep the future implementation scoped to synthetic, public-safe, static negative fixtures and optional read-only harness behavior.
- Confirm fixture root expectations, temporary copy strategy, expected blocker metadata, positive control preservation, fail-closed expectations, and validation harness constraints.
- Keep readiness review separate from fixture implementation, validator behavior changes, local diagnostic execution, Docker execution, scanner execution, credential injection, customer-target operation, report delivery, and certification/compliance/audit/legal claims.
