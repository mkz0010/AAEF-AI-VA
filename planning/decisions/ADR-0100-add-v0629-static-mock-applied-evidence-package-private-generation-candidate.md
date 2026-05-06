# ADR-0100: Add v0.6.29 static/mock applied evidence package private generation candidate

Status: Accepted  
Date: 2026-05-06

## Context

AAEF-AI-VA v0.6.28 reviewed readiness for static/mock applied evidence package
generation. The next safe step is private-first package generation under
`private-not-in-git/`, while preserving that public sample promotion and tool-backed
diagnostic execution remain separate later decisions.

## Decision

Add a v0.6.29 static/mock applied evidence package private generation candidate.

The checkpoint adds `tools/generate_static_mock_applied_evidence_package.py` and a
local test that generates and validates a private static/mock package. The generated
package covers all four minimum scenarios and includes request, gate, dispatch, result,
evidence, review, non-proof, reviewer walkthrough, and AAEF five-questions mapping
artifacts.

## Consequences

Positive:

- The project now has a private static/mock applied evidence package candidate.
- The generated package demonstrates request-to-evidence linkage without scanner
  execution.
- Non-execution evidence and non-proof boundaries are present in generated artifacts.
- Public sample promotion remains a separate gated decision.

Negative / deferred:

- This does not create public samples.
- This does not implement the structural validator.
- This does not run diagnostic tools.
- This does not enable scanner execution.
- This does not create commercial PoC readiness.
