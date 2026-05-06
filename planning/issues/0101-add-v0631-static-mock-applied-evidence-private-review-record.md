# Issue 0101: Add v0.6.31 static/mock applied evidence private review record

Status: Completed by v0.6.31 candidate  
Type: v0.6.31 private review / static mock applied evidence package

## Goal

Generate a private review record for the v0.6.29 static/mock applied evidence package
under `private-not-in-git/` without promoting public samples, running scanners,
enabling runtime execution, or authorizing delivery.

## Acceptance criteria

- [x] Add private review-record generator.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Generate private review record JSON.
- [x] Generate private review record Markdown.
- [x] Generate promotion gate result JSON.
- [x] Generate promotion gate result Markdown.
- [x] Validate scenario coverage summary.
- [x] Validate promotion remains `keep_private`.
- [x] Validate runtime/scanning/customer-target/delivery boundaries.
- [x] Keep generated review artifacts private-first under `private-not-in-git/`.

## Non-goals

- Promote public samples.
- Generate public sample artifacts.
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
