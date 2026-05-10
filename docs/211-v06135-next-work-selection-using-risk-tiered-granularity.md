# v0.6.135 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-10

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.134 closed the request/decision constraint-diff enforcement work item.

## Decision

The selected next work item is external_discovery=true fail-closed behavior.

The selected next work item risk tier is High risk.

The selected checkpoint count is 3 checkpoints.

The next checkpoint is v0.6.136 External Discovery Fail-Closed Behavior Readiness.

This checkpoint does not implement external_discovery fail-closed behavior.

This checkpoint does not modify external_discovery behavior.

This checkpoint does not reopen the AAEF main handback sequence.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06135_completed = true
next_work_selection_v06135_is_documentation_only = true
next_work_selection_v06135_uses_v06120_granularity_policy = true
next_work_selection_v06135_uses_v06134_completed_work_item = true
v06135_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = external_discovery_fail_closed_behavior
selected_next_work_item_risk_tier = high
selected_next_work_item_checkpoint_count = 3
selected_next_work_item_first_checkpoint = readiness
selected_next_work_item_second_checkpoint = candidate_implementation
selected_next_work_item_third_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.136 External Discovery Fail-Closed Behavior Readiness
external_discovery_fail_closed_selected = true
request_decision_constraint_diff_enforcement_work_item_closed = true
authorization_expiry_current_time_check_work_item_closed = true
mock_dry_run_completed_status_cleanup_selected = false
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
external_discovery_fail_closed_added = false
external_discovery_behavior_modified = false
external_discovery_gate_runtime_behavior_modified = false
constraint_diff_enforcement_added = false
authorization_expiry_now_check_added = false
mock_completed_status_renamed = false
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
| external_discovery=true fail-closed behavior | High | yes | It affects whether a request can expand beyond the expected/local target boundary and is a remaining gate-semantics risk after authorization expiry and constraint-diff checks. |
| Mock/dry-run `completed` status terminology cleanup | Medium | no | Useful, but less important than fail-closing external discovery expansion. |
| Enterprise Review Guide | Medium | no | Buyer-facing docs should wait until key gate semantics are cleaner. |
| Technical due diligence summary | Medium | no | Same dependency on gate semantics. |
| Safe PoC boundary template | Medium | no | Same dependency on gate semantics. |
| Control matrix | Medium | no | Same dependency on gate semantics. |
| Reviewer walkthrough | Medium | no | Same dependency on gate semantics. |

## Selected work item

~~~text
selected_next_work_item = external_discovery_fail_closed_behavior
selected_next_work_item_risk_tier = high
selected_next_work_item_checkpoint_count = 3
selected_next_work_item_first_checkpoint = readiness
selected_next_work_item_second_checkpoint = candidate_implementation
selected_next_work_item_third_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to ensure that requests using `external_discovery=true` fail closed unless explicitly authorized by the relevant gate decision and compatible with the configured target boundary.

## Why this is High risk

external_discovery behavior affects target expansion and boundary enforcement.

A mistake can incorrectly allow discovery outside an authorized local/specified target boundary, incorrectly block a valid authorized case, or create misleading evidence about whether external discovery was allowed at execution time.

The work may affect gate comparison logic, tests, evidence expectations, and reviewer interpretation.

Therefore, it should use the High-risk three-checkpoint pattern.

## Why not Critical risk

The selected work item should not itself authorize runtime execution, scanner execution, Docker/lab execution, credential injection, customer target handling, delivery authorization, or actual external submission.

It should remain a code/test gate-semantics hardening work item.

Therefore, the Critical-risk four-to-five-checkpoint pattern is not required unless later scope expands.

## Why not Medium or Low risk

The selected work item is not only public-facing documentation.

It can modify gate validation behavior for external discovery expansion and must be reviewed carefully.

Therefore, it should not be completed in one or two checkpoints.

## Planned checkpoint split

The selected work item should use the High-risk three-checkpoint pattern:

~~~text
v0.6.136 External Discovery Fail-Closed Behavior Readiness
v0.6.137 External Discovery Fail-Closed Behavior Candidate
v0.6.138 External Discovery Fail-Closed Behavior Review and Decision
~~~

v0.6.136 should identify current external_discovery semantics, target-boundary inputs, expected fail-closed behavior, non-goals, and tests to add or update.

v0.6.137 should implement the candidate behavior and tests.

v0.6.138 should review the behavior, confirm fail-closed boundaries, and decide whether to close the work item.

## What did not happen

No external_discovery fail-closed behavior is added in this checkpoint.

No external_discovery behavior is modified.

No external_discovery gate runtime behavior is modified.

No request/decision constraint-diff enforcement is added or modified.

No authorization expiry current-time check is added or modified.

No mock/dry-run status terminology is renamed.

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

## Relationship to v0.6.134

v0.6.134 closed the High-risk request/decision constraint-diff enforcement work item.

This checkpoint selects the next High-risk gate-semantics work item.

## Relationship to v0.6.130

v0.6.130 closed the High-risk authorization expiry current-time check work item.

This checkpoint continues the same gate-semantics hardening sequence by selecting external discovery fail-closed behavior.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.135 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to High risk with three checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.136 External Discovery Fail-Closed Behavior Readiness
~~~

That checkpoint should prepare the High-risk work item only. It should not implement the behavior until the candidate checkpoint.
