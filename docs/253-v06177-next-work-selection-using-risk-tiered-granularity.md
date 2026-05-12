# v0.6.177 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-12

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.176 closed the Current-State Executive Summary work item.

## Decision

The selected next work item is Public Demo Positioning.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.178 Public Demo Positioning Candidate.

The follow-up checkpoint is v0.6.179 Public Demo Positioning Review and Decision.

This checkpoint does not create Public Demo Positioning.

This checkpoint does not create a safe demo.

This checkpoint does not create a public demo.

This checkpoint does not start runtime or scanner work.

This checkpoint does not authorize customer PoC intake.

No AAEF main issue is opened.

No issue creation command is generated.

No issue URL is created.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06177_completed = true
next_work_selection_v06177_is_documentation_only = true
next_work_selection_v06177_uses_v06120_granularity_policy = true
next_work_selection_v06177_uses_v06176_current_state_executive_summary_closeout = true
v06177_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = public_demo_positioning
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.178 Public Demo Positioning Candidate
selected_followup_checkpoint = v0.6.179 Public Demo Positioning Review and Decision
public_demo_positioning_selected = true
public_demo_positioning_created = false
public_demo_positioning_review_decision_completed = false
current_state_executive_summary_work_item_closed = true
documentation_and_review_package_layer_status = implemented
safe_demo_layer_status = near_term_candidate
runtime_scanner_layer_status = deferred_pending_readiness_review
customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries
safe_demo_should_precede_real_scanner_execution = true
non_execution_demo_is_preferred_first_demo = true
local_only_mock_or_fixture_demo_is_preferred_initial_implementation = true
real_scanner_execution_remains_unselected = true
runtime_execution_remains_unselected = true
customer_poc_intake_remains_unselected = true
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
| Public Demo Positioning | Medium | yes | v0.6.176 accepted the Current-State Executive Summary. The natural next step is to explain what a safe public demo may show, what it must not imply, and how it differs from runtime/scanner/customer PoC work. |
| Commercial Inquiry Response Boundary | Medium | no | Useful soon, but public demo positioning should come first because inbound commercial conversations may ask to see a demo. |
| Runtime/Scanner Implementation Readiness Review | Medium or High | no | Visible but deferred. The project should clarify public demo boundaries before moving toward execution readiness. |
| Safe Demo Candidate | Medium or High | no | The actual demo should not be created before positioning language is reviewed and accepted. |
| Customer PoC Intake Boundary | Medium or High | no | Deferred pending commercial, scope, responsibility, authorization, and demo-positioning boundaries. |
| AAEF main contact publication | Medium | no | Deferred by v0.6.172 and remains outside the current direction. |

## Selected work item

~~~text
selected_next_work_item = public_demo_positioning
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to define how AAEF-AI-VA can present a safe public demonstration without implying runtime authorization, live scanning, customer PoC approval, or production readiness.

It should make clear that the first public demo should likely be non-execution, mock-based, fixture-based, or local-only, and that live scanner activity remains deferred.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, public demo language can shape external reader expectations. It can be misread as a working scanner, a customer PoC, a production deployment, or permission to test targets.

Because of that public-interpretation risk, it should use two checkpoints.

## Why not High or Critical risk

This work item should not create a demo artifact, run scanners, change execution behavior, authorize runtime activity, approve customer targets, modify credential handling, create a customer PoC, create a commercial contract, approve delivery, or submit anything to AAEF main.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not merely an internal note.

It will create public-facing positioning language for demonstrations. That language can affect buyer, reviewer, maintainer, and practitioner expectations about what the project can safely show.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.178 Public Demo Positioning Candidate
v0.6.179 Public Demo Positioning Review and Decision
~~~

v0.6.178 should create the public demo positioning candidate and tests.

v0.6.179 should review the public demo positioning candidate, confirm claim boundaries, and decide whether to close the work item.

## Expected Public Demo Positioning scope

The Public Demo Positioning candidate should likely cover:

* what a safe public demo may show,
* what a safe public demo must not imply,
* the difference between non-execution demo, mock demo, fixture demo, local-only lab demo, runtime execution, scanner execution, and customer PoC,
* why the first demo should likely be non-execution or mock/local-only,
* what evidence a reviewer should see,
* why blocked execution can be a valid demonstration outcome,
* what remains deferred,
* what wording should be avoided.

It should not create an actual demo, modify runtime behavior, add scanner execution, add Docker execution, add credential use, add target use, or approve delivery.

## Claim boundaries for the selected work

The Public Demo Positioning candidate must not claim:

~~~text
certification
legal compliance
audit opinion
audit sufficiency
production readiness
production scanner status
diagnostic completeness
authorization for third-party testing
customer PoC approval
commercial contract creation
commercial license terms publication
paid engagement approval
customer-specific material creation
customer delivery approval
runtime execution approval
scanner execution approval
Docker execution approval
credential use approval
customer target approval
equivalence with external frameworks
AAEF Core/Profile/Practical Package promotion
AAEF main handback reopening
~~~

The candidate may state that a safe public demo should prefer non-execution, mock, fixture, or local-only forms before live scanner execution.

## What did not happen

The Public Demo Positioning artifact remains uncreated in this checkpoint.

The safe demo artifact remains uncreated in this checkpoint.

The public demo artifact remains uncreated in this checkpoint.

The Runtime/Scanner Implementation Readiness Review artifact remains uncreated in this checkpoint.

Real scanner execution remains unselected in this checkpoint.

Runtime execution remains unselected in this checkpoint.

Customer PoC intake remains unselected in this checkpoint.

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

## Relationship to v0.6.176

v0.6.176 reviewed and accepted the Current-State Executive Summary candidate and closed that Medium-risk work item.

This checkpoint selects the next work item after that closeout.

## Relationship to v0.6.173

v0.6.173 recorded the safe demo layer as a near-term candidate while deferring runtime/scanner and customer PoC layers.

This checkpoint selects a positioning work item that prepares public demo language before any demo artifact is created.

## Relationship to v0.6.172

v0.6.172 deferred AAEF main contact publication.

This checkpoint preserves that deferral.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.177 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.178 Public Demo Positioning Candidate
~~~
