# ADR-0271: Add v0.6.201 next work selection using risk-tiered granularity

Status: Accepted

## Context

v0.6.200 accepted the decision to continue using `Static Fixture Review Path` as the safer public-facing phrase for the repository's static, mock, fixture-only, non-execution, reviewer-facing path.

The repository now needs a next work item that improves public explainability without changing the execution boundary.

## Decision

Add v0.6.201 as a direction-selection checkpoint.

v0.6.201 selects:

- selected_next_work_item = static_fixture_review_path_public_communication_pack
- selected_next_work_item_risk_tier = medium
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.202 Static Fixture Review Path Public Communication Pack Candidate
- selected_followup_checkpoint = v0.6.203 Static Fixture Review Path Public Communication Pack Review and Decision

## Rationale

Public-facing language is useful but can easily overstate project readiness.

A two-checkpoint split keeps candidate wording separate from accepted wording.

This supports a conservative progression:

1. select the work
2. draft the candidate
3. review and decide

## Consequences

v0.6.201 does not create the communication pack body.

The communication pack candidate is deferred to v0.6.202.

Review and acceptance are deferred to v0.6.203.

The current repository boundary remains static, mock, fixture-only, non-execution, and reviewer-facing.
