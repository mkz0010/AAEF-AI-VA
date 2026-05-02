# MVP Schema Contracts

## Purpose

This document defines the MVP schema contracts for the AAEF-controlled AI Vulnerability Assessment Platform.

The schemas define the contracts between:

- AI / LLM,
- AAEF Authorization Gateway,
- Tool Gateway,
- Sanitizer / Normalizer,
- Evidence Store,
- Human Review.

The goal is to prevent ambiguity between AI-generated requests and authorized execution.

## Core Principle

A schema-valid AI request is still not authority.

A `tool_action_request` is only a request. It must be evaluated by AAEF Authorization Gateway before Tool Gateway may execute anything.

## Schema Files

| Schema | Purpose |
|---|---|
| `schemas/tool-action-request.schema.json` | AI-generated request for a diagnostic tool action |
| `schemas/authorization-decision.schema.json` | AAEF Authorization Gateway decision |
| `schemas/tool-execution-result.schema.json` | Tool Gateway execution result |
| `schemas/evidence-record.schema.json` | Evidence Store record linking request, decision, execution, artifact, and review |

## Contract Flow

~~~text
tool_action_request
  ↓
authorization_decision
  ↓
tool_execution_result
  ↓
evidence_record
~~~

## Contract Boundary

### tool_action_request

Produced by:

- AI / LLM,
- or a human operator acting through the same request format.

Consumed by:

- AAEF Authorization Gateway.

Important rule:

The request must not be executed directly by Tool Gateway.

### authorization_decision

Produced by:

- AAEF Authorization Gateway.

Consumed by:

- Tool Gateway.

Important rule:

Tool Gateway must verify that the execution request matches the authorization decision.

### tool_execution_result

Produced by:

- Tool Gateway.

Consumed by:

- Evidence Store,
- Sanitizer / Normalizer,
- Human Review workflow,
- AI only after sanitization.

Important rule:

`secret_exposed_to_ai` must be false.

### evidence_record

Produced by:

- Evidence Store,
- or by Tool Gateway plus Evidence Store in the MVP prototype.

Consumed by:

- Human Review,
- Report Generator,
- audit/reconstruction workflow.

Important rule:

Evidence may include `credential_ref_used`, but must not include raw secrets.

## MVP Tool and Operation Scope

The schema intentionally limits tools and operations.

Initial tools:

- `zap`
- `nmap`
- `nuclei`
- `browser`

Initial operations:

- `passive_scan`
- `authenticated_crawl`
- `safe_port_discovery`
- `service_version_detection`
- `safe_template_scan`
- `safe_login_check`

This prevents the first prototype from drifting into arbitrary command execution.

## credential_ref Handling

`credential_ref` may appear in:

- tool action requests,
- authorization decisions,
- tool execution results,
- evidence records.

However, `credential_ref` is only a reference. It is not a secret and is not authority by itself.

Raw credentials must not appear in any of these schema records.

## Fail-Closed Expectations

The prototype should fail closed when:

- a required schema field is missing,
- an unknown tool is requested,
- an unknown operation is requested,
- authorization decision is missing,
- authorization decision does not match request,
- `secret_exposed_to_ai` would be true,
- evidence cannot be recorded where required.

## Validation Scope

The initial validation script checks that schema files are valid JSON and contain core JSON Schema fields.

Full JSON Schema validation of example instances can be added later.

## Relationship to Tool Gateway

Tool Gateway relies on these schemas to avoid ambiguous execution.

The MVP implementation should treat these schemas as contract boundaries rather than informal examples.
