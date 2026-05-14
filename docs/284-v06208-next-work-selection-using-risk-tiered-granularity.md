# v0.6.208 Next Work Selection Using Risk-Tiered Granularity

Status: Accepted direction-selection checkpoint

## Purpose

This checkpoint records the next work selection after v0.6.207 using risk-tiered granularity.

v0.6.208 is intentionally narrow. It selects the next work item and records the checkpoint split. It does not apply repository wording changes.

## Baseline carried forward

The latest completed checkpoint before this document is v0.6.207.

v0.6.207 accepted the Static Fixture Review Path Repository Wording Integration Plan for future integration planning only.

The following boundaries remain in force:

- repository wording changes remain not applied
- publication remains deferred
- no publication approval is granted
- no external announcement is approved
- no social-post instruction is approved
- no runtime execution is added
- no scanner readiness is added
- no customer PoC readiness is added
- no production readiness is claimed
- no certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence is claimed

## Selected next work item

The selected next work item is recorded as follows:

- selected_next_work_item = static_fixture_review_path_repository_wording_integration_implementation_candidate
- selected_next_work_item_risk_tier = medium
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.209 Static Fixture Review Path Repository Wording Integration Implementation Candidate
- selected_followup_checkpoint = v0.6.210 Static Fixture Review Path Repository Wording Integration Implementation Review and Decision

## Why this work item is selected

v0.6.207 accepted the integration plan for future planning, but no repository wording changes have been applied.

The next useful step is to create a bounded implementation candidate that applies the accepted plan to repository-facing surfaces only if the edits remain narrow, reviewable, and boundary-preserving.

This should be treated as Medium-risk because repository-facing wording can change reader expectations and may accidentally imply publication approval, demo readiness, scanner readiness, customer delivery readiness, or broader assurance claims.

## Why the work is split into two checkpoints

The selected work item is split into two checkpoints:

1. v0.6.209 creates a repository wording integration implementation candidate.
2. v0.6.210 reviews the implementation candidate, accepts or rejects it, and records the decision.

This preserves a review boundary before candidate wording changes are treated as accepted.

## Scope of the selected v0.6.209 candidate

The v0.6.209 candidate may propose and apply narrow candidate wording changes to selected repository-facing documents.

The candidate may cover only surfaces accepted by v0.6.207:

- `README.md`
- `docs/repository-landing-demo-path-clarity.md`
- `docs/examples/safe-demo/blocked-tool-action-request-review/reviewer-walkthrough.md`
- `docs/examples/safe-demo/blocked-tool-action-request-review/`
- `ROADMAP.md`

The v0.6.209 candidate must keep changes limited to repository wording integration and boundary reinforcement.

## Required v0.6.209 constraints

The v0.6.209 candidate must preserve the following constraints:

- use `Static Fixture Review Path` as the preferred label
- preserve static, mock, fixture-only, non-execution wording
- preserve reviewer-facing framing
- preserve `AI output is a request, not authority`
- preserve gate decision and execution separation
- preserve non-execution evidence visibility
- preserve publication-deferred status
- avoid public announcement or social-post approval
- avoid runtime, scanner, and customer PoC readiness claims
- avoid production, certification, legal, audit, diagnostic-completeness, and external-framework-equivalence claims
- avoid schema or validator behavior changes unless separately selected in a later checkpoint
- avoid new fixture files unless separately selected in a later checkpoint

## Explicit non-goals for v0.6.208

v0.6.208 does not:

- apply repository wording changes
- create an implementation candidate body
- publish a public announcement
- approve a social post
- create a release announcement
- create a new fixture file
- create a public sample
- create an executable demo
- add runtime execution
- add scanner readiness
- authorize real scanner execution
- authorize customer PoC intake
- create AAEF main publication material
- create an AAEF main issue, PR, command, or URL
- create commercial contract terms
- create paid engagement approval
- create customer-specific material
- change validator behavior
- add a JSON Schema
- authorize runtime, scanner, Docker, sensitive-value, customer, or delivery activity
- promote this project into AAEF Core, Profile, or Practical Package

## Claim boundary retained

This checkpoint retains the core boundary:

AI output is a request, not authority. Execution is decided by gates. Evidence links request, gate decision, execution or non-execution, and review result.

The selected next work item must preserve that boundary in any repository wording integration implementation candidate.

## Acceptance criteria

This checkpoint is accepted when:

- the selected next work item is explicitly recorded
- the selected risk tier is recorded as Medium
- the two-checkpoint split is recorded
- v0.6.209 is identified as the candidate checkpoint
- v0.6.210 is identified as the review and decision checkpoint
- the checkpoint states that repository wording changes are not applied in v0.6.208
- the checkpoint preserves the v0.6.207 not-applied and publication-deferred boundaries
