# ADR-0285: Add v0.6.215 External Review Public Exposure and Commercial Boundary Reassessment

Status: Accepted

## Context

v0.6.214 selected `mock_dry_run_completed_status_terminology_cleanup` as the first high-risk implementation work item under the accepted Gateway Core Safety Integration Plan.

A later external review raised urgent public exposure and commercial boundary concerns, including README positioning, personal contact exposure, pricing draft exposure, business-plan exposure, external-facing status labels, version clarity, and documentation curation.

## Decision

Add v0.6.215 as a public exposure and commercial boundary reassessment checkpoint.

The immediate next work item is changed to:

- selected_next_work_item = public_exposure_hygiene_plan
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.216 Public Exposure Hygiene Plan Candidate
- selected_followup_checkpoint = v0.6.217 Public Exposure Hygiene Plan Review and Decision

The previously selected Gateway terminology cleanup work is deferred, not rejected.

## Rationale

Public repository hygiene and commercial boundary exposure can affect trust, negotiation posture, and enterprise credibility before runtime or Gateway implementation maturity is evaluated.

It is safer to plan public exposure cleanup before continuing implementation-facing Gateway work.

## Consequences

v0.6.215 does not remove contact routes, move pricing files, move business-plan files, rewrite README, delete docs, rename statuses, or change Tool Gateway behavior.

A separate plan candidate is required in v0.6.216.

Runtime demo remains necessary but deferred.

Publication remains deferred.
