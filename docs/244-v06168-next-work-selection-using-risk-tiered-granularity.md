# v0.6.168 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-12

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.167 closed the Maintainer Inquiry Address Publication work item.

## Decision

The selected next work item is Public Entry and Inquiry Route Consistency Review.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.169 Public Entry and Inquiry Route Consistency Review Candidate.

This checkpoint does not create the public entry and inquiry route consistency review.

This checkpoint does not modify README public entry language.

This checkpoint does not modify commercial inquiry language.

This checkpoint does not modify the inquiry address publication.

This checkpoint does not reopen the AAEF main handback sequence.

No AAEF main issue is opened.

No issue creation command is generated.

No issue URL is created.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06168_completed = true
next_work_selection_v06168_is_documentation_only = true
next_work_selection_v06168_uses_v06120_granularity_policy = true
next_work_selection_v06168_uses_v06167_completed_work_item = true
v06168_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = public_entry_and_inquiry_route_consistency_review
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.169 Public Entry and Inquiry Route Consistency Review Candidate
selected_followup_checkpoint = v0.6.170 Public Entry and Inquiry Route Consistency Review Review and Decision
public_entry_and_inquiry_route_consistency_review_selected = true
maintainer_inquiry_address_publication_work_item_closed = true
buyer_facing_commercial_inquiry_boundary_work_item_closed = true
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
public_entry_and_inquiry_route_consistency_review_created = false
public_entry_and_inquiry_route_consistency_review_modified = false
readme_public_entry_modified = false
readme_commercial_inquiry_entry_modified = false
inquiry_address_publication_modified = false
buyer_facing_commercial_inquiry_boundary_modified = false
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
| Public Entry and Inquiry Route Consistency Review | Medium | yes | The repository now has a public review entry point, commercial inquiry boundary, and published maintainer inquiry address. The next safe step is to review whether those public routes are internally consistent without treating the repository as a contract, PoC approval, runtime authorization, scanner authorization, delivery approval, certification package, or production offering. |
| AAEF main inquiry address reflection planning | Medium | no | Useful, but this should follow an AAEF-AI-VA-side consistency review. Direct AAEF main reflection could be confused with reopening the v0.6.119 handback sequence. |
| Commercial contact replacement/domain planning | Low or Medium | no | Not urgent because the interim maintainer-approved AAEF-wide inquiry address has just been accepted. |
| PoC request intake boundary | Medium or High | no | Useful later, but the existing public review and commercial inquiry routes should first be checked for consistency. |
| Runtime execution preparation | High or Critical | no | Runtime/scanner/customer-target activity remains outside the current safe direction and would require a larger risk split. |

## Selected work item

~~~text
selected_next_work_item = public_entry_and_inquiry_route_consistency_review
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to review the consistency of the accepted public-facing routes:

* Public Review Entry Point,
* External Review Package entry route,
* Buyer-Facing Commercial Inquiry Boundary,
* maintainer-approved interim AAEF-wide inquiry address publication,
* README public/commercial navigation,
* non-authorizing interpretation boundaries.

The work should confirm that public review, commercial inquiry, and contact publication remain aligned and do not create conflicting interpretations.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, it may review and possibly recommend small public-facing wording adjustments across README and buyer-facing materials. Public-facing route consistency can influence how external readers understand review, inquiry, commercial interest, PoC boundaries, runtime authorization, and delivery approval.

Therefore, it is Medium risk and should use two checkpoints.

## Why not High or Critical risk

This work item should not change enforcement behavior, fail-closed logic, runtime execution, scanner execution, Docker/lab execution, credential injection, customer target handling, customer PoC authorization, paid engagement approval, commercial license terms, customer delivery, or external submission.

It does not create a live PoC, contract, authorization record, runtime gate integration, scanner runbook, customer delivery artifact, or AAEF main handback submission.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not only a direction-selection note.

It will likely create a review artifact for public-facing entry and inquiry route consistency. It may influence future README/contact/commercial inquiry language even if it does not directly approve contracts, PoCs, runtime behavior, scanner execution, or delivery.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.169 Public Entry and Inquiry Route Consistency Review Candidate
v0.6.170 Public Entry and Inquiry Route Consistency Review Review and Decision
~~~

v0.6.169 should create a candidate consistency review and tests. The candidate should remain claim-safe, non-authorizing, and aligned with the Public Review Entry Point, External Review Package, Buyer-Facing Commercial Inquiry Boundary, Maintainer Inquiry Address Publication, Reviewer Walkthrough, Control Matrix, Technical Due Diligence Summary, Enterprise Review Guide, and Safe PoC Boundary Template.

v0.6.170 should review the consistency review, confirm claim boundaries, and decide whether to close the work item.

## Expected Public Entry and Inquiry Route Consistency Review scope

The candidate should likely check:

* README Public Review Entry Point,
* README Commercial Inquiry Boundary,
* accepted inquiry address publication,
* `docs/external-review-package.md`,
* `docs/buyer-facing-commercial-inquiry-boundary.md`,
* `docs/reviewer-walkthrough.md`,
* `docs/control-matrix.md`,
* `docs/technical-due-diligence-summary.md`,
* `docs/enterprise-review-guide.md`,
* `docs/safe-poc-boundary-template.md`.

The review should look for:

* consistent public-review route wording,
* consistent commercial-inquiry route wording,
* consistent inquiry-route-only interpretation,
* consistent contact address use,
* consistent non-authorizing language,
* no conflict between public review and commercial inquiry routes,
* no implication of customer PoC approval,
* no implication of commercial contract creation,
* no implication of paid engagement approval,
* no implication of commercial license terms publication,
* no implication of runtime/scanner/Docker/credential/customer/delivery authorization,
* no certification/legal/audit/production/equivalence/diagnostic-completeness claims,
* no reopening of the v0.6.119 AAEF main handback sequence.

## Claim boundaries for the selected work

The Public Entry and Inquiry Route Consistency Review candidate must not claim:

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

The review may identify consistency gaps and recommend future documentation changes within conservative claim boundaries.

## What did not happen

No public entry and inquiry route consistency review is created in this checkpoint.

No README public entry language is modified.

No README commercial inquiry entry is modified.

No inquiry address publication is modified.

No Buyer-Facing Commercial Inquiry Boundary is modified.

No Public Review Entry Point is modified.

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

## Relationship to v0.6.167

v0.6.167 closed the Medium-risk Maintainer Inquiry Address Publication work item and accepted `hexroot0010@gmail.com` as the maintainer-approved interim AAEF-wide inquiry address.

This checkpoint selects the next work item after that closeout.

## Relationship to v0.6.165

v0.6.165 closed the Buyer-Facing Commercial Inquiry Boundary work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.162

v0.6.162 closed the Public Review Entry Point Polish work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.159

v0.6.159 closed the External Review Package Integration work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.168 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.169 Public Entry and Inquiry Route Consistency Review Candidate
~~~

That checkpoint may create the candidate consistency review and tests within the boundaries defined here.
