# ADR-0121: Add v0.6.50 public validator negative fixture metadata contract candidate

Status: Accepted  
Date: 2026-05-07

## Context

v0.6.49 concluded that the project is ready to consider a candidate metadata contract for public validator negative fixtures.

The v0.6.46 fixture set already includes metadata conventions for expected fail-closed behavior, public-safe static posture, positive-control linkage, non-authorization statements, and runtime boundary flags.

## Decision

Add v0.6.50 as a metadata contract candidate.

The candidate contract documents required metadata fields and boundary flags, and adds a read-only contract test over the existing public negative fixture metadata.

It does not add a JSON Schema, rewrite fixture metadata, add fixtures, or modify validator behavior.

## Consequences

The project has a candidate metadata contract for public negative fixtures.

A later checkpoint should review and close the metadata contract track before moving to validator failure category mapping or validator behavior hardening.
