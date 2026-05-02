# ADR-0018: Add controlled executor policy before real tool execution

## Status

Accepted

## Context

The ZAP adapter can now produce a dry-run command plan.

A future implementation may execute adapter command plans against real tools. Without a separate executor policy, command plans could become a new authority boundary and accidentally permit uncontrolled execution.

## Decision

Add a controlled executor policy layer before real tool execution.

For the current MVP, the executor is dry-run-only and validates command plans without executing external processes.

The executor must fail closed if a command plan requests non-dry-run execution, includes secret material, includes arbitrary command fields, enables destructive tests, enables external discovery, or writes artifacts outside ignored/private paths.

## Consequences

- Real tool integration is delayed until executor rules are explicit.
- Command plans remain internal artifacts rather than execution authority.
- A second boundary is created after adapter planning and before future execution.
- Future tool adapters must satisfy executor policy before execution can be considered.
