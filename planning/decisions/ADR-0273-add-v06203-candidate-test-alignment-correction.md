# ADR-0273: Add v0.6.203 candidate test alignment correction

Status: Accepted corrective checkpoint

## Context

v0.6.202 created the Static Fixture Review Path Public Communication Pack Candidate and registered a local test.

The local test expected the exact token `not published` in README. The README candidate section used `Not published`, which preserved the intended meaning but did not satisfy the exact token check.

The v0.6.202 commit and tag were pushed, so rewriting history or moving the tag should be avoided.

## Decision

Add v0.6.203 as a corrective checkpoint.

The correction aligns README wording with the existing v0.6.202 test expectation by using `not published` exactly.

The communication pack review-and-decision checkpoint is deferred to v0.6.204.

## Consequences

The repository can return to a passing local-check state without rewriting the v0.6.202 tag.

The v0.6.202 candidate remains candidate-only, not published, and not accepted.

No runtime, scanner, customer PoC, production-readiness, certification, legal-compliance, audit-opinion, diagnostic-completeness, or external-framework-equivalence claim is introduced.
