# Public Demo Positioning

Status: draft_candidate
Version: v0.6.178
Date: 2026-05-12

## Purpose

This document defines how AAEF-AI-VA should position public demonstrations.

A safe public demo should demonstrate control boundaries, not live diagnostic power.

Its purpose is to show that AI output is a request, gates decide execution, and evidence makes the decision reviewable.

~~~text
AI may generate a tool_action_request, but execution is decided by gates.
~~~

This positioning does not create a demo artifact.

## Demo principle

The first public demo should prefer non-execution, mock, fixture, or local-only forms.

The demo should show:

* an AI-generated tool action request,
* a gate decision,
* scope and authorization checks,
* preflight evidence expectations,
* an allowed, blocked, or human-approval-required decision path,
* evidence linking request, decision, execution or non-execution, and result,
* reviewer-facing explanation.

Blocked execution can be a valid demo outcome.

Evidence trace should be the demo focus.

## Demo types

| Demo type | Public positioning | Boundary |
| --- | --- | --- |
| Non-execution demo | Recommended first public form | Shows request, gate decision, and evidence without running tools |
| Mock demo | Recommended safe form | Uses mock or dry-run records; must not imply live target activity |
| Fixture demo | Recommended safe form | Uses static or sanitized fixtures; must not imply customer-target activity |
| Local-only lab demo | Possible later form | Must remain constrained to local targets and separate readiness checks |
| Runtime execution | Deferred | Requires dedicated readiness review and execution boundary |
| Scanner execution | Deferred | Requires separate runtime/scanner readiness and local-only authorization boundaries |
| Customer PoC | Deferred | Requires commercial, scope, responsibility, authorization, and customer-target boundaries |

## Non-execution demo

A non-execution demo can show the most important part of AAEF-AI-VA:

1. AI proposes a tool action.
2. A gate evaluates whether the action may proceed.
3. The gate blocks, allows mock handling, or requires human approval.
4. Evidence records the request, decision, non-execution, and reviewer conclusion.

This can be a strong public demo because the central claim is not that an AI can scan. The central claim is that execution authority is separated from model output and can be reviewed.

## Mock demo

A mock demo may use generated records or dry-run results to show how the workflow behaves.

It should clearly state that mock or dry-run outputs are not evidence of live assessment coverage.

It should avoid implying that a target was tested.

## Fixture demo

A fixture demo may use static examples, sanitized artifacts, or known sample records.

It should show data shape, review flow, evidence linkage, and claim boundaries.

It should avoid implying that the fixture represents complete diagnostic coverage.

## Local-only lab demo

A local-only lab demo may become appropriate after separate readiness review.

It should be limited to local targets controlled by the maintainer or test environment.

It should not be treated as customer PoC approval.

## Runtime execution

Runtime execution remains outside the first public demo.

Runtime work requires separate readiness review, explicit authorization boundaries, and evidence controls.

~~~text
runtime_execution_selected = false
runtime_execution_authorized = false
~~~

## Scanner execution

Scanner execution remains outside the first public demo.

Scanner work requires separate readiness review, target boundary, preflight checks, and authorization evidence.

~~~text
real_scanner_execution_selected = false
scanner_execution_authorized = false
~~~

## Customer PoC

Customer PoC remains outside the public demo positioning.

Customer PoC work requires separate commercial, legal, scope, responsibility, authorization, and customer-target boundaries.

~~~text
customer_poc_intake_selected = false
customer_poc_authorized = false
~~~

## What a reviewer should see

A reviewer should be able to inspect:

* who or what generated the request,
* what the requested action was,
* what scope and authorization inputs existed,
* what gate decision was made,
* whether execution occurred or did not occur,
* what evidence supports that conclusion,
* what was intentionally not authorized.

## Acceptable public demo message

A safe public message may say:

~~~text
This demo shows how AAEF-AI-VA separates AI-generated diagnostic requests from execution authority. It focuses on gate decisions and evidence traceability. It does not grant target-testing permission or represent production diagnostic coverage.
~~~

## Avoided public demo message

Avoid messages that imply:

* live scanner capability,
* production deployment approval,
* target-testing permission,
* customer PoC approval,
* diagnostic completeness,
* certification,
* legal compliance determination,
* audit opinion,
* external-framework equivalence,
* AAEF Core/Profile/Practical Package promotion.

## Relationship to current state

v0.6.176 accepted the Current-State Executive Summary.

That summary records:

~~~text
documentation_and_review_package_layer_status = implemented
safe_demo_layer_status = near_term_candidate
runtime_scanner_layer_status = deferred_pending_readiness_review
customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries
~~~

This positioning document uses that accepted current state.

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

## Next checkpoint

Proceed to:

~~~text
v0.6.179 Public Demo Positioning Review and Decision
~~~
