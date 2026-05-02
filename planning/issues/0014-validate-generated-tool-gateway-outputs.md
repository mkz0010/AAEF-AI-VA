# 0014: Validate generated Tool Gateway outputs

## Status

In Progress

## Priority

P0

## Type

Validation

## Background

Tool Gateway now uses adapter stubs. Generated outputs need to remain schema-conformant and must not expose internal adapter data.

## Decision Summary

Add generated output validation for:

- generated tool execution results,
- generated evidence records.

Also ensure `_adapter_output` does not appear in generated public outputs.

## Acceptance Criteria

- Generated `tool-execution-result.generated.json` files validate against schema
- Generated `evidence-record.generated.json` files validate against schema
- `_adapter_output` is not included in generated public outputs
- `secret_exposed_to_ai` remains false
- `run_all_local_checks.py` includes generated output validation
- Adapter output remains tested separately through adapter tests

## Related Documents

- docs/21-generated-output-validation.md
- docs/20-tool-gateway-adapter-stubs.md
- docs/14-mvp-schemas.md
- planning/decisions/ADR-0015-validate-generated-tool-gateway-outputs.md
