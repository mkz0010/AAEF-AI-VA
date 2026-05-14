# ADR-0275: Add v0.6.205 next work selection using risk-tiered granularity

Status: Accepted

## Context

v0.6.204 accepted the Static Fixture Review Path Public Communication Pack for repository wording use only.

That decision did not publish the communication pack, approve a social post, create a public announcement, or authorize runtime/scanner/customer PoC readiness.

The repository now needs a next work item that plans where accepted wording may be integrated without making broader claims.

## Decision

Add v0.6.205 as a direction-selection checkpoint.

v0.6.205 selects:

- selected_next_work_item = static_fixture_review_path_repository_wording_integration_plan
- selected_next_work_item_risk_tier = medium
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.206 Static Fixture Review Path Repository Wording Integration Plan Candidate
- selected_followup_checkpoint = v0.6.207 Static Fixture Review Path Repository Wording Integration Plan Review and Decision

## Rationale

Repository-facing wording can affect reader expectations.

A two-checkpoint split keeps candidate integration planning separate from accepted integration planning.

This supports a conservative progression:

1. select the work
2. draft the candidate plan
3. review and decide

## Consequences

v0.6.205 does not create the integration plan body.

The integration plan candidate is deferred to v0.6.206.

Review and acceptance are deferred to v0.6.207.

The current repository boundary remains static, mock, fixture-only, non-execution, reviewer-facing, and publication-deferred.
