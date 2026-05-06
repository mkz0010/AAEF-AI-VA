# Issue 0110: Add v0.6.40 public example structural validator implementation candidate

Status: Completed by v0.6.40 candidate  
Type: v0.6.40 implementation candidate / public example structural validator

## Goal

Implement a read-only validator for the sanitized public sample artifact set without running scanners, enabling runtime execution, or authorizing delivery.

## Acceptance criteria

- [x] Add public example structural validator implementation candidate.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Validate package-level artifact presence.
- [x] Validate four-scenario coverage.
- [x] Validate scenario-level artifact presence.
- [x] Validate `.example.` naming.
- [x] Validate representative linkage.
- [x] Validate non-proof visibility.
- [x] Validate AAEF five-questions mapping visibility.
- [x] Validate publication hygiene status.
- [x] Validate publication review status.
- [x] Validate runtime/scanning/customer-target/delivery boundaries.
- [x] Preserve read-only/public-example-scoped behavior.

## Non-goals

- Build a local diagnostic system.
- Run Docker.
- Run scanners.
- Pull images.
- Start containers.
- Bind ports.
- Enable runtime execution.
- Authorize report delivery.
- Expose private advanced feature details.
