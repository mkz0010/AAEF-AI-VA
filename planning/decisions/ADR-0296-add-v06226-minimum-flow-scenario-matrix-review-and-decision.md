# ADR-0296: Add v0.6.226 Minimum Flow Scenario Matrix Review and Decision

Status: Accepted for evidence linkage planning; not applied

## Context

v0.6.225 recorded the Minimum Flow Scenario Matrix Candidate.

The candidate matrix converted the accepted Existing Element Inventory into four scenario rows for the accepted AAEF Applied Evidence Minimum Flow:

- SCN-001 permitted safe diagnostic
- SCN-002 denied out-of-scope request
- SCN-003 held / requires human approval
- SCN-004 expired-not-executed

## Decision

Accept the v0.6.225 Minimum Flow Scenario Matrix Candidate as the Minimum Flow Scenario Matrix for future evidence linkage planning.

This decision does not apply the matrix to create package artifacts.

## Decision fields

- minimum_flow_scenario_matrix_accepted = true
- minimum_flow_scenario_matrix_applied_to_package = false
- minimum_flow_package_created = false
- fixtures_created = false
- fixtures_modified = false
- evidence_linkage_records_created = false
- tool_action_request_records_created = false
- gate_decision_records_created = false
- dispatch_evidence_records_created = false
- execution_result_records_created = false
- non_execution_result_records_created = false
- reviewer_walkthrough_created = false
- aaef_five_questions_mapping_created = false
- aaef_handback_summary_created = false
- private_generated_outputs_moved_public = false
- public_exposure_cleanup_applied = false
- readme_front_page_rewritten = false
- gateway_core_safety_controls_implemented = false
- tool_gateway_behavior_changed = false
- adapter_behavior_changed = false
- execution_status_renamed = false
- schema_changed = false
- validator_behavior_changed = false
- fixture_semantics_changed = false
- runtime_behavior_changed = false
- scanner_behavior_changed = false
- runtime_demo_ready = false
- scanner_readiness_claim = false
- external_poc_readiness_claim = false
- publication_approval = false
- public_announcement = deferred
- social_post_publication = deferred
- commercial_terms_created = false
- production_readiness_claim = false
- certification_claim = false
- legal_compliance_claim = false
- audit_opinion_claim = false
- diagnostic_completeness_claim = false
- external_framework_equivalence_claim = false

## Consequences

The repository now has an accepted Minimum Flow Scenario Matrix for future evidence linkage planning.

A separate future checkpoint is required before any evidence linkage table, fixture, request, decision, dispatch, result, walkthrough, mapping, or handback artifact is created.

Runtime demo remains necessary but deferred.

Publication remains deferred.
