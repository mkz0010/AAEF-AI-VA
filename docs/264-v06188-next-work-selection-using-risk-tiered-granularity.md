# v0.6.188 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-12

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.187 closed the Safe Demo Artifact Planning work item.

## Decision

The selected next work item is Safe Demo Fixture Set Planning.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.189 Safe Demo Fixture Set Planning Candidate.

The follow-up checkpoint is v0.6.190 Safe Demo Fixture Set Planning Review and Decision.

This checkpoint does not create the Safe Demo Fixture Set Planning artifact.

This checkpoint does not create fixture files.

This checkpoint does not create public samples.

This checkpoint does not create a safe demo.

This checkpoint does not create a public demo.

This checkpoint does not create an executable demo.

This checkpoint does not start runtime or scanner work.

This checkpoint does not authorize customer PoC intake.

This checkpoint does not modify runtime behavior.

This checkpoint does not modify validator behavior.

This checkpoint does not add a JSON Schema.

No AAEF main issue is opened.

No issue creation command is generated.

No issue URL is created.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06188_completed = true
next_work_selection_v06188_is_documentation_only = true
next_work_selection_v06188_uses_v06120_granularity_policy = true
next_work_selection_v06188_uses_v06187_safe_demo_artifact_planning_closeout = true
v06188_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = safe_demo_fixture_set_planning
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.189 Safe Demo Fixture Set Planning Candidate
selected_followup_checkpoint = v0.6.190 Safe Demo Fixture Set Planning Review and Decision
safe_demo_fixture_set_planning_selected = true
safe_demo_fixture_set_planning_created = false
safe_demo_fixture_set_planning_review_decision_completed = false
safe_demo_artifact_planning_work_item_closed = true
safe_demo_artifact_planning_status = accepted
safe_demo_artifact_planning_supports_accepted_scenario = true
safe_demo_scenario_definition_work_item_closed = true
safe_demo_scenario_definition_status = accepted
safe_demo_scenario_story = blocked_tool_action_request_review
safe_demo_scenario_focus = request_gate_evidence_trace
safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace
commercial_inquiry_response_boundary_deferred = true
commercial_inquiry_response_template_deferred = true
public_demo_positioning_work_item_closed = true
current_state_executive_summary_work_item_closed = true
documentation_and_review_package_layer_status = implemented
safe_demo_layer_status = near_term_candidate
runtime_scanner_layer_status = deferred_pending_readiness_review
customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries
safe_demo_fixture_set_planning_should_follow_accepted_artifact_plan = true
safe_demo_fixture_set_planning_should_define_fixture_inventory = true
safe_demo_fixture_set_planning_should_define_fixture_file_boundaries = true
safe_demo_fixture_set_planning_should_define_request_fixture_boundary = true
safe_demo_fixture_set_planning_should_define_gate_decision_fixture_boundary = true
safe_demo_fixture_set_planning_should_define_non_execution_result_fixture_boundary = true
safe_demo_fixture_set_planning_should_define_evidence_trace_fixture_boundary = true
safe_demo_fixture_set_planning_should_define_reviewer_walkthrough_boundary = true
safe_demo_fixture_set_planning_should_define_validation_expectations = true
safe_demo_fixture_set_planning_should_not_create_fixtures = true
safe_demo_fixture_set_planning_should_not_create_public_samples = true
safe_demo_fixture_set_planning_should_not_create_executable_demo = true
safe_demo_fixture_set_planning_should_not_modify_runtime_behavior = true
safe_demo_fixture_set_planning_should_not_modify_validator_behavior = true
safe_demo_fixture_set_planning_should_not_add_schema = true
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
fixture_set_created = false
fixture_files_created = false
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
~~~

## Candidate work items reviewed

| Candidate | Risk tier | Selected | Reason |
| --- | --- | --- | --- |
| Safe Demo Fixture Set Planning | Medium | yes | v0.6.187 accepted Safe Demo Artifact Planning. The next safe step is to plan the fixture set structure before creating any fixture files or public samples. |
| Safe Demo Fixture Set Candidate | High | no | Too early. Fixture set planning should precede creation of fixture files. |
| Repository Landing / Demo Path Clarity | Low or Medium | no | Useful soon, but should reference the fixture set plan once accepted. |
| Public Demo Readiness Review | Medium | no | Useful after fixture set planning is accepted. |
| Public Announcement Readiness Review | Low or Medium | no | Useful later, but public announcement should not precede clearer fixture set planning. |
| Commercial Inquiry Response Boundary | Medium | no | Deferred by v0.6.181 before candidate creation. |
| Runtime/Scanner Implementation Readiness Review | Medium or High | no | Still deferred. Fixture set planning should remain non-execution and not start runtime/scanner readiness. |
| Customer PoC Intake Boundary | Medium or High | no | Deferred pending commercial, scope, responsibility, authorization, and customer-target boundaries. |

## Selected work item

~~~text
selected_next_work_item = safe_demo_fixture_set_planning
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to plan the fixture set that could later implement the accepted safe demo artifact plan.

It should define fixture inventory, fixture file boundaries, request fixture boundary, gate decision fixture boundary, non-execution result fixture boundary, evidence trace fixture boundary, reviewer walkthrough boundary, validation expectations, file naming expectations, and non-goals before any fixture file is created.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, fixture set planning can shape the concrete files that later become public. It can determine what examples are created, what evidence is shown, and how external reviewers interpret the difference between fixture, public sample, and executable demo.

Because of that implementation-direction and public-interpretation risk, it should use two checkpoints.

## Why not High or Critical risk

This work item should not create fixture files, create public samples, add schemas, change validators, create an executable demo, run scanners, change execution behavior, authorize runtime activity, approve customer targets, modify credential handling, create a customer PoC, create a commercial contract, approve delivery, or submit anything to AAEF main.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not merely an internal note.

It defines the plan that later fixture files may follow. It can influence repository structure, public reviewer navigation, evidence trace shape, static validation expectations, and the boundary between demonstration data and execution.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.189 Safe Demo Fixture Set Planning Candidate
v0.6.190 Safe Demo Fixture Set Planning Review and Decision
~~~

v0.6.189 should create the Safe Demo Fixture Set Planning candidate and tests.

v0.6.190 should review the candidate, confirm claim boundaries, and decide whether to close the work item.

## Expected Safe Demo Fixture Set Planning scope

The Safe Demo Fixture Set Planning candidate should likely cover:

* the accepted artifact plan being supported,
* fixture inventory,
* request fixture boundary,
* gate decision fixture boundary,
* non-execution result fixture boundary,
* evidence trace fixture boundary,
* reviewer walkthrough boundary,
* static validation expectations,
* file naming expectations,
* public/private fixture distinction,
* what fixture files must not be created yet,
* what runtime, scanner, Docker, credential, customer-target, delivery, commercial, and AAEF-main boundaries remain deferred,
* what wording should be avoided.

It should not create fixture files, create public samples, modify runtime behavior, modify validator behavior, add schema behavior, add scanner execution, add Docker execution, add credential use, add target use, approve customer PoC, or approve delivery.

## Claim boundaries for the selected work

The Safe Demo Fixture Set Planning candidate must not claim:

~~~text
actual fixture creation
public sample creation
actual safe demo creation
public demo creation
executable demo creation
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

The candidate may state that later fixture files should support the accepted Blocked Tool Action Request Review scenario using mock, fixture, non-execution, or local-only boundaries.

## What did not happen

The Safe Demo Fixture Set Planning artifact remains uncreated in this checkpoint.

Fixture files remain uncreated in this checkpoint.

Public samples remain unchanged in this checkpoint.

The safe demo artifact remains uncreated in this checkpoint.

The public demo artifact remains uncreated in this checkpoint.

The executable demo artifact remains uncreated in this checkpoint.

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

## Relationship to v0.6.187

v0.6.187 reviewed and accepted the Safe Demo Artifact Planning candidate and closed that Medium-risk work item.

This checkpoint selects Safe Demo Fixture Set Planning as the next work item consistent with that accepted artifact plan.

## Relationship to v0.6.184

v0.6.184 reviewed and accepted the Safe Demo Scenario Definition candidate.

The selected fixture set planning work item should support the accepted Blocked Tool Action Request Review scenario.

## Relationship to v0.6.181

v0.6.181 deferred Commercial Inquiry Response Boundary before candidate creation because demo/story readiness should come first.

This checkpoint continues that demo/story readiness path while keeping commercial inquiry response deferred.

## Relationship to v0.6.179

v0.6.179 reviewed and accepted the Public Demo Positioning candidate.

This checkpoint selects fixture set planning that should remain aligned with accepted public demo positioning.

## Relationship to v0.6.173

v0.6.173 recorded the safe demo layer as a near-term candidate while deferring runtime/scanner and customer PoC layers.

This checkpoint selects fixture planning work for that near-term safe demo layer without creating fixture files or demo artifacts.

## Relationship to v0.6.172

v0.6.172 deferred AAEF main contact publication.

This checkpoint preserves that deferral.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.188 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.189 Safe Demo Fixture Set Planning Candidate
~~~
