# ADR-0367: Accept Safe Mock Demo Initial Path Hardening

Status: accepted
Date: 2026-05-17
Version: v0.6.292

## Context

v0.6.291 applied documentation-only hardening to the selected safe mock demo initial path.

## Decision

Accept the v0.6.291 documentation-only safe mock demo initial path hardening.

## Decision record

~~~text
safe_mock_demo_initial_path_hardening_review_completed = true
safe_mock_demo_initial_path_hardening_accepted = true
safe_mock_demo_initial_path_hardening_id = safe_mock_demo_initial_path_hardening_v06291
safe_mock_demo_initial_path_hardening_review_result = accepted_as_documentation_only_safe_mock_demo_path_hardening
safe_mock_demo_initial_path_hardening_status = accepted_as_documentation_only_safe_mock_demo_path_hardening
selected_demo_path = safe_mock_demo_initial_path
safe_mock_demo_initial_path_selected = true
safe_mock_demo_status = runnable_private_artifact_demo_available
safe_mock_demo_is_live_scanner_execution = false
safe_mock_demo_private_artifacts_remain_private = true
safe_mock_demo_command_clarity_accepted = true
safe_mock_demo_expected_status_explanation_accepted = true
safe_mock_demo_private_artifact_boundary_accepted = true
safe_mock_demo_reviewer_walkthrough_boundary_accepted = true
safe_mock_demo_non_live_scanner_warning_accepted = true
safe_mock_demo_local_only_runtime_separation_accepted = true
safe_mock_demo_initial_path_hardening_accepted_as_public_artifact_promotion = false
safe_mock_demo_initial_path_hardening_accepted_as_publication_approval = false
safe_mock_demo_initial_path_hardening_accepted_as_runtime_demo_readiness = false
safe_mock_demo_initial_path_hardening_accepted_as_scanner_readiness = false
safe_mock_demo_initial_path_hardening_accepted_as_production_readiness = false
safe_mock_demo_public_artifact_promotion_created = false
safe_mock_demo_public_artifact_promotion_approved = false
private_generated_outputs_moved_public = false
recommended_next_work_item = next_work_selection_using_risk_tiered_granularity
next_work_selection_recommended = true
runtime_demo_ready = false
runtime_demo_readiness_claim = false
scanner_readiness_claim = false
production_readiness_claim = false
execution_authorized = false
real_execution_permitted = false
local_only_demo_execution_boundary_candidate_created = false
real_scanner_execution_status = blocked
runtime_readiness_status = not_detected_execution_blocked
target_lab_gate_status = target_defined_execution_blocked
runtime_destination_binding_status = bound_execution_blocked
bounded_execution_transition_status = candidate_recorded_execution_blocked
preflight_satisfied = false
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

The project should next select follow-up work using risk-tiered granularity. Publication approval, public artifact promotion, runtime readiness, scanner readiness, and real execution remain deferred.

## Boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- safe mock demo hardening review is not publication approval
- safe mock demo hardening review is not public artifact promotion
- safe mock demo hardening review is not runtime demo readiness
- safe mock demo hardening review is not scanner readiness
- No private generated outputs are moved public in v0.6.292.

## Structural token coverage

- safe_mock_demo_initial_path_hardening_review_and_decision
- safe_mock_demo_initial_path_hardening_review_completed
- safe_mock_demo_initial_path_hardening_accepted
- safe_mock_demo_initial_path_hardening_v06291
- safe_mock_demo_initial_path_hardening
- safe_mock_demo_initial_path
- safe mock demo
- safe mock demo command clarity
- safe mock demo expected status explanation
- safe mock demo private artifact boundary
- safe mock demo reviewer walkthrough boundary
- safe mock demo non-live-scanner warning
- safe mock demo local-only runtime separation
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
- safe mock demo hardening review is not publication approval
- safe mock demo hardening review is not public artifact promotion
- safe mock demo hardening review is not runtime demo readiness
- safe mock demo hardening review is not scanner readiness
- safe mock demo hardening review is not production readiness
- No private generated outputs are moved public in v0.6.292.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
