# ADR-0017: Add dry-run command plan for ZAP adapter before real ZAP execution

## Status

Accepted

## Context

The project has adapter stubs and an internal adapter artifact policy.

The next step toward real tool integration is to make the ZAP adapter describe what it would do without actually launching ZAP, connecting to a target, or constructing arbitrary shell commands.

## Decision

Add a dry-run command plan capability to the ZAP adapter.

The command plan will describe approved operation, target, scope, credential_ref, artifact references, planned steps, and blocked behaviors.

The command plan must not include raw secrets and must not execute external processes.

## Consequences

- ZAP integration moves closer to implementation without increasing runtime risk.
- The adapter boundary becomes clearer.
- Future controlled execution can consume structured plans instead of AI-generated shell commands.
- The command plan remains internal adapter output and is not embedded in public generated Tool Gateway result objects.
