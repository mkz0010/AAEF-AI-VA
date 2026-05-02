# ADR-0015: Validate generated Tool Gateway outputs against MVP schemas

## Status

Accepted

## Context

The project validates static example contract files, but Tool Gateway runner outputs are generated dynamically under ignored local directories.

Generated outputs can drift from schema contracts if the runner adds internal implementation fields or changes output shape.

In v0.1.12, adapter stubs introduced internal adapter output. That data is useful internally but should not appear in public/generated Tool Gateway result records.

## Decision

Add generated output validation for Tool Gateway runner outputs.

Generated `tool-execution-result.generated.json` files must validate against `schemas/tool-execution-result.schema.json`.

Generated `evidence-record.generated.json` files must validate against `schemas/evidence-record.schema.json`.

Internal adapter output must not appear in generated public outputs.

## Consequences

- Tool Gateway generated outputs are constrained by the same schema contracts as examples.
- Adapter internals remain separated from AI-visible and evidence-facing objects.
- `run_all_local_checks.py` becomes a stronger safety gate before commits and tags.
- Future internal adapter artifact persistence must be explicitly designed rather than added into public result objects.
