# ADR-0094: Add v0.6.23 AAEF applied evidence package design

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.22 accepted the AAEF-side applied evidence request and reordered the
next work around a local-lab applied evidence package. The next step is to define the
package structure before generating artifacts or building tool-backed diagnostic
execution.

## Decision

Add a v0.6.23 AAEF applied evidence package design checkpoint.

The checkpoint defines package manifest design, required artifact chain,
`tool_action_request` design, `gate_decision` design, `dispatch_decision` design,
execution/non-execution result design, evidence event design, review summary design,
minimum scenario package set, public/private artifact placement, diagnostic system
build timing, AAEF five questions mapping, structural validator relationship, and
runtime/scanning boundaries.

## Consequences

Positive:

- The applied evidence work now has a concrete package structure.
- Static/mock evidence capture and real local-lab diagnostic capture are separated.
- The project can proceed to scenario planning without overclaiming scanner readiness.
- Public/private and patent-sensitive abstraction boundaries remain explicit.

Negative / deferred:

- This does not generate evidence packages.
- This does not build the local-lab diagnostic system.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
