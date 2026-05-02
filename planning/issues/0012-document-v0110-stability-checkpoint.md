# 0012: Document v0.1.10 stability checkpoint

## Status

In Progress

## Priority

P0

## Type

Maintenance

## Background

v0.1.8 and v0.1.9 were tagged even though runner validation failed before v0.1.10.

The project should explicitly document the stable checkpoint and provide a single validation command before continuing with adapter stubs or real tool integration.

## Decision Summary

Record v0.1.10 as the stable Tool Gateway mock runner checkpoint.

Add a single local validation runner:

- `tools/run_all_local_checks.py`

Add stability checkpoint documentation:

- `docs/19-v0110-stability-checkpoint.md`

## Acceptance Criteria

- v0.1.10 is documented as the stable checkpoint
- v0.1.8 and v0.1.9 are marked as superseded validation-failure remediation steps
- a single local validation command is available
- validation command passes
- future workflow says not to commit, merge, or tag after failed validation

## Related Documents

- docs/16-tool-gateway-mock-runner.md
- docs/17-tool-gateway-negative-tests.md
- docs/18-mock-vault-credential-ref-validation.md
- docs/19-v0110-stability-checkpoint.md
- planning/decisions/ADR-0013-record-v0110-as-stable-local-checkpoint.md

## Remaining Work

- Use this stable checkpoint before adapter stubs.
- Consider adding generated output schema validation.
- Consider adding CI if the repository ever moves to a private remote.
