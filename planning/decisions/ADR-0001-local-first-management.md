# ADR-0001: Local-first project management

## Status

Accepted

## Context

This project is not intended for public release at the initial stage. It may include sensitive business planning, security architecture, legal considerations, and prototype implementation details.

## Decision

Manage the project in a local Git repository by default.

## Consequences

- Project history can be maintained without publishing externally.
- Sensitive materials must still be excluded from Git.
- The repository can later be moved to a private remote if needed.
