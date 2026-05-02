# ADR-0077: Add v0.6.6 AI request decision boundary and tool selection criteria

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.5 defined a documentation-only local lab profile and action
taxonomy.

The next design risk is ambiguity in phrases such as "AI chooses the best method" or
"AI selects a tool." Those phrases can incorrectly imply that AI has execution
authority.

## Decision

Add a v0.6.6 AI request decision boundary and tool selection criteria checkpoint.

The checkpoint records:

- core proposition,
- decision boundary,
- what AI may do,
- what AI must not do,
- tool selection is not execution authority,
- tool action request fields,
- request generation context,
- current MVP tool criteria,
- future tool candidate tiers,
- tool-selection criteria,
- request outcome model,
- request quality criteria,
- rejection criteria,
- human review escalation,
- relationship to observation fidelity,
- runtime and scanning prohibitions.

## Consequences

Positive:

- The project can expand AI judgment range without granting execution authority.
- Tool-selection language becomes safer and more precise.
- Future demo and lab work can distinguish request generation from execution.
- Tool roadmap discussion remains bounded by gates.

Negative / deferred:

- This does not add tool adapters.
- This does not enable tool execution.
- This does not define observation normalization.
- This does not create commercial PoC readiness.
