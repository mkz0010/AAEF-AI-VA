# ADR-0020: Add real execution readiness gate before enabling real tool execution

## Status

Accepted

## Context

The project is approaching real tool integration. It already has ZAP dry-run command plans, a controlled executor policy, and scope registry target binding.

However, a command plan that passes dry-run executor checks should still not automatically become real execution authority.

## Decision

Add a real execution readiness gate.

The gate evaluates whether required prerequisites for future real execution are present, but current MVP behavior remains dry-run-only.

The default readiness configuration explicitly disables real execution.

## Consequences

- Real execution remains blocked by default.
- Future execution enablement requires explicit readiness configuration.
- Missing runtime, egress, sanitizer, timeout, evidence, target binding, credential injection, or human approval conditions are surfaced as blockers.
- Command plans remain dry-run-only until a future release explicitly changes that behavior.
