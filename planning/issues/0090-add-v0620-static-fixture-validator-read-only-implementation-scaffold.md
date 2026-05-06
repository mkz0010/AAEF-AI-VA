# Issue 0090: Add v0.6.20 static fixture validator read-only implementation scaffold

Status: Completed by v0.6.20 candidate  
Type: v0.6.20 implementation scaffold / static fixture validator

## Goal

Add the smallest read-only static fixture validator scaffold after implementation readiness review, while preserving that full validation, negative tests, fixture generation, Docker, scanner, runtime, customer-target, and delivery activity remain blocked.

## Acceptance criteria

- [x] Add read-only validator scaffold at `tools/validate_static_lab_fixtures.py`.
- [x] Add checkpoint documentation.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Confirm scaffold compiles.
- [x] Confirm scaffold exposes a non-authorizing CLI boundary.
- [x] Confirm missing fixture directory fails closed.
- [x] Confirm invalid fixture directory fails closed.
- [x] Confirm runtime, Docker, scanner, credential, customer-target, and delivery authorization remain disabled.

## Non-goals

- Implement complete fixture schemas.
- Implement complete fixture validators.
- Implement negative tests.
- Generate fixture files.
- Commit sample fixture artifacts.
- Install Docker.
- Run Docker.
- Pull images.
- Start containers.
- Bind ports.
- Create Docker Compose files.
- Build a local lab.
- Enable runtime execution.
- Enable scanning.
- Authorize report delivery.
- Expose private advanced feature details.
