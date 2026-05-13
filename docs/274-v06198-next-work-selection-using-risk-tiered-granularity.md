# v0.6.198 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-13

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.197 closed the Repository Landing and Demo Path Clarity work item.

## Decision

The selected next work item is Public Demo Readiness Review.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.199 Public Demo Readiness Review Candidate.

The follow-up checkpoint is v0.6.200 Public Demo Readiness Review and Decision.

This checkpoint does not create the Public Demo Readiness Review candidate.

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
next_work_selection_using_risk_tiered_granularity_v06198_completed = true
next_work_selection_v06198_is_documentation_only = true
next_work_selection_v06198_uses_v06120_granularity_policy = true
next_work_selection_v06198_uses_v06197_landing_demo_path_clarity_closeout = true
v06198_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = public_demo_readiness_review
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_review
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.199 Public Demo Readiness Review Candidate
selected_followup_checkpoint = v0.6.200 Public Demo Readiness Review and Decision
public_demo_readiness_review_selected = true
public_demo_readiness_review_candidate_created = false
public_demo_readiness_review_decision_completed = false
public_demo_readiness_review_should_evaluate_wording = true
public_demo_readiness_review_should_evaluate_public_demo_label = true
public_demo_readiness_review_should_evaluate_repository_visibility = true
public_demo_readiness_review_should_preserve_fixture_only_boundary = true
public_demo_readiness_review_should_preserve_non_execution_boundary = true
public_demo_readiness_review_should_not_create_public_demo = true
public_demo_readiness_review_should_not_create_executable_demo = true
public_demo_readiness_review_should_not_create_new_fixtures = true
public_demo_readiness_review_should_not_modify_runtime_behavior = true
public_demo_readiness_review_should_not_modify_validator_behavior = true
public_demo_readiness_review_should_not_add_schema = true
repository_landing_demo_path_clarity_work_item_closed = true
repository_landing_demo_path_clarity_status = accepted
safe_demo_fixture_review_path_readme_entry_accepted = true
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
| Public Demo Readiness Review | Medium | yes | v0.6.197 accepted repository landing and demo path clarity. The next useful step is to decide whether the accepted fixture review path can be described externally as a public demo, or whether public-facing language should avoid that label. |
| Public Announcement Readiness Review | Low or Medium | no | Useful later, but announcement should wait until public-demo readiness wording is reviewed. |
| Safe Demo Landing Walkthrough Expansion | Medium | no | Useful later, but current repository landing path already exists and should first be evaluated for public-demo readiness. |
| Commercial Inquiry Response Boundary | Medium | no | Deferred by v0.6.181 before candidate creation. |
| Runtime/Scanner Implementation Readiness Review | Medium or High | no | Still deferred. Public demo readiness must remain documentation-only and non-execution. |
| Customer PoC Intake Boundary | Medium or High | no | Deferred pending commercial, scope, responsibility, authorization, and customer-target boundaries. |

## Selected work item

~~~text
selected_next_work_item = public_demo_readiness_review
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_review
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to evaluate public-facing readiness of the accepted fixture review path.

It should answer whether the repository should use the phrase `public demo`, avoid it, or use a more conservative phrase such as `static fixture review path`.

## Why this is Medium risk

The work is documentation-only and should not create public demo artifacts, executable demos, fixture files, public samples, schemas, validators, runtime behavior, scanner behavior, customer PoC material, commercial terms, or AAEF main material.

However, the phrase `public demo` can easily be misread as a working scanner, executable demo, production readiness claim, customer PoC path, or authorization to test third-party systems.

Because the selected work affects public-facing interpretation, it should use a two-checkpoint Medium-risk pattern.

## Why not High or Critical risk

The selected work should not create executable artifacts, run scanners, enable runtime execution, approve customer targets, handle sensitive values, modify validators, create schemas, create commercial terms, approve delivery, or submit anything to AAEF main.

Because it remains a readiness and wording review, High-risk or Critical-risk sequencing is not required unless later scope expands.

## Why not Low risk

The selected work may influence external labeling of the accepted fixture review path.

The decision can affect public reader expectations around whether AAEF-AI-VA has a demo, scanner capability, executable proof, PoC readiness, or delivery readiness.

That interpretation risk is more than a simple one-checkpoint documentation note.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.199 Public Demo Readiness Review Candidate
v0.6.200 Public Demo Readiness Review and Decision
~~~

v0.6.199 should create the readiness review candidate and tests.

v0.6.200 should review the candidate, confirm claim boundaries, and decide whether to close the work item.

## Expected Public Demo Readiness Review scope

The candidate should likely evaluate:

* whether to use or avoid the phrase `public demo`,
* whether `static fixture review path` is the safer public phrase,
* what the repository can safely show now,
* whether the accepted fixture set is enough for public demonstration language,
* whether README language remains conservative,
* whether demo language could imply scanner capability,
* whether demo language could imply executable demo availability,
* whether demo language could imply PoC readiness,
* whether demo language could imply delivery authorization,
* whether demo language could imply authorization to test third-party systems,
* whether any later public announcement should wait,
* whether runtime/scanner/customer PoC layers remain deferred.

The candidate should not create new fixtures, public samples, schemas, validator behavior, runtime behavior, scanner behavior, customer PoC material, commercial terms, or AAEF main changes.

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

The selected work may evaluate whether the accepted static fixture review path should be described as a public demo or with a more conservative phrase.

## What did not happen

The Public Demo Readiness Review candidate remains uncreated in this checkpoint.

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

## Relationship to v0.6.197

v0.6.197 reviewed and accepted the Repository Landing and Demo Path Clarity candidate and closed that Medium-risk work item.

This checkpoint selects public demo readiness review as the next work item so public-facing demo language can be evaluated before announcement or broader public positioning.

## Relationship to v0.6.196

v0.6.196 added the README Safe Demo Fixture Review Path and the repository landing/demo path clarity document.

This selected work should evaluate that accepted path without changing it into an executable or public demo artifact.

## Relationship to v0.6.194

v0.6.194 reviewed and accepted the Safe Demo Fixture Set candidate.

This selected work should preserve that fixture set as static, mock, fixture-only, non-execution, and reviewer-facing.

## Relationship to v0.6.181

v0.6.181 deferred Commercial Inquiry Response Boundary before candidate creation because demo/story readiness should come first.

This checkpoint keeps commercial inquiry response deferred.

## Relationship to v0.6.172

v0.6.172 deferred AAEF main contact publication.

This checkpoint preserves that deferral.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.198 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.199 Public Demo Readiness Review Candidate
~~~
