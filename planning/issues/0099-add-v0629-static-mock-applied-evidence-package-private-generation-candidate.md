# Issue 0099: Add v0.6.29 static/mock applied evidence package private generation candidate

Status: Completed by v0.6.29 candidate  
Type: v0.6.29 private generation / static mock applied evidence package

## Goal

Generate the first private-first static/mock AAEF applied evidence package under
`private-not-in-git/` without running scanners, creating public samples, enabling
runtime execution, or authorizing delivery.

## Acceptance criteria

- [x] Add private static/mock package generator.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Generate package manifest.
- [x] Generate all four minimum scenarios.
- [x] Generate request, gate, dispatch, result, evidence, review, and non-proof artifacts.
- [x] Generate package-level reviewer walkthrough.
- [x] Generate package-level AAEF five questions mapping.
- [x] Validate representative identifier linkage.
- [x] Validate runtime/scanning/customer-target/delivery boundaries.
- [x] Keep generated artifacts private-first under `private-not-in-git/`.

## Non-goals

- Create public samples.
- Implement structural validators.
- Execute structural validator checks.
- Build a local diagnostic system.
- Run Docker.
- Run scanners.
- Pull images.
- Start containers.
- Bind ports.
- Enable runtime execution.
- Authorize report delivery.
- Expose private advanced feature details.
