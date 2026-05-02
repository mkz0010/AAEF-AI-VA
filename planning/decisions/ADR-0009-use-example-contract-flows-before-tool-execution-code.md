# ADR-0009: Use example contract flows before implementing Tool Gateway execution code

## Status

Accepted

## Context

The project has defined Tool Gateway responsibilities and MVP schema contracts.

Before implementing execution code, the project needs concrete examples showing how request, authorization, execution result, and evidence records connect.

## Decision

Create example contract flows before implementing the Tool Gateway runner.

The initial example flows are:

- allowed action,
- denied action,
- human-approval-required action.

These examples must validate against MVP schemas and must not contain raw secrets or real customer data.

## Rationale

Example contract flows reduce ambiguity and help implementation proceed safely.

They also demonstrate that AI-generated requests are not authority:

- allowed action is executed only after authorization,
- denied action is blocked,
- human-approval-required action is not automatically executed.

## Consequences

- Prototype implementation can be tested against stable examples.
- Schema drift becomes easier to detect.
- The project can demonstrate the control model before integrating real tools.
