# ADR-0282: Add v0.6.212 Gateway Core Safety Integration Plan Candidate

Status: Candidate recorded

## Context

v0.6.211 recorded external review intake and selected `gateway_core_safety_integration_plan` as the next high-risk work item.

The review identified the need to distinguish documented controls, helper implementation, local checks, and Tool Gateway core-path enforcement.

## Decision

Record v0.6.212 as the Gateway Core Safety Integration Plan Candidate.

The candidate plan covers:

- mandatory Gateway core sequence
- mock/dry-run completed status terminology cleanup
- authorization current-time expiry integration
- request/decision constraint-diff integration
- external discovery fail-closed integration
- common target/scope/tool/operation binding
- adapter consistency review
- implementation maturity matrix
- evidence wording cleanup
- public/private commercial material boundary review
- safe demo / mock runtime / controlled runtime PoC separation

## Review boundary

The candidate plan is not accepted by this ADR.

v0.6.213 must review the candidate plan and record whether it is accepted, revised, or rejected.

## Consequences

The repository gains a reviewable plan candidate without changing Tool Gateway behavior, adapter behavior, execution statuses, schemas, validators, fixtures, runtime behavior, or scanner behavior.

runtime demo remains necessary but deferred.

publication remains deferred.
