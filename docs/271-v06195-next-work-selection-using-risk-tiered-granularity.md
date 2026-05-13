# v0.6.195 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-13

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.194 closed the Safe Demo Fixture Set Creation work item.

## Decision

The selected next work item is Repository Landing and Demo Path Clarity.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.196 Repository Landing and Demo Path Clarity Candidate.

The follow-up checkpoint is v0.6.197 Repository Landing and Demo Path Clarity Review and Decision.

This checkpoint does not create the Repository Landing and Demo Path Clarity artifact.

This checkpoint does not create new fixture files.

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
next_work_selection_using_risk_tiered_granularity_v06195_completed = true
next_work_selection_v06195_is_documentation_only = true
next_work_selection_v06195_uses_v06120_granularity_policy = true
next_work_selection_v06195_uses_v06194_fixture_set_closeout = true
v06195_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = repository_landing_demo_path_clarity
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.196 Repository Landing and Demo Path Clarity Candidate
selected_followup_checkpoint = v0.6.197 Repository Landing and Demo Path Clarity Review and Decision
repository_landing_demo_path_clarity_selected = true
repository_landing_demo_path_clarity_created = false
repository_landing_demo_path_clarity_review_decision_completed = false
repository_landing_demo_path_clarity_should_reference_accepted_fixture_set = true
repository_landing_demo_path_clarity_should_reference_safe_demo_boundary = true
repository_landing_demo_path_clarity_should_explain_demo_review_path = true
repository_landing_demo_path_clarity_should_preserve_non_execution_boundary = true
repository_landing_demo_path_clarity_should_not_create_new_fixtures = true
repository_landing_demo_path_clarity_should_not_create_public_demo = true
repository_landing_demo_path_clarity_should_not_create_executable_demo = true
repository_landing_demo_path_clarity_should_not_modify_runtime_behavior = true
repository_landing_demo_path_clarity_should_not_modify_validator_behavior = true
repository_landing_demo_path_clarity_should_not_add_schema = true
safe_demo_fixture_set_creation_work_item_closed = true
safe_demo_fixture_set_status = accepted
safe_demo_fixture_set_path = docs/examples/safe-demo/blocked-tool-action-request-review
safe_demo_fixture_set_is_static = true
safe_demo_fixture_set_is_mock = true
safe_demo_fixture_set_is_non_execution = true
safe_demo_fixture_set_is_reviewer_facing = true
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
additional_fixture_files_created = false
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
sensitive_value_injection_permitted = false
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
| Repository Landing and Demo Path Clarity | Medium | yes | v0.6.194 accepted the static fixture set. The next useful step is to make the repository landing path and demo review path understandable without implying executable demo, scanner readiness, public demo, or PoC readiness. |
| Public Demo Readiness Review | Medium | no | Useful later, but the repository should first clarify the accepted fixture path and review flow. |
| Public Announcement Readiness Review | Low or Medium | no | Useful later, but announcement should not precede landing path clarity. |
| Safe Demo README Navigation Candidate | Medium | no | Overlaps with the selected work and should be handled as part of landing/demo path clarity. |
| Commercial Inquiry Response Boundary | Medium | no | Deferred by v0.6.181 before candidate creation. |
| Runtime/Scanner Implementation Readiness Review | Medium or High | no | Still deferred. Landing path clarity should remain documentation-only and non-execution. |
| Customer PoC Intake Boundary | Medium or High | no | Deferred pending commercial, scope, responsibility, authorization, and customer-target boundaries. |

## Selected work item

~~~text
selected_next_work_item = repository_landing_demo_path_clarity
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to make the accepted safe demo fixture set discoverable and reviewable from repository landing surfaces.

It should explain where reviewers should start, which fixture files to inspect, what conclusion the fixture set demonstrates, and what the fixture set does not authorize or prove.

## Why this is Medium risk

The work is documentation-only and should not modify runtime behavior, scanner behavior, validators, schemas, fixture files, public samples, customer PoC material, or AAEF main material.

However, README and repository landing text are high-visibility. Ambiguous wording could make the accepted fixture set look like a public demo, executable demo, scanner capability, production readiness evidence, customer PoC path, or authorization to test third-party systems.

Because this affects public interpretation, it should use a two-checkpoint Medium-risk pattern.

## Why not High or Critical risk

The selected work should not create fixture files, add public samples, add schema behavior, change validators, create an executable demo, run scanners, modify runtime behavior, approve customer targets, modify sensitive-value handling, create a PoC, create commercial terms, approve delivery, or submit anything to AAEF main.

Because it is landing/navigation wording only, High-risk or Critical-risk sequencing is not required unless later scope expands.

## Why not Low risk

The selected work is not a private note.

It may modify public-facing repository navigation and may influence how reviewers understand the accepted fixture set.

Therefore, it should not be completed as a single Low-risk checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.196 Repository Landing and Demo Path Clarity Candidate
v0.6.197 Repository Landing and Demo Path Clarity Review and Decision
~~~

v0.6.196 should create the landing/demo path clarity candidate and tests.

v0.6.197 should review the candidate, confirm claim boundaries, and decide whether to close the work item.

## Expected Repository Landing and Demo Path Clarity scope

The candidate should likely cover:

* a concise README entry pointing to the accepted fixture path,
* the accepted fixture path,
* the fixture review order,
* the expected reviewer conclusion,
* static/mock/non-execution labeling,
* a statement that the fixture set is not a scanner,
* a statement that the fixture set is not an executable demo,
* a statement that the fixture set is not a public demo,
* a statement that the fixture set is not PoC readiness or delivery authorization,
* a statement that the fixture set is not authorization to test third-party systems,
* links to the v0.6.194 review and decision record,
* preservation of AAEF main contact-publication deferral.

The candidate should not create new fixture files, public samples, schemas, validator behavior, runtime behavior, scanner behavior, customer PoC material, commercial terms, or AAEF main changes.

## Claim boundaries for the selected work

The selected work must not claim:

~~~text
public demo creation
executable demo creation
runtime execution approval
scanner execution approval
Docker execution approval
sensitive value use approval
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

The selected work may clarify how to review the accepted static fixture set.

## What did not happen

The Repository Landing and Demo Path Clarity artifact remains uncreated in this checkpoint.

No new fixture file is added in this checkpoint.

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

No metadata-level `expected_failure_category` is added.

No JSON Schema is added.

No public sample is changed.

No runtime behavior is modified.

No runtime, scanner, Docker, sensitive value, customer-target, or delivery authorization occurs.

No certification, legal compliance, audit opinion, production readiness, external-framework equivalence, diagnostic completeness, or third-party-testing authorization claim occurs.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.194

v0.6.194 reviewed and accepted the Safe Demo Fixture Set candidate and closed that High-risk work item.

This checkpoint selects landing/demo path clarity as the next work item so reviewers can find and understand that accepted fixture set.

## Relationship to v0.6.193

v0.6.193 created the static, mock, non-execution fixture set candidate.

This checkpoint preserves that fixture set as the accepted review target while selecting only navigation and landing clarity as the next work.

## Relationship to v0.6.190

v0.6.190 reviewed and accepted the Safe Demo Fixture Set Planning candidate.

This selected work should remain consistent with that accepted fixture plan.

## Relationship to v0.6.187

v0.6.187 reviewed and accepted the Safe Demo Artifact Planning candidate.

This selected work should point to the accepted fixture path without expanding artifact scope.

## Relationship to v0.6.184

v0.6.184 reviewed and accepted the Safe Demo Scenario Definition candidate.

This selected work should explain the accepted Blocked Tool Action Request Review scenario without turning it into a live demo.

## Relationship to v0.6.181

v0.6.181 deferred Commercial Inquiry Response Boundary before candidate creation because demo/story readiness should come first.

This checkpoint keeps commercial inquiry response deferred.

## Relationship to v0.6.172

v0.6.172 deferred AAEF main contact publication.

This checkpoint preserves that deferral.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.195 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.196 Repository Landing and Demo Path Clarity Candidate
~~~
