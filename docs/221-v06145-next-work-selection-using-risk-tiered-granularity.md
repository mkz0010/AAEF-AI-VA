# v0.6.145 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-10

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.144 closed the Enterprise Review Guide work item.

## Decision

The selected next work item is Technical Due Diligence Summary.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.146 Technical Due Diligence Summary Candidate.

This checkpoint does not create the Technical Due Diligence Summary.

This checkpoint does not modify runtime behavior.

This checkpoint does not reopen the AAEF main handback sequence.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06145_completed = true
next_work_selection_v06145_is_documentation_only = true
next_work_selection_v06145_uses_v06120_granularity_policy = true
next_work_selection_v06145_uses_v06144_completed_work_item = true
v06145_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = technical_due_diligence_summary
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.146 Technical Due Diligence Summary Candidate
technical_due_diligence_summary_selected = true
enterprise_review_guide_work_item_closed = true
mock_dry_run_completed_status_terminology_cleanup_work_item_closed = true
external_discovery_fail_closed_behavior_work_item_closed = true
request_decision_constraint_diff_enforcement_work_item_closed = true
authorization_expiry_current_time_check_work_item_closed = true
safe_poc_boundary_template_selected = false
control_matrix_selected = false
reviewer_walkthrough_selected = false
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
technical_due_diligence_summary_created = false
technical_due_diligence_summary_behavior_modified = false
safe_poc_boundary_template_created = false
control_matrix_created = false
reviewer_walkthrough_created = false
enterprise_review_guide_created = false
enterprise_review_guide_modified = false
mock_completed_status_renamed = false
mock_dry_run_status_behavior_modified = false
external_discovery_fail_closed_added = false
constraint_diff_enforcement_added = false
authorization_expiry_now_check_added = false
validator_behavior_modified = false
metadata_level_expected_failure_category_added = false
json_schema_added = false
public_sample_changed = false
runtime_behavior_modified = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
certification_claim_occurs = false
legal_compliance_claim_occurs = false
audit_opinion_claim_occurs = false
production_readiness_claim_occurs = false
external_framework_equivalence_claim_occurs = false
diagnostic_completeness_claim_occurs = false
third_party_testing_authorization_claim_occurs = false
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
~~~

## Candidate work items reviewed

| Candidate | Risk tier | Selected | Reason |
| --- | --- | --- | --- |
| Technical Due Diligence Summary | Medium | yes | The Enterprise Review Guide is now accepted, so a more technical due-diligence summary can align reviewer checks with the accepted guide without changing runtime behavior. |
| Safe PoC Boundary Template | Medium | no | Useful next, but the technical summary should first define the review surface and technical evidence expectations. |
| Control Matrix | Medium | no | Useful next, but should follow a technical summary so control rows map to a stable review narrative. |
| Reviewer Walkthrough | Medium | no | Useful next, but should follow the technical summary and likely reuse its structure. |

## Selected work item

~~~text
selected_next_work_item = technical_due_diligence_summary
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to create a claim-safe technical summary for reviewers who need to understand the repository's technical control surface, evidence paths, gate-semantics checks, and non-execution boundaries before considering any controlled PoC or commercial evaluation.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, it is technical reviewer-facing and can influence how the project is interpreted by security architects, vulnerability assessment engineers, and enterprise due-diligence reviewers.

A poorly scoped summary could imply production readiness, diagnostic completeness, certification, legal compliance, audit sufficiency, external-framework equivalence, or authorization for real scanning.

Therefore, it is Medium risk and should use two checkpoints.

## Why not High or Critical risk

This work item should not change enforcement behavior, fail-closed logic, runtime execution, scanner execution, Docker/lab execution, credential injection, customer target handling, delivery authorization, or external submission.

It is not a new gate-semantics implementation.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not only a direction-selection note.

It will create technical reviewer-facing material that can affect repository interpretation, due-diligence framing, and claim boundaries.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.146 Technical Due Diligence Summary Candidate
v0.6.147 Technical Due Diligence Summary Review and Decision
~~~

v0.6.146 should create the candidate summary and tests. The summary should remain claim-safe, non-authorizing, and aligned with the Enterprise Review Guide.

v0.6.147 should review the summary, confirm claim boundaries, and decide whether to close the work item.

## Claim boundaries for the selected work

The Technical Due Diligence Summary candidate must not claim:

~~~text
certification
legal compliance
audit opinion
audit sufficiency
production readiness
production scanner status
diagnostic completeness
authorization for third-party testing
equivalence with external frameworks
AAEF Core/Profile/Practical Package promotion
~~~

The summary may explain AAEF-AI-VA as a safety-first reference implementation and technical control-boundary example for AI-assisted vulnerability assessment action requests.

## What did not happen

No Technical Due Diligence Summary is created in this checkpoint.

No Technical Due Diligence Summary behavior is modified.

No Safe PoC Boundary Template is created.

No control matrix is created.

No reviewer walkthrough is created.

No Enterprise Review Guide is created or modified.

No mock/dry-run `completed` status is renamed.

No mock/dry-run status behavior is modified.

No external_discovery fail-closed behavior is added or modified.

No request/decision constraint-diff enforcement is added or modified.

No authorization expiry current-time check is added or modified.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

No validator behavior is modified.

No metadata-level `expected_failure_category` is added.

No JSON Schema is added.

No public sample is changed.

No runtime behavior is modified.

No runtime execution is authorized.

No scanner execution is authorized.

No Docker execution is authorized.

No credential injection is permitted.

No customer target is authorized.

No delivery is authorized.

No certification claim occurs.

No legal compliance claim occurs.

No audit opinion claim occurs.

No production readiness claim occurs.

No external-framework equivalence claim occurs.

No diagnostic completeness claim occurs.

No third-party testing authorization claim occurs.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.144

v0.6.144 closed the Medium-risk Enterprise Review Guide work item.

This checkpoint selects the next work item after that closeout.

## Relationship to v0.6.141

v0.6.141 closed the Medium-risk mock/dry-run `completed` status terminology cleanup work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.138

v0.6.138 closed the High-risk external_discovery=true fail-closed behavior work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.134

v0.6.134 closed the High-risk request/decision constraint-diff enforcement work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.130

v0.6.130 closed the High-risk authorization expiry current-time check work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.145 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.146 Technical Due Diligence Summary Candidate
~~~

That checkpoint may create the candidate summary and tests within the boundaries defined here.
