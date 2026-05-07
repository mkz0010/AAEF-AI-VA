# Issue 0147: Add v0.6.78 public sample relationship-to-validator planning

## Summary

Add a v0.6.78 checkpoint that plans public sample relationship-to-validator clarity after v0.6.76 selected it as the next Applied Evidence gap.

## Acceptance criteria

* Add `docs/154-v0678-public-sample-relationship-to-validator-planning.md`.
* Add `planning/decisions/ADR-0148-add-v0678-public-sample-relationship-to-validator-planning.md`.
* Add this issue note.
* Add `tools/test_v0678_public_sample_relationship_to_validator_planning.py`.
* Register the v0.6.78 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.76 next-gap selection exists.
* Confirm public sample relationship-to-validator planning is documentation-only.
* Confirm public sample relationship-to-validator implementation is not started.
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
* Confirm current public negative fixture set remains retained.
* Confirm all 13 negative fixture categories are retained.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not start public sample relationship-to-validator implementation work.
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
