# v0.6.90 Narrow Public-Safe AAEF Main Handback Drafting Planning

Status: planning
Date: 2026-05-08

## Purpose

This checkpoint plans how a later checkpoint may create a narrow internal public-safe AAEF main handback drafting candidate after v0.6.89 selected handback drafting planning as the next step.

It defines drafting controls, target audience, target artifact shape, permitted wording families, forbidden wording families, source boundaries, and review gates for a future internal handback drafting candidate.

It is a drafting planning checkpoint only.

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
It does not create a handback drafting candidate.
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
It does not create a new reviewer walkthrough.
It does not start validator relationship implementation work.
It does not start validator behavior hardening implementation.
It does not approve validator behavior hardening implementation readiness.
It does not create runnable lab configuration.
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Baseline reviewed

~~~text
docs/165-v0689-applied-evidence-handback-drafting-decision.md
docs/164-v0688-narrow-public-safe-aaef-main-handback-preparation-review-close-readiness.md
docs/163-v0687-narrow-public-safe-aaef-main-handback-preparation-candidate.md
docs/162-v0686-narrow-public-safe-aaef-main-handback-preparation-planning.md
tools/validate_public_example_structure.py
examples/applied-evidence/sanitized-static-mock/
examples/applied-evidence/public-validator-negative-fixtures/
~~~

## Planning conclusion

A future narrow internal public-safe AAEF main handback drafting candidate may be considered, but only as a separate checkpoint.

The future candidate may create internal draftable material only if it remains public-safe, evidence/interface-level, and limited to the already closed lesson family:

~~~text
public_safe_evidence_interface_boundary_lessons
~~~

This planning checkpoint does not create that candidate and does not write draft text.

The future candidate must preserve all current boundaries and must not open or draft AAEF main issue, pull request, release note, or document-change text unless a later checkpoint explicitly authorizes the exact public-safe handback text and target AAEF main workflow.

## Planning decision

~~~text
narrow_public_safe_aaef_main_handback_drafting_planning_completed = true
narrow_public_safe_aaef_main_handback_drafting_planning_is_documentation_only = true
narrow_public_safe_aaef_main_handback_drafting_planning_uses_v0689_decision = true
narrow_public_safe_aaef_main_handback_drafting_planning_started = true
narrow_public_safe_aaef_main_handback_drafting_planning_implemented = false
narrow_public_safe_aaef_main_handback_drafting_candidate_may_be_considered = true
narrow_public_safe_aaef_main_handback_drafting_candidate_generated = false
narrow_public_safe_aaef_main_handback_drafting_candidate_close_readiness_may_be_considered = true
narrow_public_safe_aaef_main_handback_draft_may_be_considered = true
narrow_public_safe_aaef_main_handback_draft_generated = false
aaef_main_handback_drafting_authorized_for_next_checkpoint = true
aaef_main_handback_drafting_started = false
aaef_main_handback_preparation_close_ready_retained = true
aaef_main_handback_preparation_candidate_retained = true
aaef_main_handback_preparation_candidate_internal_only = true
aaef_main_handback_preparation_candidate_lesson_family = public_safe_evidence_interface_boundary_lessons
aaef_main_handback_preparation_authorized_for_next_checkpoint = false
aaef_main_handback_preparation_started = false
aaef_main_handback_material_prepared = false
aaef_main_handback_material_drafted = false
aaef_main_handback_material_submitted = false
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
public_sample_relationship_to_validator_reader_aid_retained = true
public_sample_relationship_to_validator_candidate_revision_required = false
public_sample_relationship_to_validator_implemented = false
public_sample_relationship_to_validator_validator_changed = false
public_sample_relationship_to_validator_output_changed = false
public_sample_relationship_to_validator_contract_created = false
public_sample_relationship_to_validator_public_sample_changed = false
public_sample_relationship_to_validator_sample_refined = false
public_sample_five_questions_clarity_close_ready_retained = true
public_sample_five_questions_clarity_reader_aid_retained = true
public_sample_five_questions_clarity_implemented = false
public_sample_five_questions_clarity_sample_refined = false
public_sample_five_questions_clarity_public_sample_changed = false
applied_evidence_reviewer_current_state_summary_retained = true
applied_evidence_reviewer_current_state_summary_close_ready_retained = true
applied_evidence_current_state_summary_generated = true
applied_evidence_implementation_started = false
applied_evidence_package_generated = false
applied_evidence_private_review_record_generated = false
applied_evidence_public_sample_promoted = false
applied_evidence_sanitized_public_sample_refined = false
applied_evidence_fixture_rewrite_approved = false
applied_evidence_schema_change_approved = false
applied_evidence_handback_prepared = false
applied_evidence_static_mock_package_retained = true
applied_evidence_sanitized_public_sample_retained = true
applied_evidence_reviewer_walkthrough_history_retained = true
applied_evidence_five_questions_mapping_history_retained = true
applied_evidence_handback_boundary_retained = true
public_validator_pause_closeout_retained = true
public_validator_track_pause_state_retained = true
public_validator_maintenance_continue_now = false
validator_behavior_hardening_implementation_readiness_deferred = true
public_validator_behavior_hardening_implementation_not_approved = true
documentation_only_hardening_scope_retained = true
documentation_only_failure_category_mapping_retained = true
reviewer_navigation_note_retained = true
public_negative_fixture_index_summary_retained = true
v0689_handback_drafting_decision_retained = true
validator_behavior_hardening_implementation_may_be_considered = false
validator_behavior_hardening_candidate_added = false
validator_behavior_hardening_implemented = false
validator_behavior_modified = false
validator_behavior_expansion_implemented = false
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
~~~

## Target artifact shape for a future candidate

A later drafting candidate may define an internal draftable artifact shape, but this checkpoint does not create the artifact.

| Planned element | Planning status | Boundary |
| --- | --- | --- |
| Internal handback drafting candidate | may_be_considered_later | Internal only; not AAEF main material. |
| Source lesson family summary | may_be_considered_later | Use only `public_safe_evidence_interface_boundary_lessons`. |
| AAEF five-questions mapping | may_be_considered_later | Evidence/interface-level only. |
| Authority-boundary statement | may_be_considered_later | Model output and validator output are not authority. |
| Non-execution evidence statement | may_be_considered_later | Blocked, denied, human-review-required, and non-dispatched evidence remain meaningful. |
| Public sample boundary statement | may_be_considered_later | Static public samples are orientation artifacts, not live evidence. |
| Reviewer traceability statement | may_be_considered_later | Traceability only; no private artifacts. |
| Claim-boundary statement | may_be_considered_later | No certification, legal, audit, compliance, or equivalence claims. |
| Exclusion filter statement | may_be_considered_later | Exclude implementation, patent-sensitive, private, scanner, credential, customer, delivery, commercial, and runtime details. |
| Submission boundary statement | may_be_considered_later | Do not open, draft, or submit AAEF main issue/PR/release/document content. |

## Target audience planning

A future internal drafting candidate may be written for AAEF main maintainers and reviewers, but only at a public-safe evidence/interface level.

| Audience | Planned posture |
| --- | --- |
| AAEF main maintainers | Explain candidate evidence/interface lessons without implementation or private detail. |
| AAEF reviewers | Make the AAEF five-questions relationship reviewable. |
| AAEF framework readers | Clarify that the applied implementation lesson is not a Core/Profile/Practical Package promotion. |
| AAEF-AI-VA maintainers | Preserve the separation between applied implementation work and public AAEF artifacts. |

## Permitted wording families

A future drafting candidate may use only these wording families.

| Wording family | Permitted scope |
| --- | --- |
| Evidence answers the AAEF five questions | Permitted only as an evidence/interface-level lesson. |
| AI output as request, not authority | Permitted as a boundary lesson. |
| Gate decision decides execution permission | Permitted without implementation details. |
| Dispatch and non-dispatch both need evidence | Permitted without runtime or scanner detail. |
| Validator output is not authority | Permitted as a structural validator boundary. |
| Static public samples are not live evidence | Permitted as a sample-boundary note. |
| Reviewer traceability across request, decision, execution posture, and evidence | Permitted without private generated artifacts. |
| Non-execution evidence remains meaningful | Permitted without delivery or diagnostic completeness claims. |
| AAEF-AI-VA is an Applied Implementation example | Permitted only as boundary context, not promotion. |

## Forbidden wording families

A future drafting candidate must exclude these wording families.

| Forbidden wording family | Reason |
| --- | --- |
| AAEF-AI-VA proves AAEF compliance | Overclaim. |
| AAEF-AI-VA certifies or validates AAEF | Certification/equivalence overclaim. |
| AAEF-AI-VA is production-ready | Unsupported readiness claim. |
| AAEF-AI-VA provides legal compliance | Legal/compliance overclaim. |
| AAEF-AI-VA provides audit opinion | Audit overclaim. |
| AAEF-AI-VA proves vulnerability detection completeness | Diagnostic completeness overclaim. |
| Public validator success authorizes execution | Validator-output-as-authority error. |
| Model output authorizes execution | Model-output-as-authority error. |
| Public samples are live evidence | Static public sample boundary error. |
| Scanner output or customer evidence | Private/scanner/customer material. |
| Browser-state or diagnostic reconstruction detail | Patent-sensitive detail. |
| Commercial pricing or sales strategy | Commercial strategy boundary. |
| Credential handling details | Credential material boundary. |
| Customer target information | Customer material boundary. |
| Delivery authorization | Delivery boundary. |

## Drafting source boundaries

A future drafting candidate may only derive from public-safe repository artifacts and closed checkpoint conclusions.

Allowed sources:

~~~text
docs/165-v0689-applied-evidence-handback-drafting-decision.md
docs/164-v0688-narrow-public-safe-aaef-main-handback-preparation-review-close-readiness.md
docs/163-v0687-narrow-public-safe-aaef-main-handback-preparation-candidate.md
docs/162-v0686-narrow-public-safe-aaef-main-handback-preparation-planning.md
docs/160-v0684-evidence-interface-handback-readiness-review-close-readiness.md
docs/159-v0683-evidence-interface-handback-readiness-candidate.md
examples/applied-evidence/sanitized-static-mock/
examples/applied-evidence/public-validator-negative-fixtures/
tools/validate_public_example_structure.py
~~~

Forbidden sources:

~~~text
private-not-in-git/
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

## Drafting review gates for a future candidate

A later drafting candidate must pass these gates before any close-readiness review.

| Review gate | Required result |
| --- | --- |
| Internal-only gate | Candidate remains inside AAEF-AI-VA. |
| Public-safe source gate | Candidate derives only from allowed public-safe sources. |
| Evidence/interface scope gate | Candidate remains evidence/interface-level. |
| AAEF five-questions gate | Candidate maps lessons to the five questions without overclaiming proof. |
| Model-output-is-not-authority gate | Candidate preserves model output as request, not authority. |
| Validator-output-is-not-authority gate | Candidate preserves validator output as structural support, not authority. |
| Non-execution evidence gate | Candidate preserves blocked/denied/human-review-required/non-dispatched evidence. |
| Static public sample gate | Candidate preserves public samples as orientation artifacts. |
| Sensitive detail gate | Candidate excludes implementation and patent-sensitive details. |
| Private material gate | Candidate excludes private artifacts and private review records. |
| Scanner/customer/credential gate | Candidate excludes scanner output, customer material, and credentials. |
| Delivery gate | Candidate excludes report delivery and delivery authorization. |
| Claim boundary gate | Candidate excludes certification, legal, audit, compliance, and equivalence claims. |
| Promotion gate | Candidate does not promote anything to AAEF Core, Profile, or Practical Package. |
| AAEF main submission gate | Candidate does not open, draft, or submit AAEF main issue/PR/release/document content. |

## Retained eligible lesson family

The retained eligible lesson family remains:

~~~text
public_safe_evidence_interface_boundary_lessons
~~~

| Eligible lesson | Drafting planning status | Boundary retained |
| --- | --- | --- |
| Evidence answers the AAEF five questions | allowed_for_future_drafting_candidate_planning | Does not claim live execution proof. |
| AI output as request, not authority | allowed_for_future_drafting_candidate_planning | Does not turn model output into authority. |
| Gate decision decides execution permission | allowed_for_future_drafting_candidate_planning | Does not describe private implementation or patent-sensitive mechanics. |
| Dispatch and non-dispatch both need evidence | allowed_for_future_drafting_candidate_planning | Does not authorize runtime, scanner, Docker, credential, customer, or delivery activity. |
| Validator output is not authority | allowed_for_future_drafting_candidate_planning | Does not turn validator success into execution permission. |
| Static public samples are not live evidence | allowed_for_future_drafting_candidate_planning | Does not turn public samples into customer evidence. |
| Reviewer traceability across request, decision, execution posture, and evidence | allowed_for_future_drafting_candidate_planning | Does not disclose private generated artifacts. |
| Non-execution evidence remains meaningful | allowed_for_future_drafting_candidate_planning | Does not imply diagnostic completeness or delivery readiness. |

## Retained AAEF five-questions alignment

| AAEF question | Drafting planning status | Boundary retained |
| --- | --- | --- |
| Who or what acted? | allowed_for_future_drafting_candidate_planning | Do not name private tools, private runs, customer targets, or implementation internals. |
| On whose behalf? | allowed_for_future_drafting_candidate_planning | Do not claim public samples prove real customer delegation. |
| With what authority? | allowed_for_future_drafting_candidate_planning | Do not turn AI output or validator output into authority. |
| Was the action allowed at execution? | allowed_for_future_drafting_candidate_planning | Do not authorize runtime execution or imply live execution occurred. |
| What evidence proves what happened? | allowed_for_future_drafting_candidate_planning | Do not claim audit sufficiency, legal sufficiency, certification, compliance, or diagnostic completeness. |

## Retained public-safe filters

~~~text
handback_drafting_candidate_must_be_public_safe = true
handback_drafting_candidate_must_be_evidence_interface_level = true
handback_drafting_candidate_must_exclude_implementation_details = true
handback_drafting_candidate_must_exclude_patent_sensitive_detail = true
handback_drafting_candidate_must_exclude_private_artifacts = true
handback_drafting_candidate_must_exclude_scanner_output = true
handback_drafting_candidate_must_exclude_credentials = true
handback_drafting_candidate_must_exclude_customer_material = true
handback_drafting_candidate_must_exclude_delivery_material = true
handback_drafting_candidate_must_exclude_runtime_authorization = true
handback_drafting_candidate_must_exclude_commercial_strategy = true
handback_drafting_candidate_must_exclude_certification_claims = true
handback_drafting_candidate_must_exclude_legal_advice_claims = true
handback_drafting_candidate_must_exclude_audit_opinion_claims = true
handback_drafting_candidate_must_exclude_compliance_claims = true
handback_drafting_candidate_must_exclude_external_framework_equivalence_claims = true
handback_drafting_candidate_must_not_open_aaef_main_issue = true
handback_drafting_candidate_must_not_open_aaef_main_pr = true
handback_drafting_candidate_must_not_submit_to_aaef_main = true
handback_drafting_candidate_must_not_prepare_release_notes = true
handback_drafting_candidate_must_not_prepare_document_changes = true
~~~

## Retained authority and non-execution boundaries

~~~text
model_output_is_not_authority = true
validator_output_is_not_authority = true
validator_success_is_not_execution_permission = true
gate_decision_remains_authority_relevant = true
execution_authorization_requires_separate_gate_and_evidence = true
~~~

Eligible non-execution examples remain:

* blocked action evidence,
* denied action evidence,
* human-review-required evidence,
* non-dispatched action evidence,
* reviewer traceability evidence,
* evidence that a request did not become an authorized execution.

They do not include live runtime evidence, scanner output, customer targets, credentials, private generated artifacts, delivery material, or diagnostic completeness claims.

## Retained forbidden content filter

~~~text
implementation_details = forbidden
patent_sensitive_browser_state_or_diagnostic_reconstruction_detail = forbidden
commercial_strategy = forbidden
pricing_strategy = forbidden
customer_material = forbidden
customer_target_information = forbidden
scanner_output = forbidden
credential_material = forbidden
private_generated_artifacts = forbidden
private_review_records = forbidden
runtime_authorization = forbidden
delivery_authorization = forbidden
diagnostic_completeness_claim = forbidden
certification_claim = forbidden
legal_advice_claim = forbidden
audit_opinion_claim = forbidden
compliance_claim = forbidden
external_framework_equivalence_claim = forbidden
~~~

## Retained public validator and public sample boundaries

The public validator remains:

~~~text
tools/validate_public_example_structure.py
~~~

The public sample baseline remains:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

The public validator remains a structural validator for public examples.

It does not provide vulnerability detection, diagnostic completeness, live execution evidence, runtime authorization, scanner authorization, credential authorization, customer-target authorization, delivery authorization, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Static public samples remain public-safe orientation artifacts.

They are not live evidence, customer evidence, scanner output, credential evidence, delivery material, or diagnostic completeness proof.

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

| Negative fixture category | Drafting planning status |
| --- | --- |
| `missing-package-artifact` | retained |
| `missing-scenario-artifact` | retained |
| `missing-scenario-directory` | retained |
| `malformed-json` | retained |
| `broken-linkage` | retained |
| `scenario-posture-contradiction` | retained |
| `non-example-name` | retained |
| `missing-non-proof-statement` | retained |
| `missing-five-questions-mapping` | retained |
| `hygiene-not-passed` | retained |
| `forbidden-text-leakage` | retained |
| `overclaim-language` | retained |
| `boundary-flag-violation` | retained |

## Retained metadata and boundary posture

This drafting planning checkpoint does not add or remove metadata fields.

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

## What remains intentionally unresolved

This drafting planning checkpoint does not decide:

* the exact AAEF main handback text,
* whether any AAEF main handback material should be drafted,
* whether any AAEF main issue, pull request, release note, or document should be opened or drafted,
* whether any lesson should be promoted to AAEF main,
* whether to create a handback package,
* whether to create a handback draft,
* whether to create a handback drafting candidate,
* whether a handback drafting candidate is close-ready,
* whether to draft release notes,
* whether to draft document changes,
* whether to change the public sample,
* whether to change validator behavior,
* whether to add validator failure category output,
* whether to create a validator output contract,
* whether to refine the sanitized public sample,
* whether to create a new reviewer walkthrough,
* whether to generate a new static/mock package,
* whether to create a new private review record,
* whether to promote a new public sample,
* whether runtime/scanner/Docker/credential/customer/delivery work should ever proceed.

Those decisions require separate checkpoints.

## Maintained compatibility requirements

~~~text
positive_control_must_remain_passing = true
negative_fixtures_must_remain_fail_closed = true
public_safe_static_fixture_set_must_remain = true
metadata_contract_baseline_must_remain = true
documentation_only_mapping_baseline_must_remain = true
documentation_only_hardening_scope_must_remain = true
read_only_harnesses_must_remain = true
validator_output_must_not_become_authority = true
model_output_must_not_become_authority = true
runtime_execution_must_remain_unauthorized = true
scanner_execution_must_remain_unauthorized = true
docker_execution_must_remain_unauthorized = true
credential_injection_must_remain_unauthorized = true
customer_target_operation_must_remain_unauthorized = true
delivery_must_remain_unauthorized = true
~~~

## Applied Implementation boundary

This remains AAEF-AI-VA Applied Implementation work.

~~~text
aaef_handback_category_applied_implementation = true
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
~~~

AAEF main handback, if any, should remain evidence/interface-level only and require a separate checkpoint.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, private review records, or delivery material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.91 Narrow Public-Safe AAEF Main Handback Drafting Candidate
~~~

That checkpoint may create a narrow internal drafting candidate if it preserves this planning boundary.

It should not directly open an AAEF main issue or PR, write final AAEF main handback text, modify validator behavior, modify validator output, modify fixture metadata fields, add JSON Schema, change Applied Evidence package content, change public sample content, or authorize runtime/scanner/Docker/credential/customer/delivery activity.

## Out of scope

This checkpoint does not prepare AAEF main handback material, start AAEF main handback work, open an AAEF main issue, open an AAEF main pull request, draft AAEF main release notes, draft AAEF main document changes, write AAEF main handback text, submit anything to AAEF main, create a handback package, create a handback draft, create a handback drafting candidate, approve AAEF Core/Profile/Practical Package promotion, decide lesson promotion to AAEF main, modify validator behavior, add validator failure category output, create a validator output contract, add metadata-level failure category fields, add JSON Schema, rewrite fixture metadata, add negative fixtures, reorganize files, edit local check execution semantics, start Applied Evidence implementation work, generate new Applied Evidence packages, generate private review records, promote new public samples, refine sanitized public sample content, change public example text, create a new reviewer walkthrough, start validator relationship implementation work, start validator behavior hardening implementation, approve validator behavior hardening implementation readiness, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
