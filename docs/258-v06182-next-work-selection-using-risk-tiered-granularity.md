# v0.6.182 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-12

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.181 deferred Commercial Inquiry Response Boundary before candidate creation.

## Decision

The selected next work item is Safe Demo Scenario Definition.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.183 Safe Demo Scenario Definition Candidate.

The follow-up checkpoint is v0.6.184 Safe Demo Scenario Definition Review and Decision.

This checkpoint does not create the Safe Demo Scenario Definition artifact.

This checkpoint does not create a safe demo.

This checkpoint does not create a public demo.

This checkpoint does not start runtime or scanner work.

This checkpoint does not authorize customer PoC intake.

No AAEF main issue is opened.

No issue creation command is generated.

No issue URL is created.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06182_completed = true
next_work_selection_v06182_is_documentation_only = true
next_work_selection_v06182_uses_v06120_granularity_policy = true
next_work_selection_v06182_uses_v06181_deferral_decision = true
v06182_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = safe_demo_scenario_definition
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.183 Safe Demo Scenario Definition Candidate
selected_followup_checkpoint = v0.6.184 Safe Demo Scenario Definition Review and Decision
safe_demo_scenario_definition_selected = true
safe_demo_scenario_definition_created = false
safe_demo_scenario_definition_review_decision_completed = false
commercial_inquiry_response_boundary_deferred = true
commercial_inquiry_response_template_deferred = true
public_demo_positioning_work_item_closed = true
current_state_executive_summary_work_item_closed = true
documentation_and_review_package_layer_status = implemented
safe_demo_layer_status = near_term_candidate
runtime_scanner_layer_status = deferred_pending_readiness_review
customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries
safe_demo_should_precede_real_scanner_execution = true
non_execution_demo_is_preferred_first_demo = true
local_only_mock_or_fixture_demo_is_preferred_initial_implementation = true
blocked_execution_can_be_valid_demo_outcome = true
evidence_trace_should_be_demo_focus = true
safe_demo_scenario_should_define_request_gate_evidence_flow = true
safe_demo_scenario_should_not_create_runtime_execution = true
safe_demo_scenario_should_not_create_scanner_execution = true
safe_demo_scenario_should_not_create_customer_poc = true
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
~~~

## Candidate work items reviewed

| Candidate | Risk tier | Selected | Reason |
| --- | --- | --- | --- |
| Safe Demo Scenario Definition | Medium | yes | v0.6.181 deferred commercial inquiry response handling so demo/story readiness can come first. The next safe step is to define the scenario for a safe non-execution, mock, fixture, or local-only demonstration without creating the demo yet. |
| Public Demo Readiness Review | Medium | no | Useful soon, but the scenario definition should come first so readiness can evaluate a concrete intended demo path. |
| Repository Landing / Demo Path Clarity | Low or Medium | no | Useful soon, but it should follow or reference the selected safe demo scenario. |
| Public Announcement Readiness Review | Low or Medium | no | Useful soon, but public announcement should not precede clearer safe demo scenario definition. |
| Commercial Inquiry Response Boundary | Medium | no | Deferred by v0.6.181 before candidate creation. |
| Runtime/Scanner Implementation Readiness Review | Medium or High | no | Still deferred. Scenario definition should come before any readiness movement toward execution. |
| Customer PoC Intake Boundary | Medium or High | no | Deferred pending commercial, scope, responsibility, authorization, and customer-target boundaries. |

## Selected work item

~~~text
selected_next_work_item = safe_demo_scenario_definition
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to define what the first safe demo should show before any actual demo artifact is built.

It should make clear that the first demo should focus on request, gate decision, evidence traceability, and blocked or non-executed outcomes rather than live diagnostic power.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, demo scenario language can shape the next implementation path. If written poorly, it could imply live scanner execution, customer-target activity, production readiness, or customer PoC availability.

Because of that implementation-direction and public-interpretation risk, it should use two checkpoints.

## Why not High or Critical risk

This work item should not create an executable demo, run scanners, change execution behavior, authorize runtime activity, approve customer targets, modify credential handling, create a customer PoC, create a commercial contract, approve delivery, or submit anything to AAEF main.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not merely an internal note.

It defines the scenario that later implementation may follow. It can influence demo construction, public explanation, buyer interpretation, and the boundary between non-execution/mocked demonstration and live execution.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.183 Safe Demo Scenario Definition Candidate
v0.6.184 Safe Demo Scenario Definition Review and Decision
~~~

v0.6.183 should create the Safe Demo Scenario Definition candidate and tests.

v0.6.184 should review the candidate, confirm claim boundaries, and decide whether to close the work item.

## Expected Safe Demo Scenario Definition scope

The Safe Demo Scenario Definition candidate should likely cover:

* the first demo objective,
* the safe demo story,
* the actors or components involved,
* the AI-generated tool action request,
* the gate decision,
* authorization and scope inputs,
* preflight expectation placeholders,
* evidence records expected from the scenario,
* allowed non-execution or blocked-execution outcome,
* mock or fixture handling expectations,
* local-only constraints if used,
* reviewer questions answered by the scenario,
* what is intentionally not demonstrated,
* what wording should be avoided.

It should not create an actual demo, modify runtime behavior, add scanner execution, add Docker execution, add credential use, add target use, approve customer PoC, or approve delivery.

## Claim boundaries for the selected work

The Safe Demo Scenario Definition candidate must not claim:

~~~text
actual safe demo creation
public demo creation
runtime execution approval
scanner execution approval
Docker execution approval
credential use approval
customer target approval
authorization for third-party testing
customer PoC approval
commercial contract creation
commercial license terms publication
paid engagement approval
customer-specific material creation
customer delivery approval
certification
legal compliance
audit opinion
audit sufficiency
production readiness
production scanner status
diagnostic completeness
equivalence with external frameworks
AAEF Core/Profile/Practical Package promotion
AAEF main handback reopening
~~~

The candidate may state that the planned safe demo scenario should prefer non-execution, mock, fixture, or local-only forms and should focus on evidence traceability.

## What did not happen

The Safe Demo Scenario Definition artifact remains uncreated in this checkpoint.

The safe demo artifact remains uncreated in this checkpoint.

The public demo artifact remains uncreated in this checkpoint.

The Runtime/Scanner Implementation Readiness Review artifact remains uncreated in this checkpoint.

Real scanner execution remains unselected in this checkpoint.

Runtime execution remains unselected in this checkpoint.

Customer PoC intake remains unselected in this checkpoint.

Commercial Inquiry Response Boundary remains deferred.

The commercial inquiry response template remains deferred.

No AAEF main contact publication occurs.

No AAEF main repository is modified.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is generated.

No AAEF main handback sequence is reopened.

No customer PoC approval occurs.

No commercial contract creation occurs.

No commercial license terms are published.

No paid engagement approval occurs.

No customer-specific material is created.

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

## Relationship to v0.6.181

v0.6.181 deferred Commercial Inquiry Response Boundary before candidate creation because demo/story readiness should come first.

This checkpoint selects Safe Demo Scenario Definition as the next work item consistent with that deferral.

## Relationship to v0.6.179

v0.6.179 reviewed and accepted the Public Demo Positioning candidate and closed that Medium-risk work item.

This checkpoint selects a scenario-definition work item that follows the accepted public demo positioning.

## Relationship to v0.6.176

v0.6.176 reviewed and accepted the Current-State Executive Summary candidate and closed that Medium-risk work item.

The selected safe demo scenario definition should preserve that accepted current-state summary.

## Relationship to v0.6.173

v0.6.173 recorded the safe demo layer as a near-term candidate while deferring runtime/scanner and customer PoC layers.

This checkpoint selects a work item that starts defining that near-term layer without implementing it.

## Relationship to v0.6.172

v0.6.172 deferred AAEF main contact publication.

This checkpoint preserves that deferral.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.182 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.183 Safe Demo Scenario Definition Candidate
~~~
