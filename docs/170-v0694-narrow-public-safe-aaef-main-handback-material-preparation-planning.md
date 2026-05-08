# v0.6.94 Narrow Public-Safe AAEF Main Handback Material Preparation Planning

Status: planning
Date: 2026-05-08

## Purpose

This checkpoint plans how a later checkpoint may create a narrow internal public-safe AAEF main handback material preparation candidate after v0.6.93 selected handback material preparation planning as the next step.

It also records the public/private two-layer publication boundary for handback material preparation:

* the public repository may act as a trust proof and evaluation package,
* the paid or NDA package should remain the implementation and adoption package,
* AAEF main handback material must remain evidence/interface-level only,
* operational, commercial, customer, scanner, credential, delivery, and implementation adoption know-how must not be handed back.

It is a material preparation planning checkpoint only.

It does not prepare AAEF main handback material.
It does not start AAEF main handback work.
It does not open an AAEF main issue.
It does not open an AAEF main pull request.
It does not draft AAEF main release notes.
It does not draft AAEF main document changes.
It does not write AAEF main handback text.
It does not submit anything to AAEF main.
It does not create a handback package.
It does not create a handback draft.
It does not create final handback text.
It does not create a handback material preparation candidate.
It does not create an enterprise review guide.
It does not create a technical due diligence summary.
It does not create a safe PoC boundary template.
It does not create a control matrix.
It does not create a reviewer walkthrough.
It does not modify README current-baseline language.
It does not modify SECURITY.md reporting-channel language.
It does not modify authorization expiry behavior.
It does not modify requested-constraints or authorization-constraints enforcement.
It does not modify external discovery fail-closed behavior.
It does not rename mock or dry-run execution statuses.
It does not approve AAEF Core, Profile, or Practical Package promotion.
It does not decide that any lesson will be promoted to AAEF main.
It does not modify validator behavior.
It does not add validator failure category output.
It does not create a validator output contract.
It does not add or change fixture metadata fields.
It does not add a metadata-level `expected_failure_category` field.
It does not add a JSON Schema file.
It does not rewrite negative fixture metadata.
It does not add new negative fixtures.
It does not reorganize files.
It does not edit `run_all_local_checks.py` beyond registering this read-only planning test.
It does not start Applied Evidence implementation work.
It does not generate new Applied Evidence packages.
It does not generate private review records.
It does not promote new public samples.
It does not refine sanitized public sample content.
It does not change public example text.
It does not create runnable lab configuration.
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Baseline reviewed

~~~text
docs/169-v0693-applied-evidence-handback-material-preparation-decision.md
docs/168-v0692-narrow-public-safe-aaef-main-handback-drafting-candidate-review-close-readiness.md
docs/167-v0691-narrow-public-safe-aaef-main-handback-drafting-candidate.md
docs/166-v0690-narrow-public-safe-aaef-main-handback-drafting-planning.md
tools/validate_public_example_structure.py
examples/applied-evidence/sanitized-static-mock/
examples/applied-evidence/public-validator-negative-fixtures/
~~~

## Planning conclusion

A future narrow internal public-safe AAEF main handback material preparation candidate may be considered, but only as a separate checkpoint.

The future candidate may prepare internal material only if it remains public-safe, evidence/interface-level, and limited to the already closed lesson family:

~~~text
public_safe_evidence_interface_boundary_lessons
~~~

This planning checkpoint does not create that candidate, does not create handback material, and does not write final text.

The future material preparation candidate must preserve the two-layer boundary:

~~~text
public_evaluation_package = allowed
paid_or_nda_adoption_package = protected
aaef_main_handback = evidence_interface_lessons_only
implementation_adoption_know_how = excluded
~~~

## Planning decision

~~~text
narrow_public_safe_aaef_main_handback_material_preparation_planning_completed = true
narrow_public_safe_aaef_main_handback_material_preparation_planning_is_documentation_only = true
narrow_public_safe_aaef_main_handback_material_preparation_planning_uses_v0693_decision = true
narrow_public_safe_aaef_main_handback_material_preparation_planning_started = true
narrow_public_safe_aaef_main_handback_material_preparation_planning_implemented = false
narrow_public_safe_aaef_main_handback_material_candidate_may_be_considered = true
narrow_public_safe_aaef_main_handback_material_candidate_generated = false
narrow_public_safe_aaef_main_handback_material_candidate_close_readiness_may_be_considered = true
narrow_public_safe_aaef_main_handback_material_package_generated = false
narrow_public_safe_aaef_main_handback_material_final_text_generated = false
aaef_main_handback_material_preparation_authorized_for_next_checkpoint = true
aaef_main_handback_material_preparation_started = false
aaef_main_handback_material_prepared = false
aaef_main_handback_material_drafted = false
aaef_main_handback_material_submitted = false
aaef_main_handback_material_package_created = false
public_evaluation_package_boundary_retained = true
paid_or_nda_adoption_package_boundary_retained = true
two_layer_public_private_boundary_retained = true
public_repository_as_trust_proof_retained = true
paid_or_nda_implementation_package_protected = true
aaef_main_handback_limited_to_evidence_interface_lessons = true
aaef_main_handback_excludes_adoption_package = true
aaef_main_handback_excludes_enterprise_runbooks = true
aaef_main_handback_excludes_customer_templates = true
aaef_main_handback_excludes_poc_detail_templates = true
aaef_main_handback_excludes_commercial_tool_gateway_detail = true
aaef_main_handback_excludes_pricing_contract_material = true
aaef_main_handback_excludes_delivery_authorization_material = true
aaef_main_handback_excludes_credential_handling_detail = true
aaef_main_handback_excludes_scanner_output = true
aaef_main_handback_excludes_private_artifacts = true
aaef_main_handback_excludes_patent_sensitive_detail = true
aaef_main_handback_drafting_candidate_close_ready_retained = true
aaef_main_handback_drafting_candidate_retained = true
aaef_main_handback_drafting_candidate_internal_only = true
aaef_main_handback_drafting_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons
aaef_main_handback_drafting_authorized_for_next_checkpoint = false
aaef_main_handback_drafting_started = false
narrow_public_safe_aaef_main_handback_draft_generated = false
narrow_public_safe_aaef_main_handback_final_text_generated = false
aaef_main_handback_preparation_close_ready_retained = true
aaef_main_handback_preparation_candidate_retained = true
aaef_main_handback_preparation_candidate_internal_only = true
aaef_main_handback_preparation_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons
aaef_main_handback_preparation_authorized_for_next_checkpoint = false
aaef_main_handback_preparation_started = false
aaef_main_handback_prepared = false
aaef_main_handback_started = false
aaef_main_handback_submitted = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_release_note_drafted = false
aaef_main_document_change_drafted = false
aaef_main_handback_text_written = false
aaef_main_handback_package_created = false
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
lesson_promotion_to_aaef_main_decided = false
evidence_interface_handback_readiness_close_ready_retained = true
evidence_interface_handback_readiness_candidate_retained = true
evidence_interface_handback_readiness_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons
public_safe_evidence_interface_boundary_lessons_close_ready = true
candidate_identifies_only_evidence_interface_lessons = true
candidate_evaluates_aaef_five_questions = true
candidate_preserves_model_output_not_authority = true
candidate_preserves_validator_output_not_authority = true
candidate_preserves_non_execution_evidence_boundary = true
candidate_excludes_implementation_details = true
candidate_excludes_patent_sensitive_detail = true
candidate_excludes_private_artifacts = true
candidate_excludes_scanner_output = true
candidate_excludes_credentials = true
candidate_excludes_customer_material = true
candidate_excludes_delivery_material = true
candidate_excludes_runtime_authorization = true
candidate_excludes_overclaims = true
public_sample_relationship_to_validator_close_ready_retained = true
public_sample_relationship_to_validator_validator_changed = false
public_sample_relationship_to_validator_output_changed = false
public_sample_relationship_to_validator_contract_created = false
public_sample_relationship_to_validator_public_sample_changed = false
public_sample_relationship_to_validator_sample_refined = false
public_sample_five_questions_clarity_close_ready_retained = true
public_sample_five_questions_clarity_sample_refined = false
public_sample_five_questions_clarity_public_sample_changed = false
applied_evidence_implementation_started = false
applied_evidence_package_generated = false
applied_evidence_private_review_record_generated = false
applied_evidence_public_sample_promoted = false
applied_evidence_sanitized_public_sample_refined = false
applied_evidence_handback_prepared = false
validator_behavior_modified = false
validator_failure_category_output_added = false
validator_json_output_changed = false
validator_output_contract_created = false
metadata_level_expected_failure_category_added = false
fixture_metadata_contract_changed = false
negative_fixture_metadata_rewritten = false
negative_fixtures_added = false
json_schema_added = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
enterprise_review_guide_created = false
technical_due_diligence_summary_created = false
safe_poc_boundary_template_created = false
control_matrix_created = false
reviewer_walkthrough_created = false
readme_current_baseline_updated = false
security_reporting_channel_updated = false
authorization_expiry_now_check_added = false
constraint_diff_enforcement_added = false
external_discovery_fail_closed_added = false
mock_completed_status_renamed = false
~~~

## Two-layer publication boundary

The future material preparation candidate must keep the following split.

| Layer | Public status | Boundary |
| --- | --- | --- |
| Safe executable demo | public evaluation package allowed | Demonstrates safe control behavior, not scanning capability. |
| Boundary design | public evaluation package allowed | Evidence/interface level only. |
| Simplified control matrix | public evaluation package allowed | Summary only; not operational implementation package. |
| Simplified enterprise overview | public evaluation package allowed | Thin pre-sales review aid only. |
| AGPL-3.0 license notice | public evaluation package allowed | License and attribution context only. |
| Not-production-scanner boundary | public evaluation package required | Prevents readiness overclaim. |
| Sample evidence | public evaluation package allowed | Static public-safe sample only. |
| Diagnostic-company PoC plan details | paid_or_nda_adoption_package only | Commercial/adoption know-how. |
| Customer explanation templates | paid_or_nda_adoption_package only | Commercial/adoption know-how. |
| Deployment decision checklists | paid_or_nda_adoption_package only | Implementation adoption package. |
| Integration workflow details | paid_or_nda_adoption_package only | Practical operational know-how. |
| Human review runbooks | paid_or_nda_adoption_package only | Practical operational know-how. |
| Commercial Tool Gateway implementation details | paid_or_nda_adoption_package only | Commercial implementation know-how. |
| Evidence retention design details | paid_or_nda_adoption_package only | Operational design detail. |
| Pricing, contracts, and responsibility boundary material | paid_or_nda_adoption_package only | Commercial material. |
| Commercial license terms | paid_or_nda_adoption_package only | Commercial material. |

## Target material shape for a future candidate

A later material preparation candidate may define internal preparable material, but this checkpoint does not create that material.

The planned future material shape is:

| Planned element | Planning status | Boundary |
| --- | --- | --- |
| Internal material preparation candidate | may_be_considered_later | Internal only; not AAEF main material. |
| Public-safe lesson summary | may_be_considered_later | Use only `public_safe_evidence_interface_boundary_lessons`. |
| AAEF five-questions mapping | may_be_considered_later | Evidence/interface-level only. |
| Authority-boundary note | may_be_considered_later | Model output and validator output are not authority. |
| Non-execution evidence note | may_be_considered_later | Blocked, denied, human-review-required, and non-dispatched evidence remain meaningful. |
| Static public sample note | may_be_considered_later | Static public samples are orientation artifacts, not live evidence. |
| Reviewer traceability note | may_be_considered_later | Traceability only; no private artifacts. |
| Two-layer boundary note | may_be_considered_later | Public evaluation package vs paid/NDA adoption package. |
| Claim-boundary note | may_be_considered_later | No certification, legal, audit, compliance, readiness, diagnostic completeness, or equivalence claims. |
| Submission boundary note | may_be_considered_later | Do not open, draft, or submit AAEF main issue/PR/release/document content. |

## Material source boundaries

Allowed sources for a future material preparation candidate:

~~~text
docs/169-v0693-applied-evidence-handback-material-preparation-decision.md
docs/168-v0692-narrow-public-safe-aaef-main-handback-drafting-candidate-review-close-readiness.md
docs/167-v0691-narrow-public-safe-aaef-main-handback-drafting-candidate.md
docs/166-v0690-narrow-public-safe-aaef-main-handback-drafting-planning.md
docs/164-v0688-narrow-public-safe-aaef-main-handback-preparation-review-close-readiness.md
examples/applied-evidence/sanitized-static-mock/
examples/applied-evidence/public-validator-negative-fixtures/
tools/validate_public_example_structure.py
~~~

Forbidden sources for a future material preparation candidate:

~~~text
private-not-in-git/
diagnostic-company PoC plan details
customer explanation templates
deployment decision checklists
integration workflow details
human review runbooks
commercial Tool Gateway implementation details
evidence retention implementation details
pricing, contracts, and responsibility boundary material
commercial license terms
scanner output
credential material
customer material
private generated artifacts
private review records
commercial pricing or sales strategy
patent-sensitive browser-state or diagnostic reconstruction detail
unreviewed implementation details
runtime execution output
delivery material
~~~

## Material preparation review gates for a future candidate

A later material preparation candidate must pass these gates before any close-readiness review.

| Review gate | Required result |
| --- | --- |
| Internal-only gate | Candidate remains inside AAEF-AI-VA. |
| Public-safe source gate | Candidate derives only from allowed public-safe sources. |
| Two-layer boundary gate | Candidate separates public evaluation package from paid/NDA adoption package. |
| Evidence/interface scope gate | Candidate remains evidence/interface-level. |
| AAEF five-questions gate | Candidate maps lessons to the five questions without overclaiming proof. |
| Model-output-is-not-authority gate | Candidate preserves model output as request, not authority. |
| Validator-output-is-not-authority gate | Candidate preserves validator output as structural support, not authority. |
| Non-execution evidence gate | Candidate preserves blocked/denied/human-review-required/non-dispatched evidence. |
| Static public sample gate | Candidate preserves public samples as orientation artifacts. |
| Sensitive detail gate | Candidate excludes implementation and patent-sensitive details. |
| Commercial/adoption know-how gate | Candidate excludes paid/NDA adoption package material. |
| Private material gate | Candidate excludes private artifacts and private review records. |
| Scanner/customer/credential gate | Candidate excludes scanner output, customer material, and credentials. |
| Delivery gate | Candidate excludes report delivery and delivery authorization. |
| Claim boundary gate | Candidate excludes certification, legal, audit, compliance, readiness, diagnostic completeness, and equivalence claims. |
| Promotion gate | Candidate does not promote anything to AAEF Core, Profile, or Practical Package. |
| AAEF main submission gate | Candidate does not open, draft, or submit AAEF main issue/PR/release/document content. |
| Final-text gate | Candidate does not write final AAEF main handback text. |

## Retained eligible lesson family

The retained eligible lesson family remains:

~~~text
public_safe_evidence_interface_boundary_lessons
~~~

Eligible lessons remain evidence/interface-level only:

* Evidence answers the AAEF five questions.
* AI output as request, not authority.
* Gate decision decides execution permission.
* Dispatch and non-dispatch both need evidence.
* Validator output is not authority.
* Static public samples are not live evidence.
* Reviewer traceability across request, decision, execution posture, and evidence.
* Non-execution evidence remains meaningful.
* AAEF-AI-VA is an Applied Implementation example, as boundary context only and not promotion.

## Retained AAEF five-questions alignment

| AAEF question | Planning status | Boundary retained |
| --- | --- | --- |
| Who or what acted? | eligible_for_material_preparation_candidate | Do not name private tools, private runs, customer targets, or implementation internals. |
| On whose behalf? | eligible_for_material_preparation_candidate | Do not claim public samples prove real customer delegation. |
| With what authority? | eligible_for_material_preparation_candidate | Do not turn AI output or validator output into authority. |
| Was the action allowed at execution? | eligible_for_material_preparation_candidate | Do not authorize runtime execution or imply live execution occurred. |
| What evidence proves what happened? | eligible_for_material_preparation_candidate | Do not claim audit sufficiency, legal sufficiency, certification, compliance, readiness, or diagnostic completeness. |

## Retained public-safe filters

~~~text
handback_material_must_be_public_safe = true
handback_material_must_be_evidence_interface_level = true
handback_material_must_exclude_implementation_details = true
handback_material_must_exclude_patent_sensitive_detail = true
handback_material_must_exclude_private_artifacts = true
handback_material_must_exclude_scanner_output = true
handback_material_must_exclude_credentials = true
handback_material_must_exclude_customer_material = true
handback_material_must_exclude_delivery_material = true
handback_material_must_exclude_runtime_authorization = true
handback_material_must_exclude_commercial_strategy = true
handback_material_must_exclude_certification_claims = true
handback_material_must_exclude_legal_advice_claims = true
handback_material_must_exclude_audit_opinion_claims = true
handback_material_must_exclude_compliance_claims = true
handback_material_must_exclude_external_framework_equivalence_claims = true
handback_material_must_exclude_production_readiness_claims = true
handback_material_must_exclude_diagnostic_completeness_claims = true
handback_material_must_exclude_paid_or_nda_adoption_package = true
handback_material_must_not_open_aaef_main_issue = true
handback_material_must_not_open_aaef_main_pr = true
handback_material_must_not_submit_to_aaef_main = true
handback_material_must_not_prepare_release_notes = true
handback_material_must_not_prepare_document_changes = true
handback_material_must_not_write_final_text = true
~~~

## Retained authority and non-execution boundaries

~~~text
model_output_is_not_authority = true
validator_output_is_not_authority = true
validator_success_is_not_execution_permission = true
gate_decision_remains_authority_relevant = true
execution_authorization_requires_separate_gate_and_evidence = true
~~~

Eligible non-execution examples remain blocked action evidence, denied action evidence, human-review-required evidence, non-dispatched action evidence, reviewer traceability evidence, and evidence that a request did not become an authorized execution.

They do not include live runtime evidence, scanner output, customer targets, credentials, private generated artifacts, delivery material, or diagnostic completeness claims.

## Retained public negative fixture state

The current retained public negative fixture set remains the v0.6.46 static public-safe fixture set.

~~~text
public_negative_fixture_set_current = v0.6.46
public_negative_fixture_count = 13
public_negative_fixture_set_static = true
public_negative_fixture_set_synthetic = true
public_negative_fixture_set_public_safe = true
public_negative_fixture_set_retained = true
~~~

Retained negative fixture categories:

~~~text
missing-package-artifact
missing-scenario-artifact
missing-scenario-directory
malformed-json
broken-linkage
scenario-posture-contradiction
non-example-name
missing-non-proof-statement
missing-five-questions-mapping
hygiene-not-passed
forbidden-text-leakage
overclaim-language
boundary-flag-violation
~~~

## Retained metadata and boundary posture

This material preparation planning checkpoint does not add or remove metadata fields.

Retained metadata fields:

~~~text
negative_category
expected_validator_result
expected_blockers
synthetic_public_safe_static_fixture
source_positive_control
non_authorization_statement
runtime_boundary
runtime_execution_authorized = false
scanner_execution_authorized = false
scan_execution_allowed = false
credential_injection_permitted = false
customer_target = false
customer_target_authorized = false
delivery_authorized = false
customer_deliverable = false
fixture_live_evidence = false
validator_behavior_modified_by_fixture = false
~~~

## Explicitly deferred external review follow-up

The external review follow-up items remain deferred to later, separate checkpoints.

| Follow-up item | v0.6.94 status |
| --- | --- |
| README current/latest baseline clarity | deferred |
| SECURITY.md reporting-channel consistency | deferred |
| Authorization expiry checked against current time | deferred |
| Request/decision constraint-diff enforcement | deferred |
| Fail-closed handling for external_discovery=true | deferred |
| Mock/dry-run status terminology such as avoiding ambiguous `completed` | deferred |
| Enterprise Review Guide | deferred |
| Technical due diligence summary | deferred |
| Safe PoC boundary template | deferred |
| Control matrix | deferred |
| Reviewer walkthrough | deferred |

## What remains intentionally unresolved

This material preparation planning checkpoint does not decide the exact AAEF main handback text, whether any AAEF main handback material should be drafted, whether any AAEF main issue, pull request, release note, or document should be opened or drafted, whether any lesson should be promoted to AAEF main, whether to create a handback package, whether to create a handback draft, whether to create final handback text, whether to prepare release notes, whether to prepare document changes, whether to create a material preparation candidate, whether a material preparation candidate is close-ready, whether to change the public sample, whether to change validator behavior, whether to add validator failure category output, whether to create a validator output contract, whether to refine the sanitized public sample, whether to create a new reviewer walkthrough, whether to generate a new static/mock package, whether to create a new private review record, whether to promote a new public sample, or whether runtime/scanner/Docker/credential/customer/delivery work should ever proceed.

Those decisions require separate checkpoints.

## Applied Implementation boundary

This remains AAEF-AI-VA Applied Implementation work.

~~~text
aaef_handback_category_applied_implementation = true
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
~~~

AAEF main handback, if any, should remain evidence/interface-level only and require a separate checkpoint.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, private review records, delivery material, or paid/NDA adoption package material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.95 Narrow Public-Safe AAEF Main Handback Material Preparation Candidate
~~~

That checkpoint may create a narrow internal material preparation candidate if it preserves this planning boundary.

It should not directly open an AAEF main issue or PR, write final AAEF main handback text, modify validator behavior, modify validator output, modify fixture metadata fields, add JSON Schema, change Applied Evidence package content, change public sample content, or authorize runtime/scanner/Docker/credential/customer/delivery activity.
