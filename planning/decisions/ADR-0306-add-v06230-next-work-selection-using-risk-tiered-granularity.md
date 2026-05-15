# ADR-0306: Select Tool Action Request / Gate Decision / Dispatch Evidence Package as Next Work Item

Status: accepted  
Date: 2026-05-15  
Version: v0.6.230

## Context

v0.6.229 accepted the Evidence Linkage Table Candidate for future package planning / future record planning. The next step is to select the smallest useful work item that can move from accepted linkage planning toward package-level artifact planning without creating runtime behavior or scanner-readiness claims.

## Decision

Select the following next work item:

~~~text
tool_action_request_gate_decision_dispatch_evidence_package
~~~

This is a selection-only checkpoint. The selected package is not created in v0.6.230.

## Decision record

~~~text
next_work_selection_completed = true
selected_work_item = tool_action_request_gate_decision_dispatch_evidence_package
selected_work_item_status = selected_for_next_candidate_checkpoint
selection_applied_to_package = false
minimum_flow_package_created = false
package_candidate_created = false
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

The next checkpoint can create a candidate package shape for the selected work item. The candidate package should connect tool action request, gate decision, dispatch or non-dispatch evidence, execution or non-execution result, evidence event, and reviewer reconstruction paths.

## Boundaries

Model output is not authority. AI rationale is not authorization. A gate decision is not AI self-approval. Evidence supports reconstruction; it does not prove legal truth. Validator success is structural only.

Runtime demo remains necessary but deferred. Publication remains deferred. No private generated outputs are moved public in v0.6.230.
