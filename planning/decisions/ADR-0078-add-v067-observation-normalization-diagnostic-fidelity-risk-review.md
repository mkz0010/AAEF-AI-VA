# ADR-0078: Add v0.6.7 observation normalization and diagnostic fidelity risk review

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA v0.6.6 defined that AI generates `tool_action_request` while gates
decide execution.

The next issue is what AI should see when generating requests. Raw responses can
contain secrets, credentials, customer-sensitive material, and prompt-injection
content. But over-normalization can remove diagnostically important signals and
reduce the quality of AI-generated requests.

## Decision

Add a v0.6.7 observation normalization and diagnostic fidelity risk review.

The checkpoint records:

- Diagnostic Fidelity Risk,
- observation handling pipeline,
- raw artifact principle,
- AI diagnostic context package,
- signal-preserving extraction,
- information that should not be sent directly to AI,
- information density criteria,
- diagnostic sufficiency criteria,
- normalization loss record,
- fidelity risk levels,
- AI behavior under insufficient information,
- escalation paths,
- relationship to `tool_action_request`,
- sanitizer and normalizer responsibility separation,
- prompt injection and untrusted content handling,
- runtime and scanning prohibitions.

## Consequences

Positive:

- The project can improve AI request quality without exposing unsafe raw content.
- Normalization loss becomes explicit evidence rather than hidden behavior.
- Diagnostic insufficiency can lead to additional observation or review instead of guessing.
- Future demos can explain what AI saw, what was removed, and why gates still decide execution.

Negative / deferred:

- This does not implement sanitizer or normalizer changes.
- This does not implement signal extraction.
- This does not create new runtime behavior.
- This does not enable scanning.
