# Issue 0129: Add v0.6.59 public validator hardening maintenance direction review

## Summary

Add a v0.6.59 checkpoint that selects the conservative maintenance-first direction after v0.6.58 closed the documentation-only validator hardening scope track.

## Acceptance criteria

* Add `docs/136-v0659-public-validator-hardening-maintenance-direction-review.md`.
* Add `planning/decisions/ADR-0130-add-v0659-public-validator-hardening-maintenance-direction-review.md`.
* Add this issue note.
* Add `tools/test_v0659_public_validator_hardening_maintenance_direction_review.py`.
* Register the v0.6.59 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.58 scope close-readiness exists.
* Confirm maintenance-first direction is selected.
* Confirm validator behavior implementation readiness is deferred.
* Confirm all 13 negative fixture categories are retained.
* Confirm no validator behavior is modified.
* Confirm no validator output is added.
* Confirm no validator output contract is created.
* Confirm no metadata-level `expected_failure_category` field is added.
* Confirm no JSON Schema is added.
* Confirm no fixture metadata is rewritten.
* Confirm no fixtures are added.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not modify validator behavior.
* Do not add validator failure category output.
* Do not create a validator output contract.
* Do not add metadata-level failure category fields.
* Do not add JSON Schema.
* Do not rewrite fixture metadata.
* Do not add negative fixtures.
* Do not start validator behavior hardening implementation.
* Do not approve validator behavior hardening implementation readiness.
* Do not run scanners.
* Do not run Docker.
* Do not enable runtime execution.
* Do not inject credentials.
* Do not authorize customer targets.
* Do not authorize delivery.
