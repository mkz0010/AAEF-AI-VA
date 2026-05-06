# AAEF-AI-VA

[![Validate AAEF-AI-VA artifacts](https://github.com/mkz0010/AAEF-AI-VA/actions/workflows/validate.yml/badge.svg)](https://github.com/mkz0010/AAEF-AI-VA/actions/workflows/validate.yml)

A safety-first reference implementation for AI-assisted vulnerability assessment control boundaries.

AAEF-AI-VA demonstrates how AI-assisted vulnerability assessment workflows can remain blocked by default until authorization, contractual scope, Tool Gateway behavior, preflight evidence, and human review gates support the action.

## Current public baseline

| Item | Current state |
| --- | --- |
| Repository | `https://github.com/mkz0010/AAEF-AI-VA` |
| Visibility | Public |
| Latest repository checkpoint | `v0.5.0` |
| Latest GitHub Release | `AAEF-AI-VA v0.4.5 Public Launch Communication Package` |
| Release URL | `https://github.com/mkz0010/AAEF-AI-VA/releases/tag/v0.4.5` |
| License | GNU Affero General Public License v3.0 |
| Security policy | `SECURITY.md` |
| Private vulnerability reporting | Enabled |
| GitHub Actions | `.github/workflows/validate.yml` |
| Runtime execution | Disabled |
| Live scanning | Not authorized |
| Customer-target operation | Not authorized |

## Core principle

AI output is not authority to perform assessment actions.

AI may request assessment actions, but execution is decided by the AAEF Authorization Gateway, Tool Gateway, contractual scope, and human review.

This repository treats AI output as a request that must pass explicit control boundaries before any assessment action can proceed.

## What this is

AAEF-AI-VA is:

- a public AGPL-3.0 reference implementation,
- a control-boundary model for AI-assisted vulnerability assessment,
- a repository of local validation gates and safety checkpoints,
- a demonstration of fail-closed authorization, preflight evidence, review, and delivery boundaries,
- a technical credibility artifact for commercial adoption discussions,
- a foundation for controlled PoC and advisory conversations.

## What this is not

AAEF-AI-VA is not:

- a production scanner,
- an autonomous vulnerability scanner,
- a customer-ready managed assessment platform,
- a compliance certification scheme,
- legal advice,
- an audit opinion,
- permission to scan third-party systems,
- permission to inject credentials,
- permission to operate against customer targets.

## Commercial adoption entrypoint

The public repository is intended to provide technical credibility and reviewable boundaries.

Commercial adoption discussions are separate from vulnerability reports and do not authorize runtime execution, scanning, credential injection, or customer-target operation.

Potential commercial paths include:

- advisory workshop,
- controlled internal PoC design,
- AI-assisted assessment workflow architecture review,
- integration support,
- commercial license discussion for organizations that cannot use AGPL-3.0 as-is.

See `docs/66-commercial-adoption-preparation-checkpoint.md`.

## Safety and runtime boundary

Runtime execution remains disabled.

The current public implementation does not authorize:

- live scanning,
- external network testing,
- credential injection,
- customer-target operation,
- unmanaged tool execution,
- unreviewed report delivery.

Generated local artifacts, private sales materials, and temporary review outputs belong under `private-not-in-git/` and must not be tracked.

## Validation

Run all local checks:

~~~bash
python tools/run_all_local_checks.py
~~~

The GitHub Actions workflow also runs the same validation entry point:

~~~text
.github/workflows/validate.yml
~~~

## Public Repository Metadata

Recommended GitHub repository metadata:

- Repository name: `AAEF-AI-VA`
- Description: `Safety-first reference implementation for AI-assisted vulnerability assessment control boundaries`
- URL: `https://github.com/mkz0010/AAEF-AI-VA`
- Topics: `ai-security`, `vulnerability-assessment`, `agentic-ai`, `security-automation`, `auditability`, `agpl`, `ai-assurance`, `security-controls`

See `docs/62-public-facing-repository-metadata-and-announcement-pack.md`.

## License and commercial-use boundary

AAEF-AI-VA code is licensed under the GNU Affero General Public License v3.0.

This project builds on the Agentic Authority & Evidence Framework / AAEF.

Parent AAEF repository: https://github.com/mkz0010/agentic-authority-evidence-framework

AAEF is licensed under CC BY 4.0 (Creative Commons Attribution 4.0 International).

AAEF-AI-VA code is licensed under the GNU Affero General Public License v3.0.

For commercial licensing inquiries, private deployment discussions, proprietary integration, and managed service use, contact the project author. These discussions do not replace AGPL-3.0 obligations unless a separate commercial license is agreed.

See:

- `LICENSE`
- `docs/54-licensing-and-commercial-use-boundary.md`
- `docs/66-commercial-adoption-preparation-checkpoint.md`

## Publication Hygiene and Private Artifact Boundary

AAEF-AI-VA keeps publication hygiene and private artifact handling as explicit public repository boundaries.

Private generated artifacts, local run outputs, sales materials, release-note drafts, and customer-specific planning material must remain under `private-not-in-git/` and must not be tracked.

See `docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md`.

## Security Policy

Security reports should follow `SECURITY.md`.

Sensitive vulnerability details should not be posted publicly. Private vulnerability reporting is enabled for this public repository.

See:

- `SECURITY.md`
- `docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md`

## Publication and release checkpoints

The repository records its publication and release state in versioned checkpoints:

- `docs/55-public-repository-readiness-checkpoint.md`
- `docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md`
- `docs/58-first-publication-repository-settings-checklist.md`
- `docs/59-v040-publication-preparation-release.md`
- `docs/60-github-actions-ci-scaffold.md`
- `docs/61-readme-public-english-wording-cleanup.md`
- `docs/62-public-facing-repository-metadata-and-announcement-pack.md`
- `docs/63-public-repository-launch-checkpoint.md`
- `docs/64-public-release-notes-and-launch-announcement-package.md`
- `docs/65-github-release-publication-checkpoint.md`
- `docs/66-commercial-adoption-preparation-checkpoint.md`

## First Publication Repository Settings

The first-publication repository settings checklist records GitHub repository settings and publication decisions as manual actions.

See `docs/58-first-publication-repository-settings-checklist.md`.

## v0.4.0 Public Publication Preparation Release

v0.4.0 prepared the repository for deliberate public publication.

See `docs/59-v040-publication-preparation-release.md`.

## GitHub Actions CI Scaffold

The GitHub Actions CI scaffold validates the repository without enabling runtime execution.

See `.github/workflows/validate.yml` and `docs/60-github-actions-ci-scaffold.md`.

## Public Repository Launch Checkpoint

The public repository launch checkpoint records public visibility, Actions validation, private vulnerability reporting, repository metadata, and continued runtime-execution prohibition.

Repository URL: `https://github.com/mkz0010/AAEF-AI-VA`

See `docs/63-public-repository-launch-checkpoint.md`.

## Public Release Notes and Launch Announcement Package

The public release notes and launch announcement package records reusable launch communication material and claim boundaries.

See `docs/64-public-release-notes-and-launch-announcement-package.md`.

## GitHub Release Publication Checkpoint

The GitHub Release publication checkpoint records the first public GitHub Release publication.

Release title: `AAEF-AI-VA v0.4.5 Public Launch Communication Package`

Release URL: `https://github.com/mkz0010/AAEF-AI-VA/releases/tag/v0.4.5`

See `docs/65-github-release-publication-checkpoint.md`.

## Commercial Adoption Preparation

The commercial adoption preparation checkpoint records the public/private commercial-material boundary and targeted enterprise adoption posture.

See `docs/66-commercial-adoption-preparation-checkpoint.md`.

## Historical implementation checkpoints

Earlier implementation and readiness checkpoints remain available in the repository history, docs, changelog, roadmap, and tags.

For current public evaluation, start with:

1. this README,
2. `SECURITY.md`,
3. `LICENSE`,
4. `docs/66-commercial-adoption-preparation-checkpoint.md`,
5. `docs/65-github-release-publication-checkpoint.md`,
6. `tools/run_all_local_checks.py`.

## README Compatibility Phrase Registry

AAEF-AI-VA maintains a README compatibility phrase registry so future README rewrites preserve earlier checkpoint expectations and avoid broad false-positive claim checks.

See `docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md`.

## Licensing, Trademark, Authorship, and Commercial-Use Protection

AAEF-AI-VA includes public boundary documents for licensing, authorship, notices, trademark-like name usage, contribution rules, and commercial-use discussions.

These documents do not provide legal advice and do not claim registered trademark status unless separately registered.

See:

- `NOTICE`
- `AUTHORS`
- `COPYRIGHT`
- `COMMERCIAL-LICENSE.md`
- `TRADEMARKS.md`
- `CONTRIBUTING.md`
- `docs/69-licensing-trademark-authorship-protection-checkpoint.md`

## Dependency and Repository Governance Readiness

AAEF-AI-VA includes a dependency and repository governance readiness checkpoint.

The checkpoint records a lightweight foundation for dependency/license inventory, branch protection planning, release/tag governance, security policy alignment, and repository administration.

It does not enable runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/70-dependency-and-repository-governance-readiness-checkpoint.md`.

## GitHub Repository Ruleset and Branch Protection Planning

AAEF-AI-VA includes a GitHub repository ruleset and branch protection planning checkpoint.

The checkpoint records planned repository protections for `main`, release tags, required validation, high-risk change review, and emergency exception handling.

It is planning only and does not configure GitHub branch protection or rulesets by itself.

See `docs/71-github-repository-ruleset-and-branch-protection-planning-checkpoint.md`.

## Release Governance and Maintainer Operations Checklist

AAEF-AI-VA includes a release governance and maintainer operations checklist.

The checklist records the intended operational steps for scoped branches, local validation, fast-forward merge, tag creation, GitHub Actions verification, private artifact checks, emergency exceptions, and post-release review.

It is an operations checklist only and does not configure GitHub settings by itself.

See `docs/72-release-governance-and-maintainer-operations-checklist.md`.

## Public Trust and Reviewer Navigation

AAEF-AI-VA includes a public trust and reviewer navigation checkpoint.

The checkpoint gives first-time reviewers a role-based reading path for technical review, security review, commercial review, licensing review, and maintainer operations review.

It is a public navigation aid only and does not claim production readiness, certification, legal approval, audit opinion, scan authorization, or customer-target authorization.

See `docs/73-public-trust-and-reviewer-navigation-checkpoint.md`.

## Public Front Page and Repository Landing Polish

AAEF-AI-VA includes a public front page and repository landing polish checkpoint.

The checkpoint records how the repository should introduce itself to first-time readers: concise value proposition, clear safety boundaries, role-based navigation, trust signals, and commercial-use boundaries.

It is presentation and navigation polish only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/74-public-front-page-and-repository-landing-polish-checkpoint.md`.

## Public Evidence and Capability Boundary Summary

AAEF-AI-VA includes a public evidence and capability boundary summary.

The summary explains what the repository currently demonstrates, what it does not yet demonstrate, what remains intentionally blocked, and which public artifacts support those boundaries.

It is an evidence and capability explanation only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/75-public-evidence-and-capability-boundary-summary.md`.

## Public FAQ and Reviewer Objections Handling

AAEF-AI-VA includes a public FAQ and reviewer objections handling checkpoint.

The FAQ gives first-time reviewers direct answers to likely questions about scope, runtime execution, scanning, AGPL-3.0, commercial licensing, security reporting, evidence, governance, and what remains intentionally blocked.

It is explanatory material only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/76-public-faq-and-reviewer-objections-handling.md`.

## v0.6.0 Implementation and Evaluation Work Ordering

AAEF-AI-VA includes a v0.6.0 implementation and evaluation work-ordering checkpoint.

The checkpoint organizes the next phase before choosing whether to start with a local assessment lab, an evaluation matrix, runtime gate hardening, demo scenarios, or commercial PoC preparation.

It is planning and sequencing only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/77-v060-implementation-and-evaluation-work-ordering.md`.

## v0.6.1 Capability Inventory and Maturity Map

AAEF-AI-VA includes a v0.6.1 capability inventory and maturity map.

The map inventories current capabilities, supporting artifacts, maturity levels, known gaps, and next-step implications before deciding whether to build a local assessment lab, improve evaluation criteria, harden runtime gates, or prepare controlled demos.

It is inventory and planning only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/78-v061-capability-inventory-and-maturity-map.md`.

## v0.6.2 Evaluation Criteria and Acceptance Model

AAEF-AI-VA includes a v0.6.2 evaluation criteria and acceptance model.

The model defines how future capabilities should be evaluated before the project proceeds to local lab decisioning, demo walkthroughs, runtime gate hardening, or commercial PoC readiness.

It is evaluation planning only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/79-v062-evaluation-criteria-and-acceptance-model.md`.

## v0.6.3 Safety Boundary and Non-Goal Review

AAEF-AI-VA includes a v0.6.3 safety boundary and non-goal review.

The review reconfirms which capabilities remain intentionally blocked before the project proceeds toward local lab decisioning, demo walkthroughs, runtime gate hardening, or commercial PoC readiness.

It is boundary review only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/80-v063-safety-boundary-and-non-goal-review.md`.

## v0.6.4 Local Assessment Lab Decision Record

AAEF-AI-VA includes a v0.6.4 local assessment lab decision record.

The record decides that the project may proceed with a documentation-only local lab profile and dry-run planning, but must not build or enable localhost-only controlled execution yet.

It is a decision record only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/81-v064-local-assessment-lab-decision-record.md`.

## v0.6.5 Documentation-Only Local Lab Profile and Action Taxonomy

AAEF-AI-VA includes a v0.6.5 documentation-only local lab profile and action taxonomy.

The profile defines target mode, target ownership, network boundary, allowed action categories, denied action categories, preflight evidence requirements, human review requirements, generated output location, and what the lab does not prove.

It is documentation-only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/82-v065-documentation-only-local-lab-profile-and-action-taxonomy.md`.

## v0.6.6 AI Request Decision Boundary and Tool Selection Criteria

AAEF-AI-VA includes a v0.6.6 AI request decision boundary and tool selection criteria checkpoint.

The checkpoint defines the project’s core execution-separation rule: AI may generate `tool_action_request` and recommend candidate methods, but execution is decided by authorization, scope, preflight, Tool Gateway, and human review gates.

It is design and planning only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/83-v066-ai-request-decision-boundary-and-tool-selection-criteria.md`.

## v0.6.7 Observation Normalization and Diagnostic Fidelity Risk Review

AAEF-AI-VA includes a v0.6.7 observation normalization and diagnostic fidelity risk review.

The review defines how raw responses, sanitized artifacts, normalized observations, extracted diagnostic signals, and AI diagnostic context packages should be separated so safety controls do not erase diagnostically important information without evidence.

It is design and risk review only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/84-v067-observation-normalization-and-diagnostic-fidelity-risk-review.md`.

## v0.6.8 Demo Scenario and Reviewer Walkthrough Planning

AAEF-AI-VA includes a v0.6.8 demo scenario and reviewer walkthrough planning checkpoint.

The checkpoint defines a public-safe, non-executing reviewer walkthrough that explains what AI may see through approved diagnostic context, what `tool_action_request` it may generate, which gates evaluate the request, what evidence is expected, and what the walkthrough does not prove.

It is planning only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/85-v068-demo-scenario-and-reviewer-walkthrough-planning.md`.

## v0.6.9 Evidence Reconstruction and Sample Report Demonstration Planning

AAEF-AI-VA includes a v0.6.9 evidence reconstruction and sample report demonstration planning checkpoint.

The checkpoint defines how a public-safe, non-executing demonstration can show the relationship between approved diagnostic context, AI-generated `tool_action_request`, gate decisions, expected evidence, finding review, report finding promotion, report packet review, and delivery authorization boundaries.

It is planning only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/86-v069-evidence-reconstruction-and-sample-report-demonstration-planning.md`.

## v0.6.10 Safe Docker Lab Roadmap and Local Target Candidate Planning

AAEF-AI-VA includes a v0.6.10 safe Docker lab roadmap and local target candidate planning checkpoint.

The checkpoint defines how intentionally vulnerable local targets such as DVWA, OWASP Juice Shop, and WebGoat may be considered as future local-only candidates without enabling Docker execution, scan execution, external network testing, credential injection, or customer-target operation.

It is roadmap and candidate planning only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/87-v0610-safe-docker-lab-roadmap-and-local-target-candidate-planning.md`.

## v0.6.11 Local Lab Candidate Profile and Preflight Evidence Planning

AAEF-AI-VA includes a v0.6.11 local lab candidate profile and preflight evidence planning checkpoint.

The checkpoint defines candidate profile fields and preflight evidence expectations for future local-only lab candidates such as DVWA, OWASP Juice Shop, WebGoat, a synthetic local API, and static fixture targets, while keeping Docker execution, container startup, scanner execution, credential injection, and customer-target operation blocked.

It is candidate-profile and preflight-evidence planning only. It does not authorize runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/88-v0611-local-lab-candidate-profile-and-preflight-evidence-planning.md`.

## v0.6.12 Non-running Docker Compose Design Review Planning

AAEF-AI-VA includes a v0.6.12 non-running Docker Compose design review planning checkpoint.

The checkpoint defines review criteria for a future Docker Compose design without creating Compose files, pulling images, starting containers, opening ports, running scanners, injecting credentials, or authorizing customer-target operation.

It is non-running design review planning only. It does not authorize Docker execution, runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/89-v0612-non-running-docker-compose-design-review-planning.md`.

## v0.6.13 Static Compose Design Sketch and Network Boundary Review

AAEF-AI-VA includes a v0.6.13 static Compose design sketch and network boundary review checkpoint.

The checkpoint defines review criteria for a non-runnable static Compose design sketch, including service role inventory, local network boundary, port binding intent, outbound network posture, environment and secret posture, volume posture, reset/teardown posture, and advancement gates without creating Docker Compose files, pulling images, starting containers, opening ports, running scanners, injecting credentials, or authorizing customer-target operation.

It is static design sketch and network boundary review only. It does not authorize Docker execution, runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/90-v0613-static-compose-design-sketch-and-network-boundary-review.md`.

## v0.6.14 Static Lab Scenario Fixture Planning

AAEF-AI-VA includes a v0.6.14 static lab scenario fixture planning checkpoint.

The checkpoint defines how a future non-executing static fixture set can connect a local lab candidate profile, static Compose design sketch, approved diagnostic context summary, AI-generated `tool_action_request`, gate decision, expected evidence, reviewer questions, and non-proof statement without creating runnable configuration, starting containers, running scanners, opening ports, injecting credentials, or authorizing customer-target operation.

It is static scenario fixture planning only. It does not authorize Docker execution, runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

See `docs/91-v0614-static-lab-scenario-fixture-planning.md`.

## v0.6.15 Static Fixture Schema and Validator Planning

AAEF-AI-VA includes a v0.6.15 static fixture schema and validator planning checkpoint.

The checkpoint defines how future non-executing static lab scenario fixtures should be shaped, linked, and validated before any fixture artifacts are generated or committed. It covers fixture manifest fields, node schemas, reference integrity, synthetic data assertions, no-secret checks, no-runtime checks, no-runnable-configuration checks, scenario trace validation, and validator failure categories.

It is schema and validator planning only. It does not generate fixture files, create runnable configuration, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/92-v0615-static-fixture-schema-and-validator-planning.md`.

## v0.6.16 Static Fixture Schema Draft and Negative Test Planning

AAEF-AI-VA includes a v0.6.16 static fixture schema draft and negative test planning checkpoint.

The checkpoint defines a non-implemented schema draft posture and negative test expectations for future static lab scenario fixtures. It covers fixture manifest draft fields, node envelope draft fields, required node draft fields, reference integrity draft rules, scenario trace draft rules, negative example classes, no-secret expectations, no-runtime expectations, no-runnable-configuration expectations, and future validator failure expectations.

It is schema draft and negative test planning only. It does not implement fixture schemas, implement fixture validators, generate fixture files, create runnable configuration, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/93-v0616-static-fixture-schema-draft-and-negative-test-planning.md`.

## v0.6.17 Static Fixture Validator Scaffold Planning

AAEF-AI-VA includes a v0.6.17 static fixture validator scaffold planning checkpoint.

The checkpoint defines the responsibilities, input boundaries, output boundaries, failure categories, fail-closed behavior, implementation order, and future registration conditions for a future static fixture validator scaffold before any validator code is implemented or fixture artifacts are generated.

It is validator scaffold planning only. It does not implement fixture schemas, implement fixture validators, implement negative tests, generate fixture files, create runnable configuration, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/94-v0617-static-fixture-validator-scaffold-planning.md`.

## v0.6.18 Static Fixture Validator Minimal Scaffold Design

AAEF-AI-VA includes a v0.6.18 static fixture validator minimal scaffold design checkpoint.

The checkpoint defines a future read-only validator scaffold design before implementation. It records minimal module boundaries, CLI boundary, input model, output model, planned function boundaries, failure result model, fail-closed behavior, and future registration conditions while preserving the boundary that no validator code is implemented and no fixture artifacts are generated.

It is minimal scaffold design only. It does not implement fixture schemas, implement fixture validators, implement negative tests, generate fixture files, create runnable configuration, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/95-v0618-static-fixture-validator-minimal-scaffold-design.md`.

## v0.6.19 Static Fixture Validator Implementation Readiness Review

AAEF-AI-VA includes a v0.6.19 static fixture validator implementation readiness review checkpoint.

The checkpoint defines the review gates that must be satisfied before future validator implementation begins. It checks planned read-only behavior, fail-closed behavior, negative-test-first ordering, input and output boundaries, registration readiness, blocking issue categories, and reviewer sign-off boundaries while preserving that no validator code, CLI, checks, schemas, negative tests, or fixture artifacts are implemented by this checkpoint.

It is implementation-readiness review only. It does not implement fixture schemas, implement fixture validators, implement CLI behavior, implement negative tests, generate fixture files, create runnable configuration, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/96-v0619-static-fixture-validator-implementation-readiness-review.md`.

## v0.6.20 Static Fixture Validator Read-only Implementation Scaffold

AAEF-AI-VA includes a v0.6.20 static fixture validator read-only implementation scaffold.

The checkpoint adds a minimal read-only validator scaffold at `tools/validate_static_lab_fixtures.py`. The scaffold exposes review-only data structures, a read-only CLI boundary, planned failure categories, and fail-closed behavior for missing or invalid fixture directories. It does not generate fixture artifacts, implement full fixture validation, run Docker, run scanners, access external targets, inject credentials, authorize execution, or authorize delivery.

It is read-only implementation scaffold only. It does not implement complete fixture schemas, implement complete fixture validators, implement negative tests, generate fixture files, create runnable configuration, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/97-v0620-static-fixture-validator-read-only-implementation-scaffold.md`.

## v0.6.21 Static Fixture Validator Required-node Check Planning

AAEF-AI-VA includes a v0.6.21 static fixture validator required-node check planning checkpoint.

The checkpoint defines how future read-only validator work should check the fixture manifest and required static fixture nodes before full schema validation, reference validation, negative-test implementation, or positive fixture generation begins. It preserves that v0.6.21 is planning only and does not extend the v0.6.20 read-only scaffold with new validation behavior.

It is required-node check planning only. It does not implement complete fixture schemas, implement complete fixture validators, implement required-node checks, implement negative tests, generate fixture files, create runnable configuration, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/98-v0621-static-fixture-validator-required-node-check-planning.md`.

## v0.6.22 AAEF Applied Evidence Work Intake and Current-state Review

AAEF-AI-VA includes a v0.6.22 AAEF applied evidence work intake and current-state review checkpoint.

This checkpoint responds to the AAEF-side request to prioritize a small, safe, reviewable applied evidence record over building a stronger vulnerability scanning AI. It inventories the current repository state, restates the local-lab-only boundary, maps the required request / gate / dispatch / evidence chain, and reorders the next work so that evidence-package planning comes before further validator implementation.

It is intake, inventory, and work-ordering only. It does not implement required-node checks, generate fixture files, run scanners, create runnable configuration, authorize Docker execution, authorize runtime execution, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/99-v0622-aaef-applied-evidence-work-intake-and-current-state-review.md`.

## v0.6.23 AAEF Applied Evidence Package Design

AAEF-AI-VA includes a v0.6.23 AAEF applied evidence package design checkpoint.

This checkpoint defines the package structure for a small, safe, reviewable AAEF applied evidence record for AI-assisted vulnerability assessment workflows. It designs the artifact chain from `tool_action_request` to `gate_decision`, `dispatch_decision`, `execution_result` or `non_execution_result`, `evidence_event`, and `review_summary`, and clarifies when static/mock evidence capture and real local-lab diagnostic evidence capture should begin.

It is package design only. It does not generate applied evidence packages, implement new scanner execution, create runnable configuration, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/100-v0623-aaef-applied-evidence-package-design.md`.

## v0.6.24 Applied Evidence Scenario Set Planning

AAEF-AI-VA includes a v0.6.24 applied evidence scenario set planning checkpoint.

This checkpoint defines the four minimum scenarios for the AAEF applied evidence package: `permitted-safe-diagnostic`, `denied-out-of-scope-request`, `human-approval-required`, and `not-executed-expired`. It records scenario intent, expected decision posture, dispatch posture, result posture, evidence posture, reviewer focus, AAEF five-questions coverage, and non-proof boundaries before static/mock evidence package generation begins.

It is scenario set planning only. It does not generate applied evidence packages, generate fixture files, run scanners, create runnable configuration, authorize Docker execution, authorize runtime execution, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/101-v0624-applied-evidence-scenario-set-planning.md`.

## v0.6.25 Static Applied Evidence Fixture Planning

AAEF-AI-VA includes a v0.6.25 static applied evidence fixture planning checkpoint.

This checkpoint defines the static fixture plan for the four applied evidence scenarios: `permitted-safe-diagnostic`, `denied-out-of-scope-request`, `human-approval-required`, and `not-executed-expired`. It plans the static artifact files for `tool_action_request`, `gate_decision`, `dispatch_decision`, `execution_result` or `non_execution_result`, `evidence_event`, and `review_summary` before any fixture generation, package generation, local-lab diagnostic execution, or delivery authorization begins.

It is fixture planning only. It does not generate fixture files, generate applied evidence packages, run scanners, create runnable configuration, authorize Docker execution, authorize runtime execution, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

See `docs/102-v0625-static-applied-evidence-fixture-planning.md`.
