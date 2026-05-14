# v0.6.205 Next Work Selection Using Risk-Tiered Granularity

Status: Accepted direction-selection checkpoint

## Purpose

This checkpoint records the next work selection after v0.6.204 using risk-tiered granularity.

v0.6.205 is intentionally narrow. It selects the next work item and records the checkpoint split. It does not create or apply the selected integration plan.

## Baseline carried forward

The latest completed checkpoint before this document is v0.6.204.

v0.6.204 accepted the Static Fixture Review Path Public Communication Pack for repository wording use only.

The following boundaries remain in force:

- publication remains deferred
- no external announcement is approved
- no social-post instruction is approved
- no runtime execution is added
- no scanner readiness is added
- no customer PoC readiness is added
- no production readiness is claimed
- no certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence is claimed

## Selected next work item

The selected next work item is recorded as follows:

- selected_next_work_item = static_fixture_review_path_repository_wording_integration_plan
- selected_next_work_item_risk_tier = medium
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.206 Static Fixture Review Path Repository Wording Integration Plan Candidate
- selected_followup_checkpoint = v0.6.207 Static Fixture Review Path Repository Wording Integration Plan Review and Decision

## Why this work item is selected

v0.6.204 made the communication pack acceptable for repository wording use, but it did not decide where or how to integrate that wording across repository-facing documents.

The next useful step is to plan a bounded repository wording integration path.

This should be treated as Medium-risk because repository-facing wording can be mistaken for broader readiness, publication approval, scanner capability, customer delivery, or external assurance claims.

## Why the work is split into two checkpoints

The selected work item is split into two checkpoints:

1. v0.6.206 creates a candidate repository wording integration plan.
2. v0.6.207 reviews the candidate, accepts or rejects it, and records the decision.

This preserves a review boundary before any integration plan is treated as accepted.

## Scope of the selected v0.6.206 candidate

The v0.6.206 candidate may propose:

- target repository-facing documents for wording alignment
- exact intended purpose of each target surface
- insertion or replacement boundaries
- wording reuse rules from v0.6.204
- claim-boundary checklist
- terms and labels to avoid
- review requirements before any actual wording integration
- a no-publication reminder

## Explicit non-goals for v0.6.205

v0.6.205 does not create the repository wording integration plan body.

v0.6.205 does not:

- apply accepted wording to repository-facing documents
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

The selected next work item must preserve that boundary in any repository wording integration plan.

## Acceptance criteria

This checkpoint is accepted when:

- the selected next work item is explicitly recorded
- the selected risk tier is recorded as Medium
- the two-checkpoint split is recorded
- v0.6.206 is identified as the candidate checkpoint
- v0.6.207 is identified as the review and decision checkpoint
- the checkpoint states that the integration plan body is not created in v0.6.205
- the checkpoint preserves the v0.6.204 publication-deferred boundary
