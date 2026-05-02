# ADR-0003: Use existing LLM API for MVP

## Status

Proposed

## Context

Building or distilling a dedicated vulnerability assessment model requires data, evaluation, infrastructure, and operational cost.

## Decision

For the MVP, use existing LLM/API services with data minimization, anonymization, and AAEF controls.

## Consequences

- Faster MVP development.
- External AI usage must be controlled by policy and contract.
- High-sensitivity plans may require local or customer-controlled model options later.
