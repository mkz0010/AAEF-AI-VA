# ADR-0066: Add release governance and maintainer operations checklist

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA now has repository ruleset and branch protection planning, but actual
GitHub administration settings have not yet been changed.

Before changing GitHub settings, the project should document the maintainer release
workflow that is already being used: scoped branches, local checks, fast-forward
merge, semantic version tags, pushes, GitHub Actions verification, and private
artifact checks.

## Decision

Add a v0.5.6 release governance and maintainer operations checklist.

The checkpoint records:

- standard release workflow,
- pre-release checklist,
- commit and merge checklist,
- tag and push checklist,
- GitHub Actions verification checklist,
- private artifact checklist,
- emergency exception checklist,
- post-release review checklist,
- runtime and scanning prohibitions.

## Consequences

Positive:

- The current maintainer workflow becomes explicit and repeatable.
- Future branch protection settings can be compared against the documented workflow.
- Private artifact checks become part of the release process.
- Emergency exceptions have a documented minimum record.

Negative / deferred:

- This does not configure GitHub branch protection.
- This does not configure GitHub rulesets.
- This does not configure tag protection.
- This does not require pull requests immediately.
- This does not authorize runtime execution.
