# 0007: Build Tool Gateway mock runner

## Status

In Progress

## Priority

P0

## Type

Prototype

## Background

The project has MVP schema contracts and example contract flows.

The next step is to implement a minimal Tool Gateway mock runner that consumes example requests and authorization decisions, validates binding, and emits generated execution and evidence records.

## Decision Summary

Implement a standard-library-only Python mock runner.

The runner will:

- load a tool_action_request,
- load an authorization_decision,
- validate request/decision binding,
- emit a tool_execution_result,
- emit an evidence_record,
- write generated outputs under `private-not-in-git/prototype-runs/`.

## Acceptance Criteria

- allowed-action returns completed
- denied-action returns blocked
- human-approval-required returns requires_human_approval
- runner does not execute real tools
- runner does not resolve raw secrets
- generated records keep `secret_exposed_to_ai` false
- generated outputs are written under ignored local private area
- implementation uses only Python standard library

## Related Documents

- docs/13-tool-gateway-mvp-design.md
- docs/14-mvp-schemas.md
- docs/15-tool-gateway-prototype-examples.md
- planning/issues/0006-build-tool-gateway-prototype-scaffold.md

## Remaining Work

- Validate generated output against schemas.
- Add explicit negative tests for mismatched authorization.
- Add mock Vault metadata behavior.
- Add adapter stubs for ZAP, Nmap, and nuclei.
