# Changelog

## Unreleased

- Add v0.3.5 licensing and commercial-use boundary with AGPL-3.0 repository license, AAEF/CC BY 4.0 attribution, commercial license inquiry language, and local validation.

### Added

- Added v0.3.4 negative preflight evidence examples to document and validate representative invalid evidence claims that must fail closed without satisfying preflight or authorizing runtime execution.

### Added

- Added v0.3.3 preflight evidence validation rules for generated examples while keeping live evidence validation, preflight satisfaction, and execution disabled.

- Added v0.3.2 generated preflight evidence record examples for representative fail-closed checks while keeping live evidence generation, preflight satisfaction, and execution disabled.

- Added v0.3.1 preflight evidence record model for all required preflight checks while keeping evidence records not generated, preflight unsatisfied, and execution disabled.

- Added v0.3.0 concrete preflight check implementation scaffold with input sources, evidence types, fail-closed behavior, and responsibilities for all required preflight checks while keeping execution disabled.

- Added v0.2.9 runtime transition checkpoint summarizing v0.2.0 through v0.2.8 and confirming readiness for preflight implementation while keeping execution disabled.

- Added v0.2.8 preflight validation scaffold for future execution-before-checklist requirements while keeping preflight unsatisfied and execution disabled.

- Added v0.2.7 execution authorization gate scaffold for future approval and verification requirements while keeping execution disabled.

- Added v0.2.6 runtime enforcement design scaffold for future preflight, process wrapper, no-egress, timeout, kill-switch, evidence, and sanitizer boundary enforcement while keeping execution disabled.

- Added v0.2.5 no-egress, timeout, and kill-switch policy scaffold while keeping runtime execution disabled.

- Added v0.2.4 local-only execution plan review with plan-level runtime_detection and health_check_plan_only while keeping ZAP runtime operations disabled.

- Added v0.2.3 bounded execution transition candidate to structure future local-only execution prerequisites while keeping execution disabled.

- Added v0.2.2 scope-registry-style runtime destination binding between controlled local runtime readiness and local target lab profiles while keeping execution blocked.

- Added v0.2.1 local target lab profile to define localhost/Docker-internal intentionally vulnerable target boundaries while keeping scans disabled.

- Added v0.2.0 controlled local ZAP runtime readiness with detection-only behavior and no external process execution.

- Added v0.1.30 lifecycle integration checkpoint summarizing stable control/review capabilities and safety invariants before v0.2.x runtime work.

- Added delivery authorization gate and delivery package generation while keeping customer delivery and dispatch disabled.

- Added report packet review gate and delivery authorization candidate assembly while keeping customer delivery disabled.

- Added report review gate and report packet candidate assembly while keeping customer delivery disabled.

- Added report finding promotion gate for confirmed finding reviews while avoiding final lifecycle terminology.

- Added finding candidate review gate for confirmed, rejected, needs_more_info, duplicate, and false_positive outcomes while keeping report_ready false.

- Added sanitized finding candidate model for AI-visible-safe review objects derived from sanitized artifacts.

- Added sanitizer and redaction policy scaffold for raw adapter artifacts before AI-visible use.

- Added evidence reconstruction report generation from evidence chain and review decision linkage.

- Added evidence chain and review decision linkage across request, authorization, execution, evidence, operator review, human approval, and approval gate records.

- Added human approval record and approval gate while keeping real execution disabled in the MVP.

- Added operator readiness review summary for real execution blockers and next actions.

- Added real execution readiness gate and tests to keep real tool execution disabled until explicit prerequisites are satisfied.

- Added scope registry and target alias resolution controls for command plans and dry-run executor validation.

- Added dry-run controlled executor policy and tests before real tool execution.

- Added dry-run ZAP adapter command plan support without executing ZAP or external processes.

- Documented internal adapter artifact policy and clarified that adapter output remains private/internal by default.
- Added Tool Gateway adapter stubs and adapter registry for ZAP, Nmap, nuclei, and browser automation.
- Routed completed mock Tool Gateway actions through adapter stubs before real tool integration.


- Added v0.1.10 stability checkpoint documentation and a single local validation runner.

- Fixed remaining escaped Python docstring sequences that prevented Tool Gateway runner validation after v0.1.9.

### Fixed

- Fixed Tool Gateway mock runner syntax error introduced during mock Vault credential_ref validation.

- Added mock Vault metadata validation for credential_ref target, scope, tool, operation, expiry, and revocation constraints.
- Added credential_ref mock Vault negative tests.

- Added Tool Gateway runner self-tests for positive scenarios, generated outputs, and fail-closed negative cases.
- Added documentation and ADR for Tool Gateway negative tests.

- Added standard-library Tool Gateway mock runner for allowed, denied, and human-approval-required scenarios.
- Added Tool Gateway mock runner documentation and ADR.


- Added Tool Gateway prototype scaffold and example contract flows for allowed, denied, and human-approval-required actions.
- Added MVP example validation script.

- Added MVP schema contracts for tool action requests, authorization decisions, tool execution results, and evidence records.
- Added lightweight schema validation script.

- Defined Tool Gateway MVP design as the trusted execution control boundary.
- Added ADR for treating Tool Gateway as a trusted control boundary rather than a generic command executor.

- Defined credential_ref lifecycle, visibility boundaries, and Tool Gateway/Vault responsibilities.
- Added credential_ref flow document and ADR for secretless AI tool execution lifecycle.

- Defined initial MVP scope for controlled Web/API/NW assessment assistance.
- Added MVP scope document and ADR for initial tool and assessment boundaries.

- Initial local project scaffold.
- Local-first project management structure.
- Draft documents for business planning, architecture, AAEF controls, credential_ref, AI data handling, and exit strategy.

## v0.3.6 - Public repository readiness checkpoint

- Added a public repository readiness checkpoint before GitHub publication.
- Recorded publication gating checks for README, LICENSE, AGPL/CC BY attribution, private generated artifacts, execution prohibition, and commercial-contact placeholder handling.
- Added a local validation test for repository publication readiness boundaries.

## v0.3.7 - Publication hygiene and private artifact exclusion checkpoint

- Added a publication hygiene checkpoint before public repository publication.
- Added `.gitignore` coverage for `private-not-in-git/`, generated outputs, Python caches, local environment files, and editor noise.
- Added a local validation test to confirm private/generated artifacts are not tracked and publication hygiene does not imply runtime readiness.

## v0.3.8 - Public security policy and vulnerability disclosure checkpoint

- Added `SECURITY.md` for vulnerability disclosure posture, supported-version posture, scope, out-of-scope items, and safe testing expectations.
- Added a public security policy checkpoint that separates vulnerability reporting from commercial licensing and runtime authorization.
- Added a local validation test for security policy and vulnerability disclosure boundaries.

## v0.3.9 - First-publication repository settings checklist

- Added a first-publication repository settings checklist for GitHub repository creation and configuration.
- Recorded visibility, metadata, security, collaboration, branch protection/ruleset, and initial remote setup decision points.
- Added a local validation test that confirms first-publication guidance does not create a remote, push code, or weaken runtime execution boundaries.

## v0.4.0 - Public publication preparation release

- Added a v0.4.0 public publication preparation release summary.
- Consolidated the v0.3.5 through v0.3.9 public-readiness stack into a single publication-preparation checkpoint.
- Added a first-publication dry-run checklist and announcement draft for manual review.
- Added a local validation test confirming v0.4.0 does not create a remote, push code, change repository visibility, or weaken runtime execution boundaries.

## v0.4.1 - GitHub Actions CI scaffold

- Added a minimal GitHub Actions workflow for repository validation.
- The workflow runs `python tools/run_all_local_checks.py` on `push`, `pull_request`, and manual dispatch.
- Added a local validation test confirming the CI scaffold preserves runtime-execution and publication-safety boundaries.

## v0.4.2 - README public English wording cleanup

- Cleaned up README wording for English-first public repository presentation.
- Replaced Japanese local-management and AI authority wording with public English wording.
- Added a local validation test to keep the README public entry point English-first while preserving the AAEF authority boundary.

## v0.4.3 - Public-facing repository metadata and announcement pack

- Added a GitHub Actions validation badge to README.
- Added public repository metadata guidance for GitHub About fields and topics.
- Added a public-facing announcement draft and claim-boundary guidance.
- Added a local validation test for repository metadata and announcement positioning.

## v0.4.4 - Public repository launch checkpoint

- Added a public repository launch checkpoint after making the repository public.
- Recorded public visibility, origin publication, Actions validation, metadata, topics, private vulnerability reporting, and feature settings.
- Added a local validation test confirming the launch checkpoint preserves runtime-execution and scanning boundaries.

## v0.4.5 - Public release notes and launch announcement package

- Added a public release notes and launch announcement package.
- Added GitHub Release notes, short description, longer public announcement, LinkedIn-style announcement, and technical article lead drafts.
- Added commercial inquiry wording and public claim boundaries while preserving runtime-execution and scanning prohibitions.
- Added a local validation test for launch communication materials.

## v0.4.6 - GitHub release publication checkpoint

- Added a GitHub Release publication checkpoint after publishing the `v0.4.5` GitHub Release.
- Recorded release title, tag, URL, latest status, release-note safety boundaries, and private release-note source path.
- Added a local validation test confirming the release publication checkpoint preserves runtime-execution and scanning boundaries.

## v0.5.0 - Commercial adoption preparation checkpoint

- Added a commercial adoption preparation checkpoint for business-facing use without turning the public repository into a sales deck.
- Added public commercial-adoption boundary documentation covering OSS, commercial licensing, consulting/adoption support, and private sales-pack separation.
- Added local private sales-pack draft material under `private-not-in-git/` for enterprise outreach planning.
- Added a local validation test confirming commercial adoption wording preserves runtime-execution and scanning boundaries.

## v0.5.1 - README public baseline and commercial entrypoint cleanup

- Reworked README as the public front door for the current repository baseline.
- Moved the current public state, authority boundary, validation, security, release, and commercial adoption entrypoint near the top.
- Removed obsolete local-first/private-by-default public-entry wording.
- Added a local validation test for README public baseline and commercial entrypoint cleanup.

## v0.5.2 - README compatibility phrase registry and test design hardening

- Added a README compatibility phrase registry for stable README headings, attribution phrases, commercial-entrypoint wording, and safety-boundary phrases.
- Documented the test design distinction between forbidden positive claims and allowed negative boundary statements.
- Added a local validation test for README compatibility phrase preservation.

## v0.5.3 - Licensing, trademark, authorship, and commercial-use protection hardening

- Added public protection documents for notices, authorship, copyright attribution, commercial-license discussions, trademark-like project-name usage, and contribution boundaries.
- Added a protection checkpoint documenting commercial-use, naming, attribution, and contribution boundaries.
- Added a local validation test for licensing/trademark/authorship protection materials.

## v0.5.4 - Dependency and repository governance readiness checkpoint

- Added a dependency and repository governance readiness checkpoint.
- Documented lightweight dependency/license inventory expectations, branch protection planning, release/tag governance, and repository administration boundaries.
- Added a local validation test confirming governance readiness wording preserves runtime-execution and scanning boundaries.

## v0.5.5 - GitHub repository ruleset and branch protection planning checkpoint

- Added a GitHub repository ruleset and branch protection planning checkpoint.
- Documented planned protections for `main`, release tags, required checks, high-risk changes, emergency exceptions, and maintainer responsibilities.
- Added a local validation test confirming repository protection planning preserves runtime-execution and scanning boundaries.

## v0.5.6 - Release governance and maintainer operations checklist

- Added a release governance and maintainer operations checklist.
- Documented pre-release, merge, tag, push, GitHub Actions, private artifact, emergency exception, and post-release review steps.
- Added a local validation test confirming release operations wording preserves runtime-execution and scanning boundaries.

## v0.5.7 - Public trust and reviewer navigation checkpoint

- Added a public trust and reviewer navigation checkpoint.
- Documented role-based reading paths for technical reviewers, security reviewers, commercial reviewers, licensing reviewers, and maintainer operations reviewers.
- Added a local validation test confirming reviewer navigation preserves runtime-execution and scanning boundaries.

## v0.5.8 - Public front page and repository landing polish checkpoint

- Added a public front page and repository landing polish checkpoint.
- Documented above-the-fold README expectations, first-minute reviewer goals, trust-signal placement, role-based navigation placement, and product-introduction boundaries.
- Added a local validation test confirming front-page polish preserves runtime-execution and scanning boundaries.

## v0.5.9 - Public evidence and capability boundary summary

- Added a public evidence and capability boundary summary.
- Documented demonstrated capabilities, non-demonstrated capabilities, intentionally blocked capabilities, evidence artifacts, reviewer interpretation guidance, and public claim boundaries.
- Added a local validation test confirming the evidence/capability summary preserves runtime-execution and scanning boundaries.

## v0.5.10 - Public FAQ and reviewer objections handling

- Added a public FAQ and reviewer objections handling checkpoint.
- Documented answers to likely first-time reviewer questions about scope, runtime execution, scanning, AGPL-3.0, commercial licensing, evidence, governance, security reporting, and intentionally blocked capabilities.
- Added a local validation test confirming FAQ wording preserves runtime-execution and scanning boundaries.

## v0.6.0 - Implementation and evaluation work ordering

- Added a v0.6.0 implementation and evaluation work-ordering checkpoint.
- Documented workstream ordering across capability inventory, evaluation criteria, local lab decisioning, runtime boundary hardening, demonstration planning, and commercial PoC readiness.
- Added a local validation test confirming v0.6.0 sequencing preserves runtime-execution and scanning boundaries.

## v0.6.1 - Capability inventory and maturity map

- Added a v0.6.1 capability inventory and maturity map.
- Documented current capabilities, maturity levels, supporting artifacts, known gaps, and next-step implications across control gates, evidence/report flow, runtime boundaries, preflight scaffolding, governance, public trust, and future local-lab/commercial-PoC paths.
- Added a local validation test confirming the inventory preserves runtime-execution and scanning boundaries.

## v0.6.2 - Evaluation criteria and acceptance model

- Added a v0.6.2 evaluation criteria and acceptance model.
- Documented evaluation dimensions, acceptance gates, failure criteria, maturity advancement rules, evidence requirements, review expectations, local-lab decision criteria, demo-readiness criteria, and commercial-PoC boundary criteria.
- Added a local validation test confirming the evaluation model preserves runtime-execution and scanning boundaries.

## v0.6.3 - Safety boundary and non-goal review

- Added a v0.6.3 safety boundary and non-goal review.
- Documented hard non-goals, intentionally blocked capabilities, local-lab constraints, demo constraints, commercial-PoC constraints, fail-closed requirements, unsafe implication checks, and advancement conditions.
- Added a local validation test confirming the safety boundary and non-goal review preserves runtime-execution and scanning boundaries.

## v0.6.4 - Local assessment lab decision record

- Added a v0.6.4 local assessment lab decision record.
- Decided to proceed with documentation-only local lab profile and dry-run planning while deferring localhost-only controlled execution.
- Documented selected lab option, rejected options, entry criteria, exit criteria, allowed artifacts, prohibited behavior, local-only assumptions, and next-step implications.
- Added a local validation test confirming the lab decision preserves runtime-execution and scanning boundaries.

## v0.6.5 - Documentation-only local lab profile and action taxonomy

- Added a v0.6.5 documentation-only local lab profile and action taxonomy.
- Defined local lab profile fields, local-only assumptions, allowed action taxonomy, denied action taxonomy, preflight evidence requirements, human review requirements, generated output policy, and "what this lab does not prove" boundaries.
- Added a local validation test confirming the documentation-only lab profile preserves runtime-execution and scanning boundaries.

## v0.6.6 - AI request decision boundary and tool selection criteria

- Added a v0.6.6 AI request decision boundary and tool selection criteria checkpoint.
- Documented that AI may generate `tool_action_request` and recommend candidate methods, while execution authority remains with gates.
- Defined current and future tool-selection criteria for ZAP, Nmap, nuclei, browser, testssl.sh/sslyze, nikto, ffuf/feroxbuster, constrained sqlmap, wapiti/arachni, Burp Suite Pro CLI/API, and Nessus Essentials/OpenVAS.
- Added a local validation test confirming the AI request boundary preserves runtime-execution and scanning boundaries.

## v0.6.7 - Observation normalization and diagnostic fidelity risk review

- Added a v0.6.7 observation normalization and diagnostic fidelity risk review.
- Documented Diagnostic Fidelity Risk, loss-aware normalization, signal-preserving extraction, diagnostic context packages, sufficiency criteria, normalization loss records, escalation paths, and AI behavior under insufficient information.
- Added a local validation test confirming observation normalization guidance preserves runtime-execution and scanning boundaries.

## v0.6.8 - Demo scenario and reviewer walkthrough planning

- Added a v0.6.8 demo scenario and reviewer walkthrough planning checkpoint.
- Defined a public-safe non-executing walkthrough for explaining AI-visible context, AI-generated `tool_action_request`, gate decisions, evidence expectations, reviewer questions, and non-proof boundaries.
- Preserved the separation between demo explanation, dry-run behavior, runtime execution, and commercial PoC readiness.
- Added a local validation test confirming the demo planning preserves runtime-execution and scanning boundaries.

## v0.6.9 - Evidence reconstruction and sample report demonstration planning

- Added a v0.6.9 evidence reconstruction and sample report demonstration planning checkpoint.
- Defined public-safe non-executing planning for evidence reconstruction, sample evidence packets, sample report finding demonstration, reviewer questions, and report/delivery boundaries.
- Preserved the separation between sample evidence demonstration, dry-run behavior, runtime execution, commercial PoC readiness, and delivery authorization.
- Added a local validation test confirming the evidence/report demonstration plan preserves runtime-execution and scanning boundaries.

## v0.6.10 - Safe Docker lab roadmap and local target candidate planning

- Added a v0.6.10 safe Docker lab roadmap and local target candidate planning checkpoint.
- Defined local-only target candidate criteria, candidate lab targets, phased roadmap, preflight evidence expectations, human review expectations, network boundary requirements, reset/teardown expectations, and non-proof boundaries.
- Preserved the separation between local target candidate planning, dry-run behavior, bounded local execution, runtime execution, scan execution, commercial PoC readiness, and customer-target operation.
- Removed tracked public test inventories of specific private-sensitive terms and replaced them with abstract public-sensitive wording checks.
- Added a local validation test confirming safe Docker lab roadmap planning preserves runtime-execution and scanning boundaries.

## v0.6.11 - Local lab candidate profile and preflight evidence planning

- Added a v0.6.11 local lab candidate profile and preflight evidence planning checkpoint.
- Defined local lab candidate profile fields, candidate profile examples, preflight evidence package planning, candidate scoring, rejection criteria, human review expectations, and advancement gates.
- Preserved the separation between candidate profile planning, Docker execution, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.
- Added a local validation test confirming local lab candidate profile and preflight evidence planning preserves runtime-execution and scanning boundaries.

## v0.6.12 - Non-running Docker Compose design review planning

- Added a v0.6.12 non-running Docker Compose design review planning checkpoint.
- Defined Compose design review fields, network boundary review, port exposure review, image provenance review, environment variable review, volume and persistence review, reset/teardown review, resource limit review, preflight evidence expectations, and advancement gates.
- Preserved the separation between design review, Compose file creation, image pull, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.
- Added a local validation test confirming non-running Docker Compose design review planning preserves Docker execution, runtime-execution, scanning, and customer-target boundaries.

## v0.6.13 - Static Compose design sketch and network boundary review

- Added a v0.6.13 static Compose design sketch and network boundary review checkpoint.
- Defined non-runnable design sketch fields, service role inventory, localhost-only binding intent, isolated network posture, outbound network posture, port exposure intent, environment and secret posture, volume posture, reset/teardown posture, and advancement gates.
- Preserved the separation between static design sketch, Compose file creation, image pull, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.
- Added a local validation test confirming static Compose design sketch planning preserves Docker execution, runtime-execution, scanning, network, and customer-target boundaries.

## v0.6.14 - Static lab scenario fixture planning

- Added a v0.6.14 static lab scenario fixture planning checkpoint.
- Defined non-executing scenario fixture purpose, fixture set model, fixture node model, candidate-to-sketch linkage, AI request fixture boundary, gate decision fixture boundary, expected evidence fixture boundary, reviewer walkthrough linkage, fixture validation expectations, and advancement gates.
- Preserved the separation between static fixtures, runnable Compose configuration, image pull, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.
- Added a local validation test confirming static lab scenario fixture planning preserves Docker execution, runtime-execution, scanning, port binding, and customer-target boundaries.

## v0.6.15 - Static fixture schema and validator planning

- Added a v0.6.15 static fixture schema and validator planning checkpoint.
- Defined planning for fixture manifest schema, fixture node schemas, reference integrity, scenario trace validation, synthetic data assertions, no-secret checks, no-runtime checks, no-runnable-configuration checks, validator failure categories, and future validator boundaries.
- Preserved the separation between schema/validator planning, fixture generation, runnable Compose configuration, image pull, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.
- Added a local validation test confirming static fixture schema and validator planning preserves Docker execution, runtime-execution, scanning, port binding, fixture generation, and customer-target boundaries.

## v0.6.16 - Static fixture schema draft and negative test planning

- Added a v0.6.16 static fixture schema draft and negative test planning checkpoint.
- Defined non-implemented draft fields for fixture manifest, node envelope, required fixture nodes, AI request fixture, gate decision fixture, expected evidence fixture, scenario trace, and validator failure expectations.
- Defined negative test planning categories for missing nodes, broken references, runtime implications, runnable configuration, secret-like content, customer-like content, delivery implication, and overclaiming.
- Preserved the separation between schema draft planning, validator implementation, fixture generation, runnable Compose configuration, image pull, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.
- Added a local validation test confirming v0.6.16 preserves fixture-generation, validator-implementation, Docker execution, runtime-execution, scanning, port binding, and customer-target boundaries.

## v0.6.17 - Static fixture validator scaffold planning

- Added a v0.6.17 static fixture validator scaffold planning checkpoint.
- Defined future validator scaffold responsibilities, input and output boundaries, fail-closed behavior, planned validation stages, failure categories, negative-test handling, registration order, and review gates.
- Preserved the separation between validator scaffold planning, validator implementation, fixture generation, runnable Compose configuration, image pull, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.
- Added a local validation test confirming v0.6.17 preserves fixture-generation, validator-implementation, Docker execution, runtime-execution, scanning, port binding, and customer-target boundaries.

## v0.6.18 - Static fixture validator minimal scaffold design

- Added a v0.6.18 static fixture validator minimal scaffold design checkpoint.
- Defined future read-only validator module boundaries, CLI boundary, input model, output model, planned function boundaries, failure result model, fail-closed behavior, and future local-check registration conditions.
- Preserved the separation between minimal scaffold design, validator implementation, fixture generation, runnable Compose configuration, image pull, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.
- Added a local validation test confirming v0.6.18 preserves fixture-generation, validator-implementation, Docker execution, runtime-execution, scanning, port binding, and customer-target boundaries.

## v0.6.19 - Static fixture validator implementation readiness review

- Added a v0.6.19 static fixture validator implementation readiness review checkpoint.
- Defined readiness review posture, read-only checklist, fail-closed checklist, negative-test-first checklist, input and output boundary review, implementation gate checklist, registration readiness checklist, review record model, blocking issue categories, and future implementation order.
- Preserved the separation between implementation readiness review, validator implementation, fixture generation, runnable Compose configuration, image pull, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.
- Added a local validation test confirming v0.6.19 preserves fixture-generation, validator-implementation, CLI-implementation, Docker execution, runtime-execution, scanning, port binding, and customer-target boundaries.

## v0.6.20 - Static fixture validator read-only implementation scaffold

- Added a v0.6.20 static fixture validator read-only implementation scaffold.
- Added `tools/validate_static_lab_fixtures.py` as a minimal read-only scaffold with review-only result data, planned failure categories, fail-closed missing-directory behavior, and a non-authorizing CLI boundary.
- Added validation tests confirming the scaffold is read-only, does not create fixture artifacts, does not authorize execution, and preserves Docker/runtime/scanning/customer-target boundaries.
- Preserved the separation between read-only scaffold implementation, complete validator implementation, fixture generation, runnable Compose configuration, image pull, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.

## v0.6.21 - Static fixture validator required-node check planning

- Added a v0.6.21 static fixture validator required-node check planning checkpoint.
- Defined future manifest and required-node check boundaries for the read-only static fixture validator.
- Recorded required fixture node set, missing-node failure categories, fail-closed expected behavior, non-authorization boundaries, and future implementation sequencing.
- Preserved the separation between required-node check planning, validator implementation, fixture generation, runnable Compose configuration, image pull, container startup, bounded local execution, scan execution, commercial PoC readiness, and customer-target operation.
- Added a local validation test confirming v0.6.21 preserves required-node-check implementation, fixture-generation, Docker execution, runtime-execution, scanning, port binding, and customer-target boundaries.

## v0.6.22 - AAEF applied evidence work intake and current-state review

- Added a v0.6.22 AAEF applied evidence work intake and current-state review checkpoint.
- Recorded the AAEF-side request to prioritize a safe applied evidence record over a stronger vulnerability scanning AI.
- Inventoried current repository state, including latest tag/commit, docs/planning/ADR/issue artifacts, validators, Tool Gateway/local-lab-related files, and current local-check registration posture.
- Reordered the next work so evidence-package planning, scenario planning, reviewer walkthrough, and AAEF five-questions mapping precede further validator implementation.
- Preserved public/private boundaries, patent-sensitive abstraction boundaries, and non-goals for production readiness, certification, compliance, audit/legal sufficiency, implementation conformance, and external-framework equivalence.

## v0.6.23 - AAEF applied evidence package design

- Added a v0.6.23 AAEF applied evidence package design checkpoint.
- Defined the applied evidence package structure for `tool_action_request`, `gate_decision`, `dispatch_decision`, `execution_result` / `non_execution_result`, `evidence_event`, and `review_summary`.
- Clarified the difference between static/mock applied evidence capture and real local-lab diagnostic system evidence capture.
- Recorded that static/mock evidence package generation can begin after package design, scenario planning, fixture planning, reviewer walkthrough, and structural validator planning, while real local-lab diagnostic execution should remain deferred to a later gated local-lab phase.
- Preserved the boundary that no new runtime execution, scanner execution, credential injection, customer-target operation, certification, compliance, audit/legal sufficiency, implementation conformance, or production-readiness claim is introduced.

## v0.6.24 - Applied evidence scenario set planning

- Added a v0.6.24 applied evidence scenario set planning checkpoint.
- Defined the four minimum AAEF applied evidence scenarios: permitted safe diagnostic, denied out-of-scope request, human approval required, and not-executed / expired.
- Recorded scenario intent, expected artifact chain, decision posture, dispatch posture, result posture, evidence posture, reviewer focus, AAEF five-questions coverage, and non-proof boundaries.
- Preserved the boundary that scenario planning does not generate evidence packages, implement fixtures, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.25 - Static applied evidence fixture planning

- Added a v0.6.25 static applied evidence fixture planning checkpoint.
- Planned the static fixture artifact set for all four applied evidence scenarios: `permitted-safe-diagnostic`, `denied-out-of-scope-request`, `human-approval-required`, and `not-executed-expired`.
- Defined per-artifact fixture planning for `tool_action_request`, `gate_decision`, `dispatch_decision`, `execution_result` / `non_execution_result`, `evidence_event`, and `review_summary`.
- Recorded fixture naming, identifier-linkage, scenario consistency, non-execution evidence, AAEF five-questions coverage, non-proof statements, and future generation boundaries.
- Preserved the boundary that v0.6.25 does not generate fixtures, generate evidence packages, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.26 - Reviewer walkthrough and five questions mapping

- Added a v0.6.26 reviewer walkthrough and AAEF five questions mapping checkpoint.
- Defined reviewer walkthrough structure for the applied evidence package and all four minimum scenarios.
- Mapped `tool_action_request`, `gate_decision`, `dispatch_decision`, `execution_result` / `non_execution_result`, `evidence_event`, and `review_summary` to the AAEF five questions.
- Recorded per-scenario reviewer questions, expected reviewer conclusions, non-proof boundaries, and future walkthrough artifact planning.
- Preserved the boundary that v0.6.26 does not generate fixtures, generate evidence packages, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.27 - Applied evidence structural validator planning

- Added a v0.6.27 applied evidence structural validator planning checkpoint.
- Planned structural checks for artifact presence, required fields, identifier linkage, scenario consistency, dispatch/result contradiction prevention, non-execution evidence, reviewer walkthrough coverage, non-proof statements, and overclaim prevention.
- Defined validator input/output boundaries, fail-closed categories, scenario-specific contradiction checks, five-questions mapping checks, and future implementation sequencing.
- Preserved the boundary that v0.6.27 does not implement validators, generate fixtures, generate evidence packages, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.28 - Static/mock applied evidence package generation readiness review

- Added a v0.6.28 static/mock applied evidence package generation readiness review checkpoint.
- Reviewed readiness conditions after package design, scenario planning, fixture planning, reviewer walkthrough mapping, and structural validator planning.
- Defined generation readiness criteria, blocker categories, private-first generation posture, public-safe publication criteria, rollback boundaries, and the next checkpoint path.
- Preserved the boundary that v0.6.28 does not generate fixtures, generate evidence packages, implement structural validators, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.29 - Static/mock applied evidence package private generation candidate

- Added a v0.6.29 static/mock applied evidence package private generation candidate.
- Added `tools/generate_static_mock_applied_evidence_package.py` to generate a private-first static/mock package under `private-not-in-git/`.
- Generated package structure covers `permitted-safe-diagnostic`, `denied-out-of-scope-request`, `human-approval-required`, and `not-executed-expired`.
- Added validation tests confirming generated private artifacts preserve request-to-evidence linkage, scenario consistency, non-execution evidence, non-proof statements, AAEF five-questions mapping, and runtime/scanning/customer-target/delivery boundaries.
- Preserved the boundary that v0.6.29 does not create public samples, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.30 - Static/mock applied evidence package review and promotion gate planning

- Added a v0.6.30 static/mock applied evidence package review and promotion gate planning checkpoint.
- Defined private package review criteria for the v0.6.29 generated static/mock applied evidence package.
- Planned public sample promotion gate criteria, blocker categories, promotion outcomes, publication-safe requirements, rollback posture, and AAEF-side reporting boundaries.
- Preserved the boundary that v0.6.30 does not promote public samples, generate public artifacts, implement structural validators, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.31 - Static/mock applied evidence package private review record

- Added a v0.6.31 static/mock applied evidence package private review record checkpoint.
- Added `tools/generate_static_mock_applied_evidence_private_review_record.py` to review the private static/mock package and emit private review records under `private-not-in-git/`.
- Generated private review outputs summarize scenario coverage, artifact presence, identifier linkage posture, non-proof visibility, runtime/scanning/customer/delivery boundaries, blocker categories, and promotion gate result.
- Preserved the boundary that v0.6.31 does not promote public samples, generate public artifacts, implement structural validators, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.32 - Static/mock applied evidence package public sample promotion decision record

- Added a v0.6.32 static/mock applied evidence package public sample promotion decision record checkpoint.
- Recorded the decision after the v0.6.31 private review record: keep the private package private, do not authorize public sample generation, and allow only a later sanitized public sample planning checkpoint to be considered under separate review.
- Defined decision inputs, decision outcome, conditions for later planning, blockers that still prevent public generation, AAEF-side reporting notes, and rollback posture.
- Preserved the boundary that v0.6.32 does not promote public samples, generate public artifacts, implement structural validators, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.33 - Sanitized public sample planning

- Added a v0.6.33 sanitized public sample planning checkpoint.
- Planned public sample scope, sanitized artifact naming, public directory placement, synthetic-only requirements, private-to-public transformation rules, publication hygiene checks, non-proof visibility, overclaim prevention, patent-sensitive detail exclusion, and human publication review requirements.
- Kept direct public sample generation unauthorized while allowing a later sanitized public sample generation candidate to be considered only after this planning boundary.
- Preserved the boundary that v0.6.33 does not generate public sample artifacts, copy private generated artifacts into the public repository, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.34 - Sanitized public sample generation readiness review

- Added a v0.6.34 sanitized public sample generation readiness review checkpoint.
- Reviewed readiness after v0.6.33 sanitized public sample planning, including sample scope, `.example.` naming, public directory placement, synthetic-only requirements, publication hygiene, patent-sensitive detail exclusion, non-proof visibility, overclaim prevention, and human publication review.
- Recorded a conservative readiness outcome: a later sanitized public sample generation candidate may be considered, but public sample generation remains unauthorized by v0.6.34.
- Preserved the boundary that v0.6.34 does not generate public sample artifacts, copy private generated artifacts into the public repository, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.

## v0.6.35 - Sanitized public sample generation candidate

- Added a v0.6.35 sanitized public sample generation candidate.
- Added `tools/generate_sanitized_public_sample.py` to create synthetic, non-executing `.example.` artifacts under `examples/applied-evidence/sanitized-static-mock/`.
- Generated public-safe example artifacts for `permitted-safe-diagnostic`, `denied-out-of-scope-request`, `human-approval-required`, and `not-executed-expired`.
- Added validation tests for artifact presence, `.example.` naming, request-to-evidence linkage, non-proof statements, publication hygiene, and no runtime/scanning/customer-target/delivery authorization.
- Preserved the boundary that v0.6.35 does not copy private generated artifacts into the public repository, run scanners, create runnable configuration, authorize Docker/runtime execution, inject credentials, authorize customer-target operation, or authorize delivery.
