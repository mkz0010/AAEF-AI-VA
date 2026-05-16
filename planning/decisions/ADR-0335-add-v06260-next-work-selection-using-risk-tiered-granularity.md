# ADR-0335: Select Read-Only Symbol-Level Tracing Pass Candidate as Next Work Item

Status: accepted  
Date: 2026-05-16  
Version: v0.6.260

## Context

v0.6.259 accepted the v0.6.258 Symbol-Level Tracing Planning Candidate for a future read-only symbol-level tracing pass.

The next step is to select whether to proceed with a read-only symbol-level tracing pass candidate, a narrower symbol trace inventory, or a code-inspection report candidate.

## Decision

Select the following next work item:

~~~text
read_only_symbol_level_tracing_pass_candidate
~~~

This is a selection-only checkpoint. No read-only symbol-level tracing pass candidate artifact, symbol-level tracing result, accepted defect record, code-inspection report, verification report, gateway behavior change, adapter behavior change, schema behavior change, runtime behavior change, scanner behavior change, fixture, record candidate artifact, actual record, README front-page rewrite, repository metadata change, publication approval, or public announcement is created in v0.6.260.

## Decision record

~~~text
next_work_selection_completed = true
selected_work_item = read_only_symbol_level_tracing_pass_candidate
selected_work_item_status = selected_for_next_candidate_checkpoint
selected_work_item_reason = accepted_symbol_level_tracing_plan_requires_read_only_pass_candidate_before_results_or_report
read_only_symbol_level_tracing_pass_candidate_selected = true
read_only_symbol_level_tracing_pass_candidate_created = false
read_only_symbol_level_tracing_pass_performed = false
read_only_symbol_level_tracing_results_created = false
symbol_level_tracing_selected = false
symbol_level_tracing_performed = false
symbol_level_tracing_completed = false
symbol_level_tracing_results_created = false
accepted_defect_records_created = false
narrower_symbol_trace_inventory_selected = false
narrower_symbol_trace_inventory_created = false
code_inspection_report_candidate_selected = false
code_inspection_report_candidate_created = false
code_inspection_report_created = false
gateway_path_integration_verification_report_selected = false
gateway_path_integration_verification_report_created = false
gateway_behavior_implementation_change_selected = false
candidate_findings_accepted_as_defects = false
candidate_findings_accepted_as_integration_proof = false
candidate_findings_accepted_as_missing_integration_proof = false
candidate_findings_accepted_for_implementation_change = false
gateway_execution_path_behavior_modified = false
tool_gateway_behavior_changed = false
adapter_behavior_changed = false
schema_changed = false
runtime_behavior_changed = false
scanner_behavior_changed = false
record_candidate_artifacts_created = false
actual_records_created = false
fixtures_created = false
readme_front_page_rewritten = false
repository_metadata_changed = false
publication_approval = false
production_readiness_claim = false
certification_claim = false
legal_compliance_claim = false
audit_opinion_claim = false
diagnostic_completeness_claim = false
external_framework_equivalence_claim = false
~~~

## Boundaries

Model output is not authority. AI rationale is not authorization. A gate decision is not AI self-approval. Evidence supports reconstruction; it does not prove legal truth. Validator success is structural only.

Runtime demo remains necessary but deferred. Publication remains deferred. Read-only symbol-level tracing pass candidate selection is not symbol-level tracing. Planned symbol candidates are not observed symbols. Planned call paths are not observed call paths. No private generated outputs are moved public in v0.6.260.
