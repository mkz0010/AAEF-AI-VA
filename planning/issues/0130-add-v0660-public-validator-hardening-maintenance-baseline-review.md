# Issue 0130: Add v0.6.60 public validator hardening maintenance baseline review

## Summary

Add a v0.6.60 checkpoint that establishes a maintenance baseline after the v0.6.59 maintenance-first direction review.

## Acceptance criteria

* Add `docs/137-v0660-public-validator-hardening-maintenance-baseline-review.md`.
* Add `planning/decisions/ADR-0131-add-v0660-public-validator-hardening-maintenance-baseline-review.md`.
* Add this issue note.
* Add `tools/test_v0660_public_validator_hardening_maintenance_baseline_review.py`.
* Register the v0.6.60 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.59 maintenance direction review exists.
* Confirm maintenance baseline is documentation-only.
* Confirm all 13 negative fixture categories are retained.
* Confirm retained artifacts and baselines are documented.
* Confirm cleanup candidates are maintenance-only.
* Confirm validator behavior implementation readiness remains deferred.
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
