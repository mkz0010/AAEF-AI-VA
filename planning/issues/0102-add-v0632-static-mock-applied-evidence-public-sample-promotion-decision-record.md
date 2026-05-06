# Issue 0102: Add v0.6.32 static/mock applied evidence public sample promotion decision record

Status: Completed by v0.6.32 candidate  
Type: v0.6.32 decision record / public sample promotion planning boundary

## Goal

Record the public sample promotion decision after the v0.6.31 private review record
without generating public samples, running scanners, enabling runtime execution, or
authorizing delivery.

## Acceptance criteria

- [x] Add v0.6.32 public sample promotion decision record.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Record decision inputs.
- [x] Record decision outcome.
- [x] Keep public sample generation unauthorized.
- [x] Allow only later sanitized public sample planning consideration.
- [x] Define later planning conditions.
- [x] Define remaining blockers to public generation.
- [x] Define AAEF-side reporting note.
- [x] Preserve runtime/scanning/customer-target/delivery boundaries.

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
