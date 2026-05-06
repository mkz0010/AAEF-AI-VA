# Issue 0103: Add v0.6.33 sanitized public sample planning

Status: Completed by v0.6.33 candidate  
Type: v0.6.33 planning / sanitized public sample boundary

## Goal

Plan sanitized public sample boundaries before generating public sample artifacts,
copying private generated artifacts into the public repository, running scanners,
enabling runtime execution, or authorizing delivery.

## Acceptance criteria

- [x] Add v0.6.33 sanitized public sample planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Define public sample scope.
- [x] Define candidate public directory placement.
- [x] Define sanitized artifact naming.
- [x] Define scenario coverage plan.
- [x] Define private-to-public transformation rules.
- [x] Define synthetic-only requirements.
- [x] Define publication hygiene checks.
- [x] Define patent-sensitive detail exclusion.
- [x] Define non-proof visibility.
- [x] Define overclaim prevention.
- [x] Define human publication review.
- [x] Preserve runtime/scanning/customer-target/delivery boundaries.

## Non-goals

- Generate public sample artifacts.
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
