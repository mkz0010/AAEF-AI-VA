# ADR-0365: Accept Safe Mock Demo Initial Path Hardening Candidate

Status: accepted  
Date: 2026-05-17  
Version: v0.6.290

## Context

v0.6.289 created a documentation-only Safe Mock Demo Initial Path Hardening Candidate.

## Decision

Accept the v0.6.289 candidate for future safe mock demo initial path hardening.

## Decision record

~~~text
safe_mock_demo_initial_path_hardening_candidate_review_completed = true
safe_mock_demo_initial_path_hardening_candidate_accepted = true
safe_mock_demo_initial_path_hardening_candidate_id = safe_mock_demo_initial_path_hardening_candidate_v06289
safe_mock_demo_initial_path_hardening_candidate_review_result = accepted_for_future_safe_mock_demo_initial_path_hardening
safe_mock_demo_initial_path_hardening_candidate_status = accepted_for_future_safe_mock_demo_initial_path_hardening
future_safe_mock_demo_initial_path_hardening_accepted = true
future_safe_mock_demo_hardening_controls_accepted = true
future_safe_mock_demo_hardening_public_positioning_accepted = true
future_safe_mock_demo_hardening_private_artifact_boundary_accepted = true
future_safe_mock_demo_hardening_demo_script_boundary_accepted = true
future_safe_mock_demo_hardening_reviewer_walkthrough_boundary_accepted = true
future_safe_mock_demo_hardening_non_claim_boundaries_accepted = true
reviewed_safe_mock_demo_initial_path_hardening_candidate_id = safe_mock_demo_initial_path_hardening_candidate_v06289
reviewed_safe_runnable_demo_path_selection_id = safe_runnable_demo_path_selection_v06288
safe_mock_demo_initial_path_selected = true
selected_demo_path = safe_mock_demo_initial_path
safe_mock_demo_status = runnable_private_artifact_demo_available
safe_mock_demo_is_live_scanner_execution = false
safe_mock_demo_private_artifacts_remain_private = true
private_generated_outputs_moved_public = false
safe_mock_demo_initial_path_hardening_applied = false
safe_mock_demo_initial_path_hardening_completed = false
safe_mock_demo_public_artifact_promotion_created = false
safe_mock_demo_public_artifact_promotion_approved = false
safe_mock_demo_public_positioning_approved_for_publication = false
publication_approval = false
runtime_demo_ready = false
runtime_demo_readiness_claim = false
scanner_readiness_claim = false
production_readiness_claim = false
execution_authorized = false
real_execution_permitted = false
local_only_demo_execution_boundary_candidate_created = false
local_only_runnable_demo_path_selected = false
real_scanner_execution_path_selected = false
real_scanner_execution_status = blocked
runtime_readiness_status = not_detected_execution_blocked
target_lab_gate_status = target_defined_execution_blocked
runtime_destination_binding_status = bound_execution_blocked
bounded_execution_transition_status = candidate_recorded_execution_blocked
preflight_satisfied = false
concrete_checks_implemented = false
live_evidence_records_generated = false
runtime_enforcement_implemented = false
recommended_next_work_item = safe_mock_demo_initial_path_hardening
safe_mock_demo_initial_path_hardening_recommended = true
gateway_execution_path_behavior_modified = false
tool_gateway_behavior_changed = false
adapter_behavior_changed = false
schema_changed = false
runtime_behavior_changed = false
scanner_behavior_changed = false
fixtures_created = false
record_candidate_artifacts_created = false
actual_records_created = false
readme_front_page_rewritten = false
repository_metadata_changed = false
public_announcement = deferred
certification_claim = false
legal_compliance_claim = false
audit_opinion_claim = false
diagnostic_completeness_claim = false
external_framework_equivalence_claim = false
~~~

## Consequences

The project should next perform safe mock demo initial path hardening. Publication approval, public artifact promotion, runtime readiness, scanner readiness, and real execution remain deferred.

## Boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- safe mock demo hardening candidate review is not publication approval
- safe mock demo hardening candidate review is not public artifact promotion
- safe mock demo hardening candidate review is not runtime demo readiness
- safe mock demo hardening candidate review is not scanner readiness
- No private generated outputs are moved public in v0.6.290.

## Structural token coverage

- safe_mock_demo_initial_path_hardening_candidate_review_and_decision
- safe_mock_demo_initial_path_hardening_candidate_review_completed
- safe_mock_demo_initial_path_hardening_candidate_accepted
- safe_mock_demo_initial_path_hardening_candidate_v06289
- safe_mock_demo_initial_path_hardening_candidate
- safe_mock_demo_initial_path_hardening
- safe_mock_demo_initial_path
- safe_runnable_demo_path_selection_v06288
- safe mock demo
- safe mock demo path hardening
- safe mock demo public positioning
- safe mock demo private artifact boundary
- safe mock demo reviewer walkthrough boundary
- safe mock demo script boundary
- safe mock demo is not live scanner execution
- private-not-in-git
- allowed-action: completed
- denied-action: blocked
- human-approval-required: requires_human_approval
- local-only runnable demo
- real scanner execution remains blocked
- runtime readiness status: not_detected_execution_blocked
- target lab gate status: target_defined_execution_blocked
- binding gate status: bound_execution_blocked
- transition gate status: candidate_recorded_execution_blocked
- execution authorized: False
- real execution permitted: False
- safe mock demo hardening candidate review is not publication approval
- safe mock demo hardening candidate review is not public artifact promotion
- safe mock demo hardening candidate review is not runtime demo readiness
- safe mock demo hardening candidate review is not scanner readiness
- safe mock demo hardening candidate review is not production readiness
- No private generated outputs are moved public in v0.6.290.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
