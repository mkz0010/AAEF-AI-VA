# ADR-0023: Add evidence chain and review decision linkage

## Status

Accepted

## Context

The platform now has separate records for tool requests, authorization decisions, tool execution results, evidence records, operator readiness reviews, human approval records, and approval gate results.

These records need to be linked so that the platform can reconstruct why an action was performed, blocked, reviewed, or approved.

## Decision

Add evidence chain and review decision linkage.

The chain binds request, authorization, execution result, evidence, operator review, human approval, and approval gate records.

The current MVP keeps real execution blocked even when a human approval record is approved.

## Consequences

- Review and evidence objects become reconstructable as a chain.
- Mismatched IDs or scope fields fail closed.
- Human approval cannot be detached from the reviewed command plan.
- Evidence chain output can become the basis for later audit/reconstruction reports.
