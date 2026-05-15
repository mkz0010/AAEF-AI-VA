# Issue 0296: Add v0.6.227 Next Work Selection Using Risk-Tiered Granularity

Status: Closed by v0.6.227

## Summary

Select the next concrete work item after the accepted Minimum Flow Scenario Matrix.

## Selected work item

- selected_next_work_item = evidence_linkage_table
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.228 Evidence Linkage Table Candidate
- selected_followup_checkpoint = v0.6.229 Evidence Linkage Table Review and Decision

## Deferred work items

- deferred_work_item = public_exposure_cleanup_work
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

## Acceptance criteria

- [x] Add v0.6.227 direction-selection document.
- [x] Add ADR record.
- [x] Add planning issue record.
- [x] Select evidence linkage table as the next work item.
- [x] Record risk tier as high.
- [x] Record v0.6.228 as the candidate checkpoint.
- [x] Record v0.6.229 as the review and decision checkpoint.
- [x] Confirm that no evidence linkage table is created in v0.6.227.
- [x] Confirm that no fixtures are created or modified in v0.6.227.
- [x] Confirm that no Gateway behavior is changed in v0.6.227.
- [x] Add local test coverage for the v0.6.227 selection boundary.
- [x] Register the local test in `tools/run_all_local_checks.py`.
- [x] Update README, CHANGELOG, and ROADMAP.

## Non-goals

This issue does not create an evidence linkage table, create minimum flow package artifacts, create or modify fixtures, create reviewer walkthrough content, create AAEF handback summary, rewrite README, apply public cleanup, change Tool Gateway behavior, create runtime demo capability, approve scanner readiness, approve publication, approve a social post, or create commercial terms.
