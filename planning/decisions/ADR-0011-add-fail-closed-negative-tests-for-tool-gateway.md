# ADR-0011: Add fail-closed negative tests for Tool Gateway

## Status

Accepted

## Context

The Tool Gateway mock runner demonstrates basic allow, deny, and human-approval-required behavior.

However, the project must also show that Tool Gateway fails closed when authorization binding is unsafe or inconsistent.

## Decision

Add negative tests for Tool Gateway authorization binding and safety checks.

The initial negative tests cover:

- target_id mismatch,
- scope_id mismatch,
- tool mismatch,
- operation mismatch,
- credential_ref mismatch,
- destructive_tests=true,
- evidence_required=false,
- invalid expiration ordering.

## Rationale

The Tool Gateway is a trusted control boundary.

A trusted control boundary must not only support valid flows. It must reject unsafe or mismatched flows reliably.

These tests directly support the AAEF principle:

Model output is not authority.

## Consequences

- Tool Gateway behavior becomes testable.
- Future changes to binding or policy logic can be regression-tested.
- Real tool adapters should not be integrated until these fail-closed checks remain stable.
