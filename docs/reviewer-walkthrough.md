# Reviewer Walkthrough

Status: candidate
Version: v0.6.155
Date: 2026-05-11

## Reader

This walkthrough is for enterprise reviewers, vulnerability assessment company decision-makers, security architects, technical due-diligence reviewers, project sponsors, and maintainers who need a safe reading path through AAEF-AI-VA.

## Purpose

The purpose of this walkthrough is to explain how to read the current AAEF-AI-VA review package in a safe order.

Core boundary proposition:

~~~text
AI output is a request; gates decide execution.
~~~

The walkthrough helps reviewers understand where to start, which documents to inspect, which tests support the review surface, and which interpretations are explicitly out of scope.

## Non-authorizing notice

This walkthrough does not authorize a PoC.

This walkthrough does not approve runtime execution.

This walkthrough does not approve scanner execution.

This walkthrough does not grant permission to test any system.

This walkthrough does not create a commercial contract.

This walkthrough does not approve customer delivery.

This walkthrough does not replace legal, commercial, risk-owner, asset-owner, or customer authorization review.

## Suggested reading sequence

Recommended order:

1. `README.md`
2. `docs/enterprise-review-guide.md`
3. `docs/technical-due-diligence-summary.md`
4. `docs/safe-poc-boundary-template.md`
5. `docs/control-matrix.md`
6. Relevant test families under `tools/`
7. Current version records under `docs/`

This order starts with public positioning, moves to enterprise and technical review, then reviews PoC boundary constraints, then uses the Control Matrix to locate control boundaries and evidence expectations.

## First-pass review path

A first-pass reviewer should answer:

| Step | Artifact | Question |
| --- | --- | --- |
| 1 | `README.md` | What does the repository claim, and what does it not claim? |
| 2 | `docs/enterprise-review-guide.md` | What concerns should an enterprise reviewer inspect first? |
| 3 | `docs/technical-due-diligence-summary.md` | What technical boundaries and evidence paths are reviewable? |
| 4 | `docs/safe-poc-boundary-template.md` | What would a separately approved controlled PoC need before any real action? |
| 5 | `docs/control-matrix.md` | Which rows map review questions to boundaries, evidence, artifacts, non-goals, and notes? |

The first-pass review should end with a list of open questions, not with approval to run anything.

## Technical due-diligence review path

A technical due-diligence reviewer should inspect:

* AI request boundary,
* gate decision boundary,
* current-time authorization expiry,
* request/decision constraint drift,
* external discovery fail-closed behavior,
* mock/dry-run status disambiguation,
* non-execution evidence,
* human approval,
* credential/data handling,
* public/private artifact boundary,
* report and delivery boundary.

Recommended supporting tests include:

* `tools/test_authorization_expiry_current_time_check.py`,
* `tools/test_request_decision_constraint_diff_enforcement.py`,
* `tools/test_external_discovery_fail_closed_behavior.py`,
* `tools/test_mock_dry_run_completed_status_terminology.py`,
* `tools/test_human_approval_gate.py`,
* `tools/test_evidence_chain_linkage.py`,
* `tools/test_delivery_authorization_gate.py`,
* publication hygiene and public repository readiness tests.

The reviewer should inspect test results as evidence of local boundary behavior, not as production readiness.

## PoC-boundary review path

A PoC-boundary reviewer should inspect `docs/safe-poc-boundary-template.md`.

The reviewer should verify that the template requires:

* written authorization,
* parties and responsibilities,
* target scope,
* excluded systems,
* time window,
* tool and action limits,
* AI request and gate boundary,
* credential and data handling,
* evidence retention and deletion,
* human review and approval,
* stop conditions,
* communications and escalation,
* deliverables boundary,
* commercial and license boundary,
* pre-PoC review checklist,
* not-allowed section,
* claim boundaries.

A completed template should not be treated as permission. Separate written authorization would still be required.

## Control Matrix review path

A reviewer should use `docs/control-matrix.md` to trace:

* review question,
* control boundary,
* expected evidence,
* related artifacts,
* explicit non-goal,
* reviewer note.

The Control Matrix should be used to find boundaries and overclaims.

It should not be used as a compliance matrix, audit checklist, certification checklist, production readiness checklist, or external-framework equivalence mapping.

## Evidence and test-family inspection path

A reviewer may inspect these evidence/test-family groups:

| Group | Review purpose |
| --- | --- |
| Tool Gateway tests | Gate outcome and request/decision handling. |
| Authorization expiry tests | Current-time authorization boundary. |
| Constraint-diff tests | Request/decision drift boundary. |
| External discovery tests | External target expansion fail-closed behavior. |
| Mock/dry-run status tests | Status interpretation boundary. |
| Evidence chain tests | Evidence linkage and non-execution reviewability. |
| Human approval tests | Action-bound human review behavior. |
| Report and delivery gate tests | Separation of findings, reports, packets, and delivery. |
| Publication hygiene tests | Public/private artifact separation. |
| License/commercial boundary tests | Commercial-use and license interpretation boundaries. |

These tests support reviewability. They do not grant operational permission.

## Claim-boundary inspection path

A reviewer should explicitly check that the repository does not claim:

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

The reviewer should also check that AI-generated text is not treated as execution authority.

## Questions before asking for a PoC

Before asking for a PoC, reviewers should answer:

| Question | Expected answer type |
| --- | --- |
| What problem is the review trying to solve? | Evaluation purpose |
| Which boundary is most important: authority, evidence, scope, credential, delivery, or commercial? | Priority |
| Which target class would be considered later: lab, localhost, owned asset, or customer asset? | Target class |
| Which actions are explicitly out of scope? | Exclusions |
| Who owns risk acceptance? | Named role |
| Who owns asset authorization? | Named role |
| Who reviews legal/commercial terms? | Named role |
| What evidence can be retained? | Retention rule |
| What would stop the review? | Stop conditions |
| What output is allowed? | Delivery boundary |

These questions prepare a review conversation. They do not authorize testing.

## Reviewer outputs

Appropriate reviewer outputs include:

* review notes,
* open questions,
* requested evidence list,
* requested clarification list,
* PoC boundary questions,
* claim-boundary concerns,
* commercial/license questions,
* recommendation for further review.

Inappropriate reviewer outputs include:

* operational approval,
* scanner execution approval,
* credential injection approval,
* customer target approval,
* production readiness approval,
* legal compliance determination,
* audit opinion,
* certification statement.

## Interpretation limits

This walkthrough is intentionally narrow.

It helps reviewers navigate documents and tests.

It does not operate tools, approve testing, approve customer delivery, create commercial terms, or determine legal/audit/compliance sufficiency.

## Explicit non-goals

This walkthrough is not:

* an onboarding runbook,
* a deployment guide,
* a scanner operation guide,
* a customer PoC authorization record,
* a commercial contract,
* a legal review,
* an audit procedure,
* a certification package,
* a production readiness review,
* an external-framework equivalence mapping,
* an AAEF main handback submission.

## Claim boundaries

This walkthrough must remain conservative.

Do not interpret this walkthrough as:

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
AAEF-AI-VA provides a reviewer-facing walkthrough for safely navigating its current documentation and evidence-boundary package without authorizing real-world action.
~~~
