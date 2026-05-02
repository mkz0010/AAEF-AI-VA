# Tool Gateway Prototype

## Purpose

This directory contains the MVP prototype scaffold for the Tool Gateway.

The prototype is intended to validate the control flow before integrating real tools such as ZAP, Nmap, nuclei, Burp Suite, or Nessus.

## Prototype Goal

The first prototype should demonstrate:

1. an allowed action,
2. a denied action,
3. an action requiring human approval,
4. credential_ref remains reference-only,
5. raw secrets are not visible to AI,
6. Tool Gateway does not execute without authorization,
7. execution results can be linked to evidence records.

## Current Contents
## Adapter Stubs

The prototype includes adapter stubs for:

- ZAP
- Nmap
- nuclei
- browser automation

These adapters do not execute real tools. They expose narrow allowed operations and return mock artifact references.


~~~text
prototypes/tool-gateway/
  README.md
  examples/
    allowed-action.tool-action-request.json
    allowed-action.authorization-decision.json
    allowed-action.tool-execution-result.json
    allowed-action.evidence-record.json
    denied-action.tool-action-request.json
    denied-action.authorization-decision.json
    denied-action.tool-execution-result.json
    denied-action.evidence-record.json
    human-approval-required.tool-action-request.json
    human-approval-required.authorization-decision.json
    human-approval-required.tool-execution-result.json
    human-approval-required.evidence-record.json
  mock_vault/
    README.md
~~~

## Important Rules

- Do not put raw credentials in this repository.
- Do not put real customer scan artifacts in this repository.
- Do not put real customer contracts or target materials in this repository.
- Keep raw artifacts under ignored paths such as `private-not-in-git/`.
- Keep examples fictitious and safe.

## Expected Next Step

## Running the Mock Runner

## Mock Vault Metadata Validation

The mock runner now validates credential_ref against:

- target_id,
- scope_id,
- allowed tools,
- allowed operations,
- expiry,
- revocation status.

See `docs/18-mock-vault-credential-ref-validation.md`.


## Running Tests

Run the Tool Gateway runner self-tests from the repository root:

~~~bash
py tools/test_tool_gateway_runner.py
~~~

Expected final line:

~~~text
Tool Gateway runner tests passed.
~~~


Run all mock scenarios from the repository root:

~~~bash
py tools/run_tool_gateway_example.py all
~~~

Expected statuses:

~~~text
allowed-action: completed
denied-action: blocked
human-approval-required: requires_human_approval
~~~

Generated outputs are written under `private-not-in-git/prototype-runs/`.


The next implementation step is to add a minimal Python prototype that:

- loads a tool action request,
- loads an authorization decision,
- checks binding,
- returns blocked / requires_human_approval / completed mock result,
- emits an evidence record.
