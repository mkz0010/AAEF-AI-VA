# 0008: Add Tool Gateway negative tests

## Status

In Progress

## Priority

P0

## Type

Prototype / Test

## Background

The Tool Gateway mock runner can process allowed, denied, and human-approval-required scenarios.

The next step is to demonstrate fail-closed behavior when request and authorization data are mismatched or unsafe.

## Decision Summary

Add a standard-library-only test script for the Tool Gateway mock runner.

The script validates:

- positive example scenarios,
- negative fail-closed scenarios,
- generated runner outputs.

## Acceptance Criteria

- allowed-action returns completed
- denied-action returns blocked
- human-approval-required returns requires_human_approval
- target_id mismatch is rejected
- scope_id mismatch is rejected
- tool mismatch is rejected
- operation mismatch is rejected
- credential_ref mismatch is rejected
- destructive_tests=true is rejected
- evidence_required=false is rejected
- invalid expiration is rejected
- generated outputs remain under ignored local paths
- `secret_exposed_to_ai` remains false

## Related Documents

- docs/17-tool-gateway-negative-tests.md
- docs/16-tool-gateway-mock-runner.md
- docs/13-tool-gateway-mvp-design.md
- planning/issues/0007-build-tool-gateway-mock-runner.md

## Remaining Work

- Add schema validation for generated outputs.
- Add mock Vault metadata tests.
- Add adapter stub tests.
- Add explicit missing authorization test once runner supports direct request-only invocation.
