# v0.6.149 Safe PoC Boundary Template Candidate

Status: candidate
Date: 2026-05-11

## Purpose

This checkpoint implements the Safe PoC Boundary Template candidate after v0.6.148 selected the work item.

This is checkpoint 1 of 2 for a Medium-risk PoC-facing documentation work item.

This checkpoint creates the Safe PoC Boundary Template candidate.

The review and decision are deferred to v0.6.150.

## Candidate implementation summary

This checkpoint adds a claim-safe Safe PoC Boundary Template for enterprise reviewers, vulnerability assessment company decision-makers, security architects, technical due-diligence reviewers, and project sponsors.

The template defines boundary information that would be required before a separately approved controlled PoC could be considered.

The template is PoC-facing but remains non-authorizing.

It does not create customer authorization, a commercial contract, runtime authorization, scanner authorization, credential authorization, customer-target authorization, or delivery authorization.

## Candidate template

~~~text
docs/safe-poc-boundary-template.md
~~~

The template includes:

* reader and purpose,
* non-authorizing notice,
* boundary summary,
* required written authorization fields,
* parties and responsibilities,
* target scope,
* excluded systems,
* PoC time window,
* tool and action limits,
* AI request and gate boundary,
* credential and data handling,
* evidence retention and deletion,
* human review and approval,
* stop conditions,
* communications and escalation,
* deliverables boundary,
* commercial and license boundary,
* pre-PoC review checklist,
* not-allowed section,
* claim boundaries.

## Claim boundaries

The candidate template must not be interpreted as:

~~~text
customer authorization
commercial contract
legal compliance determination
audit opinion
audit sufficiency determination
deployment approval
complete vulnerability assessment capability
permission for testing third-party systems
equivalence mapping to external frameworks
production readiness claim
proof that gate-free AI tool execution is acceptable
promotion into AAEF Core/Profile/Practical Package status
~~~

The template may define the boundary information that a separately approved controlled PoC would need before any real action is considered.

## Candidate tests

This checkpoint adds:

~~~text
tools/test_v06149_safe_poc_boundary_template_candidate.py
~~~

The tests cover:

* template file existence,
* required reader/purpose sections,
* non-authorizing notice,
* boundary summary,
* written authorization fields,
* target scope and exclusions,
* time window,
* tool and action limits,
* AI request and gate boundary,
* credential and data handling,
* evidence retention and deletion,
* human review and approval,
* stop conditions,
* communications and escalation,
* deliverables boundary,
* commercial and license boundary,
* pre-PoC checklist,
* not-allowed section,
* claim boundaries,
* v0.6.148 selection continuity,
* v0.6.150 review/decision deferral,
* absence of forbidden affirmative claims.

## Candidate record

~~~text
safe_poc_boundary_template_candidate_completed = true
safe_poc_boundary_template_candidate_is_medium_risk = true
safe_poc_boundary_template_candidate_checkpoint_1_of_2 = true
safe_poc_boundary_template_review_decision_deferred_to_v06150 = true
safe_poc_boundary_template_created = true
safe_poc_boundary_template_candidate_claim_safe = true
safe_poc_boundary_template_non_authorizing_notice_included = true
safe_poc_boundary_template_required_written_authorization_fields_included = true
safe_poc_boundary_template_parties_and_responsibilities_included = true
safe_poc_boundary_template_target_scope_included = true
safe_poc_boundary_template_excluded_systems_included = true
safe_poc_boundary_template_time_window_included = true
safe_poc_boundary_template_tool_action_limits_included = true
safe_poc_boundary_template_ai_gate_boundary_included = true
safe_poc_boundary_template_credential_data_handling_included = true
safe_poc_boundary_template_evidence_retention_deletion_included = true
safe_poc_boundary_template_human_review_approval_included = true
safe_poc_boundary_template_stop_conditions_included = true
safe_poc_boundary_template_communications_escalation_included = true
safe_poc_boundary_template_deliverables_boundary_included = true
safe_poc_boundary_template_commercial_license_boundary_included = true
safe_poc_boundary_template_pre_poc_review_checklist_included = true
safe_poc_boundary_template_not_allowed_section_included = true
safe_poc_boundary_template_claim_boundaries_included = true
safe_poc_boundary_template_review_decision_completed = false
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
control_matrix_created = false
reviewer_walkthrough_created = false
enterprise_review_guide_modified = false
technical_due_diligence_summary_modified = false
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
selected_next_checkpoint = v0.6.150 Safe PoC Boundary Template Review and Decision
~~~

## What changed

The following files are added:

~~~text
docs/safe-poc-boundary-template.md
docs/225-v06149-safe-poc-boundary-template-candidate.md
planning/decisions/ADR-0219-add-v06149-safe-poc-boundary-template-candidate.md
planning/issues/0218-add-v06149-safe-poc-boundary-template-candidate.md
tools/test_v06149_safe_poc_boundary_template_candidate.py
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

No control matrix is created.

No reviewer walkthrough is created.

No Enterprise Review Guide is modified.

No Technical Due Diligence Summary is modified.

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

## Relationship to v0.6.148

v0.6.148 selected Safe PoC Boundary Template as a Medium-risk work item and assigned two checkpoints:

~~~text
v0.6.149 Safe PoC Boundary Template Candidate
v0.6.150 Safe PoC Boundary Template Review and Decision
~~~

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.147

v0.6.147 closed the Technical Due Diligence Summary work item.

This checkpoint builds on that accepted summary by adding a non-authorizing PoC boundary template.

## Relationship to v0.6.144

v0.6.144 closed the Enterprise Review Guide work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.150 Safe PoC Boundary Template Review and Decision
~~~

That checkpoint should review the template, confirm claim boundaries, and decide whether to close the Medium-risk work item.
