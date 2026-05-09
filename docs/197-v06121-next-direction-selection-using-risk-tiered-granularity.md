# v0.6.121 Next-Direction Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-10

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one low-risk checkpoint.

It selects the next AAEF-AI-VA work item and records the risk tier and checkpoint count before implementation begins.

## Decision

The selected next work item is README current/latest baseline clarity.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.122 README Current/Latest Baseline Clarity Candidate.

This checkpoint does not update README current/latest baseline wording.

This checkpoint does not reopen the AAEF main handback sequence.

## Risk-tiered selection record

~~~text
next_direction_selection_using_risk_tiered_granularity_completed = true
next_direction_selection_is_documentation_only = true
next_direction_selection_uses_v06120_granularity_policy = true
v06121_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = readme_current_latest_baseline_clarity
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_preparation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.122 README Current/Latest Baseline Clarity Candidate
readme_current_latest_baseline_clarity_selected = true
security_reporting_channel_consistency_selected = false
authorization_expiry_now_check_selected = false
request_decision_constraint_diff_enforcement_selected = false
external_discovery_fail_closed_selected = false
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
readme_current_baseline_updated = false
security_reporting_channel_updated = false
authorization_expiry_now_check_added = false
constraint_diff_enforcement_added = false
external_discovery_fail_closed_added = false
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
| README current/latest baseline clarity | Medium | yes | Public-facing wording should be clarified first, but it is still documentation-only and non-executing. |
| SECURITY.md reporting-channel consistency | Medium | no | Important, but README baseline clarity is the cleaner first public-facing fix. |
| Authorization expiry checked against current time | High | no | Runtime/gate behavior semantics need more implementation caution. |
| Request/decision constraint-diff enforcement | High | no | Enforcement logic can affect gate behavior. |
| Fail-closed handling for external_discovery=true | High | no | Gate behavior change; should not be first after policy adoption. |
| Mock/dry-run `completed` status terminology cleanup | Medium | no | Useful, but less foundational than README baseline clarity. |
| Enterprise Review Guide | Medium | no | Buyer-facing docs should wait until public baseline wording is clean. |
| Technical due diligence summary | Medium | no | Same dependency on baseline clarity. |
| Safe PoC boundary template | Medium | no | Same dependency on baseline clarity. |
| Control matrix | Medium | no | Same dependency on baseline clarity. |
| Reviewer walkthrough | Medium | no | Same dependency on baseline clarity. |

## Selected work item

~~~text
selected_next_work_item = readme_current_latest_baseline_clarity
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_preparation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to make the README clearer about the current/latest baseline without changing runtime behavior, validator behavior, public samples, schema, issue submission, or AAEF main handback state.

## Why this is Medium risk

README current/latest baseline clarity is public-facing documentation.

It can affect reviewer and buyer interpretation, so it should not be treated as Low risk.

It is still non-executing documentation-only work, so it does not need High or Critical risk treatment.

## Why not High or Critical risk

The selected work item should not modify:

* validator behavior,
* schemas,
* fixture metadata contracts,
* public sample content,
* runtime execution,
* scanner execution,
* Docker/lab execution,
* credential handling,
* customer target handling,
* delivery authorization,
* actual external submission.

Therefore, High or Critical checkpoint counts are not justified.

## Why not Low risk

The selected work item affects public-facing README language.

Public-facing wording can create overclaim, baseline confusion, or reviewer misunderstanding if handled too casually.

Therefore, it should use 2 checkpoints rather than 1 checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.122 README Current/Latest Baseline Clarity Candidate
v0.6.123 README Current/Latest Baseline Clarity Review and Decision
~~~

v0.6.122 should prepare the candidate README wording and tests.

v0.6.123 should review, refine if needed, and decide whether to close the work item.

## What did not happen

No README current/latest baseline wording is changed in this checkpoint.

No SECURITY.md reporting-channel wording is changed.

No authorization expiry now check is added.

No request/decision constraint-diff enforcement is added.

No external_discovery fail-closed behavior is added.

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

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.121 checkpoint applies that policy by completing a low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.122 README Current/Latest Baseline Clarity Candidate
~~~

That checkpoint should prepare README wording and tests only. It should not change runtime behavior, validator behavior, schemas, public samples, AAEF main handback state, or external submission state.
