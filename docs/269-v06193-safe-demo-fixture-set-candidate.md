# v0.6.193 Safe Demo Fixture Set Candidate

Status: candidate
Date: 2026-05-13

## Purpose

This checkpoint is checkpoint 2 of 3 for the High-risk Safe Demo Fixture Set Creation work item.

This checkpoint creates only static, mock, non-execution fixture candidates within the v0.6.192 readiness scope.

The review and decision are deferred to v0.6.194.

This checkpoint creates fixture files.

This checkpoint does not create public samples.

This checkpoint does not create a safe demo.

This checkpoint does not create a public demo.

This checkpoint does not create an executable demo.

## Fixture path

The fixture set candidate is created under:

~~~text
docs/examples/safe-demo/blocked-tool-action-request-review/
~~~

This path is selected from the v0.6.192 allowed path candidates and keeps the fixture set together.

## Fixture files created

This checkpoint creates the following static files:

~~~text
docs/examples/safe-demo/blocked-tool-action-request-review/request.fixture.json
docs/examples/safe-demo/blocked-tool-action-request-review/gate-decision.fixture.json
docs/examples/safe-demo/blocked-tool-action-request-review/non-execution-result.fixture.json
docs/examples/safe-demo/blocked-tool-action-request-review/evidence-trace.fixture.json
docs/examples/safe-demo/blocked-tool-action-request-review/reviewer-walkthrough.md
~~~

## Request fixture

The request fixture records a model-generated tool action request as a proposal only.

It explicitly records that model output is not authority and that a gate decision is required before execution.

## Gate decision fixture

The gate decision fixture records a blocked decision.

It sets:

~~~text
execution_permitted = false
execution_occurred = false
dispatch_allowed = false
~~~

## Non-execution result fixture

The non-execution result fixture records that execution did not occur.

It sets:

~~~text
execution_permitted = false
execution_occurred = false
result_status = non_executed_blocked
review_status = blocked_request_reviewable
~~~

## Evidence trace fixture

The evidence trace fixture links:

~~~text
tool_action_request -> gate_decision -> non_execution_result
~~~

It records the reviewer conclusion that AI output did not become authority, the gate controlled execution, execution was not permitted, and execution did not occur.

## Reviewer walkthrough

The reviewer walkthrough is static documentation.

It explains how to inspect the fixture set and confirms that no tool, runtime, Docker, sensitive value, target testing, or delivery action is instructed.

## Static fixture consistency

The fixture identifiers are intentionally stable:

~~~text
request_id = demo-request-0001
decision_id = demo-decision-0001
result_id = demo-result-0001
trace_id = demo-trace-0001
scenario_id = blocked-tool-action-request-review
~~~

The request, decision, result, and trace fixtures reference each other through these identifiers.

## Publication boundary

The fixture set is static, mock, fixture-only, non-execution, and reviewer-facing.

It is not a scanner, not a runtime demo, not a public demo, not PoC material, not delivery material, not production readiness evidence, not diagnostic completeness evidence, and not authorization to test third-party systems.

## Candidate record

~~~text
safe_demo_fixture_set_candidate_completed = true
safe_demo_fixture_set_candidate_is_high_risk = true
safe_demo_fixture_set_candidate_checkpoint_2_of_3 = true
safe_demo_fixture_set_creation_readiness_review_completed = true
safe_demo_fixture_set_creation_readiness_accepted = true
safe_demo_fixture_set_review_decision_deferred_to_v06194 = true
safe_demo_fixture_set_candidate_created = true
safe_demo_fixture_set_status = draft_candidate
safe_demo_fixture_set_claim_safe = true
safe_demo_fixture_set_is_static = true
safe_demo_fixture_set_is_mock = true
safe_demo_fixture_set_is_non_execution = true
safe_demo_fixture_set_is_reviewer_facing = true
safe_demo_fixture_set_supports_accepted_fixture_plan = true
safe_demo_fixture_set_supports_accepted_artifact_plan = true
safe_demo_fixture_set_supports_accepted_scenario = true
safe_demo_fixture_set_path = docs/examples/safe-demo/blocked-tool-action-request-review
safe_demo_fixture_set_allowed_file_types_respected = true
fixture_set_created = true
fixture_files_created = true
request_fixture_created = true
gate_decision_fixture_created = true
non_execution_result_fixture_created = true
evidence_trace_fixture_created = true
reviewer_walkthrough_created = true
request_fixture_static_mock_non_execution = true
gate_decision_fixture_blocks_execution = true
non_execution_result_fixture_records_no_execution = true
evidence_trace_fixture_links_request_decision_result = true
reviewer_walkthrough_is_static_documentation = true
fixture_identifier_consistency_checked = true
fixture_publication_boundary_preserved = true
safe_demo_fixture_set_planning_status = accepted
safe_demo_artifact_planning_status = accepted
safe_demo_scenario_definition_status = accepted
safe_demo_scenario_story = blocked_tool_action_request_review
safe_demo_scenario_focus = request_gate_evidence_trace
safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace
commercial_inquiry_response_boundary_deferred = true
commercial_inquiry_response_template_deferred = true
documentation_and_review_package_layer_status = implemented
safe_demo_layer_status = near_term_candidate
runtime_scanner_layer_status = deferred_pending_readiness_review
customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries
aaef_ai_va_interim_inquiry_route_continues = true
aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com
aaef_main_contact_publication_remains_deferred = true
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_repository_modified = false
aaef_main_contact_publication_modified = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
public_samples_created = false
safe_demo_created = false
public_demo_created = false
executable_demo_created = false
runtime_scanner_readiness_created = false
real_scanner_execution_selected = false
runtime_execution_selected = false
customer_poc_intake_selected = false
runtime_behavior_modified = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
customer_poc_authorized = false
commercial_contract_created = false
paid_engagement_approved = false
commercial_license_terms_created = false
customer_specific_material_created = false
delivery_authorized = false
validator_behavior_modified = false
metadata_level_expected_failure_category_added = false
json_schema_added = false
public_sample_changed = false
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
selected_next_checkpoint = v0.6.194 Safe Demo Fixture Set Review and Decision
~~~

## What changed

The following files are added:

~~~text
docs/examples/safe-demo/blocked-tool-action-request-review/request.fixture.json
docs/examples/safe-demo/blocked-tool-action-request-review/gate-decision.fixture.json
docs/examples/safe-demo/blocked-tool-action-request-review/non-execution-result.fixture.json
docs/examples/safe-demo/blocked-tool-action-request-review/evidence-trace.fixture.json
docs/examples/safe-demo/blocked-tool-action-request-review/reviewer-walkthrough.md
docs/269-v06193-safe-demo-fixture-set-candidate.md
planning/decisions/ADR-0263-add-v06193-safe-demo-fixture-set-candidate.md
planning/issues/0262-add-v06193-safe-demo-fixture-set-candidate.md
tools/test_v06193_safe_demo_fixture_set_candidate.py
~~~

The following files are updated for navigation and checks:

~~~text
README.md
CHANGELOG.md
ROADMAP.md
tools/run_all_local_checks.py
~~~

## What did not happen

The review/decision closeout remains incomplete.

Public samples remain unchanged in this checkpoint.

The safe demo artifact remains uncreated in this checkpoint.

The public demo artifact remains uncreated in this checkpoint.

The executable demo artifact remains uncreated in this checkpoint.

Runtime/scanner readiness remains uncreated in this checkpoint.

Real scanner execution remains unselected in this checkpoint.

Runtime execution remains unselected in this checkpoint.

PoC intake remains unselected in this checkpoint.

Commercial Inquiry Response Boundary remains deferred.

The commercial inquiry response template remains deferred.

No AAEF main contact publication occurs.

No AAEF main repository is modified.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is generated.

No AAEF main handback sequence is reopened.

No PoC approval occurs.

No commercial contract creation occurs.

No commercial license terms are published.

No paid engagement approval occurs.

No specific external-party material is created.

No validator behavior is modified.

No JSON Schema is added.

No public sample is changed.

No runtime behavior is modified.

No runtime, scanner, Docker, sensitive value, target, or delivery authorization occurs.

No certification, legal compliance, audit opinion, production readiness, external-framework equivalence, diagnostic completeness, or third-party-testing authorization claim occurs.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.192

v0.6.192 accepted readiness for a constrained static fixture-set candidate.

This checkpoint creates only the allowed static fixture candidates.

## Relationship to v0.6.191

v0.6.191 selected Safe Demo Fixture Set Creation as a High-risk work item and assigned three checkpoints.

This checkpoint is the candidate implementation checkpoint.

## Relationship to v0.6.190

v0.6.190 reviewed and accepted the Safe Demo Fixture Set Planning candidate.

This checkpoint follows that accepted fixture set plan.

## Relationship to v0.6.184

v0.6.184 reviewed and accepted the Safe Demo Scenario Definition candidate.

This checkpoint supports the accepted Blocked Tool Action Request Review scenario.

## Relationship to v0.6.181

v0.6.181 deferred Commercial Inquiry Response Boundary before candidate creation because demo/story readiness should come first.

This checkpoint keeps commercial inquiry response deferred.

## Relationship to v0.6.172

v0.6.172 deferred AAEF main contact publication.

This checkpoint preserves that deferral.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This checkpoint follows the High-risk three-checkpoint pattern selected in v0.6.191.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.194 Safe Demo Fixture Set Review and Decision
~~~
