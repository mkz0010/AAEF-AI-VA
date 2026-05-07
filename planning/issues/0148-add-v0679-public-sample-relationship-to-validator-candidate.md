# Issue 0148: Add v0.6.79 public sample relationship-to-validator candidate

## Summary

Add a v0.6.79 checkpoint that creates a narrow documentation-only public sample relationship-to-validator candidate based on v0.6.78 planning.

## Acceptance criteria

* Add `docs/155-v0679-public-sample-relationship-to-validator-candidate.md`.
* Add `planning/decisions/ADR-0149-add-v0679-public-sample-relationship-to-validator-candidate.md`.
* Add this issue note.
* Add `tools/test_v0679_public_sample_relationship_to_validator_candidate.py`.
* Register the v0.6.79 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.78 relationship planning exists.
* Confirm the relationship candidate is documentation-only.
* Confirm the candidate preserves current public sample content.
* Confirm the candidate preserves current validator behavior.
* Confirm the candidate preserves current validator output.
* Confirm the candidate preserves current fixture metadata.
* Confirm the candidate explains what the public sample is for.
* Confirm the candidate explains what the public validator checks.
* Confirm the candidate explains what the public validator does not check.
* Confirm the candidate explains how negative fixtures relate to validator posture.
* Confirm the candidate states validator output is not authority.
* Confirm the candidate states validator success does not authorize execution.
* Confirm the candidate states documentation-only failure category mapping is not validator output.
* Confirm the candidate states documentation-only failure category mapping is not a validator output contract.
* Confirm no public sample content is changed.
* Confirm no sanitized public sample content is refined.
* Confirm no validator behavior is modified.
* Confirm no validator output is added or changed.
* Confirm no validator output contract is created.
* Confirm no fixture metadata is changed.
* Confirm no negative fixtures are added.
* Confirm no JSON Schema is added.
* Confirm no new reviewer walkthrough is created.
* Confirm no AAEF main handback is prepared.
* Confirm Applied Evidence implementation work is not started.
* Confirm no new Applied Evidence packages are generated.
* Confirm no private review records are generated.
* Confirm no public samples are promoted.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not modify validator behavior.
* Do not add validator failure category output.
* Do not create a validator output contract.
* Do not refine sanitized public sample content.
* Do not change public example text.
* Do not create a new reviewer walkthrough.
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
