# v0.6.191 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-13

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.190 closed the Safe Demo Fixture Set Planning work item.

## Decision

The selected next work item is Safe Demo Fixture Set Creation.

The selected next work item risk tier is High risk.

The selected checkpoint count is 3 checkpoints.

The next checkpoint is v0.6.192 Safe Demo Fixture Set Creation Readiness Review.

The follow-up checkpoint is v0.6.193 Safe Demo Fixture Set Candidate.

The final checkpoint is v0.6.194 Safe Demo Fixture Set Review and Decision.

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
next_work_selection_using_risk_tiered_granularity_v06191_completed = true
next_work_selection_v06191_is_documentation_only = true
next_work_selection_v06191_uses_v06120_granularity_policy = true
next_work_selection_v06191_uses_v06190_fixture_set_planning_closeout = true
v06191_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = safe_demo_fixture_set_creation
selected_next_work_item_risk_tier = high
selected_next_work_item_checkpoint_count = 3
selected_next_work_item_first_checkpoint = readiness_review
selected_next_work_item_second_checkpoint = candidate_implementation
selected_next_work_item_third_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.192 Safe Demo Fixture Set Creation Readiness Review
selected_followup_checkpoint = v0.6.193 Safe Demo Fixture Set Candidate
selected_final_checkpoint = v0.6.194 Safe Demo Fixture Set Review and Decision
safe_demo_fixture_set_creation_selected = true
safe_demo_fixture_set_creation_readiness_review_selected = true
safe_demo_fixture_set_candidate_selected_as_future_checkpoint = true
safe_demo_fixture_set_review_decision_selected_as_future_checkpoint = true
safe_demo_fixture_set_creation_created = false
safe_demo_fixture_set_creation_readiness_review_created = false
safe_demo_fixture_set_candidate_created = false
safe_demo_fixture_set_review_decision_completed = false
safe_demo_fixture_set_planning_work_item_closed = true
safe_demo_fixture_set_planning_status = accepted
safe_demo_fixture_set_planning_candidate_accepted = true
safe_demo_artifact_planning_status = accepted
safe_demo_scenario_definition_status = accepted
safe_demo_scenario_story = blocked_tool_action_request_review
safe_demo_scenario_focus = request_gate_evidence_trace
safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace
high_risk_three_checkpoint_pattern_selected = true
readiness_before_fixture_creation_required = true
fixture_creation_should_follow_accepted_fixture_plan = true
fixture_creation_should_remain_static_mock_and_non_execution = true
fixture_creation_should_create_only_safe_static_fixtures_if_later_approved = true
fixture_creation_should_include_publication_boundary_review = true
fixture_creation_should_include_static_validation_review = true
fixture_creation_should_not_modify_runtime_behavior = true
fixture_creation_should_not_authorize_runtime_execution = true
fixture_creation_should_not_authorize_scanner_execution = true
fixture_creation_should_not_authorize_customer_target_activity = true
fixture_creation_should_not_authorize_customer_poc = true
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
fixture_set_created = false
fixture_files_created = false
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
~~~

## Candidate work items reviewed

| Candidate | Risk tier | Selected | Reason |
| --- | --- | --- | --- |
| Safe Demo Fixture Set Creation | High | yes | v0.6.190 accepted fixture set planning. The next useful step is to move toward actual static fixture files, but only after a readiness review because fixture files may become public examples. |
| Repository Landing / Demo Path Clarity | Low or Medium | no | Useful after the first fixture set path is confirmed. |
| Public Demo Readiness Review | Medium | no | Useful after fixture candidates exist and are reviewed. |
| Public Announcement Readiness Review | Low or Medium | no | Useful later, but public announcement should not precede fixture creation readiness and fixture review. |
| Commercial Inquiry Response Boundary | Medium | no | Deferred by v0.6.181 before candidate creation. |
| Runtime/Scanner Implementation Readiness Review | Medium or High | no | Still deferred. Fixture set creation must remain static and non-execution. |
| Customer PoC Intake Boundary | Medium or High | no | Deferred pending commercial, scope, responsibility, authorization, and customer-target boundaries. |

## Selected work item

~~~text
selected_next_work_item = safe_demo_fixture_set_creation
selected_next_work_item_risk_tier = high
selected_next_work_item_checkpoint_count = 3
selected_next_work_item_first_checkpoint = readiness_review
selected_next_work_item_second_checkpoint = candidate_implementation
selected_next_work_item_third_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to create a safe, static fixture set later, only if readiness review confirms the boundary.

The fixture set should support the accepted Blocked Tool Action Request Review scenario using mock, non-execution, static, reviewable data.

## Why this is High risk

Fixture files may become public reviewer-facing examples.

If created poorly, they could imply execution, scanner coverage, customer authorization, real target testing, production readiness, diagnostic completeness, or a customer PoC path.

They may also influence validator expectations, README navigation, public reviewer interpretation, and future demo readiness.

Therefore, fixture set creation should not move directly from selection to candidate. It should use a readiness review before candidate implementation.

## Why not Critical risk

The selected work item should remain limited to static fixture data and reviewer-facing documentation.

It should not start runtime execution, scanner execution, Docker execution, credential injection, customer-target activity, customer PoC intake, commercial contracting, paid engagement approval, delivery authorization, AAEF main modification, or third-party testing authorization.

Because the planned work is still static and non-execution, Critical-risk sequencing is not required unless later scope expands.

## Why not Medium or Low risk

The selected work item may create files that readers interpret as public examples.

It can affect repository trust, public demo readiness, validator expectations, and external reviewer understanding.

That is more than a documentation-only planning step, so Medium or Low risk would understate the review need.

## Planned checkpoint split

The selected work item should use a High-risk three-checkpoint pattern:

~~~text
v0.6.192 Safe Demo Fixture Set Creation Readiness Review
v0.6.193 Safe Demo Fixture Set Candidate
v0.6.194 Safe Demo Fixture Set Review and Decision
~~~

v0.6.192 should confirm readiness and define the exact allowed fixture creation scope.

v0.6.193 should create only the approved static fixture candidates if readiness is accepted.

v0.6.194 should review the fixture candidates, confirm claim boundaries, and decide whether to accept or revise the fixture set.

## Expected readiness review scope

The readiness review should likely confirm:

* accepted fixture set plan continuity,
* allowed fixture file paths,
* allowed fixture file types,
* expected fixture identifiers,
* request fixture constraints,
* gate decision fixture constraints,
* non-execution result fixture constraints,
* evidence trace fixture constraints,
* reviewer walkthrough constraints,
* no live endpoint values,
* no credentials,
* no customer-specific material,
* no runtime imports,
* no scanner execution,
* no Docker execution,
* no validator behavior changes unless separately selected,
* no schema additions unless separately selected,
* no AAEF main changes,
* no customer PoC or third-party testing authorization.

## Claim boundaries for the selected work

The selected work must not claim:

~~~text
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

The selected work may create static fixture candidates later only if v0.6.192 accepts readiness.

## What did not happen

The Safe Demo Fixture Set Creation Readiness Review artifact remains uncreated in this checkpoint.

Fixture files remain uncreated in this checkpoint.

Public samples remain unchanged in this checkpoint.

The safe demo artifact remains uncreated in this checkpoint.

The public demo artifact remains uncreated in this checkpoint.

The executable demo artifact remains uncreated in this checkpoint.

Runtime/scanner readiness remains uncreated in this checkpoint.

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

No JSON Schema is added.

No public sample is changed.

No runtime behavior is modified.

No runtime, scanner, Docker, credential, customer-target, or delivery authorization occurs.

No certification, legal compliance, audit opinion, production readiness, external-framework equivalence, diagnostic completeness, or third-party-testing authorization claim occurs.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.190

v0.6.190 reviewed and accepted the Safe Demo Fixture Set Planning candidate and closed that Medium-risk work item.

This checkpoint selects the next work item that may later create static fixtures based on that accepted plan.

## Relationship to v0.6.187

v0.6.187 reviewed and accepted the Safe Demo Artifact Planning candidate.

This selected work must support that accepted artifact plan.

## Relationship to v0.6.184

v0.6.184 reviewed and accepted the Safe Demo Scenario Definition candidate.

This selected work must support the accepted Blocked Tool Action Request Review scenario.

## Relationship to v0.6.181

v0.6.181 deferred Commercial Inquiry Response Boundary before candidate creation because demo/story readiness should come first.

This checkpoint continues the safe demo readiness path while keeping commercial inquiry response deferred.

## Relationship to v0.6.172

v0.6.172 deferred AAEF main contact publication.

This checkpoint preserves that deferral.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.191 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to High risk with three checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.192 Safe Demo Fixture Set Creation Readiness Review
~~~
