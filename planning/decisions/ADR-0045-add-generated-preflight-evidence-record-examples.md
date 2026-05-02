# ADR-0045: Add generated preflight evidence record examples

## Status

Accepted

## Context

v0.3.1 defined the preflight evidence record model for required preflight checks.

The next step is to provide representative generated examples. These examples should demonstrate fail-closed evidence behavior without becoming live evidence or satisfying preflight.

## Decision

Add v0.3.2 generated preflight evidence record examples.

The representative examples cover runtime readiness, runtime destination binding, execution authorization, no-egress guard, and sanitizer boundary checks.

The examples are generated scaffold artifacts, not live evidence. They keep checks unsatisfied, preflight unsatisfied, execution authorization false, runtime enforcement unimplemented, and runtime execution disabled.

## Consequences

- The evidence record model becomes easier to review and test.
- Future evidence validation and reconstruction work has concrete examples.
- The project keeps example generation separate from live preflight evidence generation.
- Execution remains blocked.
