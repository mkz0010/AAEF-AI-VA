# v0.6.174 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-12

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.173 completed the Current State and Priority Review.

## Decision

The selected next work item is Current-State Executive Summary.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.175 Current-State Executive Summary Candidate.

The follow-up checkpoint is v0.6.176 Current-State Executive Summary Review and Decision.

This checkpoint does not create the Current-State Executive Summary.

This checkpoint does not create a safe demo.

This checkpoint does not start runtime or scanner work.

This checkpoint does not authorize customer PoC intake.

No AAEF main issue is opened.

No issue creation command is generated.

No issue URL is created.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06174_completed = true
next_work_selection_v06174_is_documentation_only = true
next_work_selection_v06174_uses_v06120_granularity_policy = true
next_work_selection_v06174_uses_v06173_current_state_priority_review = true
v06174_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = current_state_executive_summary
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.175 Current-State Executive Summary Candidate
selected_followup_checkpoint = v0.6.176 Current-State Executive Summary Review and Decision
current_state_executive_summary_selected = true
current_state_executive_summary_created = false
current_state_executive_summary_review_decision_completed = false
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
readme_public_entry_modified = false
readme_commercial_inquiry_entry_modified = false
inquiry_address_publication_modified = false
buyer_facing_commercial_inquiry_boundary_modified = false
external_review_package_modified = false
reviewer_walkthrough_modified = false
control_matrix_modified = false
safe_poc_boundary_template_modified = false
technical_due_diligence_summary_modified = false
enterprise_review_guide_modified = false
customer_poc_authorized = false
commercial_contract_created = false
paid_engagement_approved = false
commercial_license_terms_created = false
customer_specific_material_created = false
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
| Current-State Executive Summary | Medium | yes | v0.6.173 identified that the documentation/review package layer is implemented and that the next valuable step is a concise executive summary explaining what exists now, what it proves, what remains deferred, and why the first demo should be safe non-execution or mock/local-only. |
| Public Demo Positioning | Medium | no | Useful soon, but should follow the executive summary so the demo is positioned against a clear current-state narrative. |
| Commercial Inquiry Response Boundary | Medium | no | Useful soon, but current-state explanation should come first so replies do not overrun the present capability. |
| Runtime/Scanner Implementation Readiness Review | Medium or High | no | Visible but deferred. v0.6.173 records runtime/scanner as deferred pending readiness review. |
| Customer PoC Intake Boundary | Medium or High | no | Deferred pending commercial, scope, responsibility, and authorization boundaries. |
| AAEF main contact publication | Medium | no | Deferred by v0.6.172 and remains outside the current direction. |

## Selected work item

~~~text
selected_next_work_item = current_state_executive_summary
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to create a concise executive summary explaining the current state of AAEF-AI-VA for reviewers, decision makers, and technically informed buyers.

The summary should clarify that AAEF-AI-VA is currently strongest as a public evaluation and review package for controlled AI-assisted vulnerability assessment boundaries.

It should also clarify that safe demo work is near-term, while runtime/scanner/customer PoC work remains deferred.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, an executive summary is a public-facing interpretation layer. It can strongly shape whether readers see the project as a framework-backed control boundary reference implementation, a commercial offering, a PoC packet, or a scanner.

Because of that interpretation risk, it should use two checkpoints.

## Why not High or Critical risk

This work item should not change execution behavior, authorize runtime activity, authorize scanner activity, approve customer targets, modify credentials handling, create a customer PoC, create a commercial contract, approve delivery, or submit anything to AAEF main.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not merely an internal note.

It will create a public-facing executive summary that may influence external reader expectations about capability, maturity, commercial inquiry, demo readiness, and implementation stage.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.175 Current-State Executive Summary Candidate
v0.6.176 Current-State Executive Summary Review and Decision
~~~

v0.6.175 should create the executive summary candidate and tests.

v0.6.176 should review the executive summary candidate, confirm claim boundaries, and decide whether to close the work item.

## Expected Current-State Executive Summary scope

The Current-State Executive Summary should likely cover:

* what AAEF-AI-VA is,
* what exists now,
* what the public review package demonstrates,
* what the buyer-facing materials support,
* what the current evidence/gate/control package shows,
* why AI-generated tool action requests are not execution authority,
* why safe non-execution or mock/local-only demonstration should precede live scanner execution,
* what remains deferred,
* what is not authorized,
* what a reviewer or decision maker should read first.

It should be short enough to be usable as a front-facing decision document.

It should not become a commercial contract document, PoC authorization document, production readiness claim, scanner claim, audit claim, legal compliance claim, or customer delivery artifact.

## Claim boundaries for the selected work

The Current-State Executive Summary candidate must not claim:

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

The summary may state that documentation/review package material is implemented and that safe demo work is a near-term candidate, while runtime/scanner/customer PoC layers remain deferred.

## What did not happen

The Current-State Executive Summary artifact remains uncreated in this checkpoint.

The safe demo artifact remains uncreated in this checkpoint.

The public demo artifact remains uncreated in this checkpoint.

No Public Demo Positioning work item is started.

No Commercial Inquiry Response Boundary work item is started.

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

## Relationship to v0.6.173

v0.6.173 completed the Current State and Priority Review.

It recommended Current-State Executive Summary as a likely next Medium-risk two-checkpoint work item.

This checkpoint formally selects that work item.

## Relationship to v0.6.172

v0.6.172 deferred AAEF main contact publication.

This checkpoint preserves that deferral.

## Relationship to v0.6.170

v0.6.170 closed the Public Entry and Inquiry Route Consistency Review work item.

This checkpoint treats the route consistency review as stable background for the future executive summary.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.174 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.175 Current-State Executive Summary Candidate
~~~
