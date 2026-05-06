# Issue 0108: Add v0.6.38 public example structural validation planning

Status: Completed by v0.6.38 candidate  
Type: v0.6.38 planning / public example structural validation

## Goal

Plan structural validation for the sanitized public sample artifact set without
implementing validator code, running scanners, enabling runtime execution, or
authorizing delivery.

## Acceptance criteria

- [x] Add public example structural validation planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Define validation input scope.
- [x] Define planned validation objectives.
- [x] Define planned required-artifact checks.
- [x] Define planned scenario checks.
- [x] Define planned naming checks.
- [x] Define planned linkage checks.
- [x] Define planned scenario posture checks.
- [x] Define planned non-proof checks.
- [x] Define planned AAEF five-questions checks.
- [x] Define planned publication hygiene checks.
- [x] Define planned runtime boundary checks.
- [x] Define planned failure categories.
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
