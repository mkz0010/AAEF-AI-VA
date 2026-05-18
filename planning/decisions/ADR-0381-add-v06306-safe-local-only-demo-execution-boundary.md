# ADR-0381: Define Safe Local-Only Demo Execution Boundary

Status: defined, not runtime-applied  
Date: 2026-05-18  
Version: v0.6.306

## Context

v0.6.305 accepted the Safe Local-Only Demo Execution Boundary Candidate.

## Decision

Define the Safe Local-Only Demo Execution Boundary as a documentation-level boundary.

## Decision record

~~~text
safe_local_only_demo_execution_boundary_defined = true
safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306
safe_local_only_demo_execution_boundary_status = defined_not_runtime_applied
safe_local_only_demo_execution_boundary_scope = documentation_level_localhost_only_demo_boundary
safe_local_only_demo_execution_boundary_candidate_review_completed = true
safe_local_only_demo_execution_boundary_candidate_accepted = true
safe_local_only_demo_execution_boundary_candidate_id = safe_local_only_demo_execution_boundary_candidate_v06304
safe_local_only_demo_execution_boundary_candidate_review_result = accepted_as_safe_local_only_boundary_candidate
safe_local_only_demo_execution_boundary_target_mode = localhost_only
safe_local_only_demo_execution_boundary_loopback_targets_defined = true
safe_local_only_demo_execution_boundary_allowed_targets_defined = true
safe_local_only_demo_execution_boundary_denied_targets_defined = true
safe_local_only_demo_execution_boundary_external_targets_blocked = true
safe_local_only_demo_execution_boundary_private_lan_targets_blocked = true
safe_local_only_demo_execution_boundary_public_ip_targets_blocked = true
safe_local_only_demo_execution_boundary_non_localhost_dns_targets_blocked = true
safe_local_only_demo_execution_boundary_customer_or_third_party_targets_blocked = true
safe_local_only_demo_execution_boundary_production_targets_blocked = true
safe_local_only_demo_execution_boundary_external_discovery_blocked = true
safe_local_only_demo_execution_boundary_credential_use_blocked = true
safe_local_only_demo_execution_boundary_ai_only_target_selection_blocked = true
safe_local_only_demo_execution_boundary_tool_mode = mock_first_no_live_scanner_default
safe_local_only_demo_execution_boundary_tool_allowlist_defined = true
safe_local_only_demo_execution_boundary_no_live_scanner_default_defined = true
safe_local_only_demo_execution_boundary_preflight_requirements_defined = true
safe_local_only_demo_execution_boundary_fail_closed_conditions_defined = true
safe_local_only_demo_execution_boundary_evidence_outputs_defined = true
safe_local_only_demo_execution_boundary_operator_review_defined = true
safe_local_only_demo_execution_boundary_human_approval_requirement_defined = true
safe_local_only_demo_execution_boundary_runtime_transition_conditions_defined = true
safe_local_only_demo_execution_boundary_external_authorization_boundary_defined = true
safe_local_only_demo_execution_boundary_runtime_applied = false
safe_local_only_demo_execution_boundary_applied = false
safe_local_only_demo_execution_boundary_review_completed = false
safe_local_only_demo_execution_boundary_accepted = false
safe_local_only_demo_execution_boundary_review_and_decision_created = false
safe_local_only_runnable_demo_path_selected = false
safe_local_only_runnable_demo_path_created = false
safe_local_only_runnable_demo_ready = false
safe_local_only_runnable_demo_review_completed = false
safe_mock_demo_public_artifact_promotion_review_completed = true
safe_mock_demo_public_artifact_promotion_accepted = true
safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md
safe_mock_demo_status = runnable_private_artifact_demo_available
safe_mock_demo_is_live_scanner_execution = false
safe_mock_demo_private_artifacts_remain_private = true
publication_approval_selected = false
publication_approval = false
public_announcement = deferred
private_generated_outputs_moved_public = false
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
external_target_authorization = false
runtime_readiness_status = not_detected_execution_blocked
target_lab_gate_status = target_defined_execution_blocked
runtime_destination_binding_status = bound_execution_blocked
bounded_execution_transition_status = candidate_recorded_execution_blocked
preflight_satisfied = false
concrete_checks_implemented = false
live_evidence_records_generated = false
runtime_enforcement_implemented = false
recommended_next_work_item = safe_local_only_demo_execution_boundary_review_and_decision
safe_local_only_demo_execution_boundary_review_and_decision_recommended = true
safe_local_only_demo_execution_boundary_recommended = false
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

The project should next review and decide whether to accept this boundary definition. Boundary runtime application, runnable demo path creation, runtime readiness, scanner readiness, execution authorization, and real execution remain deferred.

## Boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- safe local-only demo execution boundary is not execution authorization
- safe local-only demo execution boundary is not runtime-applied enforcement
- safe local-only demo execution boundary is not runnable demo readiness
- safe local-only demo execution boundary is not external target authorization
- No private generated outputs are moved public in v0.6.306.

## Structural token coverage

- safe_local_only_demo_execution_boundary
- safe_local_only_demo_execution_boundary_v06306
- safe_local_only_demo_execution_boundary_review_and_decision
- safe_local_only_demo_execution_boundary_candidate_v06304
- safe_local_only_demo_execution_boundary_candidate_review_and_decision
- safe_local_only_runnable_demo_path
- localhost_only
- loopback-only target boundary
- mock_first_no_live_scanner_default
- external target authorization remains false
- safe_mock_demo_public_artifact
- docs/public-artifacts/safe-mock-demo-public-artifact.md
- safe mock demo
- safe local-only demo execution boundary
- safe local-only runnable demo path
- safe mock demo is not live scanner execution
- private-not-in-git
- allowed-action: completed
- denied-action: blocked
- human-approval-required: requires_human_approval
- real scanner execution remains blocked
- runtime readiness status: not_detected_execution_blocked
- target lab gate status: target_defined_execution_blocked
- binding gate status: bound_execution_blocked
- transition gate status: candidate_recorded_execution_blocked
- execution authorized: False
- real execution permitted: False
- safe local-only demo execution boundary is not execution authorization
- safe local-only demo execution boundary is not runtime-applied enforcement
- safe local-only demo execution boundary is not runnable demo readiness
- safe local-only demo execution boundary is not scanner readiness
- safe local-only demo execution boundary is not production readiness
- safe local-only demo execution boundary is not external target authorization
- No private generated outputs are moved public in v0.6.306.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
