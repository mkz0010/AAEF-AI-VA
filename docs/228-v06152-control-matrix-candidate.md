# v0.6.152 Control Matrix Candidate

Status: candidate
Date: 2026-05-11

## Purpose

This checkpoint implements the Control Matrix candidate after v0.6.151 selected the work item.

This is checkpoint 1 of 2 for a Medium-risk reviewer-facing documentation work item.

This checkpoint creates the Control Matrix candidate.

The review and decision are deferred to v0.6.153.

## Candidate implementation summary

This checkpoint adds a claim-safe Control Matrix for enterprise reviewers, vulnerability assessment company decision-makers, security architects, technical due-diligence reviewers, project sponsors, and maintainers.

The matrix maps reviewer questions, control boundaries, expected evidence, related artifacts, explicit non-goals, and reviewer notes across the current review package.

The matrix is reviewer-facing but remains non-authorizing.

It does not create a compliance matrix, audit checklist, certification checklist, production readiness checklist, external-framework equivalence mapping, customer PoC approval, commercial contract, runtime authorization, scanner authorization, credential authorization, customer-target authorization, or delivery authorization.

## Candidate matrix

~~~text
docs/control-matrix.md
~~~

The matrix includes rows for:

* AI request is not authority,
* gate decision boundary,
* current-time authorization expiry,
* request/decision constraint drift,
* external discovery fail-closed behavior,
* mock/dry-run status disambiguation,
* non-execution evidence,
* human approval boundary,
* credential and data handling,
* public/private artifact boundary,
* report and delivery boundary,
* PoC non-authorization boundary,
* commercial and license boundary,
* conservative claim boundaries.

## Matrix row design

Each row includes:

* review question,
* control boundary,
* expected evidence,
* related artifacts,
* explicit non-goal,
* reviewer note.

## Claim boundaries

The candidate matrix must not be interpreted as:

~~~text
certification
legal compliance determination
audit opinion
audit sufficiency determination
deployment approval
complete vulnerability assessment capability
permission for testing third-party systems
customer PoC approval
commercial contract
equivalence mapping to external frameworks
production readiness claim
proof that gate-free AI tool execution is acceptable
promotion into AAEF Core/Profile/Practical Package status
~~~

The matrix may help reviewers locate control boundaries, expected evidence, related artifacts, explicit non-goals, and reviewer notes across the current AAEF-AI-VA review package.

## Candidate tests

This checkpoint adds:

~~~text
tools/test_v06152_control_matrix_candidate.py
~~~

The tests cover:

* matrix file existence,
* required reader/purpose sections,
* non-authorizing notice,
* row design,
* required matrix rows,
* required row columns,
* matrix interpretation limits,
* claim boundaries,
* v0.6.151 selection continuity,
* v0.6.153 review/decision deferral,
* absence of forbidden affirmative claims.

## Candidate record

~~~text
control_matrix_candidate_completed = true
control_matrix_candidate_is_medium_risk = true
control_matrix_candidate_checkpoint_1_of_2 = true
control_matrix_review_decision_deferred_to_v06153 = true
control_matrix_created = true
control_matrix_candidate_claim_safe = true
control_matrix_reader_identified = true
control_matrix_non_authorizing_notice_included = true
control_matrix_rows_include_review_question = true
control_matrix_rows_include_control_boundary = true
control_matrix_rows_include_expected_evidence = true
control_matrix_rows_include_related_artifacts = true
control_matrix_rows_include_explicit_non_goal = true
control_matrix_rows_include_reviewer_note = true
control_matrix_ai_request_boundary_included = true
control_matrix_gate_decision_boundary_included = true
control_matrix_authorization_expiry_boundary_included = true
control_matrix_constraint_drift_boundary_included = true
control_matrix_external_discovery_boundary_included = true
control_matrix_mock_dry_run_status_boundary_included = true
control_matrix_non_execution_evidence_boundary_included = true
control_matrix_human_approval_boundary_included = true
control_matrix_credential_data_boundary_included = true
control_matrix_public_private_artifact_boundary_included = true
control_matrix_report_delivery_boundary_included = true
control_matrix_poc_non_authorization_boundary_included = true
control_matrix_commercial_license_boundary_included = true
control_matrix_claim_boundaries_included = true
control_matrix_review_decision_completed = false
review_decision_completed = false
customer_poc_authorized = false
commercial_contract_created = false
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
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
safe_poc_boundary_template_modified = false
technical_due_diligence_summary_modified = false
enterprise_review_guide_modified = false
reviewer_walkthrough_created = false
mock_completed_status_renamed = false
mock_dry_run_status_behavior_modified = false
external_discovery_fail_closed_added = false
constraint_diff_enforcement_added = false
authorization_expiry_now_check_added = false
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
selected_next_checkpoint = v0.6.153 Control Matrix Review and Decision
~~~

## What changed

The following files are added:

~~~text
docs/control-matrix.md
docs/228-v06152-control-matrix-candidate.md
planning/decisions/ADR-0222-add-v06152-control-matrix-candidate.md
planning/issues/0221-add-v06152-control-matrix-candidate.md
tools/test_v06152_control_matrix_candidate.py
~~~

The following files are updated for repository navigation and checks:

~~~text
README.md
CHANGELOG.md
ROADMAP.md
tools/run_all_local_checks.py
~~~

## What did not happen

No review/decision closeout is completed.

No customer PoC approval occurs.

No commercial contract creation occurs.

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

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

No Safe PoC Boundary Template is modified.

No Technical Due Diligence Summary is modified.

No Enterprise Review Guide is modified.

No reviewer walkthrough is created.

No mock/dry-run status behavior is modified.

No external_discovery fail-closed behavior is added or modified.

No request/decision constraint-diff enforcement is added or modified.

No authorization expiry current-time check is added or modified.

No certification claim occurs.

No legal compliance claim occurs.

No audit opinion claim occurs.

No production readiness claim occurs.

No external-framework equivalence claim occurs.

No diagnostic completeness claim occurs.

No third-party testing authorization claim occurs.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.151

v0.6.151 selected Control Matrix as a Medium-risk work item and assigned two checkpoints:

~~~text
v0.6.152 Control Matrix Candidate
v0.6.153 Control Matrix Review and Decision
~~~

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.150

v0.6.150 closed the Safe PoC Boundary Template work item.

This checkpoint builds on that accepted template by adding a cross-document control matrix.

## Relationship to v0.6.147

v0.6.147 closed the Technical Due Diligence Summary work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.144

v0.6.144 closed the Enterprise Review Guide work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.153 Control Matrix Review and Decision
~~~

That checkpoint should review the matrix, confirm claim boundaries, and decide whether to close the Medium-risk work item.
