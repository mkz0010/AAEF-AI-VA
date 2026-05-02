# ADR-0062: Add README compatibility phrase registry and test design hardening

Status: Accepted  
Date: 2026-05-03

## Context

The v0.5.1 README public baseline cleanup improved the public repository entry
point, but it also revealed that earlier checkpoint tests depended on specific
README headings and phrases.

Several tests also needed to distinguish between unsafe positive claims and explicit
negative boundary statements. For example, `autonomous vulnerability scanner` should
be allowed when listed under "What this is not", but a claim such as "this is an
autonomous vulnerability scanner" should be rejected.

## Decision

Add a v0.5.2 README compatibility phrase registry and test design hardening
checkpoint.

The registry records:

- compatibility-sensitive README headings,
- compatibility-sensitive README phrases,
- compatibility-sensitive README links,
- forbidden positive claims,
- allowed negative boundary statements,
- README-facing test design requirements.

## Consequences

Positive:

- Future README rewrites have a clear compatibility checklist.
- Tests can reject unsafe claims without blocking safe negative boundary statements.
- License, security, metadata, release, and commercial-adoption checkpoint
  compatibility becomes easier to preserve.

Negative / deferred:

- This does not eliminate all older README-facing test coupling.
- This does not introduce a generated README.
- This does not create a commercial contact channel.
- This does not authorize runtime execution.
