# Issue 0136: Add v0.6.66 applied evidence next-direction intake

## Summary

Add a v0.6.66 checkpoint that opens Applied Evidence next-direction intake after v0.6.65 closed out the public validator pause review.

## Acceptance criteria

* Add `docs/143-v0666-applied-evidence-next-direction-intake.md`.
* Add `planning/decisions/ADR-0137-add-v0666-applied-evidence-next-direction-intake.md`.
* Add this issue note.
* Add `tools/test_v0666_applied_evidence_next_direction_intake.py`.
* Register the v0.6.66 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.65 pause review closeout exists.
* Confirm Applied Evidence current-state review is selected for the next separate checkpoint.
* Confirm Applied Evidence implementation work is not started.
* Confirm no new Applied Evidence packages are generated.
* Confirm no new public samples are promoted.
* Confirm current public negative fixture set remains retained.
* Confirm all 13 negative fixture categories are retained.
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

* Do not start Applied Evidence implementation work.
* Do not generate new Applied Evidence packages.
* Do not generate private review records.
* Do not promote new public samples.
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
