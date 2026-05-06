# Issue 0105: Add v0.6.35 sanitized public sample generation candidate

Status: Completed by v0.6.35 candidate  
Type: v0.6.35 public example / sanitized sample generation candidate

## Goal

Generate a sanitized public sample candidate under
`examples/applied-evidence/sanitized-static-mock/` without copying private generated
artifacts, running scanners, enabling runtime execution, or authorizing delivery.

## Acceptance criteria

- [x] Add sanitized public sample generator.
- [x] Add public sample candidate artifacts under `examples/applied-evidence/sanitized-static-mock/`.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Generate package-level example artifacts.
- [x] Generate all four scenario example artifacts.
- [x] Validate `.example.` naming.
- [x] Validate representative request-to-evidence linkage.
- [x] Validate non-proof statements.
- [x] Validate publication hygiene report.
- [x] Preserve runtime/scanning/customer-target/delivery boundaries.

## Non-goals

- Copy private generated artifacts into the public repository.
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
