# Safe Demo Fixture Set Planning

Status: draft_candidate
Version: v0.6.189
Date: 2026-05-13

## Purpose

This planning document supports the accepted Safe Demo Artifact Planning document.

The plan is documentation-only at this checkpoint.

No fixture files are added by this planning document.

No public samples are added by this planning document.

No executable demo artifact is added by this planning document.

The purpose is to define the fixture set that could later support the accepted Blocked Tool Action Request Review scenario while preserving static, mock, non-execution, and reviewer-facing boundaries.

## Supported planning chain

Accepted scenario:

~~~text
Blocked Tool Action Request Review
~~~

Accepted artifact plan:

~~~text
Safe Demo Artifact Planning
~~~

Planned fixture set focus:

~~~text
request fixture -> gate decision fixture -> non-execution result fixture -> evidence trace fixture -> reviewer walkthrough
~~~

The fixture plan should support the accepted scenario and artifact plan without introducing runtime execution, scanner execution, Docker execution, credential use, customer-target activity, customer PoC intake, or delivery authorization.

## Fixture inventory

A later fixture set should likely include:

| Planned fixture | Intended role | Public candidate | Added now |
| --- | --- | --- | --- |
| request fixture | Shows an AI-generated request as a proposal, not authority | yes | no |
| gate decision fixture | Shows the gate decision that blocks or does not execute the request | yes | no |
| non-execution result fixture | Shows that execution did not occur | yes | no |
| evidence trace fixture | Links request, decision, non-execution, and reviewer conclusion | yes | no |
| reviewer walkthrough | Explains the expected reviewer path across fixtures | yes | no |
| private generation notes | Records maintainer-only generation context if needed | no | no |
| validator expectation notes | Defines future static checks without changing validators now | maybe | no |

## Fixture file boundary

Fixture files should be static data.

They should not call tools.

They should not import runtime modules.

They should not contain executable instructions.

They should not contain live endpoints.

They should not contain credentials.

They should not contain customer-specific material.

They should not imply that scanner execution occurred.

They should not imply that diagnostic coverage or completeness was achieved.

## Request fixture boundary

The request fixture should show the AI request as a proposal.

Expected future fields may include:

~~~text
request_id
request_kind
requested_action
target_ref
requested_by
execution_mode
requested_at
scope_ref
~~~

The request fixture should not include a real target, a real credential, a real customer identifier, or an instruction that executes a scanner.

## Gate decision fixture boundary

The gate decision fixture should show that execution authority is separated from the AI request.

Expected future fields may include:

~~~text
decision_id
request_id
decision
decision_reason
execution_permitted
human_approval_required
scope_checked
preflight_checked
~~~

The decision fixture should be able to represent a blocked or non-executed request.

It should not approve real execution.

## Non-execution result fixture boundary

The non-execution result fixture should make non-execution explicit.

Expected future fields may include:

~~~text
result_id
request_id
decision_id
execution_occurred
execution_permitted
result_status
review_status
~~~

A valid future fixture may show:

~~~text
execution_permitted = false
execution_occurred = false
review_status = blocked_request_reviewable
~~~

The result fixture should not use wording that implies completed live testing.

## Evidence trace fixture boundary

The evidence trace fixture should connect the chain.

Expected future links:

~~~text
tool_action_request -> gate_decision -> non_execution_result -> reviewer_evidence_record
~~~

Expected future review questions:

* What was requested?
* What decision was made?
* Why was execution not permitted?
* Did execution occur?
* What evidence proves the answer?
* What should a reviewer conclude?

The evidence trace fixture should demonstrate reviewability, not diagnostic power.

## Reviewer walkthrough boundary

The reviewer walkthrough should be a static guide.

It should show the intended inspection sequence:

1. Open the request fixture.
2. Open the gate decision fixture.
3. Open the non-execution result fixture.
4. Open the evidence trace fixture.
5. Confirm that AI output did not become authority.
6. Confirm that the gate decision explains non-execution.
7. Confirm that the evidence trace supports the conclusion.

The walkthrough should not instruct users to scan a target, execute tools, run Docker, enter credentials, or test third-party systems.

## Static validation expectations

Future static validation should likely check:

* all fixture identifiers are internally consistent,
* the gate decision references the request fixture,
* the non-execution result references the request and decision,
* the evidence trace references the request, decision, and result,
* execution is explicitly not permitted,
* execution is explicitly not observed,
* no live endpoint or credential-like values are present,
* no customer-specific values are present,
* no production-readiness or diagnostic-completeness claims are present.

This checkpoint does not modify validator behavior.

This checkpoint does not add JSON Schema.

## File naming expectations

Future fixture files should use names that make the order and purpose clear.

Candidate names:

~~~text
request.fixture.json
gate-decision.fixture.json
non-execution-result.fixture.json
evidence-trace.fixture.json
reviewer-walkthrough.md
~~~

The final path is not selected in this checkpoint.

A later fixture creation work item should decide exact paths.

## Public and private fixture distinction

Public fixture candidates should be static, sanitized, mock, and reviewable.

Private-not-in-git material should be used for:

* local scratch generation,
* maintainer review notes,
* discarded drafts,
* anything that could be confused with a real customer result,
* anything that includes sensitive or patent-sensitive implementation detail.

Private material should not be promoted without an explicit later review decision.

## Future fixture creation sequence

A later sequence should likely be:

1. Accept this fixture set plan.
2. Select fixture file paths.
3. Create static fixture candidates.
4. Add or update static validation only if explicitly selected.
5. Review fixture publication boundaries.
6. Add README navigation only after the fixture set is accepted.
7. Consider public demo readiness review after fixture acceptance.

This sequence intentionally keeps fixture creation separate from runtime/scanner readiness.

## Fixtures intentionally not created yet

This planning document intentionally does not create:

* request fixture file,
* gate decision fixture file,
* non-execution result fixture file,
* evidence trace fixture file,
* reviewer walkthrough file,
* public sample files,
* JSON Schema files,
* validator behavior,
* executable demo wrapper,
* runtime behavior,
* scanner adapters,
* Docker execution,
* credential handling,
* customer-target records,
* customer PoC materials,
* delivery materials,
* commercial terms.

## Candidate record

~~~text
safe_demo_fixture_set_planning_candidate_completed = true
safe_demo_fixture_set_planning_candidate_is_medium_risk = true
safe_demo_fixture_set_planning_candidate_checkpoint_1_of_2 = true
safe_demo_fixture_set_planning_review_decision_deferred_to_v06190 = true
safe_demo_fixture_set_planning_created = true
safe_demo_fixture_set_planning_status = draft_candidate
safe_demo_fixture_set_planning_claim_safe = true
safe_demo_fixture_set_planning_is_documentation_only = true
safe_demo_fixture_set_planning_supports_accepted_artifact_plan = true
safe_demo_artifact_planning_status = accepted
safe_demo_artifact_planning_supports_accepted_scenario = true
safe_demo_scenario_definition_status = accepted
safe_demo_scenario_story = blocked_tool_action_request_review
safe_demo_scenario_focus = request_gate_evidence_trace
safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace
fixture_inventory_defined = true
fixture_file_boundary_defined = true
request_fixture_boundary_defined = true
gate_decision_fixture_boundary_defined = true
non_execution_result_fixture_boundary_defined = true
evidence_trace_fixture_boundary_defined = true
reviewer_walkthrough_boundary_defined = true
static_validation_expectations_defined = true
file_naming_expectations_defined = true
public_private_fixture_distinction_defined = true
fixture_creation_sequence_defined = true
fixture_files_created = false
public_samples_created = false
actual_fixture_creation_deferred = true
safe_demo_artifact_creation_deferred = true
public_demo_artifact_creation_deferred = true
executable_demo_creation_deferred = true
runtime_scanner_readiness_deferred = true
commercial_inquiry_response_boundary_deferred = true
commercial_inquiry_response_template_deferred = true
public_demo_positioning_work_item_closed = true
current_state_executive_summary_work_item_closed = true
documentation_and_review_package_layer_status = implemented
safe_demo_layer_status = near_term_candidate
runtime_scanner_layer_status = deferred_pending_readiness_review
customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries
aaef_ai_va_interim_inquiry_route_continues = true
aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com
aaef_main_contact_publication_remains_deferred = true
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
review_decision_completed = false
safe_demo_fixture_set_planning_review_decision_completed = false
fixture_set_created = false
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
selected_next_checkpoint = v0.6.190 Safe Demo Fixture Set Planning Review and Decision
~~~

## Next checkpoint

Proceed to:

~~~text
v0.6.190 Safe Demo Fixture Set Planning Review and Decision
~~~
