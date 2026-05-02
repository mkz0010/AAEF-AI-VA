# ADR-0036: Add bounded execution transition candidate before local execution plan

## Status

Accepted

## Context

v0.2.2 binds controlled local runtime readiness and local target lab profile through a scope-registry-style runtime destination binding.

The next step is to structure the conditions required before any future local-only execution plan can be considered.

Runtime-target binding must still not authorize execution.

## Decision

Add bounded execution transition candidate and gate.

The candidate records prerequisites for future local-only execution planning, including no-egress controls, timeout, kill-switch, operation allowlist, human approval, raw artifact capture boundary, sanitizer binding, and evidence generation.

The candidate and gate keep scan execution, network activity, real execution, process execution, credential injection, and raw artifact capture disabled.

## Consequences

- The transition toward execution remains structured and gated.
- The project gains an explicit bridge from runtime-target binding to future local-only execution planning.
- Execution is still not allowed.
- Future v0.2.x work can focus on local-only execution plan review.
