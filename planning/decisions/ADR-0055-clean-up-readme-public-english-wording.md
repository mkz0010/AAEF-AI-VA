# ADR-0055: Clean up README public English wording

Status: Accepted  
Date: 2026-05-02

## Context

AAEF-AI-VA has been pushed to GitHub and is now being reviewed as a public-facing
repository candidate.

The README still contained Japanese local-development wording, including language
that described the repository as a local management repository and an AI authority
statement written in Japanese.

The repository should be English-first for public review and commercial evaluation.

## Decision

Add a v0.4.2 README public English wording cleanup.

The cleanup replaces Japanese public-facing README wording with English wording while
preserving the core AAEF authority boundary:

- AI output is not authority to perform assessment actions.
- AI may request assessment actions.
- Execution is decided by the AAEF Authorization Gateway, Tool Gateway, contractual
  scope, and human review.

## Consequences

Positive:

- README becomes more suitable for public GitHub presentation.
- The core authority boundary is clearer to English-speaking reviewers.
- Internal/local wording is removed from the public entry point.

Negative / deferred:

- This does not provide a Japanese companion README.
- This does not rewrite every repository document for public polish.
- This does not create a GitHub release.
- This does not authorize runtime execution.
