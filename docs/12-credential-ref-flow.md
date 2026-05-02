# credential_ref Flow

## Purpose

This document defines the credential_ref flow for the AAEF-controlled AI Vulnerability Assessment Platform.

The purpose of this design is to allow AI-assisted authenticated assessment without exposing raw credentials, session cookies, API keys, VPN secrets, or other sensitive authentication material to AI systems.

## Core Principle

AI may reference an authorization context, but it must not receive raw secrets.

A `credential_ref` is not a secret and is not authority by itself. It is a reference that can be resolved only by trusted components after an AAEF authorization decision.

## Design Summary

The AI can request an action like:

~~~json
{
  "action_type": "tool_execution",
  "target_id": "webapp-001",
  "scope_id": "scope-demo-001",
  "tool": "zap",
  "operation": "authenticated_crawl",
  "credential_ref": "test-account-001",
  "reason": "Run a safe authenticated crawl against the approved demo application."
}
~~~

The AI does not know the username, password, cookie, API key, or other raw secret associated with `test-account-001`.

Only the Tool Gateway, after authorization, may resolve the reference through Vault or a mock Vault.

## Logical Flow

~~~text
AI
  ↓
Tool Action Request
  ↓
AAEF Authorization Gateway
  ↓
Authorization Decision
  ↓
Tool Gateway
  ↓
Vault / Mock Vault
  ↓
Secret injection into approved tool runtime
  ↓
Approved target
  ↓
Raw tool output
  ↓
Sanitizer / Normalizer
  ↓
Evidence Store
  ↓
AI receives sanitized result summary
  ↓
Human Review
~~~

## Components

### AI / LLM

The AI may:

- propose tool action requests,
- reference credential_ref values,
- explain why an authenticated assessment action is needed,
- summarize sanitized outputs,
- draft finding candidates.

The AI must not:

- read raw credentials,
- request Vault contents,
- receive session cookies,
- receive API keys,
- receive VPN credentials,
- execute tools directly,
- approve its own use of credential_ref,
- transform credential_ref into authority.

### AAEF Authorization Gateway

The Authorization Gateway evaluates whether a requested action may proceed.

It should evaluate at least:

- requested action type,
- target_id,
- scope_id,
- tool,
- operation,
- requested credential_ref,
- allowed assessment window,
- allowed intensity,
- prohibited actions,
- evidence requirements,
- human approval requirements,
- customer AI-use preference where relevant.

### Tool Gateway

The Tool Gateway performs authorized execution.

It should:

- accept only authorized tool actions,
- reject requests without valid authorization_decision_id,
- resolve credential_ref only when authorized,
- retrieve secrets from Vault or mock Vault,
- inject secrets into the approved tool runtime,
- prevent secrets from being returned to AI,
- capture raw tool output,
- send raw output to Sanitizer / Normalizer,
- record execution metadata for Evidence Store.

### Vault / Mock Vault

Vault stores raw secrets.

For MVP, a local mock Vault may be used with fictitious credentials only.

Vault responsibilities:

- store raw username/password/API token/session material,
- bind secrets to credential_ref values,
- support expiry and revocation,
- support purpose and scope metadata,
- deny direct AI access,
- log resolution events.

### Sanitizer / Normalizer

The Sanitizer / Normalizer reduces the risk that raw secrets or sensitive customer data are sent back to AI.

It should remove or mask:

- Authorization headers,
- Cookie headers,
- Set-Cookie headers,
- API keys,
- bearer tokens,
- CSRF tokens where sensitive,
- passwords,
- session identifiers,
- personal data where possible,
- high-risk raw exploit details where not needed for AI triage.

### Evidence Store

Evidence Store records what happened without exposing raw secrets.

It may record:

- credential_ref used,
- whether credential_ref resolution succeeded,
- authorization_decision_id,
- tool_action_request_id,
- target_id,
- scope_id,
- tool,
- operation,
- timestamp,
- sanitized output reference,
- raw artifact reference where protected,
- human review status.

It must not store raw secrets in general-purpose evidence records.

## AI-visible Fields

The following fields may be visible to AI:

| Field | Example | Notes |
|---|---|---|
| target_id | webapp-001 | Alias, not necessarily raw customer URL |
| scope_id | scope-demo-001 | Approved scope reference |
| tool | zap | Tool name |
| operation | authenticated_crawl | Controlled operation |
| credential_ref | test-account-001 | Reference only, not a secret |
| auth_profile | standard-user | Role or profile label |
| allowed_actions | passive_scan, authenticated_crawl | Policy-derived |
| prohibited_actions | destructive_test, dos | Policy-derived |
| sanitized_result_summary | Alerts and observations | No raw secrets |

## AI-hidden Fields

The following fields must not be visible to AI:

| Field | Example | Reason |
|---|---|---|
| username | real login ID | Secret or sensitive account data |
| password | raw password | Secret |
| API key | raw API token | Secret |
| session cookie | Cookie value | Secret |
| bearer token | Authorization token | Secret |
| VPN credential | VPN profile or secret | High sensitivity |
| MFA seed | TOTP seed | High sensitivity |
| raw Authorization header | Bearer value | Secret |
| unredacted Set-Cookie header | session ID | Secret |

## credential_ref Lifecycle

### 1. Create

A credential_ref is created when a test credential or auth material is registered for an assessment.

Required metadata should include:

- credential_ref,
- customer_alias or tenant_id,
- target_id or allowed target pattern,
- scope_id,
- auth_profile,
- allowed_operations,
- expires_at,
- created_by,
- storage_location,
- sensitivity_level.

### 2. Authorize Use

A credential_ref may be used only when an AAEF authorization decision allows an action requiring it.

Authorization should consider:

- whether the credential_ref belongs to the approved scope,
- whether the requested target matches the credential_ref binding,
- whether the requested operation is allowed,
- whether the credential_ref is expired or revoked,
- whether human approval is required.

### 3. Resolve

Only Tool Gateway may resolve credential_ref into raw secret material.

Resolution should be:

- time-limited,
- purpose-limited,
- logged,
- isolated from AI,
- unavailable to arbitrary scripts or direct shell access.

### 4. Inject

Tool Gateway injects the secret into an approved tool runtime.

Examples:

- browser automation login form,
- ZAP authentication context,
- API request header,
- scan profile configuration,
- temporary environment variable for a controlled subprocess.

Secrets should not be printed to logs.

### 5. Execute

The approved tool action executes against the approved target.

The execution must follow constraints such as:

- target scope,
- allowed time window,
- rate limit,
- prohibited operations,
- evidence required,
- stop conditions.

### 6. Sanitize

Raw output is sanitized before it is made visible to AI.

Sanitization should happen before:

- AI summarization,
- AI finding triage,
- AI report drafting,
- general evidence export.

### 7. Record Evidence

Evidence records should preserve traceability while avoiding secret exposure.

The evidence should answer:

- Which credential_ref was used?
- Which authorization decision allowed it?
- Which tool action used it?
- Which target was assessed?
- What sanitized result was produced?
- Who reviewed the result?

### 8. Revoke / Expire

credential_ref values should support revocation and expiry.

Revocation triggers may include:

- end of assessment,
- customer request,
- suspected exposure,
- completion of report,
- change in scope,
- account rotation.

## Example Authorization Decision

~~~json
{
  "authorization_decision_id": "authz-demo-0001",
  "tool_action_request_id": "tar-demo-0001",
  "decision": "allow",
  "action_type": "tool_execution",
  "target_id": "webapp-001",
  "scope_id": "scope-demo-001",
  "tool": "zap",
  "operation": "authenticated_crawl",
  "credential_ref": "test-account-001",
  "constraints": {
    "rate_limit": "low",
    "destructive_tests": false,
    "external_discovery": false,
    "evidence_required": true
  },
  "human_review_required": false,
  "expires_at": "2026-05-02T12:00:00Z"
}
~~~

## Example Evidence Record

~~~json
{
  "evidence_id": "ev-demo-0001",
  "authorization_decision_id": "authz-demo-0001",
  "tool_action_request_id": "tar-demo-0001",
  "target_id": "webapp-001",
  "scope_id": "scope-demo-001",
  "tool": "zap",
  "operation": "authenticated_crawl",
  "credential_ref_used": "test-account-001",
  "secret_exposed_to_ai": false,
  "raw_artifact_ref": "private-artifacts/zap/raw/ev-demo-0001.json",
  "sanitized_artifact_ref": "evidence/sanitized/ev-demo-0001.json",
  "human_review_status": "pending"
}
~~~

## MVP Implementation Guidance

For the first local prototype:

- use fictitious credentials only,
- use a local mock Vault file excluded from Git,
- store only credential_ref and metadata in committed sample files,
- log resolution events without raw secrets,
- create sanitized output files safe for AI review,
- keep raw tool artifacts under ignored directories,
- demonstrate one successful allowed action,
- demonstrate one denied action,
- demonstrate one action requiring human approval.

## Security Requirements

The implementation must enforce:

- AI cannot read Vault contents.
- AI cannot resolve credential_ref.
- Tool Gateway cannot execute without authorization.
- Authorization Gateway cannot expose raw secrets.
- Sanitizer must run before AI receives tool results.
- Evidence must link request, decision, execution, result, and review.
- Raw artifacts must be protected and excluded from Git.
- credential_ref must be revocable.

## Non-Goals

This design does not attempt to solve:

- production-grade enterprise secret management,
- full PAM integration,
- all possible authentication workflows,
- multi-tenant SaaS isolation,
- regulatory certification,
- zero-trust architecture in full scope.

Those can be added after the MVP demonstrates the control pattern.
