# Issue 0287: Add v0.6.218 AAEF Applied Evidence Minimum Flow Intake and Priority Reconciliation

Status: Closed by v0.6.218 intake and priority reconciliation checkpoint

## Summary

Record AAEF main feedback and select AAEF Applied Evidence Minimum Flow planning as the immediate next priority.

## Selected work item

- selected_next_work_item = aaef_applied_evidence_minimum_flow_plan
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.219 AAEF Applied Evidence Minimum Flow Plan Candidate
- selected_followup_checkpoint = v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision

## Deferred work items

- deferred_work_item = public_exposure_cleanup_work
- deferred_reason = aaef_main_applied_evidence_minimum_flow_priority
- deferred_return_condition = aaef_applied_evidence_minimum_flow_plan_reviewed_and_decided

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = aaef_main_applied_evidence_minimum_flow_priority
- deferred_return_condition = aaef_applied_evidence_minimum_flow_plan_reviewed_and_decided

## Acceptance criteria

- [x] Record AAEF main feedback.
- [x] Preserve v0.6.217 Public Exposure Hygiene Plan as valid but deferred.
- [x] Select AAEF Applied Evidence Minimum Flow planning as the next priority.
- [x] Record v0.6.219 as the plan candidate checkpoint.
- [x] Record v0.6.220 as the plan review and decision checkpoint.
- [x] Record minimum flow elements.
- [x] Record four-scenario matrix requirement.
- [x] Record evidence linkage table requirement.
- [x] Record AAEF five questions mapping requirement.
- [x] Record evidence trust boundary requirement.
- [x] Record AAEF handback summary requirement.
- [x] Record no fixture, runtime, Gateway, cleanup, or README changes in v0.6.218.
- [x] Add local test coverage for the intake boundary.
- [x] Register the local test in `tools/run_all_local_checks.py`.
- [x] Update README, CHANGELOG, and ROADMAP.

## Non-goals

This issue does not create fixtures, change fixtures, create reviewer walkthrough content, create AAEF handback summary, move commercial materials, rewrite README, delete docs, create runtime demo capability, rename statuses, change Tool Gateway behavior, approve scanner readiness, approve publication, approve a social post, or create commercial terms.
