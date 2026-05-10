# v0.6.129 Authorization Expiry Current-Time Check Candidate

Status: candidate
Date: 2026-05-10

## Purpose

This checkpoint implements the authorization expiry current-time check candidate after v0.6.128 readiness.

This is checkpoint 2 of 3 for a High-risk gate-semantics work item.

This checkpoint implements the authorization expiry current-time check candidate.

The review and decision are deferred to v0.6.130.

## Candidate implementation summary

This checkpoint adds a deterministic, evidence-safe authorization expiry current-time helper and tests.

The helper evaluates authorization expiry against an explicit current-time value supplied by the caller.

The helper does not read wall-clock time internally.

The helper fails closed for expired, malformed, missing-required, or ambiguous current-time inputs.

The helper returns a small evidence-safe decision object that avoids copying secrets, credentials, scanner output, customer material, or private artifacts.

## Candidate helper

~~~text
tools/authorization_expiry_current_time.py
~~~

The helper exposes:

~~~text
evaluate_authorization_expiry(authorization, *, current_time, expiry_required=False)
AuthorizationExpiryDecision.as_evidence()
~~~

## Candidate behavior

| Case | Candidate behavior |
| --- | --- |
| not expired authorization | continue existing checks |
| expiry equal to current time | continue existing checks |
| expired authorization | blocked / fail closed |
| malformed expiry timestamp | blocked / fail closed |
| missing required expiry timestamp | blocked / fail closed |
| missing optional expiry timestamp | continue existing checks |
| timezone-aware timestamp | deterministic comparison |
| timezone-naive expiry timestamp | blocked / fail closed |
| timezone-naive current time | blocked / fail closed |

## Fail-closed behavior

~~~text
expired_authorization -> blocked / not authorized
malformed_expiry -> blocked / not authorized
missing_required_expiry -> blocked / not authorized
ambiguous_current_time -> blocked / not authorized
timezone_naive_expiry -> blocked / not authorized
timezone_naive_current_time -> blocked / not authorized
~~~

## Deterministic current-time source

The candidate requires callers and tests to pass `current_time` explicitly.

This keeps tests deterministic and avoids hidden wall-clock dependency in the helper.

A future integration point may wrap this helper with a current-time provider, but this candidate does not authorize runtime execution and does not change live execution posture.

## Evidence-safe result model

The helper returns an `AuthorizationExpiryDecision` with:

~~~text
allowed_to_continue
status
reason
expiry_field
expiry_value_present
expired
comparison
~~~

The result intentionally avoids including secrets, credentials, scanner output, customer material, private artifacts, or raw authorization objects.

## Candidate tests

This checkpoint adds:

~~~text
tools/test_authorization_expiry_current_time_check.py
tools/test_v06129_authorization_expiry_current_time_check_candidate.py
~~~

The tests cover:

* not expired authorization,
* expiry equal to current time,
* expired authorization,
* malformed expiry,
* missing required expiry,
* missing optional expiry,
* timezone-aware offset comparison,
* timezone-naive expiry fail-closed,
* timezone-naive current-time fail-closed,
* evidence-safe output shape,
* v0.6.128 readiness continuity,
* v0.6.130 review/decision deferral.

## Candidate record

~~~text
authorization_expiry_current_time_check_candidate_completed = true
authorization_expiry_current_time_check_candidate_is_high_risk = true
authorization_expiry_current_time_check_candidate_checkpoint_2_of_3 = true
authorization_expiry_current_time_check_readiness_completed = true
authorization_expiry_current_time_check_review_decision_deferred_to_v06130 = true
authorization_expiry_current_time_helper_added = true
authorization_expiry_current_time_helper_tests_added = true
authorization_expiry_candidate_deterministic_current_time_supported = true
authorization_expiry_candidate_fail_closed_on_expired = true
authorization_expiry_candidate_fail_closed_on_malformed_expiry = true
authorization_expiry_candidate_fail_closed_on_missing_required_expiry = true
authorization_expiry_candidate_fail_closed_on_timezone_naive_expiry = true
authorization_expiry_candidate_fail_closed_on_timezone_naive_current_time = true
authorization_expiry_candidate_allows_not_expired_to_continue_existing_checks = true
authorization_expiry_candidate_equal_boundary_treated_as_not_expired = true
authorization_expiry_candidate_evidence_safe_result_model_added = true
authorization_expiry_behavior_modified = true
authorization_validation_logic_modified = true
authorization_gate_runtime_behavior_modified = false
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
external_discovery_fail_closed_added = false
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
selected_next_checkpoint = v0.6.130 Authorization Expiry Current-Time Check Review and Decision
~~~

## What changed

The following files are added:

~~~text
tools/authorization_expiry_current_time.py
tools/test_authorization_expiry_current_time_check.py
tools/test_v06129_authorization_expiry_current_time_check_candidate.py
docs/205-v06129-authorization-expiry-current-time-check-candidate.md
planning/decisions/ADR-0199-add-v06129-authorization-expiry-current-time-check-candidate.md
planning/issues/0198-add-v06129-authorization-expiry-current-time-check-candidate.md
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

No request/decision constraint-diff enforcement is added.

No external_discovery fail-closed behavior is added.

No mock/dry-run status terminology is renamed.

No Enterprise Review Guide is created.

No technical due diligence summary is created.

No safe PoC boundary template is created.

No control matrix is created.

No reviewer walkthrough is created.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.128

v0.6.128 prepared readiness for this High-risk work item and deferred candidate implementation to v0.6.129.

This checkpoint is the candidate implementation checkpoint.

## Relationship to v0.6.127

v0.6.127 selected authorization expiry checked against current time as a High-risk work item and assigned three checkpoints:

~~~text
v0.6.128 Authorization Expiry Current-Time Check Readiness
v0.6.129 Authorization Expiry Current-Time Check Candidate
v0.6.130 Authorization Expiry Current-Time Check Review and Decision
~~~

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.130 Authorization Expiry Current-Time Check Review and Decision
~~~

That checkpoint should review the candidate behavior, confirm fail-closed boundaries, and decide whether to close the High-risk work item.
