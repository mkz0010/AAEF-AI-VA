# ADR-0046: Add preflight evidence validation rules

## Status

Accepted

## Context

v0.3.2 added representative generated preflight evidence examples.

The next step is to define rules that validate generated examples without treating them as live evidence or satisfying preflight.

## Decision

Add v0.3.3 preflight evidence validation rules.

The rules validate generated example boundaries, fail-closed behavior, authorization and preflight boundaries, AI visibility, raw artifact constraints, sanitized summary requirements, representative coverage, and runtime execution boundary.

The rules may pass for generated examples while keeping live evidence validation false, preflight unsatisfied, execution authorization false, runtime enforcement unimplemented, and runtime execution disabled.

## Consequences

- Generated examples now have explicit validation rules.
- Future negative examples and live evidence validation can build on this layer.
- The project preserves the distinction between example validation and live evidence validation.
- Execution remains blocked.
