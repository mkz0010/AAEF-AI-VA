# Internal Adapter Artifact Policy

## Purpose

This document defines how Tool Gateway adapter output should be handled before real tool integrations are introduced.

The project now has adapter stubs for ZAP, Nmap, nuclei, and browser automation. Adapter output is useful for debugging and future tool integration, but it must not be mixed into public/generated Tool Gateway outputs, AI-visible summaries, or evidence records without explicit sanitization and classification.

## Core Decision

Adapter output is internal Tool Gateway information.

It must not be embedded directly in:

- `tool_execution_result`,
- `evidence_record`,
- AI-visible result summaries,
- report-ready finding evidence,
- customer-facing output.

Adapter output may be stored only as an internal/private artifact after it is deliberately classified and, where needed, sanitized.

## Why This Matters

Real diagnostic tools may produce sensitive output.

Examples include:

- HTTP request and response bodies,
- Authorization headers,
- Cookie and Set-Cookie headers,
- bearer tokens,
- CSRF tokens,
- session identifiers,
- reflected personal data,
- internal paths,
- stack traces,
- screenshots,
- raw scan logs,
- tool configuration details.

If adapter output is casually added to public generated results, sensitive data could be exposed to AI or included in evidence records that were intended to be safe.

## Artifact Classes

### Public Contract Objects

These are schema-bound objects that may be consumed by later platform components.

Examples:

- `tool_action_request`
- `authorization_decision`
- `tool_execution_result`
- `evidence_record`

Rules:

- Must validate against MVP schemas.
- Must not include raw secrets.
- Must not include `_adapter_output`.
- Must keep `secret_exposed_to_ai` false.
- May reference internal artifacts by path or ID after policy approval.

### Internal Adapter Artifacts

These are adapter-produced implementation artifacts.

Examples:

- raw ZAP output,
- raw Nmap XML,
- raw nuclei JSONL,
- browser automation traces,
- adapter debug output,
- temporary tool configuration,
- screenshots,
- request/response captures.

Rules:

- Must remain under ignored/private paths by default.
- Must not be committed to Git.
- Must not be sent to AI directly.
- Must be sanitized or summarized before AI-visible use.
- Must be referenced from evidence only through controlled artifact references.

### Sanitized Artifacts

These are outputs derived from internal adapter artifacts after sanitization.

Examples:

- sanitized alert summaries,
- redacted request/response snippets,
- normalized finding observations,
- token-stripped service summaries,
- safe screenshot references where allowed.

Rules:

- Must remove or mask secrets and sensitive values.
- May be used for AI summarization only after classification.
- May be referenced by evidence records.
- Should have a clear relationship to the raw artifact reference.

## Initial Storage Policy

For the MVP prototype, internal adapter artifacts should use ignored paths such as:

~~~text
private-not-in-git/raw-artifacts/
private-not-in-git/prototype-runs/
private-not-in-git/test-runs/
~~~

The repository must not track raw adapter artifacts.

## Result Object Boundary

The generated `tool_execution_result` is a public contract object.

It may contain:

- `raw_artifact_ref`
- `sanitized_artifact_ref`
- execution status
- tool and operation metadata
- credential_ref reference metadata
- secret exposure status

It must not contain:

- `_adapter_output`
- raw request/response data
- tokens
- cookies
- credentials
- unredacted tool logs
- screenshots as embedded data
- arbitrary adapter debug structures

## Evidence Boundary

The generated `evidence_record` may link to internal and sanitized artifact references, but it should not embed raw adapter output.

Evidence should preserve traceability without becoming a data leak.

## AI-visible Boundary

AI-visible summaries should be derived from sanitized artifacts only.

AI must not receive internal adapter artifacts directly.

## Future Implementation Guidance

Before integrating a real ZAP, Nmap, nuclei, Burp, or Nessus adapter, define:

- raw artifact path,
- sanitized artifact path,
- artifact classification,
- sanitization rules,
- whether AI may receive a derived summary,
- evidence reference behavior,
- retention and deletion behavior.

## Relationship to v0.1.13

v0.1.13 added generated output validation and ensured `_adapter_output` does not appear in public generated Tool Gateway result objects.

This policy records the design reason for that boundary.
