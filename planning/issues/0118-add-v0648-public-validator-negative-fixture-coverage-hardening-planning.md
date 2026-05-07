# Issue 0118: Add v0.6.48 public validator negative fixture coverage hardening planning

## Summary

Add a v0.6.48 planning checkpoint for future public validator negative fixture coverage hardening after v0.6.47 closed the first negative fixture track.

## Acceptance criteria

* Add `docs/125-v0648-public-validator-negative-fixture-coverage-hardening-planning.md`.
* Add `planning/decisions/ADR-0119-add-v0648-public-validator-negative-fixture-coverage-hardening-planning.md`.
* Add this issue note.
* Add `tools/test_v0648_public_validator_negative_fixture_coverage_hardening_planning.py`.
* Register the v0.6.48 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.47 close-readiness exists.
* Confirm the v0.6.46 fixture set remains present.
* Confirm the 13 existing categories are still recognized.
* Confirm v0.6.48 remains planning-only.
* Confirm no new fixtures are required.
* Confirm validator behavior remains unchanged.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not add negative fixtures.
* Do not rewrite negative fixtures.
* Do not modify validator behavior.
* Do not run scanners.
* Do not run Docker.
* Do not enable runtime execution.
* Do not inject credentials.
* Do not authorize customer targets.
* Do not authorize delivery.
