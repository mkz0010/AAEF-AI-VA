# Issue 0290: Add v0.6.221 Next Work Selection Using Risk-Tiered Granularity

Status: Closed by v0.6.221

## Summary

Select the first concrete work item under the accepted AAEF Applied Evidence Minimum Flow Plan.

## Selected work item

- selected_next_work_item = existing_element_inventory
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.222 Existing Element Inventory Candidate
- selected_followup_checkpoint = v0.6.223 Existing Element Inventory Review and Decision

## Deferred work items

- deferred_work_item = public_exposure_cleanup_work
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

## Acceptance criteria

- [x] Add v0.6.221 direction-selection document.
- [x] Add ADR record.
- [x] Add planning issue record.
- [x] Select existing element inventory as the next work item.
- [x] Record risk tier as high.
- [x] Record v0.6.222 as the candidate checkpoint.
- [x] Record v0.6.223 as the review and decision checkpoint.
- [x] Confirm that no existing element inventory is created in v0.6.221.
- [x] Confirm that no fixtures are created or modified in v0.6.221.
- [x] Confirm that no Gateway behavior is changed in v0.6.221.
- [x] Add local test coverage for the v0.6.221 selection boundary.
- [x] Register the local test in `tools/run_all_local_checks.py`.
- [x] Update README, CHANGELOG, and ROADMAP.

## Non-goals

This issue does not create existing element inventory, create minimum flow package artifacts, create or modify fixtures, create reviewer walkthrough content, create AAEF handback summary, rewrite README, apply public cleanup, change Tool Gateway behavior, create runtime demo capability, approve scanner readiness, approve publication, approve a social post, or create commercial terms.
