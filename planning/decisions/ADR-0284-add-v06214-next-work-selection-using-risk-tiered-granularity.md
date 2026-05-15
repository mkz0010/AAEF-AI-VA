# ADR-0284: Add v0.6.214 next work selection using risk-tiered granularity

Status: Accepted

## Context

v0.6.213 accepted the Gateway Core Safety Integration Plan for implementation planning.

The first staging item in that plan is mock/dry-run completed status terminology cleanup.

The project needs a direction-selection checkpoint before changing status terminology, generated outputs, examples, tests, or documentation.

## Decision

Add v0.6.214 as a direction-selection checkpoint.

v0.6.214 selects:

- selected_next_work_item = mock_dry_run_completed_status_terminology_cleanup
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.215 Mock/Dry-run Completed Status Terminology Cleanup Candidate
- selected_followup_checkpoint = v0.6.216 Mock/Dry-run Completed Status Terminology Cleanup Review and Decision

## Rationale

The word `completed` can imply real tool execution when the current Gateway path is mock/dry-run/non-execution oriented.

This issue should be addressed before deeper Gateway core enforcement work because it affects reviewer interpretation of results and evidence traces.

## Consequences

v0.6.214 does not rename execution statuses.

v0.6.214 does not change Tool Gateway behavior, adapter behavior, schemas, validators, fixtures, runtime behavior, or scanner behavior.

The terminology cleanup candidate is deferred to v0.6.215.

Review and acceptance are deferred to v0.6.216.

Runtime demo remains necessary but deferred.

Publication remains deferred.
