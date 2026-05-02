# ADR-0033: Add controlled local runtime readiness without execution

## Status

Accepted

## Context

v0.1.30 established a lifecycle integration checkpoint with real execution, network activity, customer delivery, and report-ready status disabled.

The next phase should move toward local runtime integration carefully.

Before any real tool execution, the platform needs a runtime readiness gate that can detect runtime availability while keeping execution blocked.

## Decision

Add controlled local ZAP runtime readiness.

The readiness gate may detect candidate ZAP binaries, but it must not execute ZAP, spawn external processes, perform network activity, inject credentials, or capture raw artifacts.

## Consequences

- v0.2.0 begins the transition toward controlled local runtime integration.
- Runtime detection is explicitly separated from execution authority.
- Existing safety invariants remain intact.
- Future bounded execution work has a safer readiness layer to build on.
