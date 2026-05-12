# v0.6.178 Public Demo Positioning Candidate

Status: candidate
Date: 2026-05-12

## Purpose

This checkpoint implements the Public Demo Positioning candidate after v0.6.177 selected the work item.

This is checkpoint 1 of 2 for a Medium-risk public-facing demo-positioning work item.

This checkpoint creates the Public Demo Positioning candidate.

The review and decision are deferred to v0.6.179.

## Candidate implementation summary

This checkpoint adds a public demo positioning document.

The document explains that the first public demo should show control boundaries and evidence traceability, not live diagnostic power.

It distinguishes:

* non-execution demo,
* mock demo,
* fixture demo,
* local-only lab demo,
* runtime execution,
* scanner execution,
* customer PoC.

It clarifies that blocked execution can be a valid demo outcome.

It preserves that runtime/scanner/customer PoC work remains deferred.

## Positioning artifact

This checkpoint adds:

~~~text
docs/public-demo-positioning.md
~~~

## Candidate conclusion

The public demo positioning candidate is created as a draft for review.

Candidate status:

~~~text
public_demo_positioning_status = draft_candidate
public_demo_positioning_review_decision_deferred_to_v06179 = true
~~~

## Candidate tests

This checkpoint adds:

~~~text
tools/test_v06178_public_demo_positioning_candidate.py
~~~

The tests cover:

* positioning file existence,
* required positioning sections,
* v0.6.177 selection continuity,
* v0.6.176 current-state executive summary closeout continuity,
* v0.6.173 safe demo priority continuity,
* v0.6.172 AAEF main contact deferral continuity,
* v0.6.119 handback pause continuity,
* absence of forbidden affirmative claims.

## Candidate record

~~~text
public_demo_positioning_candidate_completed = true
public_demo_positioning_candidate_is_medium_risk = true
public_demo_positioning_candidate_checkpoint_1_of_2 = true
public_demo_positioning_review_decision_deferred_to_v06179 = true
public_demo_positioning_created = true
public_demo_positioning_status = draft_candidate
public_demo_positioning_claim_safe = true
public_demo_positioning_for_reviewers_and_decision_makers = true
public_demo_positioning_for_technically_informed_buyers = true
public_demo_positioning_distinguishes_demo_types = true
non_execution_demo_positioning_included = true
mock_demo_positioning_included = true
fixture_demo_positioning_included = true
local_only_demo_positioning_included = true
runtime_execution_boundary_included = true
scanner_execution_boundary_included = true
customer_poc_boundary_included = true
blocked_execution_can_be_valid_demo_outcome = true
evidence_trace_should_be_demo_focus = true
tool_action_request_boundary_summary_included = true
gate_decision_boundary_summary_included = true
documentation_and_review_package_layer_status = implemented
safe_demo_layer_status = near_term_candidate
runtime_scanner_layer_status = deferred_pending_readiness_review
customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries
aaef_main_contact_publication_remains_deferred = true
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
review_decision_completed = false
public_demo_positioning_review_decision_completed = false
safe_demo_created = false
public_demo_created = false
runtime_scanner_readiness_created = false
real_scanner_execution_selected = false
runtime_execution_selected = false
customer_poc_intake_selected = false
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
selected_next_checkpoint = v0.6.179 Public Demo Positioning Review and Decision
~~~

## What changed

The following files are added:

~~~text
docs/public-demo-positioning.md
docs/254-v06178-public-demo-positioning-candidate.md
planning/decisions/ADR-0248-add-v06178-public-demo-positioning-candidate.md
planning/issues/0247-add-v06178-public-demo-positioning-candidate.md
tools/test_v06178_public_demo_positioning_candidate.py
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

## Relationship to v0.6.177

v0.6.177 selected Public Demo Positioning as a Medium-risk work item and assigned two checkpoints.

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.176

v0.6.176 reviewed and accepted the Current-State Executive Summary candidate.

This checkpoint uses that accepted current-state summary as its basis.

## Relationship to v0.6.173

v0.6.173 recorded safe demo as a near-term candidate and deferred runtime/scanner/customer PoC layers.

This checkpoint positions the safe demo before creating any demo artifact.

## Relationship to v0.6.172

v0.6.172 deferred AAEF main contact publication.

This checkpoint preserves that deferral.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.179 Public Demo Positioning Review and Decision
~~~
