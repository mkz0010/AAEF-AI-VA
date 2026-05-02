# Generated Output Validation

## Purpose

This document records the v0.1.13 generated output validation update.

The project already validates static MVP examples. This update also validates generated Tool Gateway runner outputs under the ignored local private output directory.

## Why This Matters

Tool Gateway generated outputs are the objects that later components may consume.

If generated outputs drift away from schema contracts, the platform could accidentally treat internal implementation details as public execution results or evidence.

## Decision

Generated outputs are validated against the same MVP schemas used for static examples.

Validated generated files:

- `tool-execution-result.generated.json`
- `evidence-record.generated.json`

Default generated output directory:

~~~text
private-not-in-git/prototype-runs/
~~~

## Adapter Output Handling

Adapter output is internal Tool Gateway information.

It must not appear in public/generated `tool_execution_result` objects.

In particular, `_adapter_output` must not appear in generated public outputs.

Future versions may persist adapter output separately as an internal/private artifact after explicit sanitization and classification.

## Validation Command

Run all local checks:

~~~bash
py tools/run_all_local_checks.py
~~~

Or run generated output validation directly after generating outputs:

~~~bash
py tools/run_tool_gateway_example.py all
py tools/validate_generated_outputs.py
~~~

## Acceptance Criteria

- Generated tool execution results validate against `schemas/tool-execution-result.schema.json`.
- Generated evidence records validate against `schemas/evidence-record.schema.json`.
- `_adapter_output` does not appear in generated public outputs.
- `secret_exposed_to_ai` remains false.
