# ADR-0278: Add v0.6.208 next work selection using risk-tiered granularity

Status: Accepted

## Context

v0.6.207 accepted the Static Fixture Review Path Repository Wording Integration Plan for future integration planning only.

That decision did not apply repository wording changes, approve publication, approve a social post, or authorize runtime/scanner/customer PoC readiness.

The repository now needs a next work item that can prepare a bounded implementation candidate while preserving the review boundary.

## Decision

Add v0.6.208 as a direction-selection checkpoint.

v0.6.208 selects:

- selected_next_work_item = static_fixture_review_path_repository_wording_integration_implementation_candidate
- selected_next_work_item_risk_tier = medium
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.209 Static Fixture Review Path Repository Wording Integration Implementation Candidate
- selected_followup_checkpoint = v0.6.210 Static Fixture Review Path Repository Wording Integration Implementation Review and Decision

## Rationale

Repository wording changes can affect reader expectations.

A two-checkpoint split keeps implementation candidate work separate from accepted repository wording integration.

This supports a conservative progression:

1. select the work
2. create the implementation candidate
3. review and decide

## Consequences

v0.6.208 does not apply repository wording changes.

The implementation candidate is deferred to v0.6.209.

Review and acceptance are deferred to v0.6.210.

The current repository boundary remains static, mock, fixture-only, non-execution, reviewer-facing, not-applied, and publication-deferred.
