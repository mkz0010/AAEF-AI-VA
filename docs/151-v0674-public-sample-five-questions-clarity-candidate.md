# v0.6.74 Public Sample Five-Questions Clarity Candidate

Status: candidate
Date: 2026-05-07

## Purpose

This checkpoint creates a narrow documentation-only public sample five-questions clarity candidate after v0.6.73 planned the clarity work.

It explains how a reviewer should read the existing public sample against the AAEF five questions without changing the public sample content.

It is a clarity candidate checkpoint only.

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

Previous public sample five-questions clarity planning:

~~~text
docs/150-v0673-public-sample-five-questions-clarity-planning.md
~~~

Previous Applied Evidence next gap selection review:

~~~text
docs/149-v0672-applied-evidence-next-gap-selection-review.md
~~~

Previous reviewer current-state summary review and close-readiness:

~~~text
docs/148-v0671-applied-evidence-reviewer-current-state-summary-review-close-readiness.md
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

The public sample five-questions clarity candidate is created in this document.

The candidate is intentionally narrow and documentation-only.

It helps reviewers read the current public sample by clarifying:

* where to begin reading,
* how to separate model request from authority,
* how to locate gate or authorization decision meaning,
* how to understand static sample posture versus runtime execution,
* how to read evidence-interface records without overclaiming proof,
* where the public validator helps,
* where the public validator stops,
* what must remain non-execution and non-delivery,
* what remains deferred.

The current public sample content is retained unchanged.

## Candidate decision

~~~text
public_sample_five_questions_clarity_candidate_added = true
public_sample_five_questions_clarity_candidate_is_documentation_only = true
public_sample_five_questions_clarity_candidate_uses_v0673_planning = true
public_sample_five_questions_clarity_candidate_uses_v0672_selection = true
public_sample_five_questions_clarity_selected_gap_retained = true
public_sample_five_questions_clarity_reviewer_aid_generated = true
public_sample_five_questions_clarity_candidate_close_readiness_may_be_considered = true
public_sample_five_questions_clarity_started = true
public_sample_five_questions_clarity_implemented = false
public_sample_five_questions_clarity_sample_refined = false
public_sample_five_questions_clarity_public_sample_changed = false
public_sample_five_questions_clarity_new_walkthrough_created = false
public_sample_five_questions_clarity_current_sample_content_retained = true
public_sample_relationship_to_validator_started = false
evidence_interface_handback_readiness_started = false
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
reviewer_navigation_note_retained = true
public_negative_fixture_index_summary_retained = true
v0673_clarity_planning_retained = true
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

This clarity candidate is a reader aid for the current public sample.

It does not create new evidence.  
It does not rewrite evidence.  
It does not rewrite examples.  
It does not change the public sample.  
It does not change validator behavior.  
It does not authorize runtime execution.

The retained public sample baseline remains:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

The clarity candidate should be read as an orientation layer over the existing public sample, not as a new public sample and not as a new reviewer walkthrough.

## 2. Recommended reviewer reading path

A reviewer should read the current public sample in this order.

| Step | Reviewer action | Purpose |
| --- | --- | --- |
| 1 | Read scope and non-goals before sample details. | Avoid treating the public sample as certification, compliance, legal advice, audit opinion, live evidence, or delivery authorization. |
| 2 | Identify the model request or proposed action. | Separate model output from authority. |
| 3 | Identify the gate or authorization decision artifact. | Locate the authority-relevant decision point. |
| 4 | Identify dispatch, non-dispatch, or result posture. | Understand whether execution is represented and whether it remains static. |
| 5 | Identify the evidence record. | Understand what links request, gate decision, dispatch or non-dispatch, and review posture. |
| 6 | Compare the sample against the AAEF five questions. | Confirm the reading path for actor, principal, authority, execution allowance, and evidence. |
| 7 | Check the public validator relationship. | Understand what structure is checked and what is not checked. |
| 8 | Confirm non-execution and non-delivery boundaries. | Avoid inferring runtime, scanner, Docker, credential, customer-target, or delivery authorization. |

## 3. Five-questions clarity matrix

| AAEF question | How to read the current public sample | Boundary |
| --- | --- | --- |
| Who or what acted? | Look for the request/proposal artifact, gate decision artifact, dispatch or non-dispatch posture, result/evidence record, and reviewer-facing context. | Do not invent actors, tools, executions, or results that are not represented in the current public sample. |
| On whose behalf? | Look for any public-safe principal, delegated context, or authorization context already represented in the sample. | Do not claim principal binding beyond the current public-safe artifacts. |
| With what authority? | Read authority from the gate or authorization decision artifact, not from the model request. | Model output is not authority. |
| Was the action allowed at execution? | Read execution allowance as a gate/evidence question and verify whether the sample is static, non-executing, or represents a dispatch posture. | Do not claim runtime execution, live authorization, scanner authorization, or customer-target authorization. |
| What evidence proves what happened? | Read the evidence record as the link between request, decision, dispatch/non-dispatch or result posture, and review. | Do not claim live proof, audit sufficiency, legal sufficiency, compliance, certification, or diagnostic completeness. |

This matrix explains how to read current public artifacts.  
It does not modify the sample and does not create new evidence.

## 4. Model request versus authority

The public sample should be read with the following rule:

~~~text
model_output_is_not_authority = true
gate_decision_is_authority_relevant = true
execution_authorization_must_be_evidenced = true
~~~

A model request or proposed tool action can show what the AI suggested.

It does not, by itself, authorize execution.

A reviewer should look for the gate or authorization decision artifact to understand whether an action was allowed, denied, blocked, or kept for review.

## 5. Static sample versus runtime execution

The public sample is static and public-safe.

It should not be read as live runtime evidence.

~~~text
static_public_sample_is_not_live_evidence = true
public_sample_is_not_runtime_authorization = true
public_sample_is_not_scanner_authorization = true
public_sample_is_not_credential_authorization = true
public_sample_is_not_customer_target_authorization = true
public_sample_is_not_delivery_authorization = true
public_sample_is_not_diagnostic_completeness_proof = true
public_sample_is_not_audit_opinion = true
public_sample_is_not_legal_advice = true
public_sample_is_not_compliance_claim = true
public_sample_is_not_certification = true
public_sample_is_not_external_framework_equivalence = true
~~~

A reviewer should not infer that the sample authorizes any target, scanner, Docker runtime, credential use, report delivery, or customer operation.

## 6. Validator relationship

The public validator remains:

~~~text
tools/validate_public_example_structure.py
~~~

The public validator may help confirm that public examples retain expected structure and public-safe posture.

The validator helps with structure.  
It does not prove the sample is complete.  
It does not authorize execution.  
It does not create compliance, legal, audit, or certification claims.

The public validator does not provide:

* vulnerability detection,
* diagnostic completeness,
* live execution evidence,
* runtime authorization,
* scanner authorization,
* credential authorization,
* customer-target authorization,
* delivery authorization,
* certification,
* legal advice,
* audit opinion,
* compliance claim,
* external-framework equivalence.

The documentation-only failure category mapping remains documentation-only.  
It is not validator output and not a validator output contract.

## 7. What the public sample can and cannot show

| Public sample can show | Public sample cannot show |
| --- | --- |
| How a public-safe evidence-interface example can be structured. | That a real vulnerability exists. |
| How a model request can be separated from authority. | That scanner execution occurred. |
| How a gate decision can be represented as authority-relevant evidence. | That runtime execution was authorized. |
| How dispatch or non-dispatch posture can be linked to evidence. | That credential use was authorized. |
| How a reviewer can trace the AAEF five questions. | That customer-target testing was authorized. |
| How non-execution boundaries are preserved in public artifacts. | That delivery was authorized. |
| How the public validator relates to structure. | That diagnostic coverage is complete. |
| How static examples can support review orientation. | That the project provides certification, legal advice, audit opinion, compliance, or external-framework equivalence. |

## 8. Deferred gaps

This candidate addresses public sample five-questions clarity as a documentation-only reader aid.

The following remain deferred.

| Deferred gap | Status after v0.6.74 |
| --- | --- |
| Public sample five-questions clarity close-readiness | may be considered next |
| Public sample relationship to validator | not started |
| Evidence-interface handback readiness | not started |
| Static mock package refinement | not started |
| New public sample promotion | not started |
| New package generation | not started |
| Validator behavior implementation readiness | not started |
| Runtime/scanner/Docker/credential/customer/delivery work | not started |

## Candidate acceptance checks

This candidate satisfies the v0.6.73 planning checks as follows.

| Check | Candidate result |
| --- | --- |
| Candidate preserves the current public sample content | satisfied |
| Candidate maps each AAEF five question to current sample reading guidance | satisfied |
| Candidate distinguishes model request from authority | satisfied |
| Candidate distinguishes static evidence-interface demonstration from live proof | satisfied |
| Candidate explains where validator checks help and where they stop | satisfied |
| Candidate preserves runtime/scanner/Docker/credential/customer/delivery prohibitions | satisfied |
| Candidate avoids certification, compliance, legal, audit, and equivalence claims | satisfied |
| Candidate does not prepare AAEF main handback material | satisfied |
| Candidate remains documentation-only | satisfied |

## Retained summary closeout state

The v0.6.71 summary closeout remains retained.

~~~text
applied_evidence_reviewer_current_state_summary_review_completed = true
applied_evidence_reviewer_current_state_summary_close_ready = true
retain_v0670_applied_evidence_reviewer_current_state_summary_candidate = true
applied_evidence_reviewer_current_state_summary_retained = true
applied_evidence_reviewer_current_state_summary_candidate_scope_preserved = true
~~~

The reviewer current-state summary remains the current reviewer orientation summary for the Applied Evidence track.

## Retained current Applied Evidence state

The retained current state remains unchanged.

| Area | Current state | Candidate result |
| --- | --- | --- |
| sanitized public sample baseline | `examples/applied-evidence/sanitized-static-mock/` | retained |
| static/mock Applied Evidence history | v0.6.28-v0.6.32 | retained as history |
| sanitized public sample history | v0.6.33-v0.6.37 | retained as public-safe sample path |
| reviewer walkthrough | v0.6.26 reviewer walkthrough and five questions mapping | retained as history |
| five questions mapping | reviewer-facing mapping history exists | retained |
| reviewer current-state summary | v0.6.70 candidate closed by v0.6.71 | retained |
| public structural validator | `tools/validate_public_example_structure.py` | retained |
| public negative fixture baseline | v0.6.46 static public-safe negative fixture set | retained |
| failure category mapping | v0.6.52-v0.6.54 documentation-only mapping | retained |
| behavior hardening scope | v0.6.56-v0.6.58 documentation-only scope | retained |
| public validator maintenance closeout | v0.6.65 closeout | retained |

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

* whether this clarity candidate is close-ready,
* whether to refine the sanitized public sample,
* whether to change public example text,
* whether to create a new reviewer walkthrough,
* whether to generate a new static/mock package,
* whether to create a new private review record,
* whether to promote a new public sample,
* whether to prepare an AAEF main handback,
* whether validator behavior should eventually be hardened,
* whether runtime/scanner/Docker/credential/customer/delivery work should ever proceed.

Those decisions require separate checkpoints.

## Maintained compatibility requirements

The following compatibility requirements remain active after clarity candidate creation.

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

> Public-safe Applied Implementations can add a documentation-only public sample five-questions clarity aid without changing public samples, validators, handback material, or execution boundaries.

Do not hand back implementation details, patent-sensitive detail, commercial strategy, customer material, scanner output, credentials, private generated artifacts, or delivery material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.75 Public Sample Five-Questions Clarity Review and Close-Readiness
~~~

That checkpoint should review this clarity candidate and decide whether it is close-ready.

It should not modify validator behavior, validator output, fixture metadata fields, JSON Schema, Applied Evidence package content, public sample content, AAEF main handback material, or runtime/scanner/Docker/credential/customer/delivery boundaries.

## Out of scope

This checkpoint does not modify validator behavior, add validator failure category output, create a validator output contract, add metadata-level failure category fields, add JSON Schema, rewrite fixture metadata, add negative fixtures, reorganize files, edit local check execution semantics, start Applied Evidence implementation work, generate new Applied Evidence packages, generate private review records, promote new public samples, refine sanitized public sample content, change public example text, create a new reviewer walkthrough, prepare an AAEF main handback, start validator relationship implementation work, start validator behavior hardening implementation, approve validator behavior hardening implementation readiness, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
