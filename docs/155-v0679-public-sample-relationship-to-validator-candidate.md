# v0.6.79 Public Sample Relationship-to-Validator Candidate

Status: candidate
Date: 2026-05-07

## Purpose

This checkpoint creates a narrow documentation-only public sample relationship-to-validator candidate after v0.6.78 planned the relationship work.

It explains how reviewers should understand the relationship between the retained public sample, the retained public validator, and the retained public negative fixtures without changing any of them.

It is a relationship candidate checkpoint only.

It does not modify validator behavior.  
It does not add validator failure category output.  
It does not create a validator output contract.  
It does not add or change fixture metadata fields.  
It does not add a metadata-level `expected_failure_category` field.  
It does not add a JSON Schema file.  
It does not rewrite negative fixture metadata.  
It does not add new negative fixtures.  
It does not reorganize files.  
It does not edit `run_all_local_checks.py` beyond registering this read-only candidate test.  
It does not start Applied Evidence implementation work.  
It does not generate new Applied Evidence packages.  
It does not generate private review records.  
It does not promote new public samples.  
It does not refine sanitized public sample content.  
It does not change public example text.  
It does not create a new reviewer walkthrough.  
It does not prepare AAEF main handback material.  
It does not start validator relationship implementation work.  
It does not start validator behavior hardening implementation.  
It does not approve validator behavior hardening implementation readiness.  
It does not create runnable lab configuration.  
It does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer-target operation, report delivery, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

Model output is not authority.

## Baseline reviewed

Previous public sample relationship-to-validator planning:

~~~text
docs/154-v0678-public-sample-relationship-to-validator-planning.md
~~~

Previous Applied Evidence next gap selection after clarity closeout:

~~~text
docs/153-v0676-applied-evidence-next-gap-selection-after-clarity-closeout.md
~~~

Previous public sample five-questions clarity review and close-readiness:

~~~text
docs/152-v0675-public-sample-five-questions-clarity-review-close-readiness.md
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

## Candidate conclusion

The public sample relationship-to-validator candidate is created in this document.

The candidate is intentionally narrow and documentation-only.

It helps reviewers understand:

* what the public sample is for,
* what the public validator checks,
* what the public validator does not check,
* how public negative fixtures relate to fail-closed validator posture,
* why validator output is not authority,
* why validator success does not authorize execution,
* why documentation-only failure category mapping is not validator output,
* why documentation-only failure category mapping is not a validator output contract,
* why validator checks do not prove diagnostic completeness,
* why validator checks do not create certification, compliance, legal, audit, or external-framework equivalence claims.

The current public sample, public validator, public negative fixtures, fixture metadata, and validator output remain unchanged.

## Candidate decision

~~~text
public_sample_relationship_to_validator_candidate_added = true
public_sample_relationship_to_validator_candidate_is_documentation_only = true
public_sample_relationship_to_validator_candidate_uses_v0678_planning = true
public_sample_relationship_to_validator_candidate_uses_v0676_selection = true
public_sample_relationship_to_validator_selected_gap_retained = true
public_sample_relationship_to_validator_reviewer_aid_generated = true
public_sample_relationship_to_validator_candidate_close_readiness_may_be_considered = true
public_sample_relationship_to_validator_started = true
public_sample_relationship_to_validator_implemented = false
public_sample_relationship_to_validator_validator_changed = false
public_sample_relationship_to_validator_output_changed = false
public_sample_relationship_to_validator_contract_created = false
public_sample_relationship_to_validator_public_sample_changed = false
public_sample_relationship_to_validator_sample_refined = false
public_sample_relationship_to_validator_fixture_changed = false
public_sample_relationship_to_validator_negative_fixture_changed = false
public_sample_relationship_to_validator_json_schema_added = false
public_sample_relationship_to_validator_new_walkthrough_created = false
public_sample_relationship_to_validator_current_sample_content_retained = true
public_sample_relationship_to_validator_current_validator_retained = true
public_sample_relationship_to_validator_current_negative_fixtures_retained = true
public_sample_relationship_to_validator_current_fixture_metadata_retained = true
public_sample_relationship_to_validator_current_validator_output_retained = true
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
v0678_relationship_planning_retained = true
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

## 1. Scope and non-goals

This relationship candidate is a reader aid.

It does not create new evidence.  
It does not rewrite evidence.  
It does not rewrite public examples.  
It does not change the public sample.  
It does not change the validator.  
It does not change validator output.  
It does not create a validator output contract.  
It does not change fixture metadata.  
It does not authorize runtime execution.

The retained public sample baseline remains:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

The retained public validator remains:

~~~text
tools/validate_public_example_structure.py
~~~

The retained public negative fixture root remains:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/
~~~

## 2. Public sample purpose

The public sample is a sanitized, static, public-safe evidence-interface example.

It helps reviewers see how public-safe Applied Evidence artifacts can be structured and reviewed.

It can support orientation around:

* model request versus authority,
* gate or authorization decision posture,
* dispatch or non-dispatch posture,
* evidence linkage,
* reviewer-facing traceability,
* non-execution and non-delivery boundaries.

It is not live evidence, customer evidence, scanner output, credential evidence, delivery material, or diagnostic completeness proof.

## 3. Public validator purpose

The public validator is a structural validator for public examples.

It checks expected public example structure and public-safe posture.

It is intended to help catch public-example hygiene and boundary issues.

It is not an execution system, scanner, runtime gate, credential gate, delivery gate, compliance engine, certification engine, legal review tool, audit tool, or equivalence assessment.

## 4. What the public validator checks and does not check

| Validator can help check | Validator does not check |
| --- | --- |
| Expected public example structure. | Vulnerability detection. |
| Public-safe posture expectations. | Diagnostic completeness. |
| Required or expected public example artifacts. | Live execution evidence. |
| Public-example hygiene boundaries. | Runtime authorization. |
| Boundary or overclaim posture encoded in public examples. | Scanner authorization. |
| Fail-closed behavior against public negative fixtures. | Credential authorization. |
| Static fixture expectations. | Customer-target authorization. |
| Reviewer-facing structural consistency. | Delivery authorization. |
| Documentation-aligned public sample posture. | Certification, legal advice, audit opinion, compliance claim, or external-framework equivalence. |

Validator success means the public example passed the current structural checks.

Validator success does not mean execution is authorized.

Validator success does not mean diagnostic coverage is complete.

Validator success does not mean the public sample is a customer deliverable.

## 5. Public negative fixture relationship

Public negative fixtures are synthetic, static, public-safe fail-closed examples.

They help reviewers understand how the public validator should respond to known public example posture problems.

They do not represent:

* live evidence,
* live scanner output,
* runtime execution,
* customer-target testing,
* credential use,
* production findings,
* delivery authorization.

Negative fixture categories can help organize reviewer understanding, but the mapping remains documentation-only unless and until a separate validator output contract is explicitly approved.

## 6. Validator output is not authority

The relationship boundary is:

~~~text
validator_output_is_not_authority = true
validator_success_is_not_execution_permission = true
validator_failure_is_not_a_runtime_decision = true
model_output_is_not_authority = true
gate_decision_remains_authority_relevant = true
execution_authorization_requires_separate_gate_and_evidence = true
~~~

A validator result can support structural review.

It does not authorize a tool, scanner, runtime, Docker container, credential, target, customer operation, or report delivery.

A reviewer should continue to look for separate gate decisions and evidence records when evaluating authority or execution allowance.

## 7. Documentation-only mapping boundary

The documentation-only failure category mapping remains documentation-only.

~~~text
documentation_only_failure_category_mapping_is_not_validator_output = true
documentation_only_failure_category_mapping_is_not_validator_output_contract = true
documentation_only_failure_category_mapping_does_not_change_validator_behavior = true
documentation_only_failure_category_mapping_does_not_change_fixture_metadata = true
~~~

The mapping helps reviewers understand categories.

It does not change the validator.

It does not change fixture metadata.

It does not add `expected_failure_category`.

It does not create JSON Schema.

It does not create a validator output contract.

## 8. Non-execution and non-delivery boundary

The retained relationship candidate keeps the following prohibitions.

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

The public validator does not provide vulnerability detection, diagnostic completeness, live execution evidence, runtime authorization, scanner authorization, credential authorization, customer-target authorization, delivery authorization, certification, legal advice, audit opinion, compliance claim, or external-framework equivalence.

## 9. Relationship matrix

| Relationship question | Candidate answer | Boundary |
| --- | --- | --- |
| What is the public sample for? | It is a sanitized, static, public-safe evidence-interface example. | It is not live evidence, customer evidence, or delivery material. |
| What does the public validator check? | It checks expected public example structure and public-safe posture. | It does not validate vulnerability findings, runtime state, or diagnostic completeness. |
| What does the public validator not check? | It does not check execution, scanner results, credentials, targets, delivery, certification, legal, audit, compliance, or equivalence. | Validator success must not be read as assurance beyond structural checks. |
| How do negative fixtures relate? | They are synthetic public-safe fail-closed examples for validator posture. | They are not live evidence or runtime tests. |
| Is validator output authority? | No. Validator output is not authority. | Validator success is not execution permission. |
| Does validator success authorize execution? | No. Execution authorization requires separate gates and evidence. | Runtime/scanner/Docker/credential/customer/delivery remain unauthorized. |
| Does documentation-only mapping change validator output? | No. Failure category mapping remains documentation-only. | Mapping is not validator output and not a validator output contract. |

## 10. Candidate acceptance checks

This candidate satisfies the v0.6.78 planning checks as follows.

| Check | Candidate result |
| --- | --- |
| Candidate preserves the current public sample content | satisfied |
| Candidate preserves current validator behavior | satisfied |
| Candidate explains what the public sample is for | satisfied |
| Candidate explains what the public validator checks | satisfied |
| Candidate explains what the public validator does not check | satisfied |
| Candidate explains how negative fixtures relate to validator posture | satisfied |
| Candidate states validator output is not authority | satisfied |
| Candidate states validator success does not authorize execution | satisfied |
| Candidate states documentation-only failure category mapping is not validator output | satisfied |
| Candidate states documentation-only failure category mapping is not a validator output contract | satisfied |
| Candidate preserves runtime/scanner/Docker/credential/customer/delivery prohibitions | satisfied |
| Candidate avoids certification, compliance, legal, audit, and equivalence claims | satisfied |
| Candidate does not prepare AAEF main handback material | satisfied |
| Candidate remains documentation-only | satisfied |

## Retained clarity closeout state

The v0.6.75 clarity closeout remains retained.

~~~text
public_sample_five_questions_clarity_review_completed = true
public_sample_five_questions_clarity_close_ready = true
retain_v0674_public_sample_five_questions_clarity_candidate = true
public_sample_five_questions_clarity_candidate_retained = true
public_sample_five_questions_clarity_reader_aid_retained = true
public_sample_five_questions_clarity_current_sample_content_retained = true
~~~

The public sample five-questions clarity candidate remains the current public sample five-questions reader aid.

## Retained current Applied Evidence state

The retained current state remains unchanged.

| Area | Current state | Candidate result |
| --- | --- | --- |
| sanitized public sample baseline | `examples/applied-evidence/sanitized-static-mock/` | retained |
| public sample five-questions reader aid | v0.6.74 candidate closed by v0.6.75 | retained |
| reviewer current-state summary | v0.6.70 candidate closed by v0.6.71 | retained |
| public structural validator | `tools/validate_public_example_structure.py` | retained |
| public negative fixture baseline | v0.6.46 static public-safe negative fixture set | retained |
| failure category mapping | v0.6.52-v0.6.54 documentation-only mapping | retained |
| behavior hardening scope | v0.6.56-v0.6.58 documentation-only scope | retained |
| public validator maintenance closeout | v0.6.65 closeout | retained |
| static/mock Applied Evidence history | v0.6.28-v0.6.32 | retained as history |
| sanitized public sample history | v0.6.33-v0.6.37 | retained as public-safe sample path |

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

| Negative fixture category | Candidate status |
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

This candidate checkpoint does not add or remove metadata fields.

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

This candidate checkpoint does not decide:

* whether this relationship candidate is close-ready,
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

The following compatibility requirements remain active after relationship candidate creation.

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

> Public-safe Applied Implementations can add a documentation-only public sample relationship-to-validator reader aid without changing public samples, validators, fixture metadata, handback material, or execution boundaries.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, or delivery material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.80 Public Sample Relationship-to-Validator Review and Close-Readiness
~~~

That checkpoint should review this relationship candidate and decide whether it is close-ready.

It should not modify validator behavior, validator output, fixture metadata fields, JSON Schema, Applied Evidence package content, public sample content, AAEF main handback material, or runtime/scanner/Docker/credential/customer/delivery boundaries.

## Out of scope

This checkpoint does not modify validator behavior, add validator failure category output, create a validator output contract, add metadata-level failure category fields, add JSON Schema, rewrite fixture metadata, add negative fixtures, reorganize files, edit local check execution semantics, start Applied Evidence implementation work, generate new Applied Evidence packages, generate private review records, promote new public samples, refine sanitized public sample content, change public example text, create a new reviewer walkthrough, prepare an AAEF main handback, start validator relationship implementation work, start validator behavior hardening implementation, approve validator behavior hardening implementation readiness, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
