# 0005: Define MVP schema contracts

## Status

In Progress

## Priority

P0

## Type

Design

## Background

Tool Gateway requires stable input and output contracts before a prototype can be implemented.

The MVP should define schemas for AI-generated requests, AAEF authorization decisions, Tool Gateway execution results, and Evidence Store records.

## Decision Summary

Define JSON Schema contracts for:

- tool_action_request,
- authorization_decision,
- tool_execution_result,
- evidence_record.

These schemas intentionally limit tools and operations to the MVP scope.

## Acceptance Criteria

- tool_action_request schema is defined
- authorization_decision schema is defined
- tool_execution_result schema is defined
- evidence_record schema is defined
- schema documentation is added
- schema files are valid JSON
- allowed MVP tools are constrained
- allowed MVP operations are constrained
- credential_ref appears only as a reference
- raw secrets are not modeled as allowed fields

## Related Documents

- docs/14-mvp-schemas.md
- docs/13-tool-gateway-mvp-design.md
- docs/12-credential-ref-flow.md
- docs/08-evidence-store-design.md
- planning/decisions/ADR-0008-mvp-schema-contracts.md

## Remaining Work

- Add example valid instances.
- Add example denied and human-approval-required flows.
- Add lightweight validation for example instances.
- Use schemas in the first Tool Gateway prototype.
