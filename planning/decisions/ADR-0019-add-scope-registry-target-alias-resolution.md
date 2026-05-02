# ADR-0019: Add scope registry and target alias resolution before real tool execution

## Status

Accepted

## Context

The project currently uses `target_id` values in tool action requests, authorization decisions, command plans, and evidence records.

Before real tools are executed, the project needs a controlled mechanism for resolving target aliases without letting AI decide or construct raw destinations.

## Decision

Add a Tool Gateway-controlled scope registry.

`target_id` values are aliases. They must be resolved through the scope registry before they can appear in adapter command plans.

The current MVP uses fictitious demo entries only and does not include raw customer destinations.

The current dry-run executor requires `network_execution_allowed` to remain false.

## Consequences

- AI can reference approved target aliases without seeing raw destinations.
- Adapter command plans gain target binding metadata.
- The controlled executor can validate target binding before future execution.
- Real target resolution is deferred until storage, egress, approval, and logging rules are defined.
- The project reduces the risk of AI-driven scope expansion or raw destination leakage.
