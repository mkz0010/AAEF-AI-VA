# ADR-0298: Add v0.6.228 Evidence Linkage Table Candidate

Status: Candidate recorded

## Context

v0.6.227 selected `evidence_linkage_table` as the next high-risk work item after the accepted Minimum Flow Scenario Matrix.

The accepted scenario matrix contains four scenario rows:

- SCN-001 permitted safe diagnostic
- SCN-002 denied out-of-scope request
- SCN-003 held / requires human approval
- SCN-004 expired-not-executed

## Decision

Record v0.6.228 as the Evidence Linkage Table Candidate.

The candidate table plans link fields for each scenario:

- model_output_id
- tool_action_request_id
- gate_decision_id
- dispatch_decision_id or non_dispatch_decision_id
- execution_result_id or non_execution_result_id
- evidence_event_id
- reviewer_walkthrough_id
- five_questions_mapping_id

The candidate table is a planning artifact. It does not create fixtures, evidence linkage records, request records, decision records, dispatch records, result records, walkthrough records, mapping records, or handback records.

## Review boundary

The candidate table is not accepted by this ADR.

v0.6.229 must review the candidate table and record whether it is accepted, revised, or rejected.

## Consequences

The repository gains a reviewable evidence linkage table candidate without creating a minimum flow package.

No private generated outputs are moved public.

Runtime demo remains necessary but deferred.

Publication remains deferred.
