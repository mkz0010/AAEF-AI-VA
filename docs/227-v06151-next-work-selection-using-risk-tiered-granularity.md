# v0.6.151 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-11

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.150 closed the Safe PoC Boundary Template work item.

## Decision

The selected next work item is Control Matrix.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.152 Control Matrix Candidate.

This checkpoint does not create the Control Matrix.

This checkpoint does not modify runtime behavior.

This checkpoint does not reopen the AAEF main handback sequence.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06151_completed = true
next_work_selection_v06151_is_documentation_only = true
next_work_selection_v06151_uses_v06120_granularity_policy = true
next_work_selection_v06151_uses_v06150_completed_work_item = true
v06151_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = control_matrix
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.152 Control Matrix Candidate
control_matrix_selected = true
safe_poc_boundary_template_work_item_closed = true
technical_due_diligence_summary_work_item_closed = true
enterprise_review_guide_work_item_closed = true
mock_dry_run_completed_status_terminology_cleanup_work_item_closed = true
external_discovery_fail_closed_behavior_work_item_closed = true
request_decision_constraint_diff_enforcement_work_item_closed = true
authorization_expiry_current_time_check_work_item_closed = true
reviewer_walkthrough_selected = false
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
control_matrix_created = false
control_matrix_behavior_modified = false
safe_poc_boundary_template_created = false
safe_poc_boundary_template_modified = false
technical_due_diligence_summary_created = false
technical_due_diligence_summary_modified = false
enterprise_review_guide_created = false
enterprise_review_guide_modified = false
reviewer_walkthrough_created = false
customer_poc_authorized = false
commercial_contract_created = false
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
| Control Matrix | Medium | yes | Enterprise Review Guide, Technical Due Diligence Summary, and Safe PoC Boundary Template are now accepted. A matrix can align review questions, control boundaries, evidence expectations, and non-authorizing limits across those documents. |
| Reviewer Walkthrough | Medium | no | Useful next, but should follow the Control Matrix so the walkthrough can reuse stable control rows and evidence expectations. |
| AAEF main handback reconsideration | Medium or High | no | The v0.6.119 handback sequence remains paused. A public-safe AAEF main handback should not be reopened until the applied implementation lessons are consolidated into a narrow, stable evidence/interface form. |
| Runtime execution preparation | High or Critical | no | Runtime/scanner/customer-target activity remains outside the current safe direction and would require a larger risk split. |

## Selected work item

~~~text
selected_next_work_item = control_matrix
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to create a claim-safe Control Matrix that maps reviewer-facing questions, control boundaries, expected evidence, related documents, and explicit non-goals.

The matrix should make the current review package easier to inspect without implying certification, compliance, audit sufficiency, production readiness, diagnostic completeness, or authorization for third-party testing.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, a matrix can look authoritative. A poorly scoped matrix could be mistaken for a compliance matrix, audit checklist, certification checklist, production readiness checklist, external-framework equivalence mapping, or permission structure.

Therefore, it is Medium risk and should use two checkpoints.

## Why not High or Critical risk

This work item should not change enforcement behavior, fail-closed logic, runtime execution, scanner execution, Docker/lab execution, credential injection, customer target handling, delivery authorization, or external submission.

It does not create a live PoC, contract, authorization record, runtime gate integration, scanner runbook, customer delivery artifact, or AAEF main handback submission.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not only a direction-selection note.

It will create a reviewer-facing matrix that may affect buyer, technical reviewer, and project sponsor interpretation.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.152 Control Matrix Candidate
v0.6.153 Control Matrix Review and Decision
~~~

v0.6.152 should create the candidate matrix and tests. The matrix should remain claim-safe, non-authorizing, and aligned with the Enterprise Review Guide, Technical Due Diligence Summary, and Safe PoC Boundary Template.

v0.6.153 should review the matrix, confirm claim boundaries, and decide whether to close the work item.

## Expected Control Matrix scope

The Control Matrix candidate should likely include rows for:

* AI request is not authority,
* gate decision boundary,
* current-time authorization expiry,
* request/decision constraint drift,
* external discovery fail-closed behavior,
* mock/dry-run status disambiguation,
* non-execution evidence,
* human approval,
* credential/data handling,
* public/private artifact boundary,
* report and delivery boundary,
* PoC non-authorization,
* commercial/license boundary,
* conservative claim boundaries.

Each row should identify:

* review question,
* control boundary,
* expected evidence,
* related document or test family,
* explicit non-goal,
* reviewer note.

## Claim boundaries for the selected work

The Control Matrix candidate must not claim:

~~~text
certification
legal compliance
audit opinion
audit sufficiency
production readiness
production scanner status
diagnostic completeness
authorization for third-party testing
customer PoC approval
commercial contract creation
equivalence with external frameworks
AAEF Core/Profile/Practical Package promotion
~~~

The matrix may help reviewers inspect the current AAEF-AI-VA documentation and evidence boundaries.

## What did not happen

No Control Matrix is created in this checkpoint.

No Control Matrix behavior is modified.

No Safe PoC Boundary Template is created or modified.

No Technical Due Diligence Summary is created or modified.

No Enterprise Review Guide is created or modified.

No reviewer walkthrough is created.

No customer PoC approval occurs.

No commercial contract creation occurs.

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

No runtime execution approval occurs.

No scanner execution approval occurs.

No Docker execution approval occurs.

No credential injection approval occurs.

No customer target approval occurs.

No delivery approval occurs.

No certification claim occurs.

No legal compliance claim occurs.

No audit opinion claim occurs.

No production readiness claim occurs.

No external-framework equivalence claim occurs.

No diagnostic completeness claim occurs.

No third-party testing authorization claim occurs.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.150

v0.6.150 closed the Medium-risk Safe PoC Boundary Template work item.

This checkpoint selects the next work item after that closeout.

## Relationship to v0.6.147

v0.6.147 closed the Medium-risk Technical Due Diligence Summary work item.

This checkpoint does not modify that completed work.

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

This v0.6.151 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.152 Control Matrix Candidate
~~~

That checkpoint may create the candidate matrix and tests within the boundaries defined here.
