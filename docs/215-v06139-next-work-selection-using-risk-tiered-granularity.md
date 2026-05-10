# v0.6.139 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-10

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.138 closed the external_discovery=true fail-closed behavior work item.

## Decision

The selected next work item is mock/dry-run `completed` status terminology cleanup.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.140 Mock/Dry-Run Completed Status Terminology Cleanup Candidate.

This checkpoint does not rename mock/dry-run `completed` status.

This checkpoint does not modify mock/dry-run status behavior.

This checkpoint does not reopen the AAEF main handback sequence.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06139_completed = true
next_work_selection_v06139_is_documentation_only = true
next_work_selection_v06139_uses_v06120_granularity_policy = true
next_work_selection_v06139_uses_v06138_completed_work_item = true
v06139_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = mock_dry_run_completed_status_terminology_cleanup
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.140 Mock/Dry-Run Completed Status Terminology Cleanup Candidate
mock_dry_run_completed_status_cleanup_selected = true
external_discovery_fail_closed_behavior_work_item_closed = true
request_decision_constraint_diff_enforcement_work_item_closed = true
authorization_expiry_current_time_check_work_item_closed = true
enterprise_review_guide_selected = false
technical_due_diligence_summary_selected = false
safe_poc_boundary_template_selected = false
control_matrix_selected = false
reviewer_walkthrough_selected = false
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
mock_completed_status_renamed = false
mock_dry_run_status_behavior_modified = false
external_discovery_fail_closed_added = false
constraint_diff_enforcement_added = false
authorization_expiry_now_check_added = false
enterprise_review_guide_created = false
technical_due_diligence_summary_created = false
safe_poc_boundary_template_created = false
control_matrix_created = false
reviewer_walkthrough_created = false
validator_behavior_modified = false
metadata_level_expected_failure_category_added = false
json_schema_added = false
public_sample_changed = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
~~~

## Candidate work items reviewed

| Candidate | Risk tier | Selected | Reason |
| --- | --- | --- | --- |
| Mock/dry-run `completed` status terminology cleanup | Medium | yes | It improves evidence interpretation by avoiding ambiguity between mock/dry-run completion and real execution completion. |
| Enterprise Review Guide | Medium | no | Buyer-facing docs should wait until the mock/dry-run status wording is clearer. |
| Technical due diligence summary | Medium | no | Same dependency on clearer status semantics. |
| Safe PoC boundary template | Medium | no | Same dependency on clearer status semantics. |
| Control matrix | Medium | no | Same dependency on clearer status semantics. |
| Reviewer walkthrough | Medium | no | Same dependency on clearer status semantics. |

## Selected work item

~~~text
selected_next_work_item = mock_dry_run_completed_status_terminology_cleanup
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to reduce ambiguity where mock or dry-run outputs use `completed` language that could be mistaken for real execution completion.

## Why this is Medium risk

The selected work item can affect reviewer interpretation and output wording.

It may touch status strings, generated examples, expected test phrases, README wording, or documentation that reviewers use to understand whether actual execution occurred.

However, it should not change authorization logic, target-boundary enforcement, external discovery behavior, request/decision comparison behavior, authorization expiry behavior, runtime gate behavior, or scanner execution behavior.

Therefore, it is Medium risk and should use two checkpoints.

## Why not High or Critical risk

This work item should not modify gate authorization semantics, fail-closed behavior, runtime enforcement, scanner execution, Docker/lab execution, credential injection, customer target handling, delivery authorization, or external submission.

It is terminology and evidence-interpretation cleanup, not a new enforcement gate.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not only a direction-selection or pure documentation note.

If the candidate changes status strings or test expectations, it can affect generated outputs and reviewer interpretation.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.140 Mock/Dry-Run Completed Status Terminology Cleanup Candidate
v0.6.141 Mock/Dry-Run Completed Status Terminology Cleanup Review and Decision
~~~

v0.6.140 should identify current mock/dry-run `completed` wording, implement a candidate terminology cleanup, update tests, and preserve compatibility boundaries.

v0.6.141 should review the candidate behavior, confirm no runtime/execution authorization effect, and decide whether to close the work item.

## What did not happen

No mock/dry-run `completed` status is renamed in this checkpoint.

No mock/dry-run status behavior is modified.

No external_discovery fail-closed behavior is added or modified.

No request/decision constraint-diff enforcement is added or modified.

No authorization expiry current-time check is added or modified.

No Enterprise Review Guide is created.

No technical due diligence summary is created.

No safe PoC boundary template is created.

No control matrix is created.

No reviewer walkthrough is created.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

No validator behavior is modified.

No metadata-level `expected_failure_category` is added.

No JSON Schema is added.

No public sample is changed.

No runtime execution is authorized.

No scanner execution is authorized.

No Docker execution is authorized.

No credential injection is permitted.

No customer target is authorized.

No delivery is authorized.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.138

v0.6.138 closed the High-risk external_discovery=true fail-closed behavior work item.

This checkpoint selects the next work item after that closeout.

## Relationship to v0.6.134

v0.6.134 closed the High-risk request/decision constraint-diff enforcement work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.130

v0.6.130 closed the High-risk authorization expiry current-time check work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.139 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.140 Mock/Dry-Run Completed Status Terminology Cleanup Candidate
~~~

That checkpoint may implement the candidate terminology cleanup and tests within the boundaries defined here.
