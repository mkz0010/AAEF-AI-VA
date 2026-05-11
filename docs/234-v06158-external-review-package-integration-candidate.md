# v0.6.158 External Review Package Integration Candidate

Status: candidate
Date: 2026-05-11

## Purpose

This checkpoint implements the External Review Package Integration candidate after v0.6.157 selected the work item.

This is checkpoint 1 of 2 for a Medium-risk external-review-facing documentation work item.

This checkpoint creates the External Review Package Integration candidate.

The review and decision are deferred to v0.6.159.

## Candidate implementation summary

This checkpoint adds a claim-safe External Review Package artifact for enterprise reviewers, vulnerability assessment company decision-makers, security architects, technical due-diligence reviewers, project sponsors, maintainers, and commercial reviewers.

The package integrates README positioning, Enterprise Review Guide, Technical Due Diligence Summary, Safe PoC Boundary Template, Control Matrix, Reviewer Walkthrough, test-family review paths, version records, and package-level claim boundaries.

The package is external-review-facing but remains non-authorizing.

It does not create a deployment guide, scanner operation guide, customer PoC authorization package, commercial contract, audit package, certification package, production readiness package, external-framework equivalence mapping, runtime authorization, scanner authorization, credential authorization, customer-target authorization, or delivery authorization.

## Candidate package artifact

~~~text
docs/external-review-package.md
~~~

## Package integration scope

The package includes:

* reader and purpose,
* non-authorizing notice,
* document inventory,
* recommended entry points,
* reviewer paths,
* evidence and test-family index,
* boundary and non-goal summary,
* package-level claim-boundary summary,
* questions the package can answer,
* questions the package cannot answer,
* when to use the Safe PoC Boundary Template,
* when not to request a PoC,
* what remains outside the public package,
* explicit non-goals,
* claim boundaries.

## Claim boundaries

The candidate package must not be interpreted as:

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

The package may help reviewers safely navigate the current AAEF-AI-VA documentation and evidence-boundary materials.

## Candidate tests

This checkpoint adds:

~~~text
tools/test_v06158_external_review_package_integration_candidate.py
~~~

The tests cover:

* package file existence,
* required reader/purpose sections,
* non-authorizing notice,
* document inventory,
* recommended entry points,
* reviewer paths,
* evidence/test-family index,
* boundary and non-goal summary,
* package-level claim-boundary summary,
* questions the package can and cannot answer,
* Safe PoC Boundary Template use guidance,
* when not to request a PoC,
* outside-public-package boundaries,
* explicit non-goals,
* claim boundaries,
* v0.6.157 selection continuity,
* v0.6.159 review/decision deferral,
* absence of forbidden affirmative claims.

## Candidate record

~~~text
external_review_package_integration_candidate_completed = true
external_review_package_integration_candidate_is_medium_risk = true
external_review_package_integration_candidate_checkpoint_1_of_2 = true
external_review_package_integration_review_decision_deferred_to_v06159 = true
external_review_package_created = true
external_review_package_candidate_claim_safe = true
external_review_package_reader_identified = true
external_review_package_purpose_included = true
external_review_package_non_authorizing_notice_included = true
external_review_package_document_inventory_included = true
external_review_package_recommended_entry_points_included = true
external_review_package_reviewer_paths_included = true
external_review_package_evidence_test_family_index_included = true
external_review_package_boundary_non_goal_summary_included = true
external_review_package_claim_boundary_summary_included = true
external_review_package_questions_can_answer_included = true
external_review_package_questions_cannot_answer_included = true
external_review_package_safe_poc_template_use_guidance_included = true
external_review_package_when_not_to_request_poc_included = true
external_review_package_outside_public_package_included = true
external_review_package_explicit_non_goals_included = true
external_review_package_review_decision_completed = false
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
reviewer_walkthrough_modified = false
control_matrix_modified = false
safe_poc_boundary_template_modified = false
technical_due_diligence_summary_modified = false
enterprise_review_guide_modified = false
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
selected_next_checkpoint = v0.6.159 External Review Package Integration Review and Decision
~~~

## What changed

The following files are added:

~~~text
docs/external-review-package.md
docs/234-v06158-external-review-package-integration-candidate.md
planning/decisions/ADR-0228-add-v06158-external-review-package-integration-candidate.md
planning/issues/0227-add-v06158-external-review-package-integration-candidate.md
tools/test_v06158_external_review_package_integration_candidate.py
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

No Reviewer Walkthrough is modified.

No Control Matrix is modified.

No Safe PoC Boundary Template is modified.

No Technical Due Diligence Summary is modified.

No Enterprise Review Guide is modified.

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

## Relationship to v0.6.157

v0.6.157 selected External Review Package Integration as a Medium-risk work item and assigned two checkpoints:

~~~text
v0.6.158 External Review Package Integration Candidate
v0.6.159 External Review Package Integration Review and Decision
~~~

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.156

v0.6.156 closed the Reviewer Walkthrough work item.

This checkpoint builds on that accepted walkthrough by adding a package-level external review entry point.

## Relationship to v0.6.153

v0.6.153 closed the Control Matrix work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.150

v0.6.150 closed the Safe PoC Boundary Template work item.

This checkpoint does not modify that completed work.

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
v0.6.159 External Review Package Integration Review and Decision
~~~

That checkpoint should review the package artifact, confirm claim boundaries, and decide whether to close the Medium-risk work item.
