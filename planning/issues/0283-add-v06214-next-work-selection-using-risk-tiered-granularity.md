# Issue 0283: Add v0.6.214 next work selection using risk-tiered granularity

Status: Closed by v0.6.214

## Summary

Select the first implementation work item under the accepted Gateway Core Safety Integration Plan.

## Selected work item

- selected_next_work_item = mock_dry_run_completed_status_terminology_cleanup
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.215 Mock/Dry-run Completed Status Terminology Cleanup Candidate
- selected_followup_checkpoint = v0.6.216 Mock/Dry-run Completed Status Terminology Cleanup Review and Decision

## Acceptance criteria

- [x] Add v0.6.214 direction-selection document.
- [x] Add ADR record.
- [x] Add planning issue record.
- [x] Select mock/dry-run completed status terminology cleanup as the next work item.
- [x] Record risk tier as high.
- [x] Record v0.6.215 as the candidate checkpoint.
- [x] Record v0.6.216 as the review and decision checkpoint.
- [x] Confirm that v0.6.214 does not rename execution statuses.
- [x] Add local test coverage for the v0.6.214 selection boundary.
- [x] Register the local test in `tools/run_all_local_checks.py`.
- [x] Update README, CHANGELOG, and ROADMAP.

## Non-goals

This issue does not implement Gateway core safety controls, change Tool Gateway behavior, change adapter behavior, rename statuses, change schemas, change validators, change fixtures, create runtime demo capability, approve scanner readiness, approve publication, approve a social post, or create commercial terms.
