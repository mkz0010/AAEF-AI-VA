# Issue 0144: Add v0.6.74 public sample five-questions clarity candidate

## Summary

Add a v0.6.74 checkpoint that creates a narrow documentation-only public sample five-questions clarity candidate based on v0.6.73 planning.

## Acceptance criteria

* Add `docs/151-v0674-public-sample-five-questions-clarity-candidate.md`.
* Add `planning/decisions/ADR-0145-add-v0674-public-sample-five-questions-clarity-candidate.md`.
* Add this issue note.
* Add `tools/test_v0674_public_sample_five_questions_clarity_candidate.py`.
* Register the v0.6.74 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.73 clarity planning exists.
* Confirm the clarity candidate is documentation-only.
* Confirm the candidate preserves current public sample content.
* Confirm the candidate maps each AAEF five question to current sample reading guidance.
* Confirm the candidate distinguishes model request from authority.
* Confirm the candidate distinguishes static evidence-interface demonstration from live proof.
* Confirm the candidate explains where validator checks help and where they stop.
* Confirm runtime, scanner, Docker, credential, customer-target, and delivery prohibitions are preserved.
* Confirm no public sample content is changed.
* Confirm no sanitized public sample content is refined.
* Confirm no new reviewer walkthrough is created.
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
