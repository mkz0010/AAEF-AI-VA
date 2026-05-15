# ADR-0310: Create Future Record Planning Candidate

Status: proposed candidate  
Date: 2026-05-15  
Version: v0.6.234

## Context

v0.6.233 selected `future_record_planning` as the next work item after v0.6.232 accepted the `tool_action_request_gate_decision_dispatch_evidence_package` boundary for future fixture and record planning.

The next step is to create a documentation-only candidate plan for future record groups before creating fixtures or actual records.

## Decision

Create a documentation-only future record planning candidate:

~~~text
record_planning_candidate_id = future_record_planning_candidate_v06234
record_planning_candidate_status = candidate_not_applied
record_planning_candidate_scope = documentation_only_record_planning
~~~

The candidate plans future record groups for model output reference, tool action request, gate decision, dispatch decision, non-dispatch decision, execution result, non-execution result, evidence event, reviewer reconstruction reference, and AAEF five questions mapping reference.

## Decision record

~~~text
record_planning_candidate_created = true
record_planning_candidate_id = future_record_planning_candidate_v06234
record_planning_candidate_status = candidate_not_applied
record_planning_candidate_scope = documentation_only_record_planning
selected_work_item = future_record_planning
selected_work_item_status = future_record_planning_candidate_created
accepted_package_boundary = tool_action_request_gate_decision_dispatch_evidence_package
accepted_package_boundary_application_status = not_applied_to_records
future_record_groups_planned = true
actual_records_created = false
records_created = false
minimum_flow_package_created = false
package_implementation_created = false
fixtures_created = false
fixtures_modified = false
evidence_linkage_records_created = false
model_output_reference_records_created = false
tool_action_request_records_created = false
gate_decision_records_created = false
dispatch_decision_records_created = false
non_dispatch_decision_records_created = false
dispatch_evidence_records_created = false
non_dispatch_evidence_records_created = false
execution_result_records_created = false
non_execution_result_records_created = false
evidence_event_records_created = false
reviewer_reconstruction_reference_records_created = false
aaef_five_questions_mapping_reference_records_created = false
reviewer_walkthrough_created = false
aaef_five_questions_mapping_created = false
aaef_handback_summary_created = false
private_generated_outputs_moved_public = false
public_exposure_cleanup_applied = false
readme_front_page_rewritten = false
gateway_core_safety_controls_implemented = false
tool_gateway_behavior_changed = false
adapter_behavior_changed = false
execution_status_renamed = false
schema_changed = false
validator_behavior_changed = false
fixture_semantics_changed = false
runtime_behavior_changed = false
scanner_behavior_changed = false
runtime_demo_ready = false
scanner_readiness_claim = false
external_poc_readiness_claim = false
publication_approval = false
public_announcement = deferred
social_post_publication = deferred
commercial_terms_created = false
production_readiness_claim = false
certification_claim = false
legal_compliance_claim = false
audit_opinion_claim = false
diagnostic_completeness_claim = false
external_framework_equivalence_claim = false
~~~

## Consequences

A later checkpoint can review whether this future record planning candidate should be accepted for future fixture planning and record candidate planning.

## Boundaries

Model output is not authority. AI rationale is not authorization. A gate decision is not AI self-approval. Evidence supports reconstruction; it does not prove legal truth. Validator success is structural only.

Runtime demo remains necessary but deferred. Publication remains deferred. No private generated outputs are moved public in v0.6.234.
