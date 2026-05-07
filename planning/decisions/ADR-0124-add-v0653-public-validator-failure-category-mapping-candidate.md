# ADR-0124: Add v0.6.53 public validator failure category mapping candidate

Status: Accepted  
Date: 2026-05-07

## Context

v0.6.52 concluded that the project is ready to consider a future mapping between public negative fixture categories and public validator failure category names.

The lowest-risk option is a documentation-only mapping table. This avoids validator behavior changes, validator output changes, fixture metadata rewrites, and schema changes.

## Decision

Add v0.6.53 as a documentation-only failure category mapping candidate.

The candidate maps the current 13 public negative fixture categories to stable candidate failure category names.

It does not add validator output, modify validator behavior, add metadata fields, rewrite fixture metadata, add JSON Schema, or add fixtures.

## Consequences

The project has a reviewable documentation-only mapping candidate.

A later checkpoint should review and close the mapping track before any validator output, metadata-field, or behavior work is considered.
