# ADR-0012: Validate credential_ref against mock Vault metadata

## Status

Accepted

## Context

The project has defined credential_ref as a reference-only value visible to AI. The first mock runner validated request and authorization binding, but credential_ref still needed stronger validation against trusted metadata.

If Tool Gateway treats credential_ref only as a matching string between request and decision, the design does not yet prove that the reference is constrained by target, scope, tool, operation, expiry, and revocation.

## Decision

Add mock Vault metadata validation to the Tool Gateway mock runner.

For allowed actions that require credential_ref resolution, Tool Gateway must validate the credential_ref against mock Vault metadata.

The metadata must confirm:

- credential_ref exists,
- target_id matches,
- scope_id matches,
- requested tool is allowed,
- requested operation is allowed,
- credential_ref is not revoked,
- credential_ref has not expired at decision time.

## Rationale

This makes credential_ref a constrained reference rather than a free-form label.

It also better reflects the intended production pattern where Tool Gateway resolves secrets only through a trusted secret store after authorization.

## Consequences

- Tool Gateway now requires mock Vault metadata for allowed credentialed actions.
- Negative tests cover missing, unknown, mismatched, revoked, and expired credential_ref cases.
- The mock Vault metadata remains secretless and safe to commit.
- Real secrets must continue to stay outside Git.
