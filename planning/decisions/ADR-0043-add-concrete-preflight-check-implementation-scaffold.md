# ADR-0043: Add concrete preflight check implementation scaffold

## Status

Accepted

## Context

v0.2.9 recorded the runtime transition checkpoint. The project is ready for preflight implementation work, but not runtime execution.

The next phase should define implementation scaffolds for each required preflight check without satisfying any check or authorizing execution.

## Decision

Add v0.3.0 concrete preflight check implementation scaffold.

Each required preflight check receives input sources, evidence type, fail-closed behavior, and implementation responsibility.

The scaffold keeps concrete checks unimplemented, preflight unsatisfied, execution authorization false, runtime enforcement unimplemented, and runtime execution disabled.

## Consequences

- v0.3.0 begins concrete preflight implementation planning.
- Future preflight evidence record work has a defined check inventory.
- Execution remains blocked.
- The project continues moving toward controlled runtime execution without skipping preflight evidence design.
