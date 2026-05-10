# v0.6.138 External Discovery Fail-Closed Behavior Review and Decision

Status: decision
Date: 2026-05-10

## Purpose

This checkpoint reviews the external_discovery=true fail-closed behavior candidate implemented in v0.6.137.

This is checkpoint 3 of 3 for a High-risk gate-semantics work item.

This checkpoint reviews and accepts the external_discovery=true fail-closed behavior candidate from v0.6.137.

The external_discovery=true fail-closed behavior work item is closed.

## Review conclusion

Candidate accepted.

Deterministic comparison confirmed.

Fail-closed behavior confirmed.

Evidence-safe result model confirmed.

No runtime gate integration effect.

No runtime execution authorization effect.

No scanner execution authorization effect.

No Docker execution authorization effect.

No credential injection authorization effect.

No customer target authorization effect.

No delivery authorization effect.

The v0.6.137 candidate is accepted as a deterministic, evidence-safe external discovery fail-closed helper and test set.

## Decision record

~~~text
external_discovery_fail_closed_behavior_review_decision_completed = true
external_discovery_fail_closed_behavior_review_decision_is_high_risk = true
external_discovery_fail_closed_behavior_review_decision_checkpoint_3_of_3 = true
external_discovery_fail_closed_behavior_candidate_reviewed = true
external_discovery_fail_closed_behavior_candidate_accepted = true
external_discovery_fail_closed_behavior_work_item_closed = true
external_discovery_fail_closed_helper_reviewed = true
external_discovery_fail_closed_helper_tests_reviewed = true
external_discovery_deterministic_comparison_confirmed = true
external_discovery_fail_closed_without_decision_allowance_confirmed = true
external_discovery_fail_closed_decision_allowance_false_confirmed = true
external_discovery_fail_closed_localhost_only_boundary_confirmed = true
external_discovery_fail_closed_local_lab_only_boundary_confirmed = true
external_discovery_fail_closed_missing_destination_binding_confirmed = true
external_discovery_fail_closed_malformed_destination_binding_confirmed = true
external_discovery_fail_closed_missing_scope_support_confirmed = true
external_discovery_fail_closed_ambiguous_target_boundary_confirmed = true
external_discovery_fail_closed_expired_or_invalid_authorization_confirmed = true
external_discovery_fail_closed_malformed_external_discovery_flag_confirmed = true
external_discovery_false_continue_existing_checks_confirmed = true
external_discovery_missing_not_required_continue_existing_checks_confirmed = true
external_discovery_explicitly_allowed_boundary_compatible_continue_existing_checks_confirmed = true
external_discovery_evidence_safe_result_confirmed = true
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
review_decision_completed = true
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
selected_next_direction = next_work_selection_using_risk_tiered_granularity
selected_next_checkpoint = v0.6.139 Next Work Selection Using Risk-Tiered Granularity
~~~

## Reviewed candidate behavior

| Case | Reviewed result |
| --- | --- |
| external_discovery=false | continue existing checks |
| external_discovery missing and not required | continue existing checks |
| external_discovery=true explicitly allowed and boundary-compatible | continue existing checks |
| external_discovery=true without explicit decision allowance | blocked / fail closed |
| external_discovery=true with decision allowance=false | blocked / fail closed |
| external_discovery=true against localhost_only target boundary | blocked / fail closed |
| external_discovery=true against local-lab-only target boundary | blocked / fail closed |
| external_discovery=true without required destination binding | blocked / fail closed |
| external_discovery=true with malformed destination binding | blocked / fail closed |
| external_discovery=true without scope support | blocked / fail closed |
| external_discovery=true with ambiguous target boundary | blocked / fail closed |
| external_discovery=true with expired or invalid authorization result | blocked / fail closed |
| malformed external_discovery flag | blocked / fail closed |
| evidence-safe result | decision facts, categories, and field names only; no raw secrets, raw credentials, tokens, private customer material, scanner output, private artifacts, full raw payloads, or live third-party target details |

## Reviewed helper and tests

Reviewed helper:

~~~text
tools/external_discovery_fail_closed.py
~~~

Reviewed helper tests:

~~~text
tools/test_external_discovery_fail_closed_behavior.py
tools/test_v06137_external_discovery_fail_closed_behavior_candidate.py
tools/test_v06138_external_discovery_fail_closed_behavior_review_and_decision.py
~~~

The helper keeps comparison deterministic.

The helper returns an evidence-safe `ExternalDiscoveryDecision`.

The helper does not integrate into a live runtime gate in this checkpoint.

The helper does not authorize runtime execution, scanner execution, Docker execution, credential injection, customer targets, or delivery.

## Review checklist

| Check | Result |
| --- | --- |
| Deterministic external discovery comparison | pass |
| external_discovery=false continues existing checks | pass |
| missing/not-required external_discovery continues existing checks | pass |
| explicitly allowed and boundary-compatible external discovery continues existing checks | pass |
| missing decision allowance fails closed | pass |
| decision allowance=false fails closed | pass |
| localhost_only target boundary fails closed | pass |
| local-lab-only target boundary fails closed | pass |
| missing destination binding fails closed | pass |
| malformed destination binding fails closed | pass |
| missing scope support fails closed | pass |
| ambiguous target boundary fails closed | pass |
| expired or invalid authorization result fails closed | pass |
| malformed external_discovery flag fails closed | pass |
| Evidence-safe result fields avoid secrets and private artifacts | pass |
| No runtime gate integration introduced | pass |
| No runtime execution authorization introduced | pass |
| No scanner execution authorization introduced | pass |
| No Docker execution authorization introduced | pass |
| No credential injection authorization introduced | pass |
| No customer target authorization introduced | pass |
| No delivery authorization introduced | pass |
| No AAEF main handback sequence reopened | pass |
| No AAEF Core/Profile/Practical Package promotion | pass |

## Work item closeout

The High-risk external_discovery=true fail-closed behavior work item is closed.

The completed three-checkpoint split is:

~~~text
v0.6.136 External Discovery Fail-Closed Behavior Readiness
v0.6.137 External Discovery Fail-Closed Behavior Candidate
v0.6.138 External Discovery Fail-Closed Behavior Review and Decision
~~~

## Relationship to v0.6.137

v0.6.137 implemented the candidate helper and tests.

This checkpoint reviews and accepts that candidate.

## Relationship to v0.6.136

v0.6.136 prepared readiness, current semantics to inspect, target-boundary inputs, expected behavior, fail-closed boundary, expected tests, evidence boundary, and non-goals.

This checkpoint confirms the candidate stayed within that readiness boundary.

## Relationship to v0.6.135

v0.6.135 selected external_discovery=true fail-closed behavior as a High-risk work item and assigned three checkpoints.

This checkpoint completes that planned High-risk sequence.

## Relationship to v0.6.134

v0.6.134 closed the request/decision constraint-diff enforcement work item.

This checkpoint preserves that completed gate-semantics hardening sequence and does not modify request/decision constraint-diff behavior.

## Relationship to v0.6.130

v0.6.130 closed the authorization expiry current-time check work item.

This checkpoint preserves that completed gate-semantics hardening sequence and does not modify authorization expiry behavior.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## What did not happen

No runtime gate integration is added.

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

## Next direction

The next checkpoint should select the next work item using the v0.6.120 risk-tiered checkpoint granularity policy.

Likely next checkpoint:

~~~text
v0.6.139 Next Work Selection Using Risk-Tiered Granularity
~~~

That checkpoint should be a Low-risk one-checkpoint direction-selection record unless a specific risk requires a larger split.
