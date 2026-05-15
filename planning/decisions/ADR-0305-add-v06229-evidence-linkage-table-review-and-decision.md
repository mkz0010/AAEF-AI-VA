# ADR-0305: Accept v0.6.228 Evidence Linkage Table Candidate for Future Package Planning

Status: accepted  
Date: 2026-05-15  
Version: v0.6.229

## Context

v0.6.228 produced an Evidence Linkage Table Candidate for the currently selected minimum-flow scenarios:

- `SCN-001 permitted safe diagnostic`
- `SCN-002 denied out-of-scope request`
- `SCN-003 held / requires human approval`
- `SCN-004 expired-not-executed`

The candidate proposed a linkage structure connecting model output, tool action request, gate decision, dispatch or non-dispatch, execution or non-execution result, evidence event, reviewer walkthrough, and AAEF five questions mapping.

## Decision

The v0.6.228 Evidence Linkage Table Candidate is accepted for future package planning / future record planning.

The table is not applied in v0.6.229. No minimum flow package, fixtures, evidence linkage records, tool action request records, gate decision records, dispatch records, execution result records, non-execution result records, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.

## Decision record

~~~text
evidence_linkage_table_accepted = true
evidence_linkage_table_applied_to_package = false
minimum_flow_package_created = false
fixtures_created = false
fixtures_modified = false
evidence_linkage_records_created = false
tool_action_request_records_created = false
gate_decision_records_created = false
dispatch_evidence_records_created = false
execution_result_records_created = false
non_execution_result_records_created = false
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

The accepted table can be used by a later checkpoint to plan the first package-level artifact that links tool action requests, gate decisions, dispatch or non-dispatch evidence, and execution or non-execution outcomes.

The next likely checkpoint is v0.6.230 Next Work Selection Using Risk-Tiered Granularity. The expected candidate work item is `tool_action_request_gate_decision_dispatch_evidence_package`, but the selection is deferred to v0.6.230.

## Boundaries

Model output is not authority. AI rationale is not authorization. A gate decision is not AI self-approval. Evidence supports reconstruction; it does not prove legal truth. Validator success is structural only.

Runtime demo remains necessary but deferred. Publication remains deferred. No private generated outputs are moved public in v0.6.229.
