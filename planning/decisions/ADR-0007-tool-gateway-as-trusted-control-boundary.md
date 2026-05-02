# ADR-0007: Treat Tool Gateway as a trusted control boundary

## Status

Accepted

## Context

The platform allows AI to request vulnerability assessment actions. If those requests are executed directly, AI output could become de facto authority.

That would violate the core AAEF principle: Model output is not authority.

The project needs a component that mediates the transition from AI-generated requests to real diagnostic activity.

## Decision

Tool Gateway will be treated as a trusted control boundary.

It will not be a generic command executor or a thin integration wrapper.

Tool Gateway must execute only authorized, constrained, known operations through controlled tool adapters.

It must reject missing, expired, denied, mismatched, or scope-expanding requests.

It must resolve credential_ref only after AAEF authorization and must prevent raw secrets from being returned to AI.

## Responsibilities

Tool Gateway is responsible for:

- authorization binding,
- scope enforcement,
- tool adapter routing,
- credential_ref resolution through Vault or mock Vault,
- secret injection into approved tool runtimes,
- raw artifact capture,
- sanitizer handoff,
- evidence metadata emission,
- fail-closed behavior.

## Consequences

- Tool Gateway becomes one of the most security-critical components.
- Arbitrary AI-generated shell execution is explicitly out of scope.
- Tool adapters must expose narrow, approved operations.
- Evidence must show that Tool Gateway enforced the authorization decision.
- Future Burp, Nessus, and custom validation integrations must follow the same gateway pattern.
