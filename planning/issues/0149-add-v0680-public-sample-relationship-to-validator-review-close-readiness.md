# Issue 0149: Add v0.6.80 public sample relationship-to-validator review and close-readiness

## Summary

Add a v0.6.80 checkpoint that reviews and closes the v0.6.79 public sample relationship-to-validator candidate.

## Acceptance criteria

* Add `docs/156-v0680-public-sample-relationship-to-validator-review-close-readiness.md`.
* Add `planning/decisions/ADR-0150-add-v0680-public-sample-relationship-to-validator-review-close-readiness.md`.
* Add this issue note.
* Add `tools/test_v0680_public_sample_relationship_to_validator_review_close_readiness.py`.
* Register the v0.6.80 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.79 relationship candidate exists.
* Confirm the relationship candidate is retained.
* Confirm the relationship candidate is close-ready.
* Confirm current public sample content remains unchanged.
* Confirm current validator behavior remains unchanged.
* Confirm current validator output remains unchanged.
* Confirm current fixture metadata remains unchanged.
* Confirm no public sample content is refined.
* Confirm no public example text is changed.
* Confirm no validator output contract is created.
* Confirm no evidence-interface handback readiness planning is started.
* Confirm no AAEF main handback is prepared.
* Confirm Applied Evidence implementation work is not started.
* Confirm no new Applied Evidence packages are generated.
* Confirm no private review records are generated.
* Confirm no public samples are promoted.
* Confirm current public negative fixture set remains retained.
* Confirm all 13 negative fixture categories are retained.
* Confirm validator behavior implementation readiness remains deferred.
* Confirm no metadata-level `expected_failure_category` field is added.
* Confirm no JSON Schema is added.
* Confirm no fixture metadata is rewritten.
* Confirm no fixtures are added.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not modify validator behavior.
* Do not add validator failure category output.
* Do not create a validator output contract.
* Do not refine sanitized public sample content.
* Do not change public example text.
* Do not create a new reviewer walkthrough.
* Do not start evidence-interface handback readiness planning.
* Do not prepare AAEF main handback material.
* Do not start Applied Evidence implementation work.
* Do not generate new Applied Evidence packages.
* Do not generate private review records.
* Do not promote new public samples.
* Do not reorganize files.
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
