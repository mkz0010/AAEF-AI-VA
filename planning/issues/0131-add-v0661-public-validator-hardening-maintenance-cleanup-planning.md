# Issue 0131: Add v0.6.61 public validator hardening maintenance cleanup planning

## Summary

Add a v0.6.61 checkpoint that plans maintenance cleanup after the v0.6.60 documentation-only maintenance baseline review.

## Acceptance criteria

* Add `docs/138-v0661-public-validator-hardening-maintenance-cleanup-planning.md`.
* Add `planning/decisions/ADR-0132-add-v0661-public-validator-hardening-maintenance-cleanup-planning.md`.
* Add this issue note.
* Add `tools/test_v0661_public_validator_hardening_maintenance_cleanup_planning.py`.
* Register the v0.6.61 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.60 maintenance baseline review exists.
* Confirm cleanup planning is documentation-only.
* Confirm cleanup implementation is not approved.
* Confirm all 13 negative fixture categories are retained.
* Confirm retained artifacts and baselines are documented.
* Confirm cleanup candidates are ordered and maintenance-only.
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

* Do not implement cleanup in this checkpoint beyond the planning document and read-only test.
* Do not reorganize files.
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
