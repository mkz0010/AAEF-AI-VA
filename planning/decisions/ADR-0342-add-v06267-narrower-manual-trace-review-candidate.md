# ADR-0342: Create Narrower Manual Trace Review Candidate

Status: proposed candidate  
Date: 2026-05-16  
Version: v0.6.267

## Context

v0.6.266 selected `narrower_manual_trace_review` as the next work item after v0.6.265 accepted the v0.6.264 read-only symbol-level tracing pass as static inspection records.

The next step is to create a documentation-only candidate that defines the future manual trace review scope, inputs, questions, disposition vocabulary, record schema, output fields, and non-claim boundaries.

## Decision

Create a Narrower Manual Trace Review Candidate.

~~~text
narrower_manual_trace_review_candidate_created = true
narrower_manual_trace_review_candidate_id = narrower_manual_trace_review_candidate_v06267
narrower_manual_trace_review_candidate_status = candidate_not_applied
narrower_manual_trace_review_candidate_scope = documentation_only_manual_review_candidate_for_static_symbol_trace_records
selected_work_item = narrower_manual_trace_review
selected_work_item_status = narrower_manual_trace_review_candidate_created
manual_trace_review_lanes_defined = true
manual_trace_review_input_records_defined = true
manual_trace_review_questions_defined = true
manual_trace_review_disposition_vocabulary_defined = true
manual_trace_review_record_schema_defined = true
manual_trace_review_output_fields_defined = true
manual_trace_review_candidate_procedure_defined = true
manual_trace_review_non_claim_boundaries_defined = true
narrower_manual_trace_review_performed = false
narrower_manual_trace_review_completed = false
narrower_manual_trace_review_records_created = false
manual_trace_review_records_created = false
manual_trace_review_results_created = false
accepted_defect_candidate_planning_created = false
accepted_defect_records_created = false
accepted_defect_records_accepted = false
code_inspection_report_candidate_created = false
code_inspection_report_created = false
gateway_path_integration_verification_report_candidate_created = false
gateway_path_integration_verification_report_created = false
gateway_execution_path_behavior_modified = false
tool_gateway_behavior_changed = false
adapter_behavior_changed = false
schema_changed = false
runtime_behavior_changed = false
scanner_behavior_changed = false
record_candidate_artifacts_created = false
actual_records_created = false
fixtures_created = false
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

Runtime demo remains necessary but deferred. Publication remains deferred. Narrower manual trace review candidate is not manual trace review execution. Manual review questions are not manual review conclusions. Gap records are not accepted defects. No private generated outputs are moved public in v0.6.267.

## Structural token coverage

The following exact structural tokens are included for v0.6.267 validator coverage. They do not expand the claim scope of this checkpoint.

- readme_front_page_rewritten = false
- repository_metadata_changed = false
