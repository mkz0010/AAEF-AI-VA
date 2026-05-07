# v0.6.78 Public Sample Relationship-to-Validator Planning

Status: planning
Date: 2026-05-07

## Purpose

This checkpoint plans public sample relationship-to-validator clarity after v0.6.76 selected it as the next Applied Evidence gap.

It defines how a future documentation-only candidate may explain the relationship between the retained public sample and the retained public validator without changing either one.

It is a planning checkpoint only.

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
It does not prepare AAEF main handback material.  
It does not start public sample relationship-to-validator implementation work.  
It does not start validator relationship implementation work.  
It does not start validator behavior hardening implementation.  
It does not approve validator behavior hardening implementation readiness.  
It does not create runnable lab configuration.  
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Version continuity note

Tag `v0.6.77` was used for the repository hygiene cleanup that removed an accidental root-level `FETCH_HEAD` artifact.

This checkpoint therefore uses `v0.6.78` for the next substantive Applied Evidence planning work.

## Baseline reviewed

Previous Applied Evidence next gap selection after clarity closeout:

~~~text
docs/153-v0676-applied-evidence-next-gap-selection-after-clarity-closeout.md
~~~

Previous public sample five-questions clarity review and close-readiness:

~~~text
docs/152-v0675-public-sample-five-questions-clarity-review-close-readiness.md
~~~

Previous public sample five-questions clarity candidate:

~~~text
docs/151-v0674-public-sample-five-questions-clarity-candidate.md
~~~

Retained public validator:

~~~text
tools/validate_public_example_structure.py
~~~

Retained sanitized public sample baseline:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

Retained public negative fixture root:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/
~~~

## Planning conclusion

Public sample relationship-to-validator clarity should be planned as a documentation-only reader aid before any public sample or validator changes are considered.

The future candidate should explain what the public sample is for, what the validator checks, what the validator does not check, how negative fixtures relate to validator posture, and why validator output is not authority.

The future candidate should not change the public sample, change validator behavior, add validator output, create a validator output contract, rewrite fixture metadata, generate packages, prepare AAEF handback material, or authorize runtime activity.

## Planning decision

~~~text
public_sample_relationship_to_validator_planning_completed = true
public_sample_relationship_to_validator_planning_is_documentation_only = true
public_sample_relationship_to_validator_planning_uses_v0676_selection = true
public_sample_relationship_to_validator_selected_gap_retained = true
public_sample_relationship_to_validator_may_be_considered = true
public_sample_relationship_to_validator_candidate_may_be_considered = true
public_sample_relationship_to_validator_planning_only = true
public_sample_relationship_to_validator_started = false
public_sample_relationship_to_validator_implemented = false
public_sample_relationship_to_validator_reviewer_aid_generated = false
public_sample_relationship_to_validator_validator_changed = false
public_sample_relationship_to_validator_output_changed = false
public_sample_relationship_to_validator_contract_created = false
public_sample_relationship_to_validator_public_sample_changed = false
public_sample_relationship_to_validator_sample_refined = false
public_sample_relationship_to_validator_fixture_changed = false
public_sample_relationship_to_validator_negative_fixture_changed = false
public_sample_relationship_to_validator_json_schema_added = false
public_sample_relationship_to_validator_new_walkthrough_created = false
evidence_interface_handback_readiness_started = false
public_sample_five_questions_clarity_close_ready_retained = true
public_sample_five_questions_clarity_reader_aid_retained = true
public_sample_five_questions_clarity_candidate_revision_required = false
public_sample_five_questions_clarity_implemented = false
public_sample_five_questions_clarity_sample_refined = false
public_sample_five_questions_clarity_public_sample_changed = false
public_sample_five_questions_clarity_new_walkthrough_created = false
applied_evidence_reviewer_current_state_summary_retained = true
applied_evidence_reviewer_current_state_summary_close_ready_retained = true
applied_evidence_reviewer_current_state_summary_revision_required = false
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
v0676_next_gap_selection_retained = true
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
validator_does_not_authorize_execution = true
validator_output_is_not_authority = true
validator_success_is_not_runtime_authorization = true
validator_success_is_not_scanner_authorization = true
validator_success_is_not_credential_authorization = true
validator_success_is_not_customer_target_authorization = true
validator_success_is_not_delivery_authorization = true
validator_success_is_not_diagnostic_completeness_proof = true
validator_success_is_not_certification = true
validator_success_is_not_compliance_claim = true
validator_success_is_not_legal_advice = true
validator_success_is_not_audit_opinion = true
validator_success_is_not_external_framework_equivalence = true
documentation_only_failure_category_mapping_is_not_validator_output = true
documentation_only_failure_category_mapping_is_not_validator_output_contract = true
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
~~~

## Planned relationship approach

The future relationship-to-validator candidate should be a reviewer aid that maps the retained public sample to the retained public validator.

It should use the current public sample baseline as-is:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

It should use the current public validator as-is:

~~~text
tools/validate_public_example_structure.py
~~~

The candidate may explain:

* what the public sample is for,
* what the public validator checks,
* what the public validator does not check,
* how public negative fixtures relate to fail-closed validator posture,
* why validator output is not authority,
* why validator success does not authorize execution,
* why documentation-only failure category mapping is not validator output,
* why documentation-only failure category mapping is not a validator output contract,
* why validator checks do not prove diagnostic completeness,
* why validator checks do not create certification, compliance, legal, audit, or equivalence claims.

The candidate should not change the public sample or the validator.

## Planned relationship matrix

| Relationship question | Planned clarity target | Boundary |
| --- | --- | --- |
| What is the public sample for? | Explain that it is a sanitized, static, public-safe evidence-interface example. | Do not treat it as live evidence, customer evidence, or delivery material. |
| What does the public validator check? | Explain that it checks expected public example structure and public-safe posture. | Do not claim it validates vulnerability findings, runtime state, or diagnostic completeness. |
| What does the public validator not check? | Explain that it does not perform vulnerability detection, scanner execution, runtime authorization, credential authorization, delivery authorization, certification, compliance, legal advice, audit opinion, or equivalence review. | Do not infer assurance claims from validator success. |
| How do negative fixtures relate? | Explain that they are synthetic public-safe fail-closed examples for validator posture. | Do not treat negative fixtures as live evidence or runtime tests. |
| Is validator output authority? | State that validator output is not authority. | Do not treat validator success as execution permission. |
| Does validator success authorize execution? | State that execution authorization requires separate gates and evidence. | Do not authorize runtime, scanner, Docker, credential, customer-target, or delivery activity. |
| Does documentation-only mapping change validator output? | State that failure category mapping remains documentation-only. | Do not treat mapping as validator output or an output contract. |

This matrix is planning-only. It does not change the public sample, validator, fixtures, or metadata.

## Planned validator non-goals

A future relationship candidate should explicitly preserve these validator non-goals.

~~~text
validator_does_not_authorize_execution = true
validator_output_is_not_authority = true
validator_success_is_not_runtime_authorization = true
validator_success_is_not_scanner_authorization = true
validator_success_is_not_credential_authorization = true
validator_success_is_not_customer_target_authorization = true
validator_success_is_not_delivery_authorization = true
validator_success_is_not_diagnostic_completeness_proof = true
validator_success_is_not_certification = true
validator_success_is_not_compliance_claim = true
validator_success_is_not_legal_advice = true
validator_success_is_not_audit_opinion = true
validator_success_is_not_external_framework_equivalence = true
documentation_only_failure_category_mapping_is_not_validator_output = true
documentation_only_failure_category_mapping_is_not_validator_output_contract = true
~~~

## Planned public negative fixture relationship

The future relationship candidate may describe the public negative fixture set as follows.

| Fixture relationship point | Planned statement |
| --- | --- |
| Fixture set scope | The fixture set is synthetic, static, and public-safe. |
| Fixture set purpose | The fixture set exercises fail-closed public validator posture. |
| Fixture set limit | The fixture set is not runtime evidence and not live scanner output. |
| Category mapping | Negative fixture categories can aid reviewer understanding. |
| Mapping boundary | Documentation-only category mapping is not validator output and not a validator output contract. |
| Authority boundary | Negative fixture outcomes do not authorize execution. |

## Planned reader path

A future relationship candidate should guide reviewers through this sequence.

| Step | Reviewer action | Purpose |
| --- | --- | --- |
| 1 | Read the public sample purpose. | Understand what the sample is intended to show. |
| 2 | Read the public validator purpose. | Understand what the validator checks. |
| 3 | Read validator non-goals. | Avoid inferring runtime or assurance claims. |
| 4 | Review public negative fixture posture. | Understand fail-closed structural posture. |
| 5 | Confirm documentation-only mapping boundary. | Avoid treating mapping as validator output. |
| 6 | Confirm validator-output-is-not-authority boundary. | Avoid treating validation success as execution permission. |
| 7 | Confirm non-execution and non-delivery boundaries. | Avoid runtime/scanner/Docker/credential/customer/delivery assumptions. |

## Planned candidate acceptance checks

A later relationship candidate should satisfy these checks.

| Check | Expected result |
| --- | --- |
| Candidate preserves the current public sample content | required |
| Candidate preserves current validator behavior | required |
| Candidate explains what the public sample is for | required |
| Candidate explains what the public validator checks | required |
| Candidate explains what the public validator does not check | required |
| Candidate explains how negative fixtures relate to validator posture | required |
| Candidate states validator output is not authority | required |
| Candidate states validator success does not authorize execution | required |
| Candidate states documentation-only failure category mapping is not validator output | required |
| Candidate states documentation-only failure category mapping is not a validator output contract | required |
| Candidate preserves runtime/scanner/Docker/credential/customer/delivery prohibitions | required |
| Candidate avoids certification, compliance, legal, audit, and equivalence claims | required |
| Candidate does not prepare AAEF main handback material | required |
| Candidate remains documentation-only | required |

## Retained clarity closeout state

~~~text
public_sample_five_questions_clarity_review_completed = true
public_sample_five_questions_clarity_close_ready = true
retain_v0674_public_sample_five_questions_clarity_candidate = true
public_sample_five_questions_clarity_candidate_retained = true
public_sample_five_questions_clarity_reader_aid_retained = true
public_sample_five_questions_clarity_current_sample_content_retained = true
~~~

## Retained public validator relationship

The public validator remains a structural validator for public examples.

It does not provide vulnerability detection, diagnostic completeness, live execution evidence, runtime authorization, scanner authorization, credential authorization, customer-target authorization, delivery authorization, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

The documentation-only failure category mapping remains documentation-only.  
It is not validator output and not a validator output contract.

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

| Negative fixture category | Planning status |
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

This planning checkpoint does not add or remove metadata fields.

Retained metadata fields:

~~~text
negative_category
expected_validator_result
expected_blockers
synthetic_public_safe_static_fixture
source_positive_control
non_authorization_statement
runtime_boundary
~~~

Retained runtime boundary flags remain false for each current negative fixture:

~~~text
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

This planning checkpoint does not decide:

* the exact public sample relationship-to-validator wording,
* whether to change the public sample,
* whether to change validator behavior,
* whether to add validator failure category output,
* whether to create a validator output contract,
* whether to refine the sanitized public sample,
* whether to create a new reviewer walkthrough,
* whether to prepare an AAEF main handback,
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

AAEF main handback, if any, should remain evidence/interface-level only:

> Public-safe Applied Implementations can plan public sample relationship-to-validator clarity without changing public samples, validators, fixture metadata, handback material, or execution boundaries.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, or delivery material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.79 Public Sample Relationship-to-Validator Candidate
~~~

That checkpoint may create a narrow documentation-only relationship-to-validator candidate if it preserves the planning boundaries above.

## Out of scope

This checkpoint does not modify validator behavior, add validator failure category output, create a validator output contract, add metadata-level failure category fields, add JSON Schema, rewrite fixture metadata, add negative fixtures, reorganize files, edit local check execution semantics, start Applied Evidence implementation work, generate new Applied Evidence packages, generate private review records, promote new public samples, refine sanitized public sample content, change public example text, create a new reviewer walkthrough, prepare an AAEF main handback, start public sample relationship-to-validator implementation work, start validator relationship implementation work, start validator behavior hardening implementation, approve validator behavior hardening implementation readiness, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
