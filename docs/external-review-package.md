# External Review Package

Status: candidate
Version: v0.6.158
Date: 2026-05-11

## Reader

This package is for enterprise reviewers, vulnerability assessment company decision-makers, security architects, technical due-diligence reviewers, project sponsors, maintainers, and commercial reviewers who need one safe entry point into AAEF-AI-VA.

## Purpose

The purpose of this package is to integrate the current external-review-facing materials into a single navigation and boundary artifact.

Core boundary proposition:

~~~text
AI output is a request; gates decide execution.
~~~

This package helps reviewers understand which documents exist, where to start, which paths to follow, what evidence/test families support the review surface, and what the repository does not claim.

## Non-authorizing notice

This package does not authorize a PoC.

This package does not approve runtime execution.

This package does not approve scanner execution.

This package does not grant permission to test any system.

This package does not create a commercial contract.

This package does not approve customer delivery.

This package does not replace legal, commercial, risk-owner, asset-owner, customer, or delivery authorization review.

## Document inventory

| Artifact | Role in review |
| --- | --- |
| `README.md` | Public entry point, baseline positioning, and claim boundaries. |
| `docs/enterprise-review-guide.md` | Executive and enterprise reviewer concerns. |
| `docs/technical-due-diligence-summary.md` | Technical review summary for boundaries and evidence. |
| `docs/safe-poc-boundary-template.md` | Non-authorizing template for future controlled PoC boundary information. |
| `docs/control-matrix.md` | Matrix of review questions, boundaries, evidence, artifacts, non-goals, and notes. |
| `docs/reviewer-walkthrough.md` | Safe reading path through the package. |
| `tools/run_all_local_checks.py` | Local validation entry point for review-oriented checks. |
| Versioned records under `docs/` | Historical decision and checkpoint evidence. |

## Recommended entry points

| Reviewer type | Start here | Then read |
| --- | --- | --- |
| Executive sponsor | `README.md` | Enterprise Review Guide, Reviewer Walkthrough, Control Matrix |
| Technical due-diligence reviewer | Technical Due Diligence Summary | Control Matrix, relevant test families, Reviewer Walkthrough |
| PoC-boundary reviewer | Safe PoC Boundary Template | Reviewer Walkthrough, Control Matrix |
| Commercial reviewer | README and Safe PoC Boundary Template | licensing/commercial boundary sections, Reviewer Walkthrough |
| Maintainer | Reviewer Walkthrough | Control Matrix, versioned records, tests |

## Reviewer paths

Use the package in one of these paths:

1. First-pass package review.
2. Technical due-diligence review.
3. PoC-boundary review.
4. Control-boundary review.
5. Evidence/test-family review.
6. Claim-boundary review.
7. Commercial/license-boundary review.

Each path is for review and interpretation only. None of the paths grants operational permission.

## Evidence and test-family index

| Test family | Review purpose |
| --- | --- |
| Tool Gateway and runner tests | Request/decision/gate behavior. |
| Authorization expiry tests | Current-time expiry behavior. |
| Request/decision constraint-diff tests | Constraint drift review. |
| External discovery fail-closed tests | External target expansion boundary. |
| Mock/dry-run status tests | Non-real-execution status clarity. |
| Evidence chain and reconstruction tests | Evidence linkage and reviewer traceability. |
| Human approval gate tests | Action-bound human review. |
| Finding/report/packet/delivery gate tests | Separation of candidate, report, packet, and delivery approval states. |
| Runtime readiness and execution authorization tests | Runtime remains blocked unless separately reviewed. |
| Publication hygiene tests | Public/private artifact boundary. |
| Licensing and commercial-use boundary tests | License and commercial-use interpretation boundaries. |
| Version-specific review tests | Checkpoint-specific claim-boundary and continuity checks. |

These tests support reviewability. They do not grant operational permission.

## Boundary and non-goal summary

| Boundary | Package interpretation |
| --- | --- |
| AI request | AI text can request an action but is not execution authority. |
| Gate decision | Gates decide allowed, blocked, or review-required states. |
| Human review | Human review is action-bound and evidence-linked. |
| Credential handling | Secrets should not be exposed in AI-visible or public artifacts. |
| Evidence | Evidence supports reviewability and reconstruction. |
| PoC boundary | PoC planning requires separate written authorization. |
| Delivery | Customer delivery requires separate delivery authorization. |
| Commercial use | Commercial terms require separate agreement or review. |
| Public/private split | Public artifacts should not expose sensitive operational details. |
| Claim boundary | The package should help locate boundaries, not make overclaims. |

## Package-level claim-boundary summary

This package does not claim:

* certification,
* legal compliance,
* audit opinion,
* audit sufficiency,
* production readiness,
* production scanner status,
* diagnostic completeness,
* authorization for third-party testing,
* customer PoC approval,
* commercial contract creation,
* customer delivery approval,
* equivalence with external frameworks,
* AAEF Core/Profile/Practical Package promotion.

## Questions this package can answer

This package can help answer:

* What is AAEF-AI-VA trying to demonstrate?
* How does it separate AI requests from execution authority?
* Where are gate decisions and evidence boundaries discussed?
* Which documents should an external reviewer read first?
* Which tests are relevant to boundary review?
* What would need to be defined before any future controlled PoC could be considered?
* Which interpretations are explicitly out of scope?

## Questions this package cannot answer

This package cannot answer:

* Whether a customer target may be tested.
* Whether runtime execution may occur.
* Whether scanner execution may occur.
* Whether credentials may be injected.
* Whether customer delivery may occur.
* Whether legal compliance has been achieved.
* Whether an audit opinion exists.
* Whether production readiness has been established.
* Whether the project is diagnostically complete.
* Whether it is equivalent to an external framework.

Those questions require separate authorization, legal/commercial review, technical review, or scope-specific evidence outside this public package.

## When to use the Safe PoC Boundary Template

Use `docs/safe-poc-boundary-template.md` when a reviewer needs to understand which boundary fields would be required before a future controlled PoC could even be considered.

Use it to identify missing information.

Do not use it as permission.

A completed template should still require separate written authorization, commercial/legal review, environment approval, tool approval, credential approval, evidence handling approval, human-review approval, and stop-condition approval.

## When not to request a PoC

Do not request a PoC when:

* asset ownership is unclear,
* authorization is unclear,
* target scope is unclear,
* excluded systems are unclear,
* time window is unclear,
* credential handling is unclear,
* evidence retention is unclear,
* stop conditions are unclear,
* commercial or legal basis is unclear,
* reviewer outputs are still open questions,
* the request would require production, third-party, or customer testing without separate written authorization.

## What remains outside the public package

The public package does not include:

* customer-specific targets,
* customer credentials,
* customer contracts,
* commercial license terms,
* paid engagement materials,
* private generated outputs,
* raw scanner outputs,
* operational playbooks for customer delivery,
* patent-sensitive browser-state intelligence details,
* NDA materials,
* authorization to test third-party systems.

## Explicit non-goals

This package is not:

* a deployment guide,
* a scanner operation guide,
* a customer PoC authorization package,
* a commercial contract,
* a legal review,
* an audit package,
* a certification package,
* a production readiness package,
* a diagnostic-completeness claim,
* an external-framework equivalence mapping,
* an AAEF main handback submission.

## Claim boundaries

This package must remain conservative.

Do not interpret this package as:

* customer authorization,
* commercial contract,
* legal compliance determination,
* audit opinion,
* audit sufficiency determination,
* deployment approval,
* complete vulnerability assessment capability,
* permission for testing third-party systems,
* equivalence mapping to external frameworks,
* production readiness claim,
* proof that gate-free AI tool execution is acceptable,
* promotion of AAEF-AI-VA into AAEF Core, Profile, or Practical Package status.

Allowed interpretation:

~~~text
AAEF-AI-VA provides a public external-review package for navigating its safety-first documentation and evidence-boundary materials without authorizing real-world action.
~~~
