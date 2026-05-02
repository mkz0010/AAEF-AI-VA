# ADR-0038: Add no-egress, timeout, and kill-switch policy scaffold

## Status

Accepted

## Context

v0.2.4 introduced local-only execution plan review.

Before any future local runtime process launch can be considered, the project needs explicit safety policy requirements for no-egress, timeout, and kill-switch behavior.

These policies must remain non-executing scaffolds until runtime enforcement exists.

## Decision

Add a no-egress, timeout, and kill-switch policy scaffold.

The scaffold records local-only destination constraints, denied destination categories, timeout values, kill-switch modes, process tree termination requirement, evidence requirement, sanitizer requirement, and human approval requirement.

The scaffold and gate keep real execution, external process execution, network activity, scan execution, credential injection, raw artifact capture, customer targets, and external network targets disabled.

## Consequences

- Future runtime enforcement work has explicit policy requirements.
- The project separates safety policy definition from execution authority.
- The no-execution boundary remains intact.
- v0.2.x can next move toward runtime enforcement design without skipping safety prerequisites.
