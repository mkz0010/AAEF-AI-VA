# ADR-0002: Do not commit raw customer data

## Status

Accepted

## Context

The project may later handle customer contracts, scope documents, scan artifacts, credentials, logs, and vulnerability details.

## Decision

Raw customer data, credentials, secrets, raw scan logs, and confidential client materials must not be committed to Git.

## Consequences

- Git contains reusable design, code, policy, and templates only.
- Sensitive materials are stored outside the repository or under ignored directories.
- Demo materials must be fictitious or sanitized.
