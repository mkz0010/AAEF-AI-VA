# ADR-0004: Use credential_ref for secretless AI tool execution

## Status

Accepted

## Context

Authenticated vulnerability assessment requires credentials, but exposing raw credentials to AI increases confidentiality and NDA risk.

## Decision

AI receives only credential_ref values. Raw secrets are stored in Vault and injected into approved tool runtimes by Tool Gateway after AAEF authorization.

## Consequences

- AI does not directly see credentials.
- Vault and Tool Gateway become trusted control components.
- Tool output sanitization is required before returning data to AI.
- Evidence must record credential_ref usage without exposing raw secrets.
