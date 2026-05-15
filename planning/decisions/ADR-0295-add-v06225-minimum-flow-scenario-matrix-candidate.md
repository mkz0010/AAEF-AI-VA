# ADR-0295: Add v0.6.225 Minimum Flow Scenario Matrix Candidate

Status: Candidate recorded

## Context

v0.6.224 selected `minimum_flow_scenario_matrix` as the next high-risk work item after the accepted Existing Element Inventory.

The accepted inventory identified partially present coverage for permitted, denied, held, and expired-not-executed scenario paths.

## Decision

Record v0.6.225 as the Minimum Flow Scenario Matrix Candidate.

The candidate matrix covers:

- permitted safe diagnostic
- denied out-of-scope request
- held / requires human approval
- expired-not-executed

The candidate matrix is a planning artifact. It does not create fixtures, evidence linkage records, request records, decision records, dispatch records, walkthrough records, mapping records, or handback records.

## Review boundary

The candidate matrix is not accepted by this ADR.

v0.6.226 must review the candidate matrix and record whether it is accepted, revised, or rejected.

## Consequences

The repository gains a reviewable scenario matrix candidate without creating a minimum flow package.

No private generated outputs are moved public.

Runtime demo remains necessary but deferred.

Publication remains deferred.
