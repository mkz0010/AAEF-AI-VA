# v0.6.143 Enterprise Review Guide Candidate

Status: candidate
Date: 2026-05-10

## Purpose

This checkpoint implements the Enterprise Review Guide candidate after v0.6.142 selected the work item.

This is checkpoint 1 of 2 for a Medium-risk buyer/reviewer-facing documentation work item.

This checkpoint creates the Enterprise Review Guide candidate.

The review and decision are deferred to v0.6.144.

## Candidate implementation summary

This checkpoint adds a claim-safe enterprise review guide for enterprise reviewers, vulnerability assessment company decision-makers, security architects, and technical reviewers.

The guide explains what AAEF-AI-VA demonstrates, what it does not demonstrate, what reviewers should inspect, and which claim boundaries must remain conservative.

The guide is buyer/reviewer-facing but remains non-authorizing.

## Candidate guide

~~~text
docs/enterprise-review-guide.md
~~~

The guide includes:

* reader and purpose,
* decision-maker summary,
* what AAEF-AI-VA demonstrates,
* what AAEF-AI-VA does not demonstrate,
* review path,
* evidence review questions,
* gate-semantics review questions,
* demo boundary review,
* deployment due-diligence prompts,
* commercial evaluation boundary,
* claim boundaries,
* suggested review outcome categories,
* reviewer notes.

## Claim boundaries

The candidate guide must not be interpreted as:

~~~text
certification
legal compliance determination
audit opinion
audit sufficiency determination
deployment approval
complete vulnerability assessment capability
authorization for testing third-party systems
equivalence mapping to external frameworks
proof that AI can safely run tools without gates
promotion into AAEF Core/Profile/Practical Package status
~~~

The guide may describe AAEF-AI-VA as a safety-first reference implementation for reviewable control boundaries around AI-assisted vulnerability assessment action requests.

## Candidate tests

This checkpoint adds:

~~~text
tools/test_v06143_enterprise_review_guide_candidate.py
~~~

The tests cover guide file existence, required reviewer-facing sections, conservative claim boundaries, v0.6.142 selection continuity, v0.6.144 review/decision deferral, and absence of forbidden affirmative claims.

## Candidate record

~~~text
enterprise_review_guide_candidate_completed = true
enterprise_review_guide_candidate_is_medium_risk = true
enterprise_review_guide_candidate_checkpoint_1_of_2 = true
enterprise_review_guide_review_decision_deferred_to_v06144 = true
enterprise_review_guide_created = true
enterprise_review_guide_candidate_claim_safe = true
enterprise_review_guide_target_reader_identified = true
enterprise_review_guide_project_positioning_included = true
enterprise_review_guide_review_questions_included = true
enterprise_review_guide_evidence_review_path_included = true
enterprise_review_guide_gate_semantics_review_included = true
enterprise_review_guide_demo_boundary_included = true
enterprise_review_guide_non_goals_included = true
enterprise_review_guide_deployment_due_diligence_prompts_included = true
enterprise_review_guide_commercial_evaluation_boundary_included = true
enterprise_review_guide_review_decision_completed = false
review_decision_completed = false
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
technical_due_diligence_summary_created = false
safe_poc_boundary_template_created = false
control_matrix_created = false
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
selected_next_checkpoint = v0.6.144 Enterprise Review Guide Review and Decision
~~~

## What changed

The following files are added:

~~~text
docs/enterprise-review-guide.md
docs/219-v06143-enterprise-review-guide-candidate.md
planning/decisions/ADR-0213-add-v06143-enterprise-review-guide-candidate.md
planning/issues/0212-add-v06143-enterprise-review-guide-candidate.md
tools/test_v06143_enterprise_review_guide_candidate.py
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

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

No technical due diligence summary is created.

No safe PoC boundary template is created.

No control matrix is created.

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

## Relationship to v0.6.142

v0.6.142 selected Enterprise Review Guide as a Medium-risk work item and assigned two checkpoints:

~~~text
v0.6.143 Enterprise Review Guide Candidate
v0.6.144 Enterprise Review Guide Review and Decision
~~~

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.141

v0.6.141 closed the mock/dry-run `completed` status terminology cleanup work item.

This checkpoint builds on that claim-safety cleanup by adding buyer/reviewer-facing guidance.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.144 Enterprise Review Guide Review and Decision
~~~

That checkpoint should review the guide, confirm claim boundaries, and decide whether to close the Medium-risk work item.
