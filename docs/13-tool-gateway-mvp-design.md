# Tool Gateway MVP Design

## Purpose

This document defines the MVP design for the Tool Gateway in the AAEF-controlled AI Vulnerability Assessment Platform.

Tool Gateway is the controlled execution layer that turns authorized assessment actions into actual tool execution.

It is one of the most important trusted components in the project because it is the boundary between AI-generated requests and real diagnostic activity.

## Core Principle

AI may request a diagnostic action, but Tool Gateway decides what is actually executed after AAEF authorization.

Tool Gateway must not behave as a general-purpose shell, unrestricted automation agent, or blind executor of AI instructions.

## Design Position

Tool Gateway is not merely an integration wrapper.

It is a trusted control boundary responsible for:

- accepting only authorized tool action requests,
- enforcing target and scope constraints,
- resolving credential_ref only after authorization,
- injecting secrets without exposing them to AI,
- executing only approved tool operations,
- capturing raw artifacts,
- sending results to Sanitizer / Normalizer,
- recording evidence metadata,
- failing closed when required information is missing.

## Logical Flow

~~~text
AI / LLM
  ↓
tool_action_request
  ↓
AAEF Authorization Gateway
  ↓
authorization_decision
  ↓
Tool Gateway
  ↓
optional credential_ref resolution through Vault / Mock Vault
  ↓
approved tool runtime
  ↓
approved target
  ↓
raw artifact
  ↓
Sanitizer / Normalizer
  ↓
Evidence Store
  ↓
sanitized result for AI / human review
~~~

## MVP Responsibilities

### 1. Request Intake

Tool Gateway receives an authorized execution request.

The request must include or reference:

- tool_action_request_id,
- authorization_decision_id,
- target_id,
- scope_id,
- tool,
- operation,
- constraints,
- evidence_required,
- credential_ref if authentication is required.

Tool Gateway must reject requests that do not include a valid authorization decision.

### 2. Authorization Binding

Tool Gateway must verify that the execution request matches the authorization decision.

It should check:

- same target_id,
- same scope_id,
- same tool,
- same operation,
- same credential_ref where applicable,
- unexpired authorization decision,
- operation is not prohibited,
- evidence requirements are present.

Tool Gateway must not allow AI to modify the execution request after authorization in a way that expands scope.

### 3. Scope Enforcement

Tool Gateway must enforce scope before execution.

For MVP, scope enforcement may be simple but explicit.

It should validate:

- target_id is known,
- target alias maps to an approved demo target,
- operation is allowed for that target,
- external discovery is not allowed unless explicitly authorized,
- scan intensity is within the approved level.

### 4. Tool Adapter Selection

Tool Gateway routes authorized actions to controlled tool adapters.

Initial adapters:

- ZAP adapter,
- Nmap adapter,
- nuclei adapter,
- simple browser automation adapter where necessary.

Deferred adapters:

- Burp Suite adapter,
- Nessus / Tenable adapter,
- cloud posture adapter,
- custom exploit validation adapter.

### 5. credential_ref Resolution

When the action requires authentication, Tool Gateway may resolve credential_ref.

Resolution is allowed only when:

- authorization decision allows the credential_ref,
- credential_ref belongs to the approved scope,
- credential_ref is not expired,
- requested operation is allowed for that credential_ref,
- the action is not prohibited,
- evidence recording is enabled.

Tool Gateway must never return raw secret values to AI.

### 6. Secret Injection

Tool Gateway injects secrets only into the approved runtime.

Examples:

- ZAP authentication context,
- browser login workflow,
- API request header,
- controlled subprocess environment,
- temporary configuration file excluded from Git and logs.

Secrets must not be printed, logged, committed, or returned to AI.

### 7. Execution Control

Tool Gateway must execute only known operations.

MVP operations may include:

| Tool | Operation | Initial Status |
|---|---|---|
| ZAP | passive_scan | In scope |
| ZAP | authenticated_crawl | In scope with credential_ref |
| Nmap | safe_port_discovery | In scope |
| Nmap | service_version_detection | In scope with constraints |
| nuclei | safe_template_scan | In scope |
| browser | safe_login_check | Optional / limited |

Tool Gateway must not execute arbitrary AI-generated shell commands.

### 8. Artifact Capture

Tool Gateway captures raw artifacts from tools.

Raw artifacts may include sensitive data and must be stored in a protected or ignored location.

Examples:

- ZAP raw JSON,
- Nmap XML,
- nuclei JSONL,
- browser automation logs,
- screenshots where explicitly allowed,
- request/response samples where sanitized.

Raw artifacts must not be committed to Git.

### 9. Sanitizer / Normalizer Handoff

Tool Gateway must send raw artifacts to Sanitizer / Normalizer before AI analysis.

Sanitization should remove or mask:

- Authorization headers,
- Cookie headers,
- Set-Cookie headers,
- API keys,
- bearer tokens,
- session identifiers,
- passwords,
- personal data where possible,
- secrets injected by Tool Gateway.

### 10. Evidence Handoff

Tool Gateway must emit execution metadata for Evidence Store.

Evidence metadata should include:

- tool_execution_id,
- tool_action_request_id,
- authorization_decision_id,
- target_id,
- scope_id,
- tool,
- operation,
- credential_ref_used,
- credential_resolved_by,
- started_at,
- completed_at,
- decision_constraints_applied,
- raw_artifact_ref,
- sanitized_artifact_ref,
- execution_status,
- error_summary if any.

## Fail-Closed Conditions

Tool Gateway must fail closed when:

- authorization_decision_id is missing,
- authorization decision is denied,
- authorization decision is expired,
- target_id does not match authorization,
- scope_id does not match authorization,
- requested tool or operation differs from authorization,
- credential_ref differs from authorization,
- credential_ref is expired or revoked,
- required evidence cannot be recorded,
- requested operation is destructive but not explicitly approved,
- raw secret would be exposed to AI,
- sanitizer handoff fails for AI-visible output.

## MVP Action Model

## Schema Contract Dependency

Tool Gateway MVP implementation should consume and emit the schema contracts defined in `docs/14-mvp-schemas.md`.

The relevant schema files are:

- `schemas/tool-action-request.schema.json`
- `schemas/authorization-decision.schema.json`
- `schemas/tool-execution-result.schema.json`
- `schemas/evidence-record.schema.json`


An MVP tool action request may look like:

~~~json
{
  "tool_action_request_id": "tar-demo-0001",
  "requested_by": "ai-agent-demo",
  "action_type": "tool_execution",
  "target_id": "webapp-001",
  "scope_id": "scope-demo-001",
  "tool": "zap",
  "operation": "authenticated_crawl",
  "credential_ref": "test-account-001",
  "reason": "Perform a safe authenticated crawl of the approved demo application.",
  "requested_constraints": {
    "rate_limit": "low",
    "destructive_tests": false,
    "external_discovery": false,
    "evidence_required": true
  }
}
~~~

Tool Gateway must not execute this request directly. It must wait for an authorization decision.

## MVP Authorization Decision Binding

A matching authorization decision may look like:

~~~json
{
  "authorization_decision_id": "authz-demo-0001",
  "tool_action_request_id": "tar-demo-0001",
  "decision": "allow",
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
  "expires_at": "2026-05-02T12:00:00Z",
  "human_review_required": false
}
~~~

Tool Gateway must verify the binding before execution.

## MVP Execution Result

A Tool Gateway execution result may look like:

~~~json
{
  "tool_execution_id": "exec-demo-0001",
  "tool_action_request_id": "tar-demo-0001",
  "authorization_decision_id": "authz-demo-0001",
  "execution_status": "completed",
  "target_id": "webapp-001",
  "scope_id": "scope-demo-001",
  "tool": "zap",
  "operation": "authenticated_crawl",
  "credential_ref_used": "test-account-001",
  "secret_exposed_to_ai": false,
  "raw_artifact_ref": "private-not-in-git/raw-artifacts/zap/exec-demo-0001.json",
  "sanitized_artifact_ref": "evidence/sanitized/zap/exec-demo-0001.json",
  "started_at": "2026-05-02T10:00:00Z",
  "completed_at": "2026-05-02T10:03:00Z"
}
~~~

## Tool Adapter Model
## Adapter Stub Status

As of v0.1.12, Tool Gateway routes completed mock actions through adapter stubs.

The adapter stubs do not execute real tools. They validate the adapter boundary before real ZAP, Nmap, nuclei, or browser automation integrations are added.


Each tool adapter should expose a narrow set of approved operations.

For example:

~~~text
Tool Gateway
  ├─ zap_adapter
  │   ├─ passive_scan
  │   └─ authenticated_crawl
  ├─ nmap_adapter
  │   ├─ safe_port_discovery
  │   └─ service_version_detection
  ├─ nuclei_adapter
  │   └─ safe_template_scan
  └─ browser_adapter
      └─ safe_login_check
~~~

Adapters should not expose arbitrary command construction to AI.

## MVP Directory Guidance

Prototype code may later use a structure like:

~~~text
prototypes/tool-gateway/
  README.md
  gateway.py
  models.py
  policy.py
  adapters/
    zap_adapter.py
    nmap_adapter.py
    nuclei_adapter.py
    browser_adapter.py
  mock_vault/
    README.md
  examples/
    allowed-action.json
    denied-action.json
    human-approval-required.json
~~~

Sensitive mock secret files must remain under ignored paths.

## Relationship to AAEF

Tool Gateway implements the execution boundary that gives AAEF practical force.

AAEF Authorization Gateway decides whether an action is allowed. Tool Gateway ensures that only that allowed action is executed.

This preserves the principle:

Model output is not authority.

## MVP Success Criteria

Tool Gateway MVP is successful when it can demonstrate:

1. an allowed action is executed,
2. a denied action is not executed,
3. a human-approval-required action is not executed automatically,
4. credential_ref is resolved only after authorization,
5. raw secrets are not returned to AI,
6. raw artifacts are not committed to Git,
7. sanitized results are produced for AI analysis,
8. execution evidence links request, decision, execution, result, and review.

## Non-Goals

The MVP Tool Gateway does not initially need:

- production-grade multi-tenant isolation,
- enterprise PAM integration,
- full SIEM integration,
- complete Burp Suite automation,
- complete Nessus / Tenable integration,
- arbitrary exploit validation,
- autonomous attack chaining,
- production SaaS hardening.

Those are deferred until the core boundary model is proven.

## Internal Adapter Artifact Policy

Tool adapters may produce internal implementation artifacts.

Tool Gateway must not place raw adapter output directly into public generated result objects, evidence records, or AI-visible summaries.

Raw adapter artifacts should remain under ignored/private paths, and sanitized artifacts should be referenced explicitly.

See `docs/22-internal-adapter-artifact-policy.md`.

## Controlled Executor Policy

Tool Gateway command plans are not execution authority.

Before real tool execution is introduced, command plans must pass a controlled executor policy.

In the current MVP, the controlled executor is dry-run-only and rejects non-dry-run execution, arbitrary command fields, secret material, destructive tests, external discovery, and unsafe artifact paths.

See `docs/24-controlled-executor-policy.md`.
