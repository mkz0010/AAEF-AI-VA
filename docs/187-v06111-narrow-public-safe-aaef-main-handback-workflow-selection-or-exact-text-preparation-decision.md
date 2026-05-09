# v0.6.111 Narrow Public-Safe AAEF Main Handback Workflow Selection or Exact Text Preparation Decision

Status: decision
Date: 2026-05-09

## Purpose

This checkpoint decides the next step after v0.6.110 planned the narrow public-safe AAEF main handback submission workflow boundary.

It is a workflow selection or exact text preparation decision checkpoint only.

This checkpoint selects the AAEF main issue workflow as the lower-risk public handback workflow to plan next.

It does not start AAEF main handback work.
It does not open an AAEF main issue.
It does not open an AAEF main pull request.
It does not draft exact AAEF main issue text.
It does not draft exact AAEF main pull request text.
It does not draft AAEF main release notes.
It does not draft AAEF main document changes.
It does not submit anything to AAEF main.
It does not create a handback package.
It does not create a handback draft.
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
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Baseline reviewed

~~~text
docs/186-v06110-narrow-public-safe-aaef-main-handback-submission-workflow-planning.md
docs/185-v06109-applied-evidence-handback-submission-or-pause-decision.md
docs/184-v06108-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate-review-close-readiness.md
docs/183-v06107-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate.md
tools/validate_public_example_structure.py
examples/applied-evidence/sanitized-static-mock/
examples/applied-evidence/public-validator-negative-fixtures/
~~~

## Decision conclusion

The selected workflow is:

~~~text
selected_workflow_after_submission_workflow_planning = aaef_main_issue_workflow
~~~

The selected next checkpoint is:

~~~text
selected_next_step_after_workflow_selection = narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_planning
~~~

This selects planning for exact issue text as the next checkpoint. It does not create the exact issue text now.

Exact issue text is not prepared in this checkpoint.

Exact pull request text is not prepared in this checkpoint.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No content is submitted to AAEF main.

## Decision record

~~~text
narrow_public_safe_aaef_main_handback_workflow_selection_or_exact_text_preparation_decision_completed = true
narrow_public_safe_aaef_main_handback_workflow_selection_or_exact_text_preparation_decision_is_documentation_only = true
narrow_public_safe_aaef_main_handback_workflow_selection_or_exact_text_preparation_decision_uses_v06110_planning = true
selected_workflow_after_submission_workflow_planning = aaef_main_issue_workflow
aaef_main_issue_workflow_selected = true
aaef_main_pull_request_workflow_selected = false
aaef_main_discussion_or_maintainer_note_workflow_selected = false
no_submission_pause_workflow_selected = false
handback_sequence_closeout_workflow_selected = false
exact_issue_text_preparation_planning_selected = true
exact_pr_text_preparation_planning_selected = false
exact_issue_text_preparation_now_selected = false
exact_pr_text_preparation_now_selected = false
selected_next_step_after_workflow_selection = narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_planning
narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_planning_selected = true
narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_planning_started = false
narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_planning_implemented = false
narrow_public_safe_aaef_main_handback_exact_issue_text_generated = false
narrow_public_safe_aaef_main_handback_exact_pr_text_generated = false
narrow_public_safe_aaef_main_handback_issue_text_submission_ready = false
narrow_public_safe_aaef_main_handback_pr_text_submission_ready = false
narrow_public_safe_aaef_main_handback_submission_ready = false
narrow_public_safe_aaef_main_handback_submission_selected = false
narrow_public_safe_aaef_main_handback_submission_started = false
narrow_public_safe_aaef_main_handback_submission_completed = false
aaef_main_handback_exact_issue_text_preparation_planning_authorized_for_next_checkpoint = true
aaef_main_handback_exact_issue_text_authorized_for_next_checkpoint = false
aaef_main_handback_exact_pr_text_authorized_for_next_checkpoint = false
aaef_main_handback_release_note_text_authorized_for_next_checkpoint = false
aaef_main_handback_document_change_text_authorized_for_next_checkpoint = false
aaef_main_handback_package_authorized_for_next_checkpoint = false
direct_submission_selected = false
direct_aaef_main_workflow_selected = false
aaef_main_direct_submission_selected = false
aaef_main_issue_direct_creation_selected = false
aaef_main_pr_direct_creation_selected = false
aaef_main_release_note_direct_drafting_selected = false
aaef_main_document_change_direct_drafting_selected = false
aaef_main_handback_package_direct_creation_selected = false
narrow_public_safe_aaef_main_handback_submittable_text_candidate_close_ready = true
narrow_public_safe_aaef_main_handback_submittable_text_candidate_retained = true
narrow_public_safe_aaef_main_handback_submittable_text_candidate_internal_only = true
narrow_public_safe_aaef_main_handback_submittable_text_candidate_submittable = false
narrow_public_safe_aaef_main_handback_submittable_text_candidate_submission_ready = false
narrow_public_safe_aaef_main_handback_submittable_text_candidate_not_submitted = true
narrow_public_safe_aaef_main_handback_submittable_text_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons
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
aaef_main_handback_package_created = false
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
lesson_promotion_to_aaef_main_decided = false
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
handback_text_must_be_public_safe = true
handback_text_must_be_evidence_interface_level = true
handback_text_must_exclude_implementation_details = true
handback_text_must_exclude_patent_sensitive_detail = true
handback_text_must_exclude_paid_or_nda_adoption_package = true
handback_text_must_not_open_aaef_main_issue = true
handback_text_must_not_open_aaef_main_pr = true
handback_text_must_not_submit_to_aaef_main = true
~~~

## Workflow decision

| Workflow option | Decision | Reason |
| --- | --- | --- |
| AAEF main issue workflow | selected_for_planning | Lowest-change public handback route; can share an evidence/interface lesson without proposing repository content changes. |
| AAEF main pull request workflow | not selected now | PR implies document changes and is higher-impact than needed at this stage. |
| AAEF main discussion or maintainer-note workflow | not selected now | Less direct than an issue and may not preserve issue-based review traceability. |
| No-submission pause workflow | not selected now | The close-ready candidate and workflow planning justify a narrow exact issue text planning step. |
| Handback sequence closeout workflow | not selected now | Closeout remains available later if exact issue text planning fails public-safe gates. |
| Exact issue text preparation now | not selected now | A planning checkpoint should define exact-text controls before text generation. |
| Exact pull request text preparation now | not selected now | PR workflow is not selected. |
| Release note text preparation | not selected | Out of scope. |
| Document-change text preparation | not selected | Out of scope. |
| Handback package creation | not selected | Out of scope. |
| Direct AAEF main submission | not selected | Requires separate exact text and human approval gates. |

## Why issue workflow first

The AAEF main issue workflow is selected for planning because it is narrower than a pull request, does not imply immediate AAEF main document changes, preserves public review traceability, and can communicate an Applied Implementation evidence/interface lesson without promoting AAEF-AI-VA into AAEF Core, Profile, or Practical Package material.

This selection is still non-executing.

Only the human maintainer may execute an AAEF main workflow.

AI output is workflow planning support, not execution authority.

Validator output may support structural review, but validator output is not authority.

## Exact text preparation boundary

The next checkpoint may plan exact AAEF main issue text preparation.

It may define exact issue text source controls, exact issue text public-safe filters, title/body/labels/milestone constraints, non-submission controls, human approval gates, target repository boundary, and how to preserve AAEF five-questions alignment, evidence/interface-level scope, model-output-is-not-authority, validator-output-is-not-authority, non-execution evidence, and the two-layer public/private boundary.

It must not open the issue, submit the issue, or prepare pull request text.

## Required gates before exact issue text can become executable workflow material

| Gate | Required result |
| --- | --- |
| Exact issue text planning gate | Plan exact issue text constraints before generating exact text. |
| Exact issue text candidate gate | Generate exact issue text only in a later candidate checkpoint. |
| Close-readiness gate | Review exact issue text before any submission decision. |
| Human approval gate | Human maintainer explicitly approves exact text and target workflow. |
| Non-submission gate | No workflow is executed unless a later checkpoint explicitly authorizes it. |
| Public-safe source gate | Text derives only from allowed public-safe sources. |
| Evidence/interface scope gate | Text remains evidence/interface-level. |
| AAEF five-questions gate | Text maps lessons to the five questions without overclaiming proof. |
| Authority-boundary gate | Text preserves model-output-is-not-authority and validator-output-is-not-authority. |
| Two-layer boundary gate | Text separates public evaluation package from paid/NDA adoption package. |
| Claim-boundary gate | Text excludes certification, legal, audit, compliance, readiness, diagnostic completeness, and equivalence claims. |

## Retained close-ready candidate boundary

The v0.6.108 close-ready submittable text preparation candidate remains close-ready but internal only.

~~~text
candidate_close_ready = true
candidate_internal_only = true
candidate_not_submitted = true
candidate_not_opened_as_issue = true
candidate_not_opened_as_pr = true
candidate_not_release_note_text = true
candidate_not_document_change_text = true
candidate_not_handback_package = true
reviewer_aid_only = true
~~~

## Retained eligible lesson family

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
| Who or what acted? | retained_for_exact_issue_text_preparation_planning | Do not name private tools, private runs, customer targets, or implementation internals. |
| On whose behalf? | retained_for_exact_issue_text_preparation_planning | Do not claim public samples prove real customer delegation. |
| With what authority? | retained_for_exact_issue_text_preparation_planning | Do not turn AI output or validator output into authority. |
| Was the action allowed at execution? | retained_for_exact_issue_text_preparation_planning | Do not authorize runtime execution or imply live execution occurred. |
| What evidence proves what happened? | retained_for_exact_issue_text_preparation_planning | Do not claim audit sufficiency, legal sufficiency, certification, compliance, readiness, or diagnostic completeness. |

## Retained two-layer publication boundary

| Layer | Decision status | Boundary |
| --- | --- | --- |
| Public evaluation package | retained | Trust proof only. |
| Paid or NDA adoption package | retained | Implementation/adoption package protected. |
| AAEF main handback | retained | Evidence/interface lessons only. |

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
~~~

## Retained authority and non-execution boundaries

~~~text
model_output_is_not_authority = true
validator_output_is_not_authority = true
validator_success_is_not_execution_permission = true
gate_decision_remains_authority_relevant = true
execution_authorization_requires_separate_gate_and_evidence = true
~~~

## Retained public negative fixture state

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

## Explicitly deferred external review follow-up

| Follow-up item | v0.6.111 status |
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

This checkpoint does not prepare exact issue text, prepare exact PR text, open an AAEF main issue, open an AAEF main pull request, submit anything to AAEF main, create a handback package, create a handback draft, prepare release notes, prepare document changes, decide lesson promotion to AAEF main, change public samples, change validator behavior, add validator output, add metadata-level failure categories, add JSON Schema, generate packages, create private review records, promote public samples, or authorize runtime/scanner/Docker/credential/customer/delivery activity.

Those decisions require separate checkpoints.

## Applied Implementation boundary

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
v0.6.112 Narrow Public-Safe AAEF Main Handback Exact Issue Text Preparation Planning
~~~

That checkpoint should plan how exact public-safe AAEF main issue text could be prepared while preserving evidence/interface boundaries and non-submission controls.

It should not directly open an AAEF main issue or PR, submit anything to AAEF main, prepare PR text, modify validator behavior, modify validator output, modify fixture metadata fields, add JSON Schema, change Applied Evidence package content, change public sample content, or authorize runtime/scanner/Docker/credential/customer/delivery activity.
