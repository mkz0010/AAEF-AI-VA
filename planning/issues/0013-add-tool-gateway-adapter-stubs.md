# 0013: Add Tool Gateway adapter stubs

## Status

In Progress

## Priority

P0

## Type

Prototype

## Background

Tool Gateway should not become a generic command executor.

Before real tool integration, the project needs adapter stubs that expose narrow, approved operations for each tool category.

## Decision Summary

Add adapter stubs for:

- ZAP,
- Nmap,
- nuclei,
- browser automation.

Tool Gateway will route completed mock executions through the adapter registry.

## Acceptance Criteria

- adapter package is added
- adapter registry is added
- ZAP adapter stub is added
- Nmap adapter stub is added
- nuclei adapter stub is added
- browser adapter stub is added
- Tool Gateway routes completed actions through adapter registry
- unsupported operations fail closed
- local checks include adapter tests
- no real tools are executed

## Related Documents

- docs/20-tool-gateway-adapter-stubs.md
- docs/13-tool-gateway-mvp-design.md
- docs/16-tool-gateway-mock-runner.md
- planning/decisions/ADR-0014-add-tool-gateway-adapter-stubs-before-real-tool-integration.md

## Remaining Work

- Add real ZAP adapter behind the same interface.
- Add real Nmap adapter behind the same interface.
- Add real nuclei adapter behind the same interface.
- Add adapter-level artifact sanitizer hooks.
