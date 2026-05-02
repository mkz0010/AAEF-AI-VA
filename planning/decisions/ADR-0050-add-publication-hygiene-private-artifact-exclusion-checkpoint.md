# ADR-0050: Add publication hygiene and private artifact exclusion checkpoint

Status: Accepted  
Date: 2026-05-02

## Context

AAEF-AI-VA now includes a public repository readiness checkpoint. However, before
publication, the project also needs a hygiene boundary that prevents accidental
publication of generated, private, local, or customer-specific artifacts.

The repository generates local outputs under `private-not-in-git/`. These outputs are
useful for validation but are not source artifacts.

## Decision

Add a v0.3.7 publication hygiene and private artifact exclusion checkpoint.

The checkpoint adds:

- `.gitignore` coverage for private/generated/local artifacts,
- documentation for publication hygiene,
- a local validation test,
- registration in `tools/run_all_local_checks.py`.

## Consequences

Positive:

- Publication safety is improved before a remote repository is created or pushed.
- Private/generated outputs are explicitly separated from source artifacts.
- The publication process remains separate from runtime authorization.

Negative / deferred:

- This does not decide whether the first remote should be public or private.
- This does not perform a full dependency license inventory.
- This does not replace manual review before publication.
