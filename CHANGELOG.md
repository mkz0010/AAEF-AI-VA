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
