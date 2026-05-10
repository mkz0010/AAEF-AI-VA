# v0.6.137 External Discovery Fail-Closed Behavior Candidate

Status: candidate
Date: 2026-05-10

## Purpose

This checkpoint implements the external_discovery=true fail-closed behavior candidate after v0.6.136 readiness.

This is checkpoint 2 of 3 for a High-risk gate-semantics work item.

This checkpoint implements the external_discovery=true fail-closed behavior candidate.

The review and decision are deferred to v0.6.138.

## Candidate implementation summary

This checkpoint adds a deterministic, evidence-safe helper and tests for evaluating `external_discovery=true` against explicit decision allowance and target-boundary compatibility.

The helper fails closed when external discovery is requested without explicit decision allowance, against localhost-only or local-lab-only boundaries, without required destination binding, with malformed destination binding, without scope support, with ambiguous target boundary, with expired or invalid authorization result, or with malformed external discovery flag.

The helper returns a small evidence-safe result object that records categories and field names without copying raw secrets, raw credentials, tokens, private customer material, scanner output, private artifacts, or live third-party target details.

## Candidate helper

~~~text
tools/external_discovery_fail_closed.py
~~~

The helper exposes:

~~~text
evaluate_external_discovery_fail_closed(request, decision, *, target_boundary=..., authorization_result=...)
ExternalDiscoveryDecision.as_evidence()
ExternalDiscoveryBlock.as_evidence()
~~~

## Candidate behavior

| Case | Candidate behavior |
| --- | --- |
| external_discovery=false | continue existing checks |
| external_discovery missing and not required | continue existing checks |
| external_discovery=true without explicit decision allowance | blocked / fail closed |
| external_discovery=true with decision allowance=false | blocked / fail closed |
| external_discovery=true against localhost_only target boundary | blocked / fail closed |
| external_discovery=true against local-lab-only target boundary | blocked / fail closed |
| external_discovery=true without required destination binding | blocked / fail closed |
| external_discovery=true with malformed destination binding | blocked / fail closed |
| external_discovery=true without scope support | blocked / fail closed |
| external_discovery=true with ambiguous target boundary | blocked / fail closed |
| external_discovery=true with expired or invalid authorization result | blocked / fail closed |
| external_discovery=true explicitly allowed and boundary-compatible | continue existing checks |

## Fail-closed behavior

~~~text
external_discovery_requested_without_decision_allowance -> blocked / not authorized
external_discovery_requested_against_localhost_only_boundary -> blocked / not authorized
external_discovery_requested_against_local_lab_only_boundary -> blocked / not authorized
external_discovery_requested_without_runtime_destination_binding -> blocked / not authorized
external_discovery_requested_with_malformed_destination_binding -> blocked / not authorized
external_discovery_requested_without_scope_support -> blocked / not authorized
external_discovery_requested_with_ambiguous_target_boundary -> blocked / not authorized
external_discovery_requested_with_expired_or_invalid_authorization -> blocked / not authorized
malformed_external_discovery_flag -> blocked / not authorized
ambiguous_external_discovery_comparison -> blocked / not authorized
~~~

## Evidence-safe result model

The helper returns an `ExternalDiscoveryDecision` with:

~~~text
allowed_to_continue
status
reason
external_discovery_requested
block_categories
blocks
matched_constraints
checked_fields
~~~

The result intentionally avoids including raw secrets, raw credentials, tokens, private customer material, scanner output, private artifacts, full raw request payloads, full raw authorization decision payloads, or live third-party target details.

## Candidate tests

This checkpoint adds:

~~~text
tools/test_external_discovery_fail_closed_behavior.py
tools/test_v06137_external_discovery_fail_closed_behavior_candidate.py
~~~

The tests cover:

* external_discovery=false,
* external_discovery missing and not required,
* external_discovery=true explicitly allowed and boundary-compatible,
* external_discovery=true without decision allowance,
* external_discovery=true with decision allowance=false,
* localhost_only target boundary,
* local-lab-only target boundary,
* missing required destination binding,
* malformed destination binding,
* missing scope support,
* ambiguous target boundary,
* expired or invalid authorization result,
* malformed external discovery flag,
* evidence-safe output shape,
* v0.6.136 readiness continuity,
* v0.6.138 review/decision deferral.

## Candidate record

~~~text
external_discovery_fail_closed_behavior_candidate_completed = true
external_discovery_fail_closed_behavior_candidate_is_high_risk = true
external_discovery_fail_closed_behavior_candidate_checkpoint_2_of_3 = true
external_discovery_fail_closed_behavior_readiness_completed = true
external_discovery_fail_closed_behavior_review_decision_deferred_to_v06138 = true
external_discovery_fail_closed_helper_added = true
external_discovery_fail_closed_helper_tests_added = true
external_discovery_candidate_deterministic_comparison_supported = true
external_discovery_candidate_fail_closed_without_decision_allowance = true
external_discovery_candidate_fail_closed_decision_allowance_false = true
external_discovery_candidate_fail_closed_localhost_only_boundary = true
external_discovery_candidate_fail_closed_local_lab_only_boundary = true
external_discovery_candidate_fail_closed_missing_destination_binding = true
external_discovery_candidate_fail_closed_malformed_destination_binding = true
external_discovery_candidate_fail_closed_missing_scope_support = true
external_discovery_candidate_fail_closed_ambiguous_target_boundary = true
external_discovery_candidate_fail_closed_expired_or_invalid_authorization = true
external_discovery_candidate_fail_closed_malformed_external_discovery_flag = true
external_discovery_candidate_allows_external_false_to_continue_existing_checks = true
external_discovery_candidate_allows_explicitly_allowed_boundary_compatible_external = true
external_discovery_candidate_evidence_safe_result_model_added = true
external_discovery_fail_closed_added = true
external_discovery_behavior_modified = true
external_discovery_helper_added = true
external_discovery_gate_runtime_behavior_modified = false
target_boundary_behavior_modified = true
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
review_decision_completed = false
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
constraint_diff_enforcement_added = false
authorization_expiry_now_check_added = false
mock_completed_status_renamed = false
enterprise_review_guide_created = false
technical_due_diligence_summary_created = false
safe_poc_boundary_template_created = false
control_matrix_created = false
reviewer_walkthrough_created = false
validator_behavior_modified = false
metadata_level_expected_failure_category_added = false
json_schema_added = false
public_sample_changed = false
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
selected_next_checkpoint = v0.6.138 External Discovery Fail-Closed Behavior Review and Decision
~~~

## What changed

The following files are added:

~~~text
tools/external_discovery_fail_closed.py
tools/test_external_discovery_fail_closed_behavior.py
tools/test_v06137_external_discovery_fail_closed_behavior_candidate.py
docs/213-v06137-external-discovery-fail-closed-behavior-candidate.md
planning/decisions/ADR-0207-add-v06137-external-discovery-fail-closed-behavior-candidate.md
planning/issues/0206-add-v06137-external-discovery-fail-closed-behavior-candidate.md
~~~

The following files are updated for repository navigation and checks:

~~~text
README.md
CHANGELOG.md
ROADMAP.md
tools/run_all_local_checks.py
~~~

## What did not happen

No review/decision closeout is completed.

No external_discovery gate runtime behavior is modified.

No runtime execution is authorized.

No scanner execution is authorized.

No Docker execution is authorized.

No credential injection is permitted.

No customer target is authorized.

No delivery is authorized.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

No validator behavior is modified.

No metadata-level `expected_failure_category` is added.

No JSON Schema is added.

No public sample is changed.

No request/decision constraint-diff enforcement is added or modified.

No authorization expiry current-time check is added or modified.

No mock/dry-run status terminology is renamed.

No Enterprise Review Guide is created.

No technical due diligence summary is created.

No safe PoC boundary template is created.

No control matrix is created.

No reviewer walkthrough is created.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.136

v0.6.136 prepared readiness for this High-risk work item and deferred candidate implementation to v0.6.137.

This checkpoint is the candidate implementation checkpoint.

## Relationship to v0.6.135

v0.6.135 selected external_discovery=true fail-closed behavior as a High-risk work item and assigned three checkpoints:

~~~text
v0.6.136 External Discovery Fail-Closed Behavior Readiness
v0.6.137 External Discovery Fail-Closed Behavior Candidate
v0.6.138 External Discovery Fail-Closed Behavior Review and Decision
~~~

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.138 External Discovery Fail-Closed Behavior Review and Decision
~~~

That checkpoint should review the candidate behavior, confirm fail-closed boundaries, and decide whether to close the High-risk work item.
