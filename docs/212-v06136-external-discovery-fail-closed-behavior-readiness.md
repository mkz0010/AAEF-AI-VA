# v0.6.136 External Discovery Fail-Closed Behavior Readiness

Status: readiness
Date: 2026-05-10

## Purpose

This checkpoint prepares the external_discovery=true fail-closed behavior work item selected in v0.6.135.

This is checkpoint 1 of 3 for a High-risk gate-semantics work item.

This checkpoint prepares external_discovery=true fail-closed behavior readiness.

The candidate implementation is deferred to v0.6.137.

The review and decision are deferred to v0.6.138.

This checkpoint does not implement external_discovery fail-closed behavior.

This checkpoint does not modify external_discovery behavior.

This checkpoint does not modify runtime behavior.

## Readiness record

~~~text
external_discovery_fail_closed_behavior_readiness_completed = true
external_discovery_fail_closed_behavior_readiness_is_high_risk = true
external_discovery_fail_closed_behavior_readiness_checkpoint_1_of_3 = true
external_discovery_fail_closed_behavior_candidate_deferred_to_v06137 = true
external_discovery_fail_closed_behavior_review_decision_deferred_to_v06138 = true
external_discovery_fail_closed_behavior_readiness_documentation_only = true
external_discovery_fail_closed_behavior_readiness_identifies_target_discovery = true
external_discovery_fail_closed_behavior_readiness_identifies_current_semantics = true
external_discovery_fail_closed_behavior_readiness_identifies_target_boundary_inputs = true
external_discovery_fail_closed_behavior_readiness_identifies_expected_behavior = true
external_discovery_fail_closed_behavior_readiness_identifies_fail_closed_boundary = true
external_discovery_fail_closed_behavior_readiness_identifies_tests_to_add_or_update = true
external_discovery_fail_closed_behavior_readiness_identifies_evidence_boundary = true
external_discovery_fail_closed_behavior_readiness_identifies_non_goals = true
external_discovery_fail_closed_added = false
external_discovery_behavior_modified = false
external_discovery_helper_added = false
external_discovery_gate_runtime_behavior_modified = false
target_boundary_behavior_modified = false
candidate_implementation_started = false
review_decision_completed = false
request_decision_constraint_diff_enforcement_work_item_closed = true
authorization_expiry_current_time_check_work_item_closed = true
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
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
selected_next_checkpoint = v0.6.137 External Discovery Fail-Closed Behavior Candidate
~~~

## Readiness target discovery

The readiness scan looked for repository files that mention external_discovery or external discovery and related target-boundary, request, authorization, decision, or gate concepts.

Potential target files or review starting points:

- `docs/11-mvp-scope.md` — matched terms: authorization, decision, external discovery, gate, request, scope
- `docs/12-credential-ref-flow.md` — matched terms: authorization, decision, external_discovery, gate, request, scope
- `docs/13-tool-gateway-mvp-design.md` — matched terms: authorization, decision, external discovery, external_discovery, fail closed, gate, request, scope
- `docs/15-tool-gateway-prototype-examples.md` — matched terms: authorization, blocked, decision, external discovery, gate, request
- `docs/170-v0694-narrow-public-safe-aaef-main-handback-material-preparation-planning.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/171-v0695-narrow-public-safe-aaef-main-handback-material-preparation-candidate.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/172-v0696-narrow-public-safe-aaef-main-handback-material-preparation-candidate-review-close-readiness.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/173-v0697-applied-evidence-handback-material-drafting-or-submission-decision.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/174-v0698-narrow-public-safe-aaef-main-handback-text-drafting-planning.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/175-v0699-narrow-public-safe-aaef-main-handback-text-drafting-candidate.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/176-v06100-narrow-public-safe-aaef-main-handback-text-drafting-candidate-review-close-readiness.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/177-v06101-applied-evidence-handback-text-submission-or-pause-decision.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request
- `docs/178-v06102-narrow-public-safe-aaef-main-handback-final-text-preparation-planning.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request
- `docs/179-v06103-narrow-public-safe-aaef-main-handback-final-text-preparation-candidate.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/180-v06104-narrow-public-safe-aaef-main-handback-final-text-preparation-candidate-review-close-readiness.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/181-v06105-applied-evidence-handback-submittable-text-or-pause-decision.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request
- `docs/182-v06106-narrow-public-safe-aaef-main-handback-submittable-text-preparation-planning.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/183-v06107-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/184-v06108-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate-review-close-readiness.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/185-v06109-applied-evidence-handback-submission-or-pause-decision.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/186-v06110-narrow-public-safe-aaef-main-handback-submission-workflow-planning.md` — matched terms: authorization, blocked, decision, external discovery, external_discovery, gate, request, scope
- `docs/187-v06111-narrow-public-safe-aaef-main-handback-workflow-selection-or-exact-text-preparation-decision.md` — matched terms: authorization, decision, external discovery, external_discovery, gate, request, scope
- `docs/188-v06112-narrow-public-safe-aaef-main-handback-exact-issue-text-preparation-planning.md` — matched terms: authorization, decision, external discovery, external_discovery, gate, request
- `docs/189-v06113-narrow-public-safe-aaef-main-handback-exact-issue-text-preparation-candidate.md` — matched terms: authorization, blocked, decision, external_discovery, gate, request, scope
- `docs/190-v06114-narrow-public-safe-aaef-main-handback-exact-issue-text-preparation-candidate-review-close-readiness.md` — matched terms: authorization, decision, external_discovery, gate, request, scope
- `docs/191-v06115-narrow-public-safe-aaef-main-handback-exact-issue-submission-or-pause-decision.md` — matched terms: authorization, decision, external_discovery, gate, request, scope
- `docs/192-v06116-narrow-public-safe-aaef-main-handback-human-submission-checklist-preparation.md` — matched terms: authorization, blocked, decision, external_discovery, gate, request
- `docs/193-v06117-narrow-public-safe-aaef-main-handback-human-submission-checklist-review-close-readiness.md` — matched terms: authorization, decision, external_discovery, gate, request
- `docs/194-v06118-narrow-public-safe-aaef-main-handback-human-maintainer-final-submission-decision-or-pause.md` — matched terms: authorization, decision, external_discovery, gate, request, scope
- `docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md` — matched terms: authorization, decision, external_discovery, gate, request
- `docs/197-v06121-next-direction-selection-using-risk-tiered-granularity.md` — matched terms: authorization, decision, external_discovery, gate, request
- `docs/198-v06122-readme-current-latest-baseline-clarity-candidate.md` — matched terms: authorization, decision, external_discovery, request, scope
- `docs/199-v06123-readme-current-latest-baseline-clarity-review-and-decision.md` — matched terms: authorization, decision, external_discovery, request, scope
- `docs/200-v06124-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, decision, external_discovery, gate, request
- `docs/201-v06125-security-reporting-channel-consistency-candidate.md` — matched terms: authorization, decision, external_discovery, request, scope
- `docs/202-v06126-security-reporting-channel-consistency-review-and-decision.md` — matched terms: authorization, decision, external_discovery, request, scope
- `docs/203-v06127-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, decision, external_discovery, gate, request, scope
- `docs/204-v06128-authorization-expiry-current-time-check-readiness.md` — matched terms: authorization, blocked, decision, external_discovery, fail closed, gate, request, scope
- `docs/205-v06129-authorization-expiry-current-time-check-candidate.md` — matched terms: authorization, blocked, decision, external_discovery, fail closed, gate, request
- `docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md` — matched terms: authorization, blocked, decision, external_discovery, fail closed, gate, request
- `docs/207-v06131-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, decision, external_discovery, gate, request, scope
- `docs/208-v06132-request-decision-constraint-diff-enforcement-readiness.md` — matched terms: authorization, blocked, decision, destination_binding, external discovery, external_discovery, fail closed, gate, local-lab, request, scope, target_mode
- `docs/209-v06133-request-decision-constraint-diff-enforcement-candidate.md` — matched terms: authorization, blocked, decision, destination_binding, external_discovery, fail closed, gate, request, scope, target_mode
- `docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md` — matched terms: authorization, blocked, decision, destination_binding, external discovery, external_discovery, fail closed, gate, request, scope, target_mode
- `docs/211-v06135-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, decision, external discovery, external_discovery, fail closed, gate, request, scope, target boundary
- `docs/24-controlled-executor-policy.md` — matched terms: authorization, decision, external discovery, gate, request, scope
- `docs/25-scope-registry-target-alias-resolution.md` — matched terms: external discovery, fail closed, gate, request, scope
- `planning/decisions/ADR-0018-add-controlled-executor-policy-before-real-tool-execution.md` — matched terms: decision, external discovery, fail closed, request
- `planning/decisions/ADR-0203-add-v06133-request-decision-constraint-diff-enforcement-candidate.md` — matched terms: authorization, decision, external_discovery, request
- `planning/decisions/ADR-0204-add-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md` — matched terms: authorization, decision, external_discovery, gate, request
- `planning/decisions/ADR-0205-add-v06135-next-work-selection-using-risk-tiered-granularity.md` — matched terms: decision, external discovery, external_discovery, gate, request
- `planning/issues/0017-add-controlled-executor-policy.md` — matched terms: decision, external discovery
- `planning/issues/0202-add-v06133-request-decision-constraint-diff-enforcement-candidate.md` — matched terms: authorization, decision, external_discovery, fail closed, gate, request
- `planning/issues/0203-add-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md` — matched terms: authorization, decision, external_discovery, gate, request
- `planning/issues/0204-add-v06135-next-work-selection-using-risk-tiered-granularity.md` — matched terms: decision, external_discovery, request
- `prototypes/tool-gateway/adapters/zap_adapter.py` — matched terms: blocked, decision, external discovery, gate, request, scope
- `prototypes/tool-gateway/controlled_executor.py` — matched terms: authorization, external_discovery, scope
- `prototypes/tool-gateway/examples/README.md` — matched terms: external discovery, gate, request
- `prototypes/tool-gateway/examples/allowed-action.authorization-decision.json` — matched terms: authorization, decision, external_discovery, request, scope
- `prototypes/tool-gateway/examples/allowed-action.tool-action-request.json` — matched terms: external_discovery, request, scope
- `prototypes/tool-gateway/examples/denied-action.authorization-decision.json` — matched terms: authorization, decision, external discovery, external_discovery, request, scope
- `prototypes/tool-gateway/examples/denied-action.tool-action-request.json` — matched terms: external discovery, external_discovery, request, scope
- `prototypes/tool-gateway/examples/human-approval-required.authorization-decision.json` — matched terms: authorization, decision, external_discovery, gate, request, scope
- `prototypes/tool-gateway/examples/human-approval-required.tool-action-request.json` — matched terms: external_discovery, request, scope
- `prototypes/tool-gateway/scope_registry/registry.json` — matched terms: blocked, external discovery, scope
- `tools/request_decision_constraint_diff.py` — matched terms: allow_external_discovery, authorization, blocked, decision, destination_binding, external_discovery, external_discovery_allowed, gate, request, runtime_destination_binding, scope, target_boundary, target_mode
- `tools/test_controlled_executor_policy.py` — matched terms: authorization, decision, external discovery, external_discovery, fail closed, gate, request, scope
- `tools/test_request_decision_constraint_diff_enforcement.py` — matched terms: blocked, decision, destination_binding, external_discovery, external_discovery_allowed, fail closed, local-lab, localhost_only, request, scope, target_mode
- `tools/test_v06100_narrow_public_safe_aaef_main_handback_text_drafting_candidate_review_close_readiness.py` — matched terms: authorization, decision, external_discovery, gate, request, scope
- `tools/test_v06101_applied_evidence_handback_text_submission_or_pause_decision.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06102_narrow_public_safe_aaef_main_handback_final_text_preparation_planning.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06103_narrow_public_safe_aaef_main_handback_final_text_preparation_candidate.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06104_narrow_public_safe_aaef_main_handback_final_text_preparation_candidate_review_close_readiness.py` — matched terms: authorization, decision, external_discovery, gate, request, scope
- `tools/test_v06105_applied_evidence_handback_submittable_text_or_pause_decision.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06106_narrow_public_safe_aaef_main_handback_submittable_text_preparation_planning.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06107_narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06108_narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate_review_close_readiness.py` — matched terms: authorization, decision, external_discovery, gate, request, scope
- `tools/test_v06109_applied_evidence_handback_submission_or_pause_decision.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06110_narrow_public_safe_aaef_main_handback_submission_workflow_planning.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06111_narrow_public_safe_aaef_main_handback_workflow_selection_or_exact_text_preparation_decision.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06112_narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_planning.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06113_narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_candidate.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06114_narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_candidate_review_close_readiness.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06115_narrow_public_safe_aaef_main_handback_exact_issue_submission_or_pause_decision.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06116_narrow_public_safe_aaef_main_handback_human_submission_checklist_preparation.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06117_narrow_public_safe_aaef_main_handback_human_submission_checklist_review_close_readiness.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06118_narrow_public_safe_aaef_main_handback_human_maintainer_final_submission_decision_or_pause.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06119_narrow_public_safe_aaef_main_handback_pause_and_current_state_closeout_review.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v06121_next_direction_selection_using_risk_tiered_granularity.py` — matched terms: authorization, decision, external_discovery, request
- `tools/test_v06122_readme_current_latest_baseline_clarity_candidate.py` — matched terms: authorization, decision, external_discovery, request
- `tools/test_v06123_readme_current_latest_baseline_clarity_review_and_decision.py` — matched terms: authorization, decision, external_discovery, request
- `tools/test_v06124_next_work_selection_using_risk_tiered_granularity.py` — matched terms: authorization, decision, external_discovery, request
- `tools/test_v06125_security_reporting_channel_consistency_candidate.py` — matched terms: authorization, decision, external_discovery, request, scope
- `tools/test_v06126_security_reporting_channel_consistency_review_and_decision.py` — matched terms: authorization, decision, external_discovery, request, scope
- `tools/test_v06127_next_work_selection_using_risk_tiered_granularity.py` — matched terms: authorization, decision, external_discovery, request
- `tools/test_v06128_authorization_expiry_current_time_check_readiness.py` — matched terms: authorization, blocked, decision, external_discovery, gate, request
- `tools/test_v06129_authorization_expiry_current_time_check_candidate.py` — matched terms: authorization, blocked, decision, external_discovery, fail closed, gate, request
- `tools/test_v06130_authorization_expiry_current_time_check_review_and_decision.py` — matched terms: authorization, decision, external_discovery, fail closed, gate, request
- `tools/test_v06131_next_work_selection_using_risk_tiered_granularity.py` — matched terms: authorization, decision, external_discovery, request
- `tools/test_v06132_request_decision_constraint_diff_enforcement_readiness.py` — matched terms: authorization, blocked, decision, destination_binding, external_discovery, gate, request, scope, target_mode
- `tools/test_v06133_request_decision_constraint_diff_enforcement_candidate.py` — matched terms: authorization, decision, destination_binding, external discovery, external_discovery, external_discovery_allowed, fail closed, gate, local-lab, localhost_only, request, scope, target_mode
- `tools/test_v06134_request_decision_constraint_diff_enforcement_review_and_decision.py` — matched terms: authorization, decision, destination_binding, external_discovery, external_discovery_allowed, fail closed, gate, local-lab, localhost_only, request, scope, target_mode
- `tools/test_v06135_next_work_selection_using_risk_tiered_granularity.py` — matched terms: authorization, decision, external discovery, external_discovery, gate, request
- `tools/test_v0694_narrow_public_safe_aaef_main_handback_material_preparation_planning.py` — matched terms: authorization, blocked, decision, external_discovery, gate, request
- `tools/test_v0695_narrow_public_safe_aaef_main_handback_material_preparation_candidate.py` — matched terms: authorization, blocked, decision, external_discovery, gate, request, scope
- `tools/test_v0696_narrow_public_safe_aaef_main_handback_material_preparation_candidate_review_close_readiness.py` — matched terms: authorization, blocked, decision, external_discovery, gate, request, scope
- `tools/test_v0697_applied_evidence_handback_material_drafting_or_submission_decision.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v0698_narrow_public_safe_aaef_main_handback_text_drafting_planning.py` — matched terms: authorization, decision, external_discovery, gate, request
- `tools/test_v0699_narrow_public_safe_aaef_main_handback_text_drafting_candidate.py` — matched terms: authorization, decision, external_discovery, gate, request, scope

This discovery is advisory only. It does not prove that these are the only files that matter, and it does not authorize implementation in this checkpoint.

## Current semantics to inspect

The v0.6.137 candidate should inspect how `external_discovery` is represented in the current request, authorization decision, target-boundary, and gate artifacts.

The candidate should specifically inspect whether the repository currently has one or more of these concepts:

* request field such as `external_discovery`,
* authorization decision field such as `external_discovery_allowed` or `allow_external_discovery`,
* target-boundary field such as `target_mode`, `target_boundary`, `localhost_only`, or `runtime_destination_binding`,
* scope or destination-binding field that constrains target expansion,
* evidence field that records whether external discovery was requested, allowed, blocked, or not applicable.

## Target-boundary inputs

The v0.6.137 candidate should evaluate external discovery against evidence-safe, gate-relevant target-boundary inputs.

Candidate inputs should include, where present:

| Input area | Expected purpose |
| --- | --- |
| requested external_discovery flag | determine whether the request asks to discover beyond a known target |
| authorization decision external_discovery allowance | determine whether external discovery was explicitly authorized |
| target_mode or target_boundary | determine whether the target profile permits external expansion |
| runtime destination binding | determine whether runtime destination is constrained |
| scope_id or assessment scope | determine whether target expansion stays within scope |
| request/decision constraint-diff result | avoid duplicating but remain compatible with constraint-diff enforcement |
| authorization expiry result | avoid treating expired authorization as allowing external discovery |

The candidate should not compare or expose raw secrets, raw credentials, private customer material, scanner output, or private artifacts.

## Expected candidate behavior

The v0.6.137 candidate should evaluate whether a request with `external_discovery=true` is explicitly allowed by the authorization decision and compatible with the configured target boundary.

Expected behavior:

* If `external_discovery=true` and the decision does not explicitly allow external discovery, the gate should fail closed.
* If `external_discovery=true` and the target boundary is `localhost_only`, local-lab-only, or otherwise non-external, the gate should fail closed.
* If `external_discovery=true` and the runtime destination binding is missing, malformed, or ambiguous where required, the gate should fail closed.
* If `external_discovery=true` and the scope cannot prove that external discovery is in bounds, the gate should fail closed.
* If `external_discovery=false` or missing and external discovery is not required, the gate may continue existing checks.
* If `external_discovery=true` is explicitly allowed and compatible with the target boundary, the gate may continue existing checks.
* The result should be evidence-safe and reviewable.

## Fail-closed boundary

The fail-closed boundary for this work item is:

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

The candidate should not introduce permissive fallback behavior for ambiguous external discovery handling.

## Expected tests to add or update

The v0.6.137 candidate should add or update tests for at least these cases:

| Case | Expected result |
| --- | --- |
| external_discovery=false | continue existing checks |
| external_discovery missing and not required | continue existing checks |
| external_discovery=true without explicit decision allowance | fail closed |
| external_discovery=true with decision allowance=false | fail closed |
| external_discovery=true against localhost_only target boundary | fail closed |
| external_discovery=true against local-lab-only target boundary | fail closed |
| external_discovery=true without required destination binding | fail closed |
| external_discovery=true with malformed destination binding | fail closed |
| external_discovery=true without scope support | fail closed |
| external_discovery=true with ambiguous target boundary | fail closed |
| external_discovery=true with expired or invalid authorization result | fail closed |
| external_discovery=true explicitly allowed and boundary-compatible | continue existing checks |
| evidence output | records safe categories without sensitive material |

The candidate should prefer deterministic fixtures over environment-dependent behavior.

## Evidence boundary

The candidate result should be evidence-safe.

It may record:

~~~text
external_discovery_requested
external_discovery_allowed_by_decision
target_boundary_status
allowed_to_continue
status
reason
block_categories
matched_constraints
checked_fields
~~~

It should not record:

~~~text
raw secrets
raw credentials
tokens
private customer material
scanner output
private artifacts
full raw request payloads when unnecessary
full raw authorization decision payloads when unnecessary
live third-party target details
~~~

## Non-goals

This readiness checkpoint does not:

* implement external_discovery fail-closed behavior,
* modify external_discovery behavior,
* modify runtime behavior,
* authorize runtime execution,
* authorize scanner execution,
* authorize Docker/lab execution,
* permit credential injection,
* authorize customer targets,
* authorize delivery,
* change validator behavior,
* change schemas,
* change public samples,
* reopen AAEF main handback,
* open an AAEF main issue or PR,
* generate an issue command or URL,
* promote AAEF-AI-VA into AAEF Core/Profile/Practical Package status.

## Relationship to v0.6.135

v0.6.135 selected external_discovery=true fail-closed behavior as the next High-risk work item and assigned three checkpoints:

~~~text
v0.6.136 External Discovery Fail-Closed Behavior Readiness
v0.6.137 External Discovery Fail-Closed Behavior Candidate
v0.6.138 External Discovery Fail-Closed Behavior Review and Decision
~~~

This checkpoint is the readiness checkpoint.

## Relationship to v0.6.134

v0.6.134 closed the request/decision constraint-diff enforcement work item.

This checkpoint starts the next selected High-risk gate-semantics track without implementing behavior.

## Relationship to v0.6.130

v0.6.130 closed the authorization expiry current-time check work item.

This checkpoint preserves that completed gate-semantics hardening sequence and does not modify authorization expiry behavior.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## What did not happen

No external_discovery fail-closed behavior is added in this checkpoint.

No external_discovery behavior is modified.

No external_discovery helper is added.

No external_discovery gate runtime behavior is modified.

No target-boundary behavior is modified.

No candidate implementation is started.

No review/decision closeout is completed.

No request/decision constraint-diff enforcement is added or modified.

No authorization expiry current-time check is added or modified.

No mock/dry-run status terminology is renamed.

No Enterprise Review Guide is created.

No technical due diligence summary is created.

No safe PoC boundary template is created.

No control matrix is created.

No reviewer walkthrough is created.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

No validator behavior is modified.

No metadata-level `expected_failure_category` is added.

No JSON Schema is added.

No public sample is changed.

No runtime execution is authorized.

No scanner execution is authorized.

No Docker execution is authorized.

No credential injection is permitted.

No customer target is authorized.

No delivery is authorized.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Next checkpoint

Proceed to:

~~~text
v0.6.137 External Discovery Fail-Closed Behavior Candidate
~~~

That checkpoint may implement the candidate behavior and tests within the boundaries defined here.
