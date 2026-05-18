# ADR-0373: Select Safe Mock Demo Public Artifact Promotion Candidate

Status: accepted  
Date: 2026-05-18  
Version: v0.6.298

## Context

v0.6.297 accepted the Safe Mock Demo Pre-Public Boundary Review as review records.

## Decision

Select `safe_mock_demo_public_artifact_promotion_candidate` as the next work item.

## Decision record

~~~text\nnext_work_selection_completed = true
next_work_selection_id = next_work_selection_v06298
selected_work_item = safe_mock_demo_public_artifact_promotion_candidate
selected_work_item_status = selected_for_public_artifact_promotion_candidate
selected_work_item_reason = pre_public_boundary_review_accepted_and_public_artifact_promotion_still_not_created
safe_mock_demo_public_artifact_promotion_candidate_selected = true
safe_mock_demo_public_artifact_promotion_candidate_recommended = true
safe_mock_demo_public_artifact_promotion_candidate_created = false
safe_mock_demo_public_artifact_promotion_candidate_review_completed = false
safe_mock_demo_public_artifact_promotion_candidate_accepted = false
safe_mock_demo_public_artifact_promotion_created = false
safe_mock_demo_public_artifact_promotion_approved = false
safe_mock_demo_public_positioning_approved_for_publication = false
safe_mock_demo_pre_public_boundary_review_decision_completed = true
safe_mock_demo_pre_public_boundary_review_accepted = true
safe_mock_demo_pre_public_boundary_review_id = safe_mock_demo_pre_public_boundary_review_v06296
safe_mock_demo_pre_public_boundary_review_decision_result = accepted_as_pre_public_boundary_review_records
safe_mock_demo_status = runnable_private_artifact_demo_available
safe_mock_demo_is_live_scanner_execution = false
safe_mock_demo_private_artifacts_remain_private = true
private_generated_outputs_moved_public = false
publication_approval_selected = false
publication_approval = false
public_announcement = deferred
local_only_demo_execution_boundary_candidate_selected = false
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
preflight_satisfied = false
concrete_checks_implemented = false
live_evidence_records_generated = false
runtime_enforcement_implemented = false
recommended_next_work_item = safe_mock_demo_public_artifact_promotion_candidate
next_work_selection_recommended = false
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
external_framework_equivalence_claim = false\n~~~

## Consequences

The project should next create a Safe Mock Demo Public Artifact Promotion Candidate. Actual public artifact promotion, publication approval, local-only execution boundary work, runtime readiness, scanner readiness, and real execution remain deferred.

## Boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- public artifact promotion candidate is not publication approval
- public artifact promotion candidate is not public artifact promotion
- public artifact promotion candidate is not runtime demo readiness
- public artifact promotion candidate is not scanner readiness
- No private generated outputs are moved public in v0.6.298.

## Structural token coverage

- next_work_selection_using_risk_tiered_granularity
- next_work_selection_v06298
- safe_mock_demo_public_artifact_promotion_candidate
- safe_mock_demo_public_artifact_promotion
- safe_mock_demo_pre_public_boundary_review_and_decision
- safe_mock_demo_pre_public_boundary_review_v06296
- safe_mock_demo_initial_path
- safe mock demo
- safe mock demo public artifact promotion candidate
- safe mock demo public artifact promotion
- safe mock demo public positioning
- safe mock demo private artifact boundary
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
- public artifact promotion candidate is not publication approval
- public artifact promotion candidate is not public artifact promotion
- public artifact promotion candidate is not runtime demo readiness
- public artifact promotion candidate is not scanner readiness
- public artifact promotion candidate is not production readiness
- No private generated outputs are moved public in v0.6.298.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
