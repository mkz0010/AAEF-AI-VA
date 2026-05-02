# Mock Vault credential_ref Validation

## Purpose

This document describes the MVP mock Vault metadata validation for credential_ref.

The goal is to ensure that credential_ref is not treated as a free-form label. It must be validated against mock Vault metadata before Tool Gateway may resolve it for an allowed action.

## Core Principle

A credential_ref is a constrained reference.

It is visible to AI, but it is not authority and it is not a secret.

Tool Gateway may resolve it only after:

1. AAEF authorization allows the action.
2. The request and decision are bound.
3. Mock Vault metadata confirms the credential_ref is valid for the target, scope, tool, and operation.
4. The credential_ref is not expired or revoked.

## Mock Vault Metadata

The committed MVP metadata file is:

~~~text
prototypes/tool-gateway/mock_vault/metadata.json
~~~

It contains only fictitious metadata.

It must not contain:

- usernames,
- passwords,
- API keys,
- session cookies,
- bearer tokens,
- VPN credentials,
- MFA seeds,
- real customer secrets.

## Validation Checks

Tool Gateway now checks:

- credential_ref exists in mock Vault metadata,
- credential_ref is not revoked,
- target_id matches,
- scope_id matches,
- tool is allowed,
- operation is allowed,
- credential_ref has not expired at decision time.

## Fail-Closed Behavior

The runner must fail closed when:

- mock Vault metadata is missing for an allowed credentialed action,
- credential_ref is unknown,
- target binding differs,
- scope binding differs,
- requested tool is not allowed,
- requested operation is not allowed,
- credential_ref is revoked,
- credential_ref is expired.

## Relationship to AAEF

This extends the AAEF control chain:

~~~text
AI request
  ↓
AAEF authorization decision
  ↓
Tool Gateway binding check
  ↓
mock Vault credential_ref metadata validation
  ↓
secretless mock execution
  ↓
evidence record
~~~

This reinforces the principle:

Model output is not authority.
