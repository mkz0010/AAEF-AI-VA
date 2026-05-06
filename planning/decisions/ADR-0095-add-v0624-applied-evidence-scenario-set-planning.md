# ADR-0095: Add v0.6.24 applied evidence scenario set planning

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.23 defined the AAEF applied evidence package design. The next step is
to define the minimum scenario set that future static/mock evidence fixtures should
cover.

## Decision

Add a v0.6.24 applied evidence scenario set planning checkpoint.

The checkpoint defines the four minimum scenarios: `permitted-safe-diagnostic`,
`denied-out-of-scope-request`, `human-approval-required`, and
`not-executed-expired`. It records common artifact chain, common scenario fields,
per-scenario expected posture, scenario outcome matrix, AAEF five-questions mapping,
reviewer focus, static/mock evidence capture readiness, tool-backed local-lab
diagnostic capture readiness, and runtime/scanning boundaries.

## Consequences

Positive:

- Future fixture planning can target a concrete scenario set.
- Non-execution outcomes are explicitly first-class evidence.
- Static/mock evidence capture remains separate from tool-backed local-lab diagnostic
  capture.
- Public/private and safety boundaries remain explicit.

Negative / deferred:

- This does not generate scenarios.
- This does not generate evidence packages.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
