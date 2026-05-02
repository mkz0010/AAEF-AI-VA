# Human Approval Record and Gate

## Purpose

This document defines the first human approval record and approval gate for the AAEF-controlled AI Vulnerability Assessment Platform.

The operator readiness review explains why real execution is blocked and what actions are needed. The next step is to record an explicit human approval decision without allowing that decision to bypass other execution controls.

## Core Principle

Human approval is not sufficient authority for real execution by itself.

Human approval must be bound to:

- command plan ID,
- tool,
- operation,
- target ID,
- scope ID,
- approval scope,
- expiration,
- evidence requirement.

Even an `approved` record does not permit real execution in the current MVP.

## Approval Decisions

The MVP supports:

- `approved`
- `rejected`
- `needs_more_info`
- `keep_blocked`

The default generated decision is:

~~~text
keep_blocked
~~~

## MVP Safety Boundary

In the current MVP, every approval record must keep:

~~~text
real_execution_allowed: false
evidence_required: true
~~~

This means approval records can validate the review workflow without enabling real tool execution.

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/human-approvals/demo/
~~~

Generated files:

- `human-approval-record.generated.json`
- `human-approval-gate-result.generated.json`
- `human-approval-record.generated.md`

## Example Command

~~~bash
py tools/generate_human_approval_record.py
~~~

You can also generate an approved record for workflow testing:

~~~bash
py tools/generate_human_approval_record.py approved
~~~

Even with `approved`, real execution remains blocked in the current MVP.

## Fail-Closed Conditions

The approval gate fails closed when:

- required fields are missing,
- approval decision is unsupported,
- approval scope does not match the operator summary,
- command plan ID does not match,
- target ID does not match,
- scope ID does not match,
- tool or operation does not match,
- approval is expired,
- evidence is not required,
- `real_execution_allowed` is true in the current MVP.

## Relationship to Readiness Gate

The readiness gate identifies blockers.

The operator review explains blockers.

The human approval record records a human decision.

None of these alone grant real execution authority in the current MVP.

## Future Use

Future versions may bind human approval records to:

- reviewer identity,
- customer authorization reference,
- ticket ID,
- approval expiration,
- scope hash,
- command plan hash,
- runtime readiness result,
- evidence store record,
- SIEM event.

## Relationship to Evidence Chain

Human approval records are linked into the evidence chain with the operator review and approval gate result.

This makes approval decisions reconstructable and prevents approval records from being detached from the command plan they reviewed.

See `docs/29-evidence-chain-review-linkage.md`.

## Relationship to Evidence Reconstruction Report

Human approval records are included in the evidence reconstruction report so that reviewers can see what decision was recorded and whether it permitted execution.

In the current MVP, approval does not permit real execution.

See `docs/30-evidence-reconstruction-report.md`.
