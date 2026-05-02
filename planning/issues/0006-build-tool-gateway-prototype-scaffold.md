# 0006: Build Tool Gateway prototype scaffold

## Status

In Progress

## Priority

P0

## Type

Prototype

## Background

MVP schema contracts are now defined. The next step is to prepare a prototype scaffold and example contract flows so that implementation can start from stable examples.

## Decision Summary

Create Tool Gateway prototype scaffold and example JSON flows for:

- allowed action,
- denied action,
- human-approval-required action.

The examples should validate against the MVP schema contracts and must not contain raw secrets or real customer data.

## Acceptance Criteria

- Tool Gateway prototype directory is created
- allowed-action example flow is added
- denied-action example flow is added
- human-approval-required example flow is added
- example validation script is added
- examples validate against MVP schema contracts
- examples contain no raw credentials
- examples demonstrate credential_ref as reference only
- examples demonstrate blocked and review-gated behavior

## Related Documents

- docs/13-tool-gateway-mvp-design.md
- docs/14-mvp-schemas.md
- docs/12-credential-ref-flow.md
- planning/issues/0005-define-mvp-schema-contracts.md

## Remaining Work

- Implement minimal Tool Gateway Python runner.
- Implement authorization binding checks.
- Implement mock Vault behavior.
- Implement mock adapter dispatch.
- Implement evidence emission from runner output.
