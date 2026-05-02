# ADR-0037: Add local-only execution plan review without execution authority

## Status

Accepted

## Context

v0.2.3 introduced a bounded execution transition candidate.

The next step is to describe a local-only execution plan while keeping execution blocked. This plan must not become execution authority.

Only plan-level operations should be allowed. Runtime process launch, ZAP API calls, scans, network activity, credential injection, and raw artifact capture must remain prohibited.

## Decision

Add local-only execution plan review.

The plan allows only `runtime_detection` and `health_check_plan_only` as plan-level operations.

The plan and review gate keep real execution, external process execution, network activity, scans, credential injection, raw artifact capture, customer targets, and external network targets disabled.

## Consequences

- The project gains a structured execution planning layer.
- Future execution work is narrowed to explicit allowlisted operation categories.
- ZAP runtime operation remains disabled.
- Future v0.2.x work can define no-egress, timeout, kill-switch, and health-check design.
