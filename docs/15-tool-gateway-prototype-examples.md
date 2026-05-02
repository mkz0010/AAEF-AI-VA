# Tool Gateway Prototype Examples

## Purpose

This document explains the initial Tool Gateway prototype example contract flows.

These examples are not real scans. They are fictitious contract examples used to validate schema shape and control behavior before implementing real tool execution.

## Example Flow Set

The prototype example set contains three flows.

### 1. Allowed Action

Files:

- `prototypes/tool-gateway/examples/allowed-action.tool-action-request.json`
- `prototypes/tool-gateway/examples/allowed-action.authorization-decision.json`
- `prototypes/tool-gateway/examples/allowed-action.tool-execution-result.json`
- `prototypes/tool-gateway/examples/allowed-action.evidence-record.json`

Meaning:

A safe ZAP authenticated crawl is requested, authorized, completed, and linked to an evidence record.

### 2. Denied Action

Files:

- `prototypes/tool-gateway/examples/denied-action.tool-action-request.json`
- `prototypes/tool-gateway/examples/denied-action.authorization-decision.json`
- `prototypes/tool-gateway/examples/denied-action.tool-execution-result.json`
- `prototypes/tool-gateway/examples/denied-action.evidence-record.json`

Meaning:

A nuclei scan requiring external discovery is denied and blocked before execution.

### 3. Human Approval Required

Files:

- `prototypes/tool-gateway/examples/human-approval-required.tool-action-request.json`
- `prototypes/tool-gateway/examples/human-approval-required.authorization-decision.json`
- `prototypes/tool-gateway/examples/human-approval-required.tool-execution-result.json`
- `prototypes/tool-gateway/examples/human-approval-required.evidence-record.json`

Meaning:

An Nmap service version detection request is classified as requiring human approval and is not automatically executed.

## Validation

Run:

~~~bash
py tools/validate_mvp_schemas.py
py tools/validate_mvp_examples.py
~~~

## Safety Notes

The examples must remain fictitious.

They must not contain:

- real customer targets,
- raw credentials,
- API keys,
- session cookies,
- bearer tokens,
- real scan artifacts,
- real vulnerability data.

## Implementation Use

The next Tool Gateway runner should use these examples to validate behavior:

- allowed action returns completed,
- denied action returns blocked,
- human-approval-required action returns requires_human_approval,
- credential_ref is never resolved by AI,
- evidence records are emitted for reconstruction.
