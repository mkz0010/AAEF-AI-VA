# ADR-0024: Add evidence reconstruction report

## Status

Accepted

## Context

The platform can now link request, authorization, execution result, evidence, operator review, human approval, and approval gate records into an evidence chain.

The next step is to make that chain understandable to human reviewers.

## Decision

Add an evidence reconstruction report.

The report converts evidence chain and review objects into a human-readable explanation with safety assertions, blockers, next actions, chain nodes, and review questions.

The current MVP report continues to state that real execution is not permitted.

## Consequences

- Evidence chain data becomes reviewable by operators, auditors, and future customers.
- The project gains an explanation artifact, not just linked JSON records.
- Real execution remains blocked.
- The report becomes the basis for future audit and customer-facing reconstruction packages.
