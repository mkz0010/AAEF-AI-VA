# v0.6.97 Applied Evidence Handback Material Drafting or Submission Decision

Status: decision
Date: 2026-05-08

## Purpose

This checkpoint decides the next step after v0.6.96 closed the internal narrow public-safe AAEF main handback material preparation candidate.

It decides whether AAEF-AI-VA should move toward narrow public-safe AAEF main handback text drafting planning, directly submit to AAEF main, pause, or move to another Applied Evidence gap.

It is a drafting or submission decision checkpoint only.

It does not prepare AAEF main handback material.
It does not start AAEF main handback work.
It does not open an AAEF main issue.
It does not open an AAEF main pull request.
It does not draft AAEF main issue text.
It does not draft AAEF main pull request text.
It does not draft AAEF main release notes.
It does not draft AAEF main document changes.
It does not write AAEF main handback text.
It does not write final AAEF main handback text.
It does not submit anything to AAEF main.
It does not create a handback package.
It does not create a handback draft.
It does not create final handback text.
It does not create submittable handback text.
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
It does not edit `run_all_local_checks.py` beyond registering this read-only decision test.
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
docs/172-v0696-narrow-public-safe-aaef-main-handback-material-preparation-candidate-review-close-readiness.md
docs/171-v0695-narrow-public-safe-aaef-main-handback-material-preparation-candidate.md
docs/170-v0694-narrow-public-safe-aaef-main-handback-material-preparation-planning.md
docs/169-v0693-applied-evidence-handback-material-preparation-decision.md
tools/validate_public_example_structure.py
examples/applied-evidence/sanitized-static-mock/
examples/applied-evidence/public-validator-negative-fixtures/
~~~

## Decision conclusion

AAEF-AI-VA should proceed to a separate, narrow, documentation-only AAEF main handback text drafting planning checkpoint.

The selected next step is:

~~~text
selected_next_step_after_material_preparation_closeout = narrow_public_safe_aaef_main_handback_text_drafting_planning
~~~

Direct submission to AAEF main is not selected. Direct AAEF main issue creation is not selected. Direct AAEF main pull request creation is not selected. Direct release note drafting, document-change drafting, and handback package creation are not selected.

This decision only authorizes a later planning checkpoint to decide how exact public-safe AAEF main handback text could be drafted while preserving the existing boundaries.

## Decision record

~~~text
applied_evidence_handback_material_drafting_or_submission_decision_completed = true
applied_evidence_handback_material_drafting_or_submission_decision_is_documentation_only = true
applied_evidence_handback_material_drafting_or_submission_decision_uses_v0696_close_readiness = true
selected_next_step_after_material_preparation_closeout = narrow_public_safe_aaef_main_handback_text_drafting_planning
narrow_public_safe_aaef_main_handback_text_drafting_planning_selected = true
narrow_public_safe_aaef_main_handback_text_drafting_planning_may_be_considered = true
narrow_public_safe_aaef_main_handback_text_drafting_planning_started = false
narrow_public_safe_aaef_main_handback_text_drafting_planning_implemented = false
narrow_public_safe_aaef_main_handback_text_candidate_may_be_considered = true
narrow_public_safe_aaef_main_handback_text_candidate_generated = false
narrow_public_safe_aaef_main_handback_text_package_generated = false
narrow_public_safe_aaef_main_handback_submittable_text_generated = false
narrow_public_safe_aaef_main_handback_submission_selected = false
narrow_public_safe_aaef_main_handback_submission_started = false
aaef_main_direct_submission_selected = false
aaef_main_issue_direct_creation_selected = false
aaef_main_pr_direct_creation_selected = false
aaef_main_release_note_direct_drafting_selected = false
aaef_main_document_change_direct_drafting_selected = false
aaef_main_handback_package_direct_creation_selected = false
aaef_main_handback_material_preparation_close_ready_retained = true
aaef_main_handback_material_preparation_candidate_retained = true
aaef_main_handback_material_preparation_candidate_internal_only = true
aaef_main_handback_material_preparation_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons
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

## Options reviewed

| Option | Decision | Reason |
| --- | --- | --- |
| Narrow public-safe AAEF main handback text drafting planning | selected | v0.6.96 closed material preparation candidate, so the next safe step is to plan exact text drafting without preparing or submitting text. |
| Direct AAEF main submission now | not selected | Too early; exact public-safe text and target workflow require a separate planning checkpoint. |
| Open AAEF main issue now | not selected | Public AAEF main work should wait until exact public-safe text and workflow are explicitly authorized. |
| Open AAEF main PR now | not selected | No final or submittable handback text has been prepared or authorized. |
| Draft AAEF main release notes now | not selected | No AAEF main release text has been authorized. |
| Draft AAEF main document changes now | not selected | No AAEF main document change has been authorized. |
| Create a handback package now | not selected | Packaging requires a separate text-drafting and package decision. |
| Move to external review P0 fixes now | not selected now | Important but separate implementation/documentation tracks should remain separate from handback text drafting. |
| Move to buyer-facing P1 docs now | not selected now | Enterprise review docs remain a separate public/commercial documentation track. |
| Runtime/scanner/Docker/credential/customer/delivery work | not selected now | Runtime work remains unauthorized. |
| Pause | not selected now | The close-ready material preparation candidate provides a safe next planning step. |

## Selected next-step boundary

The selected next step may plan narrow public-safe AAEF main handback text drafting.

The next checkpoint may plan target text shape, target audience, permitted public-safe text families, forbidden text families, exact source boundaries for draftable text, review gates before any final text or AAEF main workflow, and how to preserve evidence/interface-level scope, AAEF five-questions alignment, model-output-is-not-authority, validator-output-is-not-authority, non-execution evidence, static public sample boundaries, the two-layer public/private boundary, and non-promotion to AAEF Core, Profile, or Practical Package.

The next checkpoint must avoid implementation detail, patent-sensitive detail, private artifacts, scanner output, credentials, customer material, delivery material, commercial strategy, paid/NDA adoption package material, production-readiness, diagnostic-completeness, certification, legal, audit, compliance, and equivalence claims.

The next checkpoint should not write final handback text. The next checkpoint should not create submittable AAEF main text. The next checkpoint should not open an AAEF main issue or PR.

## Retained two-layer publication boundary

The decision retains this split.

| Layer | Decision status | Boundary |
| --- | --- | --- |
| Safe executable demo | retained | Public evaluation package allowed; not scanning capability proof. |
| Boundary design | retained | Public evaluation package allowed; evidence/interface level only. |
| Simplified control matrix | retained | Public evaluation package allowed; summary only. |
| Simplified enterprise overview | retained | Public evaluation package allowed; thin review aid only. |
| AGPL-3.0 license notice | retained | Public evaluation package allowed; license context only. |
| Not-production-scanner boundary | retained | Public evaluation package required; prevents readiness overclaim. |
| Sample evidence | retained | Public evaluation package allowed; static public-safe sample only. |
| Diagnostic-company PoC plan details | retained | Paid/NDA adoption package only. |
| Customer explanation templates | retained | Paid/NDA adoption package only. |
| Deployment decision checklists | retained | Paid/NDA adoption package only. |
| Integration workflow details | retained | Paid/NDA adoption package only. |
| Human review runbooks | retained | Paid/NDA adoption package only. |
| Commercial Tool Gateway implementation details | retained | Paid/NDA adoption package only. |
| Evidence retention design details | retained | Paid/NDA adoption package only. |
| Pricing, contracts, and responsibility boundary material | retained | Paid/NDA adoption package only. |
| Commercial license terms | retained | Paid/NDA adoption package only. |

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

| AAEF question | Decision status | Boundary retained |
| --- | --- | --- |
| Who or what acted? | eligible_for_text_drafting_planning | Do not name private tools, private runs, customer targets, or implementation internals. |
| On whose behalf? | eligible_for_text_drafting_planning | Do not claim public samples prove real customer delegation. |
| With what authority? | eligible_for_text_drafting_planning | Do not turn AI output or validator output into authority. |
| Was the action allowed at execution? | eligible_for_text_drafting_planning | Do not authorize runtime execution or imply live execution occurred. |
| What evidence proves what happened? | eligible_for_text_drafting_planning | Do not claim audit sufficiency, legal sufficiency, certification, compliance, readiness, or diagnostic completeness. |

## Retained public-safe filters

~~~text
handback_text_must_be_public_safe = true
handback_text_must_be_evidence_interface_level = true
handback_text_must_exclude_implementation_details = true
handback_text_must_exclude_patent_sensitive_detail = true
handback_text_must_exclude_private_artifacts = true
handback_text_must_exclude_scanner_output = true
handback_text_must_exclude_credentials = true
handback_text_must_exclude_customer_material = true
handback_text_must_exclude_delivery_material = true
handback_text_must_exclude_runtime_authorization = true
handback_text_must_exclude_commercial_strategy = true
handback_text_must_exclude_paid_or_nda_adoption_package = true
handback_text_must_exclude_certification_claims = true
handback_text_must_exclude_legal_advice_claims = true
handback_text_must_exclude_audit_opinion_claims = true
handback_text_must_exclude_compliance_claims = true
handback_text_must_exclude_external_framework_equivalence_claims = true
handback_text_must_exclude_production_readiness_claims = true
handback_text_must_exclude_diagnostic_completeness_claims = true
handback_text_must_not_open_aaef_main_issue = true
handback_text_must_not_open_aaef_main_pr = true
handback_text_must_not_submit_to_aaef_main = true
handback_text_must_not_prepare_release_notes = true
handback_text_must_not_prepare_document_changes = true
handback_text_must_not_write_final_text = true
handback_text_must_not_create_submittable_text = true
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

This drafting or submission decision checkpoint does not add or remove metadata fields.

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

| Follow-up item | v0.6.97 status |
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

This drafting or submission decision checkpoint does not decide the exact AAEF main handback text, whether any AAEF main handback material should be drafted, whether any AAEF main issue, pull request, release note, or document should be opened or drafted, whether any lesson should be promoted to AAEF main, whether to create a handback package, whether to create a handback draft, whether to create final handback text, whether to create submittable text, whether to prepare release notes, whether to prepare document changes, whether to create a text drafting candidate, whether a text drafting candidate is close-ready, whether to change the public sample, whether to change validator behavior, whether to add validator failure category output, whether to create a validator output contract, whether to refine the sanitized public sample, whether to create a new reviewer walkthrough, whether to generate a new static/mock package, whether to create a new private review record, whether to promote a new public sample, or whether runtime/scanner/Docker/credential/customer/delivery work should ever proceed.

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
v0.6.98 Narrow Public-Safe AAEF Main Handback Text Drafting Planning
~~~

That checkpoint should plan how to draft exact public-safe AAEF main handback text while preserving evidence/interface boundaries.

It should not directly open an AAEF main issue or PR, write final AAEF main handback text, create submittable text, modify validator behavior, modify validator output, modify fixture metadata fields, add JSON Schema, change Applied Evidence package content, change public sample content, or authorize runtime/scanner/Docker/credential/customer/delivery activity.
