# ADR-0063: Add licensing, trademark, authorship, and commercial-use protection hardening

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA has reached public repository, GitHub Release, commercial adoption, README
baseline, and README compatibility-registry milestones.

The next commercial-readiness need is to clarify public protection boundaries:
authorship, notice, commercial-use discussion, project-name usage, and contribution
rules.

The repository should support commercial conversations while preserving AGPL-3.0,
avoiding legal overclaims, and avoiding confusion about endorsement, certification,
production readiness, or permission to scan third-party systems.

## Decision

Add v0.5.3 licensing, trademark, authorship, and commercial-use protection hardening.

The release adds:

- `NOTICE`,
- `AUTHORS`,
- `COPYRIGHT`,
- `COMMERCIAL-LICENSE.md`,
- `TRADEMARKS.md`,
- `CONTRIBUTING.md`,
- a protection checkpoint document,
- a validation test.

## Consequences

Positive:

- Commercial boundaries become clearer.
- Authorship and attribution are easier to identify.
- Project-name usage expectations are documented.
- Contribution and security disclosure boundaries become clearer.
- The public repository is better prepared for targeted commercial discussions.

Negative / deferred:

- This does not register a trademark.
- This does not provide legal advice.
- This does not define final commercial contract terms.
- This does not authorize runtime execution.
