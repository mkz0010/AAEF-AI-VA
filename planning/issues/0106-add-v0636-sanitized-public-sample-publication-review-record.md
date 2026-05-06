# Issue 0106: Add v0.6.36 sanitized public sample publication review record

Status: Completed by v0.6.36 candidate  
Type: v0.6.36 public example / publication review record

## Goal

Generate a publication review record for the sanitized public sample candidate under
`examples/applied-evidence/sanitized-static-mock/` without running scanners, enabling
runtime execution, or authorizing delivery.

## Acceptance criteria

- [x] Add sanitized public sample publication review generator.
- [x] Generate publication review record artifacts under the public example directory.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Validate package-level artifact presence.
- [x] Validate four-scenario coverage.
- [x] Validate `.example.` naming.
- [x] Validate representative linkage.
- [x] Validate non-proof visibility.
- [x] Validate publication hygiene status.
- [x] Preserve runtime/scanning/customer-target/delivery boundaries.

## Non-goals

- Implement structural validators.
- Execute validator checks.
- Build a local diagnostic system.
- Run Docker.
- Run scanners.
- Pull images.
- Start containers.
- Bind ports.
- Enable runtime execution.
- Authorize report delivery.
- Expose private advanced feature details.
