# ADR-0044: Add preflight evidence record model

## Status

Accepted

## Context

v0.3.0 defined concrete preflight check implementation scaffolds with input sources, evidence types, responsibilities, and fail-closed behavior.

The next step is to define the evidence record model each preflight check will eventually generate.

The model must remain separate from generated evidence, check satisfaction, preflight satisfaction, and execution authorization.

## Decision

Add v0.3.1 preflight evidence record model.

Each required preflight check gets an evidence record model with evidence type, input sources, fail-closed behavior, validation result, failure mode, AI visibility boundary, raw artifact capture boundary, and sanitized summary requirement.

The model keeps evidence records not generated, checks unsatisfied, preflight unsatisfied, execution authorization false, runtime enforcement unimplemented, and runtime execution disabled.

## Consequences

- Future generated preflight evidence work has a stable record shape.
- AI visibility and raw artifact boundaries are defined early.
- Preflight evidence remains non-authoritative by itself.
- Execution remains blocked.
