# ADR-0091: Add v0.6.20 static fixture validator read-only implementation scaffold

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.19 defined implementation readiness review for the future static fixture validator. The next step is to implement the smallest read-only validator scaffold without generating fixtures or implementing full fixture validation.

## Decision

Add a v0.6.20 static fixture validator read-only implementation scaffold.

The checkpoint adds `tools/validate_static_lab_fixtures.py` with review-only result structures, planned failure categories, fail-closed missing-directory behavior, and a non-authorizing CLI boundary. It also adds a local boundary test and documentation.

## Consequences

Positive:

- The project now has a concrete read-only validator scaffold.
- The scaffold can be compiled, imported, and invoked locally.
- Missing and invalid fixture directories fail closed.
- Runtime, Docker, scanner, credential, customer-target, and delivery authorization remain blocked.

Negative / deferred:

- This does not implement complete fixture schema validation.
- This does not implement negative tests.
- This does not generate fixture files.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
