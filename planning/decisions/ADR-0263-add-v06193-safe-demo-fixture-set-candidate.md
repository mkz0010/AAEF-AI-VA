# ADR-0263: Add v0.6.193 Safe Demo Fixture Set candidate

Status: Accepted
Date: 2026-05-13

## Context

v0.6.191 selected Safe Demo Fixture Set Creation as a High-risk work item with three checkpoints. v0.6.192 accepted readiness for a constrained static fixture candidate.

## Decision

Add a static, mock, non-execution Safe Demo Fixture Set candidate under `docs/examples/safe-demo/blocked-tool-action-request-review/`.

The candidate includes request, gate decision, non-execution result, evidence trace, and reviewer walkthrough fixtures.

## Consequences

v0.6.194 should review the fixture set candidate and decide whether to accept, revise, or reject the fixture set.

This candidate does not create public samples, schemas, validators, executable demos, runtime behavior, scanner behavior, PoC materials, or AAEF main changes.
