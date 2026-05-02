# ADR-0061: Clean up README public baseline and commercial entrypoint

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA has reached a public repository state with a GitHub Release and commercial
adoption preparation checkpoint.

The README still needed to be aligned with the current public baseline. Older
implementation checkpoint material could appear too prominently, and obsolete
local-first/private-first wording could confuse visitors after the repository became
public.

The README is the first public entry point and should clearly present what the
project is, what it is not, how it is validated, and how commercial adoption
conversations should be approached.

## Decision

Add a v0.5.1 README public baseline and commercial entrypoint cleanup.

The cleanup rewrites the README front door around:

- current public baseline,
- authority boundary,
- what this is / what this is not,
- commercial adoption entrypoint,
- validation,
- license,
- security,
- publication and release checkpoints.

## Consequences

Positive:

- First-time visitors see the current state immediately.
- Obsolete local-only wording is removed from the public entry point.
- Commercial adoption is visible without making the repository a sales deck.
- Runtime-execution and scanning prohibitions remain clear.

Negative / deferred:

- This does not rewrite every historical document.
- This does not create a commercial contact channel.
- This does not publish outreach material.
- This does not authorize runtime execution.
