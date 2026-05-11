# v0.6.164 Buyer-Facing Commercial Inquiry Boundary Candidate

Status: candidate
Date: 2026-05-12

## Purpose

This checkpoint implements the Buyer-Facing Commercial Inquiry Boundary candidate after v0.6.163 selected the work item.

This is checkpoint 1 of 2 for a Medium-risk buyer-facing documentation work item.

This checkpoint creates the Buyer-Facing Commercial Inquiry Boundary candidate.

The review and decision are deferred to v0.6.165.

## Candidate implementation summary

This checkpoint adds a claim-safe buyer-facing commercial inquiry boundary.

The boundary clarifies that commercial inquiry can be accepted as a discussion channel without becoming:

* customer PoC approval,
* paid engagement approval,
* commercial contract creation,
* commercial license terms creation,
* runtime execution approval,
* scanner execution approval,
* credential use approval,
* customer target approval,
* customer delivery approval,
* legal/compliance claim,
* audit claim,
* certification claim,
* production readiness claim,
* diagnostic-completeness claim,
* external-framework equivalence claim,
* AAEF Core/Profile/Practical Package promotion.

## Commercial inquiry boundary artifact

This checkpoint adds:

~~~text
docs/buyer-facing-commercial-inquiry-boundary.md
~~~

## README commercial inquiry entry

This checkpoint adds:

~~~text
## Commercial Inquiry Boundary
~~~

to:

~~~text
README.md
~~~

The README entry points to the commercial inquiry boundary document while keeping inquiry separate from authorization, contract, paid engagement, runtime/scanner execution, credential use, customer target use, and delivery.

## Commercial inquiry contact model

Email-based inquiry is the selected contact model.

The candidate intentionally does not commit an email address because no maintainer-approved public email address has been provided in this checkpoint.

The public text uses this boundary instead:

~~~text
Use the maintainer-provided email address when it is published or otherwise provided by the maintainer.
~~~

This avoids placing a fake address, private address, inferred address, or unsupported contact claim in the public repository.

## Boundary scope

The boundary includes:

* intended commercial reader,
* contact channel,
* allowed commercial inquiry topics,
* topics requiring separate agreement,
* inquiry-is-not-contract notice,
* no paid engagement approval notice,
* no customer PoC authorization notice,
* no runtime/scanner authorization notice,
* no credential/customer/delivery authorization notice,
* relationship to the External Review Package,
* relationship to the Safe PoC Boundary Template,
* relationship to licensing and commercial-use boundaries,
* public/private material boundary,
* claim boundaries.

## Claim boundaries

The candidate must not be interpreted as:

~~~text
certification
legal compliance determination
audit opinion
audit sufficiency determination
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

The boundary may help commercial readers ask safe questions without converting inquiry into authorization, contract, delivery, or production claims.

## Candidate tests

This checkpoint adds:

~~~text
tools/test_v06164_buyer_facing_commercial_inquiry_boundary_candidate.py
~~~

The tests cover:

* boundary file existence,
* README commercial inquiry entry existence,
* email-based contact model,
* no committed email address,
* allowed inquiry topics,
* topics requiring separate agreement,
* not-a-contract notice,
* no paid engagement approval notice,
* no customer PoC authorization notice,
* no runtime/scanner authorization notice,
* no credential/customer/delivery authorization notice,
* External Review Package relationship,
* Safe PoC Boundary Template relationship,
* licensing and commercial-use relationship,
* public/private material boundary,
* claim-boundary language,
* v0.6.163 selection continuity,
* v0.6.165 review/decision deferral,
* absence of forbidden affirmative claims.

## Candidate record

~~~text
buyer_facing_commercial_inquiry_boundary_candidate_completed = true
buyer_facing_commercial_inquiry_boundary_candidate_is_medium_risk = true
buyer_facing_commercial_inquiry_boundary_candidate_checkpoint_1_of_2 = true
buyer_facing_commercial_inquiry_boundary_review_decision_deferred_to_v06165 = true
buyer_facing_commercial_inquiry_boundary_created = true
buyer_facing_commercial_inquiry_boundary_candidate_claim_safe = true
buyer_facing_commercial_inquiry_boundary_email_based_contact_selected = true
buyer_facing_commercial_inquiry_email_address_not_specified = true
buyer_facing_commercial_inquiry_uses_maintainer_provided_email = true
buyer_facing_commercial_inquiry_boundary_allowed_topics_included = true
buyer_facing_commercial_inquiry_boundary_topics_requiring_separate_agreement_included = true
buyer_facing_commercial_inquiry_boundary_not_contract_notice_included = true
buyer_facing_commercial_inquiry_boundary_no_paid_engagement_approval_included = true
buyer_facing_commercial_inquiry_boundary_no_customer_poc_authorization_included = true
buyer_facing_commercial_inquiry_boundary_no_runtime_scanner_authorization_included = true
buyer_facing_commercial_inquiry_boundary_no_credential_customer_delivery_authorization_included = true
buyer_facing_commercial_inquiry_boundary_relationship_to_external_review_package_included = true
buyer_facing_commercial_inquiry_boundary_relationship_to_safe_poc_template_included = true
buyer_facing_commercial_inquiry_boundary_license_commercial_use_boundary_included = true
buyer_facing_commercial_inquiry_boundary_public_private_material_boundary_included = true
buyer_facing_commercial_inquiry_boundary_claim_boundaries_included = true
readme_commercial_inquiry_entry_modified = true
commercial_inquiry_contact_channel_is_email = true
commercial_inquiry_email_address_placeholder_used = false
commercial_inquiry_email_address_committed = false
commercial_inquiry_boundary_review_decision_completed = false
review_decision_completed = false
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
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
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
selected_next_checkpoint = v0.6.165 Buyer-Facing Commercial Inquiry Boundary Review and Decision
~~~

## What changed

The following files are added:

~~~text
docs/buyer-facing-commercial-inquiry-boundary.md
docs/240-v06164-buyer-facing-commercial-inquiry-boundary-candidate.md
planning/decisions/ADR-0234-add-v06164-buyer-facing-commercial-inquiry-boundary-candidate.md
planning/issues/0233-add-v06164-buyer-facing-commercial-inquiry-boundary-candidate.md
tools/test_v06164_buyer_facing_commercial_inquiry_boundary_candidate.py
~~~

The following files are updated for commercial inquiry boundary navigation and checks:

~~~text
README.md
CHANGELOG.md
ROADMAP.md
tools/run_all_local_checks.py
~~~

## What did not happen

No review/decision closeout is completed.

No public review entry point is modified.

No External Review Package is modified.

No Reviewer Walkthrough is modified.

No Control Matrix is modified.

No Safe PoC Boundary Template is modified.

No Technical Due Diligence Summary is modified.

No Enterprise Review Guide is modified.

No customer PoC approval occurs.

No commercial contract creation occurs.

No paid engagement approval occurs.

No commercial license terms are published.

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

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

No certification claim occurs.

No legal compliance claim occurs.

No audit opinion claim occurs.

No production readiness claim occurs.

No external-framework equivalence claim occurs.

No diagnostic completeness claim occurs.

No third-party testing authorization claim occurs.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.163

v0.6.163 selected Buyer-Facing Commercial Inquiry Boundary as a Medium-risk work item and assigned two checkpoints:

~~~text
v0.6.164 Buyer-Facing Commercial Inquiry Boundary Candidate
v0.6.165 Buyer-Facing Commercial Inquiry Boundary Review and Decision
~~~

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.162

v0.6.162 closed the Public Review Entry Point Polish work item.

This checkpoint builds on that accepted public entry path by adding a commercial inquiry boundary.

## Relationship to v0.6.159

v0.6.159 closed the External Review Package Integration work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.156

v0.6.156 closed the Reviewer Walkthrough work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.153

v0.6.153 closed the Control Matrix work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.150

v0.6.150 closed the Safe PoC Boundary Template work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.147

v0.6.147 closed the Technical Due Diligence Summary work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.144

v0.6.144 closed the Enterprise Review Guide work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.165 Buyer-Facing Commercial Inquiry Boundary Review and Decision
~~~

That checkpoint should review the commercial inquiry boundary, confirm claim boundaries, and decide whether to close the Medium-risk work item.
