# ADR-0016: Keep adapter output as private internal artifact by default

## Status

Accepted

## Context

The Tool Gateway now routes completed actions through adapter stubs.

Adapters may produce useful implementation output. In real tool integrations, that output may include raw scan logs, HTTP messages, headers, cookies, tokens, screenshots, tool configuration, or other sensitive material.

The project already validates generated Tool Gateway outputs against schemas and prevents `_adapter_output` from appearing in public generated results.

## Decision

Adapter output will be treated as private internal artifact material by default.

It must not be embedded directly in public/generated `tool_execution_result` or `evidence_record` objects.

Generated public outputs may reference raw or sanitized artifacts through controlled reference fields, but must not embed raw adapter output.

AI-visible summaries must be derived only from sanitized or explicitly approved artifact content.

## Consequences

- Public generated outputs remain schema-conformant.
- Internal adapter details remain separated from AI-visible and evidence-facing records.
- Future real tool integrations must define raw artifact, sanitized artifact, and evidence reference behavior explicitly.
- Adapter debugging remains possible under ignored local paths.
- The project reduces the risk of accidentally exposing secrets through adapter output.
