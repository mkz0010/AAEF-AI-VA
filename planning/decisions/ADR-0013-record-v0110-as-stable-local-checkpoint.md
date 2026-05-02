# ADR-0013: Record v0.1.10 as the stable local checkpoint

## Status

Accepted

## Context

The v0.1.8 and v0.1.9 steps introduced and partially remediated Python escaped docstring syntax issues.

Although tags were created for those versions, validation failed before v0.1.10.

The project needs a clear stable baseline before adding adapter stubs or real tool integration.

## Decision

Treat v0.1.10 as the stable local checkpoint for the Tool Gateway MVP mock runner.

v0.1.8 and v0.1.9 remain in local history as superseded remediation steps.

Future implementation work should branch from v0.1.10 or later.

## Validation Basis

v0.1.10 passed:

- Python compile checks,
- MVP schema validation,
- MVP example validation,
- Tool Gateway mock runner scenarios,
- positive Tool Gateway runner tests,
- fail-closed negative tests,
- credential_ref mock Vault metadata negative tests,
- generated output tests.

## Consequences

- The project avoids rewriting local history unnecessarily.
- The failed intermediate tags are documented rather than hidden.
- Future work has a clear stable baseline.
- A shared local validation command should be used before commits and tags.
