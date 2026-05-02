# ADR-0054: Add GitHub Actions CI scaffold

Status: Accepted  
Date: 2026-05-02

## Context

AAEF-AI-VA v0.4.0 prepared the repository for public publication, but the project does
not yet contain a GitHub Actions workflow.

A visible CI signal is useful before or alongside first public repository publication,
because it demonstrates that the repository's validation suite can be executed
outside the author's local environment.

## Decision

Add a v0.4.1 GitHub Actions CI scaffold.

The workflow runs the existing local validation suite with:

~~~text
python tools/run_all_local_checks.py
~~~

The workflow must remain a validation-only scaffold. It must not run scans, use
credentials, contact customer targets, configure remotes, or weaken runtime execution
boundaries.

## Consequences

Positive:

- Public reviewers can see an initial CI validation path.
- The repository gains a standard location for future checks.
- The existing local validation suite remains the source of truth.

Negative / deferred:

- CI will only run after the repository is pushed to GitHub.
- This does not create the remote repository.
- This does not configure branch protection or rulesets.
- This does not add dependency caching or dependency installation.
- This does not authorize runtime execution.
