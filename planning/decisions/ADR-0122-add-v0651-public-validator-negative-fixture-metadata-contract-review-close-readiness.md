# ADR-0122: Add v0.6.51 public validator negative fixture metadata contract review and close-readiness

Status: Accepted  
Date: 2026-05-07

## Context

v0.6.50 added a candidate metadata contract and read-only contract test for public validator negative fixtures.

Before moving to validator failure category mapping, the metadata contract candidate should be reviewed and either retained or revised.

## Decision

Add v0.6.51 as a review and close-readiness checkpoint for the public validator negative fixture metadata contract.

This checkpoint records that the v0.6.50 candidate contract is close-ready for the current v0.6.46 public-safe static fixture set.

It does not add JSON Schema, rewrite metadata, add fixtures, modify validator behavior, or start validator failure category mapping implementation.

## Consequences

The metadata contract track can be treated as closed for the current public negative fixture set.

Future work may move to validator failure category mapping readiness review, but validator behavior changes remain out of scope until separately reviewed.
