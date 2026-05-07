# ADR-0123: Add v0.6.52 public validator failure category mapping readiness review

Status: Accepted  
Date: 2026-05-07

## Context

v0.6.51 closed the public validator negative fixture metadata contract track for the current v0.6.46 public-safe static fixture set.

The next hardening step is to consider whether negative fixture categories should be mapped to stable validator failure category names.

## Decision

Add v0.6.52 as a readiness review for public validator failure category mapping.

This checkpoint identifies candidate mapping names and readiness criteria, but does not implement mapping, add validator output, rewrite metadata, add fixtures, or modify validator behavior.

## Consequences

The project has a bounded readiness basis for a later failure category mapping candidate.

Any later implementation that changes validator output or behavior should be preceded by a separate validator behavior implementation readiness review.
