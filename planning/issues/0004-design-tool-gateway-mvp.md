# 0004: Design Tool Gateway MVP

## Status

In Progress

## Priority

P0

## Type

Design

## Background

Tool Gateway is the boundary between AI-generated diagnostic requests and real tool execution.

If Tool Gateway is weak, AI output can become de facto authority. Therefore, Tool Gateway must be treated as a trusted control boundary rather than a simple wrapper.

## Decision Summary

The MVP Tool Gateway will:

- accept only authorized tool actions,
- verify authorization binding,
- enforce target and scope constraints,
- route actions to narrow tool adapters,
- resolve credential_ref only after authorization,
- inject secrets without exposing them to AI,
- capture raw artifacts,
- hand off raw artifacts to Sanitizer / Normalizer,
- emit execution metadata for Evidence Store,
- fail closed on missing or mismatched authorization.

## Initial Tool Adapters

- ZAP adapter
- Nmap adapter
- nuclei adapter
- limited browser adapter where necessary

## Deferred Tool Adapters

- Burp Suite
- Nessus / Tenable
- cloud posture tools
- custom exploit validation scripts

## Acceptance Criteria

- Tool Gateway role is defined
- Tool Gateway is identified as a trusted control boundary
- Authorization binding requirements are defined
- Scope enforcement requirements are defined
- credential_ref handling requirements are defined
- Secret injection requirements are defined
- Tool adapter model is defined
- Fail-closed conditions are defined
- Evidence handoff requirements are defined
- MVP success criteria are defined

## Related Documents

- docs/13-tool-gateway-mvp-design.md
- docs/07-tool-gateway-design.md
- docs/03-architecture.md
- docs/04-aaef-control-model.md
- docs/12-credential-ref-flow.md
- planning/decisions/ADR-0007-tool-gateway-as-trusted-control-boundary.md

## Remaining Work

- Define tool_action_request schema.
- Define authorization_decision schema.
- Define tool_execution_result schema.
- Define first prototype code layout.
- Implement allowed / denied / human-approval-required mock execution examples.
