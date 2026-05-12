# Safe Demo Scenario Definition

Status: draft_candidate
Version: v0.6.183
Date: 2026-05-12

## Purpose

This document defines the first safe demo scenario for AAEF-AI-VA.

The first safe demo should show the authority boundary, not live diagnostic power.

~~~text
AI may generate a tool_action_request, but execution is decided by gates.
~~~

The scenario is documentation-only at this checkpoint.

No executable demo artifact is added by this scenario definition.

## Scenario summary

Scenario name: Blocked Tool Action Request Review

Primary outcome: blocked or non-executed request with reviewable evidence.

The scenario uses mock or fixture-only inputs.

The scenario should not require runtime execution.

The scenario should not require scanner execution.

The scenario should not require a customer target.

The scenario should show that a model-generated request can be reviewed, constrained, blocked, and evidenced without treating model output as authority.

## Demo objective

The safe demo should answer one question clearly:

~~~text
Can a reviewer see why an AI-generated diagnostic request did not become an authorized tool action?
~~~

The expected answer is yes.

The demo should focus on the chain from request to gate decision to evidence.

## Scenario flow

| Step | Scenario element | Expected public demonstration |
| --- | --- | --- |
| 1 | Request | A mock AI component proposes a diagnostic action as a `tool_action_request`. |
| 2 | Scope input | The request references an intentionally limited demo scope. |
| 3 | Gate decision | The gate evaluates the request against authorization, scope, and preflight expectations. |
| 4 | Outcome | The request is blocked or held as non-executed. |
| 5 | Evidence trace | The evidence record links request, decision, non-execution, and reviewer explanation. |
| 6 | Reviewer view | A reviewer can inspect what was requested, why it was not executed, and what evidence proves that state. |

## Request

The request should be represented as a safe, non-operational request object.

Example request shape:

~~~text
request_id = demo-request-001
request_kind = mock_diagnostic_request
requested_action = mock_http_header_review
target_ref = demo_fixture_target
requested_by = ai_assistant_demo
execution_mode = non_execution
~~~

The request should be treated as a proposal only.

It should not be treated as execution authority.

## Gate decision

The gate decision should demonstrate that execution authority is separate from the request.

Example decision shape:

~~~text
decision_id = demo-decision-001
request_id = demo-request-001
decision = blocked
decision_reason = preflight_evidence_missing_or_execution_not_authorized
execution_permitted = false
human_approval_required = false
~~~

A blocked decision is acceptable for the first demo.

Blocked execution can be a valid demo outcome.

## Authorization and scope inputs

The scenario should include placeholder inputs showing what the gate considered.

Expected inputs:

* declared demo scope,
* action category,
* execution mode,
* target reference,
* preflight evidence expectation,
* runtime authorization status,
* reviewer-facing explanation.

The values should remain mock, fixture, or documentation-only until a later implementation checkpoint explicitly changes scope.

## Preflight expectation placeholders

The scenario may include preflight expectation placeholders such as:

~~~text
preflight_expected = true
preflight_satisfied = false
execution_authorized = false
real_execution_permitted = false
~~~

These placeholders should show why a request cannot proceed.

They should not imply that live preflight evidence has been collected.

## Evidence trace

Evidence trace should be the core of the scenario.

Expected evidence questions:

* Who or what generated the request?
* What was requested?
* What scope and authorization inputs were considered?
* What gate decision was made?
* Was execution permitted?
* Did execution occur?
* What evidence proves execution or non-execution?
* What should a reviewer conclude?

Expected evidence links:

~~~text
tool_action_request -> gate_decision -> non_execution_result -> reviewer_evidence_record
~~~

## Reviewer questions

The scenario should help a reviewer answer:

1. Was the AI output treated as a request rather than authority?
2. Was execution decided by a gate?
3. Was the request within the declared demo scope?
4. Was the decision recorded?
5. Was execution blocked or non-executed?
6. Does the evidence show why?
7. Does the demo avoid implying live scanner coverage?
8. Does the demo avoid implying customer PoC approval?

## Public explanation

A safe public explanation may say:

~~~text
This scenario demonstrates how AAEF-AI-VA separates an AI-generated diagnostic request from execution authority. The demo focuses on a blocked or non-executed request and the evidence that allows a reviewer to inspect the decision.
~~~

## Intentionally not demonstrated

This scenario intentionally does not demonstrate:

* live scanner execution,
* runtime execution,
* Docker execution,
* credential injection,
* customer-target activity,
* customer PoC approval,
* commercial contract creation,
* commercial license terms,
* paid engagement approval,
* delivery approval,
* production readiness,
* diagnostic completeness,
* certification,
* legal compliance determination,
* audit opinion,
* external-framework equivalence.

## Relationship to accepted public demo positioning

v0.6.179 accepted Public Demo Positioning.

This scenario follows that accepted positioning by preferring a blocked or non-executed evidence trace before any live scanner or customer-target activity.

## Candidate record

~~~text
safe_demo_scenario_definition_candidate_completed = true
safe_demo_scenario_definition_candidate_is_medium_risk = true
safe_demo_scenario_definition_candidate_checkpoint_1_of_2 = true
safe_demo_scenario_definition_review_decision_deferred_to_v06184 = true
safe_demo_scenario_definition_created = true
safe_demo_scenario_definition_status = draft_candidate
safe_demo_scenario_definition_claim_safe = true
safe_demo_scenario_story = blocked_tool_action_request_review
safe_demo_scenario_focus = request_gate_evidence_trace
safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace
safe_demo_scenario_is_documentation_only = true
safe_demo_scenario_uses_mock_or_fixture_only = true
safe_demo_scenario_uses_local_only_if_later_implemented = true
safe_demo_scenario_does_not_require_runtime_execution = true
safe_demo_scenario_does_not_require_scanner_execution = true
safe_demo_scenario_does_not_require_customer_target = true
tool_action_request_boundary_included = true
gate_decision_boundary_included = true
authorization_scope_inputs_included = true
preflight_expectation_placeholders_included = true
evidence_trace_expectations_included = true
blocked_execution_outcome_included = true
non_execution_outcome_included = true
reviewer_questions_included = true
intentionally_not_demonstrated_section_included = true
documentation_and_review_package_layer_status = implemented
safe_demo_layer_status = near_term_candidate
runtime_scanner_layer_status = deferred_pending_readiness_review
customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries
commercial_inquiry_response_boundary_deferred = true
commercial_inquiry_response_template_deferred = true
public_demo_positioning_work_item_closed = true
current_state_executive_summary_work_item_closed = true
aaef_ai_va_interim_inquiry_route_continues = true
aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com
aaef_main_contact_publication_remains_deferred = true
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
review_decision_completed = false
safe_demo_scenario_definition_review_decision_completed = false
safe_demo_created = false
public_demo_created = false
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
selected_next_checkpoint = v0.6.184 Safe Demo Scenario Definition Review and Decision
~~~

## Next checkpoint

Proceed to:

~~~text
v0.6.184 Safe Demo Scenario Definition Review and Decision
~~~
