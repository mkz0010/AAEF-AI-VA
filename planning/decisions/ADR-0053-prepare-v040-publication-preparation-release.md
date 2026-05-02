# ADR-0053: Prepare v0.4.0 public publication preparation release

Status: Accepted  
Date: 2026-05-02

## Context

AAEF-AI-VA has completed a publication-readiness stack:

- v0.3.5 licensing and commercial-use boundary,
- v0.3.6 public repository readiness checkpoint,
- v0.3.7 publication hygiene and private artifact exclusion checkpoint,
- v0.3.8 public security policy and vulnerability disclosure checkpoint,
- v0.3.9 first-publication repository settings checklist.

The project now needs a clean release-level summary before any GitHub remote is
created or public publication is attempted.

## Decision

Prepare v0.4.0 as a public publication preparation release.

This release summarizes readiness work, records a dry-run checklist, prepares public
positioning language, and preserves the execution-blocked posture.

It must not create a remote repository, push code, change repository visibility, or
configure GitHub settings automatically.

## Consequences

Positive:

- v0.4.0 becomes a clean publication-preparation milestone.
- The repository can be reviewed before first remote creation.
- Public messaging is aligned with safety, evidence, authorization, and publication hygiene.

Negative / deferred:

- This does not publish the repository.
- This does not add CI.
- This does not choose a final durable commercial contact.
- This does not choose a final durable security reporting channel.
- This does not authorize runtime execution.
