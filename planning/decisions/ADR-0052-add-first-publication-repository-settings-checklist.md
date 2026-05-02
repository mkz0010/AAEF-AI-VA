# ADR-0052: Add first-publication repository settings checklist

Status: Accepted  
Date: 2026-05-02

## Context

AAEF-AI-VA now has:

- licensing and commercial-use boundary,
- public repository readiness checkpoint,
- publication hygiene and private artifact exclusion checkpoint,
- public security policy and vulnerability disclosure checkpoint.

The next step before first publication is to record repository-level decisions that
will be made in GitHub rather than in source code.

These include repository visibility, metadata, security settings, collaboration
features, branch protection or rulesets, and initial remote/push procedure.

## Decision

Add a v0.3.9 first-publication repository settings checklist.

The checklist is advisory and manual. It must not create a remote repository, push
code, change visibility, or configure GitHub settings automatically.

## Consequences

Positive:

- First publication becomes deliberate instead of accidental.
- Public/private/staged-public choices are recorded before action.
- Security, visibility, and collaboration settings are separated from runtime readiness.

Negative / deferred:

- This does not create the remote repository.
- This does not configure GitHub settings.
- This does not add CI.
- This does not define durable commercial or security contact channels.
