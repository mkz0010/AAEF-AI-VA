# ADR-0067: Add public trust and reviewer navigation checkpoint

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA now has public launch, commercial adoption, README compatibility,
licensing/trademark/authorship protection, dependency/repository governance,
branch-protection planning, and release-governance checkpoints.

The project may be evaluated before a direct commercial conversation exists. The
public repository therefore needs to function as a product introduction and trust
surface without becoming a sales deck or making unsupported claims.

## Decision

Add a v0.5.7 public trust and reviewer navigation checkpoint.

The checkpoint records:

- public trust signals,
- first-time reader path,
- technical reviewer path,
- security reviewer path,
- commercial reviewer path,
- licensing reviewer path,
- maintainer operations reviewer path,
- recommended review questions,
- product introduction boundary,
- runtime and scanning prohibitions.

## Consequences

Positive:

- Reviewers can navigate the repository by role.
- The repository becomes easier to evaluate without a sales meeting.
- Commercial introduction is supported without creating private sales material.
- Unsupported production, certification, legal, audit, and scan-authorization claims remain avoided.

Negative / deferred:

- This does not create commercial sales material.
- This does not create a target customer list.
- This does not configure GitHub branch protection.
- This does not authorize runtime execution.
