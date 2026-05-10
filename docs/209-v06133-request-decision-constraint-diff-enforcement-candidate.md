# v0.6.133 Request/Decision Constraint-Diff Enforcement Candidate

Status: candidate
Date: 2026-05-10

## Purpose

This checkpoint implements the request/decision constraint-diff enforcement candidate after v0.6.132 readiness.

This is checkpoint 2 of 3 for a High-risk gate-semantics work item.

This checkpoint implements the request/decision constraint-diff enforcement candidate.

The review and decision are deferred to v0.6.134.

## Candidate implementation summary

This checkpoint adds a deterministic, evidence-safe helper and tests for comparing request constraints with authorization decision constraints.

The helper detects material request/decision drift before a dispatch path can treat the request as still covered by the decision.

The helper returns a small evidence-safe result object that records categories and field names without copying raw secrets, raw credentials, tokens, private customer material, scanner output, or private artifacts.

## Candidate helper

~~~text
tools/request_decision_constraint_diff.py
~~~

The helper exposes:

~~~text
evaluate_request_decision_constraint_diff(request, decision, *, required_fields=..., optional_fields=...)
RequestDecisionConstraintDiffResult.as_evidence()
ConstraintDiff.as_evidence()
~~~

## Candidate behavior

| Case | Candidate behavior |
| --- | --- |
| exact request/decision match | continue existing checks |
| tool/action mismatch | blocked / fail closed |
| target mismatch | blocked / fail closed |
| destination binding mismatch | blocked / fail closed |
| target mode mismatch | blocked / fail closed |
| scope mismatch | blocked / fail closed |
| credential_ref mismatch | blocked / fail closed |
| execution mode mismatch | blocked / fail closed |
| external_discovery escalation | blocked / fail closed |
| missing required request field | blocked / fail closed |
| missing required decision field | blocked / fail closed |
| malformed request constraints | blocked / fail closed |
| malformed decision constraints | blocked / fail closed |

## Fail-closed behavior

~~~text
tool_action_mismatch -> blocked / not authorized
target_mismatch -> blocked / not authorized
destination_binding_mismatch -> blocked / not authorized
target_mode_mismatch -> blocked / not authorized
scope_mismatch -> blocked / not authorized
credential_ref_mismatch -> blocked / not authorized
execution_mode_mismatch -> blocked / not authorized
external_discovery_escalation -> blocked / not authorized
missing_required_request_field -> blocked / not authorized
missing_required_decision_field -> blocked / not authorized
malformed_request_constraints -> blocked / not authorized
malformed_decision_constraints -> blocked / not authorized
ambiguous_constraint_comparison -> blocked / not authorized
~~~

## Evidence-safe result model

The helper returns a `RequestDecisionConstraintDiffResult` with:

~~~text
allowed_to_continue
status
reason
diff_categories
diffs
matched_constraints
compared_fields
~~~

The result intentionally avoids including raw secrets, raw credentials, tokens, private customer material, scanner output, private artifacts, full raw request payloads, or full raw authorization decision payloads.

## Candidate tests

This checkpoint adds:

~~~text
tools/test_request_decision_constraint_diff_enforcement.py
tools/test_v06133_request_decision_constraint_diff_enforcement_candidate.py
~~~

The tests cover:

* exact request/decision match,
* tool/action mismatch,
* target mismatch,
* destination binding mismatch,
* target mode mismatch,
* scope mismatch,
* credential_ref mismatch,
* execution mode mismatch,
* external_discovery escalation,
* missing required request field,
* missing required decision field,
* malformed request constraints,
* malformed decision constraints,
* evidence-safe output shape,
* v0.6.132 readiness continuity,
* v0.6.134 review/decision deferral.

## Candidate record

~~~text
request_decision_constraint_diff_enforcement_candidate_completed = true
request_decision_constraint_diff_enforcement_candidate_is_high_risk = true
request_decision_constraint_diff_enforcement_candidate_checkpoint_2_of_3 = true
request_decision_constraint_diff_enforcement_readiness_completed = true
request_decision_constraint_diff_enforcement_review_decision_deferred_to_v06134 = true
constraint_diff_helper_added = true
constraint_diff_helper_tests_added = true
constraint_diff_candidate_deterministic_comparison_supported = true
constraint_diff_candidate_fail_closed_on_tool_action_mismatch = true
constraint_diff_candidate_fail_closed_on_target_mismatch = true
constraint_diff_candidate_fail_closed_on_destination_binding_mismatch = true
constraint_diff_candidate_fail_closed_on_target_mode_mismatch = true
constraint_diff_candidate_fail_closed_on_scope_mismatch = true
constraint_diff_candidate_fail_closed_on_credential_ref_mismatch = true
constraint_diff_candidate_fail_closed_on_execution_mode_mismatch = true
constraint_diff_candidate_fail_closed_on_external_discovery_escalation = true
constraint_diff_candidate_fail_closed_on_missing_required_request_field = true
constraint_diff_candidate_fail_closed_on_missing_required_decision_field = true
constraint_diff_candidate_fail_closed_on_malformed_request_constraints = true
constraint_diff_candidate_fail_closed_on_malformed_decision_constraints = true
constraint_diff_candidate_allows_exact_match_to_continue_existing_checks = true
constraint_diff_candidate_evidence_safe_result_model_added = true
constraint_diff_enforcement_added = true
constraint_diff_behavior_modified = true
request_decision_comparison_logic_modified = true
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
authorization_expiry_now_check_added = false
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
selected_next_checkpoint = v0.6.134 Request/Decision Constraint-Diff Enforcement Review and Decision
~~~

## What changed

The following files are added:

~~~text
tools/request_decision_constraint_diff.py
tools/test_request_decision_constraint_diff_enforcement.py
tools/test_v06133_request_decision_constraint_diff_enforcement_candidate.py
docs/209-v06133-request-decision-constraint-diff-enforcement-candidate.md
planning/decisions/ADR-0203-add-v06133-request-decision-constraint-diff-enforcement-candidate.md
planning/issues/0202-add-v06133-request-decision-constraint-diff-enforcement-candidate.md
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

No authorization gate runtime behavior is modified.

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

No authorization expiry current-time check is added or modified.

No external_discovery fail-closed behavior is added.

No mock/dry-run status terminology is renamed.

No Enterprise Review Guide is created.

No technical due diligence summary is created.

No safe PoC boundary template is created.

No control matrix is created.

No reviewer walkthrough is created.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.132

v0.6.132 prepared readiness for this High-risk work item and deferred candidate implementation to v0.6.133.

This checkpoint is the candidate implementation checkpoint.

## Relationship to v0.6.131

v0.6.131 selected request/decision constraint-diff enforcement as a High-risk work item and assigned three checkpoints:

~~~text
v0.6.132 Request/Decision Constraint-Diff Enforcement Readiness
v0.6.133 Request/Decision Constraint-Diff Enforcement Candidate
v0.6.134 Request/Decision Constraint-Diff Enforcement Review and Decision
~~~

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.134 Request/Decision Constraint-Diff Enforcement Review and Decision
~~~

That checkpoint should review the candidate behavior, confirm fail-closed boundaries, and decide whether to close the High-risk work item.
