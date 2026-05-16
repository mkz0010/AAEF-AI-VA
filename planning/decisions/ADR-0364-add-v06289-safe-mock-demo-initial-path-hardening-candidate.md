# ADR-0364: Create Safe Mock Demo Initial Path Hardening Candidate

Status: proposed candidate  
Date: 2026-05-17  
Version: v0.6.289

## Context

v0.6.288 selected `safe_mock_demo_initial_path` as the initial safe demo path.

## Decision

Create a documentation-only Safe Mock Demo Initial Path Hardening Candidate.

## Decision record

~~~text
safe_mock_demo_initial_path_hardening_candidate_created = true
safe_mock_demo_initial_path_hardening_candidate_id = safe_mock_demo_initial_path_hardening_candidate_v06289
safe_mock_demo_initial_path_hardening_candidate_status = candidate_not_applied
safe_mock_demo_initial_path_hardening_candidate_scope = documentation_only_candidate_for_safe_mock_demo_review_path_hardening
selected_demo_path = safe_mock_demo_initial_path
selected_demo_path_status = selected_for_initial_safe_demo_path_hardening
safe_mock_demo_initial_path_selected = true
safe_runnable_demo_path_selection_completed = true
safe_runnable_demo_path_selection_id = safe_runnable_demo_path_selection_v06288
safe_mock_demo_status = runnable_private_artifact_demo_available
safe_mock_demo_is_live_scanner_execution = false
safe_mock_demo_private_artifacts_remain_private = true
private_generated_outputs_moved_public = false
safe_mock_demo_hardening_questions_defined = true
safe_mock_demo_hardening_scope_defined = true
safe_mock_demo_hardening_controls_defined = true
safe_mock_demo_hardening_review_inputs_defined = true
safe_mock_demo_hardening_expected_outputs_defined = true
safe_mock_demo_hardening_non_claim_boundaries_defined = true
safe_mock_demo_hardening_public_positioning_defined = true
safe_mock_demo_hardening_private_artifact_boundary_defined = true
safe_mock_demo_hardening_demo_script_boundary_defined = true
safe_mock_demo_hardening_reviewer_walkthrough_boundary_defined = true
safe_mock_demo_hardening_public_artifact_promotion_created = false
safe_mock_demo_public_artifact_promotion_created = false
safe_mock_demo_public_artifact_promotion_approved = false
safe_mock_demo_initial_path_hardening_applied = false
safe_mock_demo_initial_path_hardening_completed = false
safe_mock_demo_initial_path_review_and_decision_created = false
recommended_next_work_item = safe_mock_demo_initial_path_hardening_candidate_review_and_decision
safe_mock_demo_initial_path_hardening_candidate_review_and_decision_recommended = true
safe_runnable_demo_path_selection_recommended = false
local_only_demo_execution_boundary_candidate_recommended = false
local_only_demo_execution_boundary_candidate_created = false
local_only_runnable_demo_path_selected = false
real_scanner_execution_path_selected = false
real_scanner_execution_status = blocked
runtime_demo_ready = false
runtime_demo_readiness_claim = false
scanner_readiness_claim = false
production_readiness_claim = false
execution_authorized = false
real_execution_permitted = false
runtime_readiness_status = not_detected_execution_blocked
target_lab_gate_status = target_defined_execution_blocked
runtime_destination_binding_status = bound_execution_blocked
bounded_execution_transition_status = candidate_recorded_execution_blocked
local_execution_plan_review_status = plan_recorded_execution_blocked
runtime_safety_policy_status = policy_recorded_execution_blocked
preflight_satisfied = false
concrete_checks_implemented = false
live_evidence_records_generated = false
runtime_enforcement_implemented = false
publication_approval = false
public_announcement = deferred
readme_front_page_rewritten = false
repository_metadata_changed = false
gateway_execution_path_behavior_modified = false
tool_gateway_behavior_changed = false
adapter_behavior_changed = false
schema_changed = false
runtime_behavior_changed = false
scanner_behavior_changed = false
fixtures_created = false
record_candidate_artifacts_created = false
actual_records_created = false
certification_claim = false
legal_compliance_claim = false
audit_opinion_claim = false
diagnostic_completeness_claim = false
external_framework_equivalence_claim = false
~~~

## Consequences

The project should next review this hardening candidate before applying any demo hardening or public artifact promotion.

## Boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- safe mock demo hardening candidate is not publication approval
- safe mock demo hardening candidate is not public artifact promotion
- safe mock demo hardening candidate is not runtime demo readiness
- safe mock demo hardening candidate is not scanner readiness
- No private generated outputs are moved public in v0.6.289.

## Structural token coverage

- safe_mock_demo_initial_path_hardening_candidate
- safe_mock_demo_initial_path_hardening_candidate_v06289
- safe_mock_demo_initial_path_hardening_candidate_review_and_decision
- safe_mock_demo_initial_path
- safe_mock_demo_initial_path_selected
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
- safe mock demo hardening candidate is not publication approval
- safe mock demo hardening candidate is not public artifact promotion
- safe mock demo hardening candidate is not runtime demo readiness
- safe mock demo hardening candidate is not scanner readiness
- safe mock demo hardening candidate is not production readiness
- No private generated outputs are moved public in v0.6.289.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
