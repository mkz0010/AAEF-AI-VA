# Evidence Chain Review Linkage

## Purpose

This document defines the first evidence chain and review decision linkage model for the AAEF-controlled AI Vulnerability Assessment Platform.

The project now has request, authorization, execution result, evidence, readiness review, human approval, and approval gate objects.

v0.1.21 links these objects into a reconstruction chain.

## Core Principle

A diagnostic action must be reconstructable.

The platform should be able to explain:

- what was requested,
- what was authorized,
- what happened,
- what evidence was generated,
- why real execution was blocked,
- what the operator reviewed,
- what human decision was recorded,
- whether real execution was permitted.

## Chain Objects

The MVP evidence chain links:

~~~text
tool_action_request
  ↓
authorization_decision
  ↓
tool_execution_result
  ↓
evidence_record
  ↓
operator_readiness_review
  ↓
human_approval_record
  ↓
human_approval_gate_result
~~~

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/evidence-chains/demo/
~~~

Generated files:

- `evidence-chain.generated.json`
- `evidence-chain.generated.md`

## Example Command

~~~bash
py tools/generate_evidence_chain_review.py
~~~

You can also generate a chain using an approved approval record for workflow testing:

~~~bash
py tools/generate_evidence_chain_review.py approved
~~~

Even with an approved human approval record, real execution remains blocked in the current MVP.

## Validation

The chain validates that:

- request ID matches across request, authorization, result, and evidence,
- authorization decision ID matches result and evidence,
- tool execution ID matches evidence,
- target/scope/tool/operation are consistent,
- operator review and human approval bind to the same command plan,
- human approval gate binds to the approval record,
- secrets were not exposed to AI,
- evidence is required,
- real execution is not permitted in the current MVP.

## Fail-Closed Conditions

Evidence chain construction fails closed when:

- required objects are missing,
- IDs do not match,
- target/scope/tool/operation mismatch,
- evidence does not match execution result,
- human approval does not match operator review,
- human approval gate permits real execution,
- secret exposure flag is true.

## Relationship to Future Auditability

This chain is the basis for later:

- evidence reconstruction reports,
- customer-facing assessment traceability,
- internal review logs,
- audit support,
- readiness review packets,
- incident reconstruction.

## Relationship to Evidence Reconstruction Report

The evidence chain provides structure.

The evidence reconstruction report turns that structure into a human-readable explanation of the action, review, approval, and real-execution blocking status.

See `docs/30-evidence-reconstruction-report.md`.
