# v0.6.148 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-10

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.147 closed the Technical Due Diligence Summary work item.

## Decision

The selected next work item is Safe PoC Boundary Template.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.149 Safe PoC Boundary Template Candidate.

This checkpoint does not create the Safe PoC Boundary Template.

This checkpoint does not authorize a customer PoC.

This checkpoint does not modify runtime behavior.

This checkpoint does not reopen the AAEF main handback sequence.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06148_completed = true
next_work_selection_v06148_is_documentation_only = true
next_work_selection_v06148_uses_v06120_granularity_policy = true
next_work_selection_v06148_uses_v06147_completed_work_item = true
v06148_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = safe_poc_boundary_template
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.149 Safe PoC Boundary Template Candidate
safe_poc_boundary_template_selected = true
technical_due_diligence_summary_work_item_closed = true
enterprise_review_guide_work_item_closed = true
mock_dry_run_completed_status_terminology_cleanup_work_item_closed = true
external_discovery_fail_closed_behavior_work_item_closed = true
request_decision_constraint_diff_enforcement_work_item_closed = true
authorization_expiry_current_time_check_work_item_closed = true
control_matrix_selected = false
reviewer_walkthrough_selected = false
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
safe_poc_boundary_template_created = false
safe_poc_boundary_template_behavior_modified = false
technical_due_diligence_summary_created = false
technical_due_diligence_summary_modified = false
enterprise_review_guide_created = false
enterprise_review_guide_modified = false
control_matrix_created = false
reviewer_walkthrough_created = false
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
commercial_contract_created = false
customer_poc_authorized = false
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
| Safe PoC Boundary Template | Medium | yes | The Enterprise Review Guide and Technical Due Diligence Summary are now accepted, so a non-authorizing PoC boundary template can define what a controlled evaluation would need without granting permission or enabling runtime execution. |
| Control Matrix | Medium | no | Useful next, but should follow the Safe PoC boundary so controls can map to a stable evaluation boundary. |
| Reviewer Walkthrough | Medium | no | Useful next, but should follow the PoC boundary and likely reuse its scope, evidence, and non-authorization framing. |

## Selected work item

~~~text
selected_next_work_item = safe_poc_boundary_template
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to create a claim-safe template that helps reviewers define the boundary of a future controlled PoC without authorizing real targets, real scanning, customer delivery, credential injection, or commercial deployment.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, it is close to commercial evaluation and customer-facing PoC planning. A poorly scoped template could be misread as permission to test a customer target, approval to run scanners, deployment readiness, diagnostic completeness, legal sufficiency, or a commercial delivery commitment.

Therefore, it is Medium risk and should use two checkpoints.

## Why not High or Critical risk

This work item should not change enforcement behavior, fail-closed logic, runtime execution, scanner execution, Docker/lab execution, credential injection, customer target handling, delivery authorization, or external submission.

It does not create a live PoC, contract, authorization record, runtime gate integration, scanner runbook, or customer delivery artifact.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not only a direction-selection note.

It will create a PoC-facing boundary template that may affect commercial evaluation framing and customer discussion. Even when non-authorizing, it must be precise about written authorization, target boundaries, excluded systems, tool limits, evidence retention, human review, stop conditions, and delivery boundaries.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.149 Safe PoC Boundary Template Candidate
v0.6.150 Safe PoC Boundary Template Review and Decision
~~~

v0.6.149 should create the candidate template and tests. The template should remain claim-safe, non-authorizing, and aligned with the Enterprise Review Guide and Technical Due Diligence Summary.

v0.6.150 should review the template, confirm claim boundaries, and decide whether to close the work item.

## Claim boundaries for the selected work

The Safe PoC Boundary Template candidate must not claim:

~~~text
customer authorization
commercial contract creation
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

The template may define fields that a separately authorized controlled PoC would need to fill in before any real action is considered.

## What did not happen

No Safe PoC Boundary Template is created in this checkpoint.

No Safe PoC Boundary Template behavior is modified.

No Technical Due Diligence Summary is created or modified.

No Enterprise Review Guide is created or modified.

No control matrix is created.

No reviewer walkthrough is created.

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

No customer PoC is authorized.

No commercial contract is created.

No delivery is authorized.

No certification claim occurs.

No legal compliance claim occurs.

No audit opinion claim occurs.

No production readiness claim occurs.

No external-framework equivalence claim occurs.

No diagnostic completeness claim occurs.

No third-party testing authorization claim occurs.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.147

v0.6.147 closed the Medium-risk Technical Due Diligence Summary work item.

This checkpoint selects the next work item after that closeout.

## Relationship to v0.6.144

v0.6.144 closed the Medium-risk Enterprise Review Guide work item.

This checkpoint does not modify that completed work.

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

This v0.6.148 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.149 Safe PoC Boundary Template Candidate
~~~

That checkpoint may create the candidate template and tests within the boundaries defined here.
