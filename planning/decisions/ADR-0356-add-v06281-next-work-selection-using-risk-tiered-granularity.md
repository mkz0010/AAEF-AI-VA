# ADR-0356: Select Continued Follow-Up Trace Candidate as Next Work Item

Status: accepted  
Date: 2026-05-16  
Version: v0.6.281

## Context

v0.6.280 accepted the Continued Follow-Up Trace Planning Candidate for future continued planning and recommended `continued_follow_up_trace_candidate`.

## Decision

Select the following next work item:

~~~text
continued_follow_up_trace_candidate
~~~

This is a selection-only checkpoint.

## Decision record

~~~text
next_work_selection_completed = true
selected_work_item = continued_follow_up_trace_candidate
selected_work_item_status = selected_for_next_continued_follow_up_trace_candidate_checkpoint
continued_follow_up_trace_candidate_selected = true
continued_follow_up_trace_candidate_created = false
continued_follow_up_trace_candidate_completed = false
continued_follow_up_trace_planning_candidate_review_completed = true
continued_follow_up_trace_planning_candidate_accepted = true
continued_follow_up_trace_planning_candidate_id = continued_follow_up_trace_planning_candidate_v06279
continued_follow_up_trace_planning_candidate_review_result = accepted_for_future_continued_follow_up_trace_planning
future_continued_follow_up_trace_planning_accepted = true
future_continued_follow_up_trace_planning_candidate_decision_options_accepted = true
continued_follow_up_trace_candidate_recommended = true
continued_follow_up_trace_records_created = false
continued_follow_up_trace_results_created = false
continued_follow_up_trace_dispositions_created = false
continued_follow_up_trace_gap_triage_created = false
continued_follow_up_trace_conclusions_created = false
continued_follow_up_trace_report_findings_created = false
accepted_defect_records_created = false
accepted_defect_records_accepted = false
code_inspection_report_candidate_created = false
code_inspection_report_created = false
gateway_path_integration_verification_report_candidate_created = false
gateway_path_integration_verification_report_created = false
implementation_change_required_count = 0
continued_follow_up_trace_candidate_accepted_as_defect_planning = false
continued_follow_up_trace_candidate_accepted_as_report_scope = false
continued_follow_up_trace_candidate_accepted_as_integration_proof = false
continued_follow_up_trace_candidate_accepted_as_implementation_change = false
continued_follow_up_trace_records_accepted_as_defects = false
continued_follow_up_trace_results_accepted_as_report_findings = false
continued_follow_up_trace_dispositions_accepted_as_implementation_change = false
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

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- Continued follow-up trace candidate selection is not continued trace execution.
- Continued follow-up trace candidate selection is not defect acceptance.
- Continued follow-up trace candidate selection is not report finding creation.
- Continued follow-up trace candidate selection is not gateway execution path modification.
- No private generated outputs are moved public in v0.6.281.

## Structural token coverage

- continued_follow_up_trace_candidate
- continued_follow_up_trace_candidate_selected
- continued_follow_up_trace_planning_candidate_review_and_decision
- continued_follow_up_trace_planning_candidate_accepted
- continued_follow_up_trace_planning_candidate_v06279
- continued_follow_up_trace_planning
- continued_follow_up_trace_records
- continued_follow_up_trace_results
- continued_follow_up_trace_dispositions
- continued_follow_up_trace_gap_triage
- continued_follow_up_trace_conclusions
- continued_follow_up_trace_report_findings
- next_work_selection_using_risk_tiered_granularity
- report-scope candidate planning
- accepted defect candidate planning
- code-inspection report candidate
- gateway-path integration verification report candidate
- no-action non-claim closeout
- Continued follow-up trace candidate selection is not continued trace execution.
- Continued follow-up trace candidate selection is not defect acceptance.
- Continued follow-up trace candidate selection is not report finding creation.
- Continued follow-up trace candidate selection is not gateway execution path modification.
- No private generated outputs are moved public in v0.6.281.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
