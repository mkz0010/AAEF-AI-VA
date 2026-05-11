# v0.6.163 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-12

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.162 closed the Public Review Entry Point Polish work item.

## Decision

The selected next work item is Buyer-Facing Commercial Inquiry Boundary.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.164 Buyer-Facing Commercial Inquiry Boundary Candidate.

This checkpoint does not create the buyer-facing commercial inquiry boundary.

This checkpoint does not create commercial license terms.

This checkpoint does not approve a paid engagement.

This checkpoint does not authorize a customer PoC.

This checkpoint does not modify runtime behavior.

This checkpoint does not reopen the AAEF main handback sequence.

No AAEF main issue is opened.

No issue creation command is generated.

No issue URL is created.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06163_completed = true
next_work_selection_v06163_is_documentation_only = true
next_work_selection_v06163_uses_v06120_granularity_policy = true
next_work_selection_v06163_uses_v06162_completed_work_item = true
v06163_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = buyer_facing_commercial_inquiry_boundary
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.164 Buyer-Facing Commercial Inquiry Boundary Candidate
buyer_facing_commercial_inquiry_boundary_selected = true
public_review_entry_point_polish_work_item_closed = true
external_review_package_integration_work_item_closed = true
reviewer_walkthrough_work_item_closed = true
control_matrix_work_item_closed = true
safe_poc_boundary_template_work_item_closed = true
technical_due_diligence_summary_work_item_closed = true
enterprise_review_guide_work_item_closed = true
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
buyer_facing_commercial_inquiry_boundary_created = false
buyer_facing_commercial_inquiry_boundary_modified = false
readme_commercial_inquiry_entry_modified = false
public_review_entry_point_modified = false
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
| Buyer-Facing Commercial Inquiry Boundary | Medium | yes | Public review entry points are now accepted. The next safe step is to clarify how interested commercial readers can ask questions without treating the public repository as a contract, customer PoC approval, paid engagement, production offering, delivery approval, or authorization to run tools. |
| Public review package maintenance index | Low or Medium | no | Useful, but less urgent than separating review interest from commercial commitment and customer-specific authorization. |
| PoC request intake boundary | Medium or High | no | Closely related, but PoC request language should follow the commercial inquiry boundary so commercial interest, review interest, and PoC authorization remain separated. |
| AAEF main handback reconsideration | Medium or High | no | The v0.6.119 handback sequence remains paused. A public-safe AAEF main handback should wait until applied-implementation lessons are consolidated into narrow evidence/interface lessons. |
| Runtime execution preparation | High or Critical | no | Runtime/scanner/customer-target activity remains outside the current safe direction and would require a larger risk split. |

## Selected work item

~~~text
selected_next_work_item = buyer_facing_commercial_inquiry_boundary
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to create a claim-safe public boundary for buyer-facing commercial inquiry.

The work should clarify:

* what commercial readers may ask about,
* what the public repository does and does not offer,
* how commercial inquiry differs from customer PoC authorization,
* how commercial inquiry differs from runtime/scanner execution authorization,
* how commercial inquiry differs from customer delivery authorization,
* how commercial inquiry differs from commercial license terms or paid engagement approval,
* which materials remain outside the public repository,
* which claims must not be inferred from public commercial inquiry language.

It should not create runtime approval, scanner approval, customer PoC approval, paid engagement approval, customer delivery approval, commercial license terms, customer-specific materials, legal/compliance claims, audit claims, certification claims, production readiness claims, diagnostic-completeness claims, or external-framework equivalence claims.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, buyer-facing and commercial-inquiry wording can influence how external readers interpret the repository. Poor wording could make the project appear to be a contract offer, customer PoC package, production scanner, deployment-ready service, audit/certification package, paid engagement approval, or permission to test systems.

Therefore, it is Medium risk and should use two checkpoints.

## Why not High or Critical risk

This work item should not change enforcement behavior, fail-closed logic, runtime execution, scanner execution, Docker/lab execution, credential injection, customer target handling, delivery authorization, customer PoC authorization, paid engagement approval, commercial license terms, or external submission.

It does not create a live PoC, contract, authorization record, runtime gate integration, scanner runbook, customer delivery artifact, or AAEF main handback submission.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not only a direction-selection note.

It will likely create or modify public-facing commercial inquiry language, which may influence buyer, sponsor, maintainer, and commercial-reader interpretation.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.164 Buyer-Facing Commercial Inquiry Boundary Candidate
v0.6.165 Buyer-Facing Commercial Inquiry Boundary Review and Decision
~~~

v0.6.164 should create the candidate commercial inquiry boundary and tests. The candidate should remain claim-safe, non-authorizing, and aligned with the Public Review Entry Point, External Review Package, Reviewer Walkthrough, Control Matrix, Technical Due Diligence Summary, Enterprise Review Guide, and Safe PoC Boundary Template.

v0.6.165 should review the commercial inquiry boundary, confirm claim boundaries, and decide whether to close the work item.

## Expected Buyer-Facing Commercial Inquiry Boundary scope

The candidate should likely include:

* intended commercial reader,
* allowed commercial inquiry topics,
* topics that require separate agreement,
* explicit statement that inquiry is not a contract,
* explicit statement that inquiry does not approve a paid engagement,
* explicit statement that inquiry does not authorize customer PoC activity,
* explicit statement that inquiry does not authorize runtime/scanner execution,
* explicit statement that inquiry does not authorize credential use, customer target use, or delivery,
* relationship to the External Review Package,
* relationship to the Safe PoC Boundary Template,
* relationship to licensing and commercial-use boundaries,
* public/private material boundary,
* claim-boundary language preventing certification, audit, legal compliance, production readiness, diagnostic-completeness, and external-framework equivalence interpretations,
* tests verifying the commercial inquiry boundary and absence of forbidden claims.

The work should help commercial readers ask safe boundary questions, not operate a scanner, approve testing, approve delivery, create a contract, or grant commercial license terms.

## Claim boundaries for the selected work

The Buyer-Facing Commercial Inquiry Boundary candidate must not claim:

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
commercial license terms creation
paid engagement approval
customer delivery approval
equivalence with external frameworks
AAEF Core/Profile/Practical Package promotion
~~~

The boundary may help commercial readers understand how to ask about AAEF-AI-VA without converting public review language into authorization, contract, delivery, or production claims.

## What did not happen

No buyer-facing commercial inquiry boundary is created in this checkpoint.

No README commercial inquiry entry is modified in this checkpoint.

No External Review Package is modified.

No Reviewer Walkthrough is modified.

No Control Matrix is modified.

No Safe PoC Boundary Template is modified.

No Technical Due Diligence Summary is modified.

No Enterprise Review Guide is modified.

No customer PoC approval occurs.

No commercial contract creation occurs.

No commercial license terms are created.

No paid engagement approval occurs.

No customer-specific material is created.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

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

## Relationship to v0.6.162

v0.6.162 closed the Medium-risk Public Review Entry Point Polish work item.

This checkpoint selects the next work item after that closeout.

## Relationship to v0.6.159

v0.6.159 closed the Medium-risk External Review Package Integration work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.156

v0.6.156 closed the Medium-risk Reviewer Walkthrough work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.153

v0.6.153 closed the Medium-risk Control Matrix work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.150

v0.6.150 closed the Medium-risk Safe PoC Boundary Template work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.147

v0.6.147 closed the Medium-risk Technical Due Diligence Summary work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.144

v0.6.144 closed the Medium-risk Enterprise Review Guide work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.163 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.164 Buyer-Facing Commercial Inquiry Boundary Candidate
~~~

That checkpoint may create the candidate commercial inquiry boundary and tests within the boundaries defined here.
