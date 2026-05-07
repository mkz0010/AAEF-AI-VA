# ADR-0120: Add v0.6.49 public validator negative fixture metadata contract readiness review

Status: Accepted  
Date: 2026-05-07

## Context

v0.6.48 planned future hardening for public validator negative fixture coverage and identified expected blocker metadata as the next likely workstream.

Before adding any metadata contract, schema checks, fixture rewrites, or validator behavior changes, the project needs a readiness review.

## Decision

Add v0.6.49 as a metadata contract readiness review.

This checkpoint confirms that a later metadata contract candidate may be considered and defines candidate required fields, boundary flags, risks to avoid, and sequencing.

It does not implement the contract, add schemas, rewrite fixture metadata, add fixtures, or modify validator behavior.

## Consequences

The project has a bounded readiness basis for a future metadata contract candidate.

Any later metadata contract candidate should remain public-safe, static, synthetic, non-running, and Applied Implementation-scoped.
