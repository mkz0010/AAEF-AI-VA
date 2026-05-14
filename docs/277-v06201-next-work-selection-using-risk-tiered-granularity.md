# v0.6.201 Next Work Selection Using Risk-Tiered Granularity

Status: Accepted direction-selection checkpoint

## Purpose

This checkpoint records the next work selection after v0.6.200 using risk-tiered granularity.

v0.6.201 is intentionally narrow. It selects the next work item and records the checkpoint split. It does not create the selected communication materials.

## Baseline carried forward

The latest completed checkpoint before this document is v0.6.200.

v0.6.200 accepted the decision that the repository should continue to use the phrase `Static Fixture Review Path` for the public-facing review path.

The accepted fixture path remains:

- static
- mock
- fixture-only
- non-execution
- reviewer-facing
- publicly reviewable as a static fixture set

## Selected next work item

The selected next work item is recorded as follows:

- selected_next_work_item = static_fixture_review_path_public_communication_pack
- selected_next_work_item_risk_tier = medium
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.202 Static Fixture Review Path Public Communication Pack Candidate
- selected_followup_checkpoint = v0.6.203 Static Fixture Review Path Public Communication Pack Review and Decision

## Why this work item is selected

The repository now has an accepted static fixture review path and an accepted wording boundary.

The next useful step is to prepare a minimal public communication pack that explains the accepted phrase without expanding the project into execution, scanning, customer delivery, production assurance, or external-framework equivalence.

This is Medium-risk because public-facing wording can accidentally create stronger claims than the repository currently supports.

## Why the work is split into two checkpoints

The selected work item is split into two checkpoints:

1. v0.6.202 creates a candidate communication pack.
2. v0.6.203 reviews the candidate, accepts or rejects it, and records the decision.

This preserves a review boundary before any wording is treated as accepted.

## Scope of the selected v0.6.202 candidate

The v0.6.202 candidate may propose:

- short public description
- medium public description
- README-compatible summary
- social-post-style draft that is not published
- approved wording around `Static Fixture Review Path`
- terms to avoid
- required boundary sentences
- reviewer path summary

## Explicit non-goals for v0.6.201

v0.6.201 does not create the communication pack body.

v0.6.201 does not:

- publish a public announcement
- create a new fixture file
- create a public sample
- create a safe demo
- create an executable demo
- add runtime execution
- add scanner readiness
- select real scanner execution
- select customer PoC intake
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

The selected next work item must preserve that boundary in public-facing wording.

## Acceptance criteria

This checkpoint is accepted when:

- the selected next work item is explicitly recorded
- the selected risk tier is recorded as Medium
- the two-checkpoint split is recorded
- v0.6.202 is identified as the candidate checkpoint
- v0.6.203 is identified as the review and decision checkpoint
- the checkpoint states that the communication pack body is not created in v0.6.201
- the checkpoint preserves the `Static Fixture Review Path` wording boundary
