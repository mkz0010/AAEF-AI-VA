# ADR-0006: Define credential_ref lifecycle and visibility boundaries

## Status

Accepted

## Context

The project needs to support authenticated vulnerability assessment without exposing raw credentials or secrets to AI systems.

Earlier project documents introduced the credential_ref concept. However, the design needs clearer lifecycle rules, visibility boundaries, and component responsibilities before a prototype is implemented.

## Decision

The project will treat credential_ref as a reference-only identifier that is visible to AI but not sufficient to access secrets.

A credential_ref may be resolved only by Tool Gateway after a valid AAEF authorization decision.

The raw secret value remains AI-hidden and is stored in Vault or a local mock Vault for MVP.

The lifecycle of credential_ref is:

1. create,
2. authorize use,
3. resolve,
4. inject,
5. execute,
6. sanitize,
7. record evidence,
8. revoke or expire.

## Visibility Boundary

AI-visible:

- credential_ref,
- target_id,
- scope_id,
- tool,
- operation,
- auth_profile,
- allowed and prohibited action metadata,
- sanitized result summaries.

AI-hidden:

- username,
- password,
- session cookie,
- API key,
- bearer token,
- VPN credential,
- MFA seed,
- raw authorization headers,
- unredacted cookies,
- raw secret values.

## Component Responsibilities

### AAEF Authorization Gateway

Determines whether a requested tool action may use a credential_ref.

### Tool Gateway

Resolves credential_ref after authorization and injects the secret into the approved tool runtime.

### Vault / Mock Vault

Stores raw secret values and denies direct AI access.

### Sanitizer / Normalizer

Prevents raw secrets and sensitive response data from being returned to AI.

### Evidence Store

Records credential_ref usage and execution traceability without exposing raw secrets.

## Consequences

- AI can participate in authenticated assessment planning without seeing credentials.
- Tool Gateway and Vault become trusted control components.
- Sanitization is mandatory before AI receives tool output.
- Evidence records must distinguish credential_ref from raw secrets.
- The MVP can demonstrate the pattern with a mock Vault before integrating production-grade secret management.
