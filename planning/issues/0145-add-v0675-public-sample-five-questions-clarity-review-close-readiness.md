# Issue 0145: Add v0.6.75 public sample five-questions clarity review and close-readiness

## Summary

Add a v0.6.75 checkpoint that reviews and closes the v0.6.74 public sample five-questions clarity candidate.

## Acceptance criteria

* Add `docs/152-v0675-public-sample-five-questions-clarity-review-close-readiness.md`.
* Add `planning/decisions/ADR-0146-add-v0675-public-sample-five-questions-clarity-review-close-readiness.md`.
* Add this issue note.
* Add `tools/test_v0675_public_sample_five_questions_clarity_review_close_readiness.py`.
* Register the v0.6.75 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.74 clarity candidate exists.
* Confirm the clarity candidate is retained.
* Confirm the clarity candidate is close-ready.
* Confirm current public sample content remains unchanged.
* Confirm no public sample content is refined.
* Confirm no public example text is changed.
* Confirm no new reviewer walkthrough is created.
* Confirm no public sample relationship-to-validator work is started.
* Confirm no AAEF main handback is prepared.
* Confirm Applied Evidence implementation work is not started.
* Confirm no new Applied Evidence packages are generated.
* Confirm no private review records are generated.
* Confirm no public samples are promoted.
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

* Do not refine sanitized public sample content.
* Do not change public example text.
* Do not create a new reviewer walkthrough.
* Do not start public sample relationship-to-validator review.
* Do not prepare AAEF main handback material.
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
