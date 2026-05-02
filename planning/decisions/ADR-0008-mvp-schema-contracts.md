# ADR-0008: Define MVP schema contracts for request, authorization, execution, and evidence

## Status

Accepted

## Context

The project now has initial designs for MVP scope, credential_ref, and Tool Gateway.

Before implementing the prototype, the project needs stable contracts for the objects exchanged between AI, AAEF Authorization Gateway, Tool Gateway, Sanitizer / Normalizer, Evidence Store, and Human Review.

Without explicit schemas, AI-generated requests could be interpreted inconsistently, Tool Gateway behavior could drift, and evidence records may fail to support reconstruction.

## Decision

Define MVP JSON Schema contracts for:

- tool_action_request,
- authorization_decision,
- tool_execution_result,
- evidence_record.

These schemas will be stored under `schemas/` and documented in `docs/14-mvp-schemas.md`.

## Rationale

The schemas provide a stable interface between design and implementation.

They also reinforce the AAEF principle that model output is not authority:

- a valid request is still only a request,
- authorization is a separate object,
- execution result is emitted by Tool Gateway,
- evidence records link request, decision, execution, artifact, and review.

## Consequences

- Tool Gateway implementation can be built against explicit contracts.
- AI-generated requests have a constrained shape.
- Allowed tools and operations are intentionally limited in the MVP.
- Future Burp, Nessus, or custom validation integrations will require schema expansion.
- Evidence reconstruction becomes easier because identifiers are consistent across objects.
