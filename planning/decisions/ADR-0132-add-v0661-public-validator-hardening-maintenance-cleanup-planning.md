# ADR-0132: Add v0.6.61 public validator hardening maintenance cleanup planning

Status: Accepted  
Date: 2026-05-07

## Context

v0.6.60 established a conservative documentation-only maintenance baseline for the public validator hardening track.

The next safe step is to plan cleanup of reviewer navigation, ordering, readability, and non-implementation clarity before any validator behavior implementation readiness review is considered.

## Decision

Add v0.6.61 as a public validator hardening maintenance cleanup planning checkpoint.

This checkpoint defines a narrow cleanup planning scope, cleanup non-goals, retained baselines, candidate cleanup ordering, and deferred implementation paths.

It does not implement cleanup beyond the planning document and read-only test, does not reorganize files, does not modify validator behavior, does not add validator output, does not create an output contract, does not add metadata fields, does not rewrite fixtures, does not add JSON Schema, does not add fixtures, and does not authorize runtime/scanner/Docker/credential/customer/delivery activity.

## Consequences

Future work may implement a narrow maintenance cleanup candidate, starting with reviewer navigation and summary improvements.

Validator behavior implementation readiness remains deferred.
