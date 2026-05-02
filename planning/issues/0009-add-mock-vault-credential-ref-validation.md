# 0009: Add mock Vault credential_ref validation

## Status

In Progress

## Priority

P0

## Type

Prototype

## Background

credential_ref must be more than a string that appears in both the request and authorization decision.

For the Tool Gateway control boundary to be meaningful, credential_ref must be validated against trusted metadata before it can be resolved for allowed execution.

## Decision Summary

Add mock Vault metadata and validate credential_ref against:

- target_id,
- scope_id,
- allowed tools,
- allowed operations,
- expiry,
- revocation status.

## Acceptance Criteria

- mock Vault metadata file is added without raw secrets
- Tool Gateway validates credential_ref against mock Vault metadata
- allowed-action still completes
- denied-action still blocks
- human-approval-required still pauses
- missing mock Vault metadata fails closed
- unknown credential_ref fails closed
- target mismatch fails closed
- scope mismatch fails closed
- disallowed tool fails closed
- disallowed operation fails closed
- revoked credential_ref fails closed
- expired credential_ref fails closed

## Related Documents

- docs/18-mock-vault-credential-ref-validation.md
- docs/12-credential-ref-flow.md
- docs/13-tool-gateway-mvp-design.md
- planning/decisions/ADR-0012-validate-credential-ref-against-vault-metadata.md

## Remaining Work

- Add mock Vault resolution event records.
- Add adapter stubs for real tool integration.
- Add generated output schema validation.
