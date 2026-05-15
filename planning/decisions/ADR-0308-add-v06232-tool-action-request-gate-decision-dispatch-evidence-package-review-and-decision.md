# ADR-0308: Accept Tool Action Request / Gate Decision / Dispatch Evidence Package Candidate for Future Planning

Status: accepted  
Date: 2026-05-15  
Version: v0.6.232

## Context

v0.6.231 created a documentation-only candidate package shape for `tool_action_request_gate_decision_dispatch_evidence_package`. The candidate package shape connected model output reference, tool action request, gate decision, dispatch or non-dispatch decision, execution or non-execution result, evidence event, reviewer reconstruction path, and AAEF five questions mapping reference.

## Decision

Accept the v0.6.231 candidate package shape for future fixture and record planning.

~~~text
package_candidate_review_completed = true
package_candidate_accepted = true
package_candidate_review_result = accepted_for_future_fixture_and_record_planning
package_candidate_status = accepted_for_future_fixture_and_record_planning
package_candidate_applied = false
~~~

The accepted package boundary is not applied in v0.6.232. No fixtures, actual records, reviewer walkthrough, AAEF five questions mapping, AAEF handback summary, runtime behavior, scanner behavior, publication approval, or public announcement are created.

## Decision record

~~~text
package_candidate_review_completed = true
package_candidate_accepted = true
package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231
package_candidate_review_result = accepted_for_future_fixture_and_record_planning
package_candidate_status = accepted_for_future_fixture_and_record_planning
package_candidate_applied = false
selected_work_item = tool_action_request_gate_decision_dispatch_evidence_package
selected_work_item_status = accepted_package_boundary_for_future_planning
accepted_package_boundary = tool_action_request_gate_decision_dispatch_evidence_package
accepted_package_boundary_application_status = not_applied
minimum_flow_package_created = false
package_implementation_created = false
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

A later checkpoint can select whether to proceed toward fixture planning, record planning, reviewer walkthrough planning, or another narrow planning item.

## Boundaries

Model output is not authority. AI rationale is not authorization. A gate decision is not AI self-approval. Evidence supports reconstruction; it does not prove legal truth. Validator success is structural only.

Runtime demo remains necessary but deferred. Publication remains deferred. No private generated outputs are moved public in v0.6.232.
