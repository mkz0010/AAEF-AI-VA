# Issue 0116: Add v0.6.46 public validator negative fixture implementation candidate

Status: Completed by v0.6.46 candidate
Type: v0.6.46 implementation candidate / public validator negative fixtures

## Goal

Implement synthetic, public-safe, static negative fixtures and a read-only harness test for the existing public example structural validator without modifying validator behavior, running scanners, enabling runtime execution, or authorizing delivery.

## Acceptance criteria

- [x] Add v0.6.46 public validator negative fixture implementation candidate documentation.
- [x] Add ADR recording the decision.
- [x] Add issue/planning record.
- [x] Add fixture root under `examples/applied-evidence/public-validator-negative-fixtures/`.
- [x] Add synthetic, public-safe, static fixtures for all v0.6.44 planned negative categories.
- [x] Add fixture metadata with expected blocker categories.
- [x] Add fixture index.
- [x] Add read-only local harness test.
- [x] Confirm positive control remains passing.
- [x] Confirm negative fixtures fail closed with expected blockers.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Preserve runtime/scanning/customer-target/delivery boundaries.

## Non-goals

- Modify validator behavior.
- Build a local diagnostic system.
- Run Docker.
- Run scanners.
- Pull images.
- Start containers.
- Bind ports.
- Enable runtime execution.
- Authorize report delivery.
- Expose private advanced feature details.
