# Tool Gateway Mock Runner

## Purpose

This document describes the first executable Tool Gateway mock runner.

The runner is intentionally not connected to real tools. It validates the control flow before ZAP, Nmap, nuclei, Burp Suite, or Nessus integrations are added.

## Files

~~~text
prototypes/tool-gateway/
  models.py
  policy.py
  gateway.py
  runner.py

tools/
  run_tool_gateway_example.py
~~~

## Run Commands

## Complete Local Check

Run all local checks:

~~~bash
py tools/run_all_local_checks.py
~~~

Do not commit, merge, or tag if this command fails.


Run all scenarios:

~~~bash
py tools/run_tool_gateway_example.py all
~~~

Run individual scenarios:

~~~bash
py tools/run_tool_gateway_example.py allowed-action
py tools/run_tool_gateway_example.py denied-action
py tools/run_tool_gateway_example.py human-approval-required
~~~

## Expected Results

~~~text
allowed-action: completed
denied-action: blocked
human-approval-required: requires_human_approval
~~~

## Output Location

Generated outputs are written to:

~~~text
private-not-in-git/prototype-runs/
~~~

This path is intentionally ignored by Git.

## Safety

## Mock Vault Metadata

The runner loads secretless mock Vault metadata from:

~~~text
prototypes/tool-gateway/mock_vault/metadata.json
~~~

This metadata is used to validate credential_ref constraints. It must not contain raw secrets.


The mock runner:

- does not execute real tools,
- does not access customer systems,
- does not resolve real credentials,
- does not expose raw secrets to AI,
- does not write generated outputs into tracked directories by default.

## Next Step

## Self-Test Command

Run the Tool Gateway runner tests:

~~~bash
py tools/test_tool_gateway_runner.py
~~~

The tests cover positive scenarios, fail-closed negative scenarios, and generated runner outputs.


The next step is to validate generated outputs against schemas and then add explicit negative tests for mismatched authorization.
