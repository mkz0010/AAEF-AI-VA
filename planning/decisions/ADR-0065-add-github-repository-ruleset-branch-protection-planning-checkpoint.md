# ADR-0065: Add GitHub repository ruleset and branch protection planning checkpoint

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA has public launch, commercial adoption, README compatibility,
licensing/trademark/authorship protection, and dependency/repository governance
readiness checkpoints.

The next repository-foundation step is to plan GitHub branch protection and
repository rulesets before changing GitHub administration settings.

The repository is still primarily solo-maintained, so immediately requiring pull
requests or strict branch protection could disrupt the current local workflow.
However, the expected protections should be documented before future collaboration
or commercial review.

## Decision

Add a v0.5.5 GitHub repository ruleset and branch protection planning checkpoint.

The checkpoint records:

- planned `main` branch protections,
- planned required checks,
- planned release tag protections,
- high-risk change review expectations,
- emergency exception planning,
- maintainer responsibility planning,
- GitHub administration checklist,
- runtime and scanning prohibitions.

## Consequences

Positive:

- Future GitHub administration changes have a documented plan.
- Reviewers can see that branch protection and rulesets were considered.
- High-risk changes have a clearer review path.
- Release tag governance becomes clearer.

Negative / deferred:

- This does not configure GitHub branch protection.
- This does not configure GitHub rulesets.
- This does not configure tag protection.
- This does not require pull requests immediately.
- This does not authorize runtime execution.
