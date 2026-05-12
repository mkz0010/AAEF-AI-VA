# v0.6.166 Maintainer Inquiry Address Publication Candidate

Status: candidate
Date: 2026-05-12

## Purpose

This checkpoint implements the Maintainer Inquiry Address Publication candidate after v0.6.165 accepted the email-based inquiry model and deferred actual address publication to a dedicated contact-publication checkpoint.

This is checkpoint 1 of 2 for a Medium-risk contact-publication work item.

This checkpoint publishes the maintainer-approved interim AAEF-wide inquiry address.

The review and decision are deferred to v0.6.167.

## Maintainer-approved interim AAEF-wide inquiry address

The maintainer-approved interim AAEF-wide inquiry address is:

~~~text
hexroot0010@gmail.com
~~~

This address is used as an interim public inquiry route for AAEF-wide and AAEF-AI-VA inquiry.

## Publication scope

The address is published for AAEF framework review inquiry, AAEF research discussion inquiry, AAEF general inquiry, AAEF-AI-VA buyer-facing inquiry, and AAEF-AI-VA commercial inquiry.

Publishing the address provides an inquiry route only.

It does not create a contract, approve a customer PoC, approve paid engagement, publish commercial license terms, authorize runtime execution, authorize scanner execution, authorize Docker execution, authorize credential use, authorize customer target use, approve delivery, or create customer-specific material.

## Repository updates

This checkpoint updates:

~~~text
README.md
docs/buyer-facing-commercial-inquiry-boundary.md
~~~

## Contact interpretation boundaries

Contact publication must not be interpreted as certification, legal compliance determination, audit opinion, audit sufficiency determination, production readiness, production scanner status, diagnostic completeness, authorization for third-party testing, customer PoC approval, commercial contract creation, commercial license terms publication, paid engagement approval, customer-specific material creation, runtime execution approval, scanner execution approval, Docker execution approval, credential use approval, customer target approval, customer delivery approval, equivalence with external frameworks, or AAEF Core/Profile/Practical Package promotion.

The address may be used to ask questions.

It does not grant permission to test systems.

It does not grant access to private materials.

It does not substitute for separate written agreement or authorization.

## Candidate tests

This checkpoint adds:

~~~text
tools/test_v06166_maintainer_inquiry_address_publication_candidate.py
~~~

The tests cover README address publication, commercial inquiry boundary address publication, AAEF-wide inquiry framing, inquiry-route-only interpretation, v0.6.165 continuity, and absence of forbidden affirmative claims.

## Candidate record

~~~text
maintainer_inquiry_address_publication_candidate_completed = true
maintainer_inquiry_address_publication_candidate_is_medium_risk = true
maintainer_inquiry_address_publication_candidate_checkpoint_1_of_2 = true
maintainer_inquiry_address_publication_review_decision_deferred_to_v06167 = true
maintainer_approved_interim_aaef_wide_inquiry_address_published = true
maintainer_approved_interim_aaef_wide_inquiry_address = hexroot0010@gmail.com
inquiry_address_publication_is_email_based = true
inquiry_address_publication_is_aaef_wide = true
readme_inquiry_address_published = true
buyer_facing_commercial_inquiry_boundary_address_published = true
contact_publication_is_not_contract = true
contact_publication_is_not_customer_poc_approval = true
contact_publication_is_not_paid_engagement_approval = true
contact_publication_is_not_runtime_authorization = true
contact_publication_is_not_scanner_authorization = true
contact_publication_is_not_delivery_authorization = true
maintainer_inquiry_address_publication_review_decision_completed = false
review_decision_completed = false
customer_poc_authorized = false
commercial_contract_created = false
paid_engagement_approved = false
commercial_license_terms_created = false
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
selected_next_checkpoint = v0.6.167 Maintainer Inquiry Address Publication Review and Decision
~~~

## What changed

The following files are added:

~~~text
docs/242-v06166-maintainer-inquiry-address-publication-candidate.md
planning/decisions/ADR-0236-add-v06166-maintainer-inquiry-address-publication-candidate.md
planning/issues/0235-add-v06166-maintainer-inquiry-address-publication-candidate.md
tools/test_v06166_maintainer_inquiry_address_publication_candidate.py
~~~

The following files are updated:

~~~text
README.md
docs/buyer-facing-commercial-inquiry-boundary.md
CHANGELOG.md
ROADMAP.md
tools/run_all_local_checks.py
~~~

## What did not happen

No review/decision closeout is completed.

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

No AAEF main handback sequence is reopened.

No certification claim occurs.

No legal compliance claim occurs.

No audit opinion claim occurs.

No production readiness claim occurs.

No external-framework equivalence claim occurs.

No diagnostic completeness claim occurs.

No third-party testing authorization claim occurs.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.165

v0.6.165 accepted the email-based inquiry model and maintainer-provided inquiry address model, then deferred actual inquiry address publication to a dedicated contact-publication checkpoint.

This checkpoint is that publication candidate.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.167 Maintainer Inquiry Address Publication Review and Decision
~~~
