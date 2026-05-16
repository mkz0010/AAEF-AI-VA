# ADR-0363: Select Safe Mock Demo Initial Path

Status: accepted  
Date: 2026-05-17  
Version: v0.6.288

## Context

v0.6.287 created a Safe Runnable Demo Gap Inventory and recommended safe runnable demo path selection.

## Decision

Select `safe_mock_demo_initial_path` as the initial safe demo path.

## Decision record

~~~text
safe_runnable_demo_path_selection_completed = true
safe_runnable_demo_path_selection_id = safe_runnable_demo_path_selection_v06288
selected_demo_path = safe_mock_demo_initial_path
selected_demo_path_status = selected_for_initial_safe_demo_path_hardening
selected_demo_path_reason = safe_mock_demo_is_currently_runnable_while_local_only_runtime_remains_blocked
safe_mock_demo_initial_path_selected = true
safe_mock_demo_path_hardening_recommended = true
safe_mock_demo_public_positioning_recommended = true
local_only_demo_execution_boundary_candidate_recommended = true
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
runtime_enforcement_design_status = design_recorded_execution_blocked
execution_authorization_gate_status = authorization_scaffold_recorded_execution_blocked
preflight_validation_status = preflight_scaffold_recorded_execution_blocked
preflight_satisfied = false
concrete_checks_implemented = false
live_evidence_records_generated = false
runtime_enforcement_implemented = false
safe_mock_demo_status = runnable_private_artifact_demo_available
safe_mock_demo_is_live_scanner_execution = false
safe_mock_demo_private_artifacts_remain_private = true
private_generated_outputs_moved_public = false
safe_runnable_demo_gap_inventory_completed = true
safe_runnable_demo_gap_inventory_id = safe_runnable_demo_gap_inventory_v06287
safe_runnable_demo_gap_inventory_accepted_as_runtime_demo = false
safe_runnable_demo_gap_inventory_accepted_as_scanner_readiness = false
recommended_next_work_item = safe_mock_demo_initial_path_hardening_candidate
safe_mock_demo_initial_path_hardening_candidate_created = false
safe_mock_demo_public_artifact_promotion_created = false
safe_mock_demo_public_artifact_promotion_approved = false
publication_approval = false
public_announcement = deferred
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
certification_claim = false
legal_compliance_claim = false
audit_opinion_claim = false
diagnostic_completeness_claim = false
external_framework_equivalence_claim = false
~~~

## Consequences

The project should next create a Safe Mock Demo Initial Path Hardening Candidate. Local-only runtime execution and real scanner execution remain blocked.

## Boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- safe mock demo initial path selection is not runtime demo readiness
- safe mock demo initial path selection is not scanner readiness
- safe mock demo initial path selection is not production readiness
- safe mock demo public positioning is not publication approval
- No private generated outputs are moved public in v0.6.288.

## Structural token coverage

- safe_runnable_demo_path_selection
- safe_runnable_demo_path_selection_v06288
- safe_mock_demo_initial_path
- safe_mock_demo_initial_path_selected
- safe_mock_demo_initial_path_hardening_candidate
- safe_runnable_demo_gap_inventory_v06287
- safe mock demo
- local-only runnable demo
- real scanner execution remains blocked
- mock demo is not live scanner execution
- allowed-action: completed
- denied-action: blocked
- human-approval-required: requires_human_approval
- runtime readiness status: not_detected_execution_blocked
- target lab gate status: target_defined_execution_blocked
- binding gate status: bound_execution_blocked
- transition gate status: candidate_recorded_execution_blocked
- execution authorized: False
- real execution permitted: False
- safe mock demo initial path selection is not runtime demo readiness
- safe mock demo initial path selection is not scanner readiness
- safe mock demo initial path selection is not production readiness
- safe mock demo public positioning is not publication approval
- No private generated outputs are moved public in v0.6.288.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
