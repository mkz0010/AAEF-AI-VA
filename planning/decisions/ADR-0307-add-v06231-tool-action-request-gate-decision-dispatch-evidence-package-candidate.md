# ADR-0307: Create Tool Action Request / Gate Decision / Dispatch Evidence Package Candidate Shape

Status: proposed candidate  
Date: 2026-05-15  
Version: v0.6.231

## Context

v0.6.230 selected `tool_action_request_gate_decision_dispatch_evidence_package` as the next work item. The project now needs a narrow candidate package shape before creating fixtures, actual records, reviewer walkthrough artifacts, AAEF five questions mapping artifacts, or AAEF handback artifacts.

## Decision

Create a documentation-only candidate package shape:

~~~text
package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231
package_candidate_status = candidate_not_applied
package_candidate_scope = documentation_only_package_shape
~~~

The candidate package shape connects future planning for model output reference, tool action request, gate decision, dispatch or non-dispatch decision, execution or non-execution result, evidence event, reviewer reconstruction path, and AAEF five questions mapping reference.

## Decision record

~~~text
package_candidate_created = true
package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231
package_candidate_status = candidate_not_applied
package_candidate_scope = documentation_only_package_shape
selected_work_item = tool_action_request_gate_decision_dispatch_evidence_package
selected_work_item_status = candidate_package_shape_created
minimum_flow_package_created = false
package_candidate_applied = false
fixtures_created = false
fixtures_modified = false
evidence_linkage_records_created = false
tool_action_request_records_created = false
gate_decision_records_created = false
dispatch_evidence_records_created = false
non_dispatch_evidence_records_created = false
execution_result_records_created = false
non_execution_result_records_created = false
evidence_event_records_created = false
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

A later checkpoint can review this candidate package shape and decide whether it should be accepted for future fixture and record planning.

## Boundaries

Model output is not authority. AI rationale is not authorization. A gate decision is not AI self-approval. Evidence supports reconstruction; it does not prove legal truth. Validator success is structural only.

Runtime demo remains necessary but deferred. Publication remains deferred. No private generated outputs are moved public in v0.6.231.
