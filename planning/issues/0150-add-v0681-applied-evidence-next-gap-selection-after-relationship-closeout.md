# Issue 0150: Add v0.6.81 applied evidence next gap selection after relationship closeout

## Summary

Add a v0.6.81 checkpoint that selects the next Applied Evidence gap after v0.6.80 closed the public sample relationship-to-validator candidate.

## Acceptance criteria

* Add `docs/157-v0681-applied-evidence-next-gap-selection-after-relationship-closeout.md`.
* Add `planning/decisions/ADR-0151-add-v0681-applied-evidence-next-gap-selection-after-relationship-closeout.md`.
* Add this issue note.
* Add `tools/test_v0681_applied_evidence_next_gap_selection_after_relationship_closeout.py`.
* Register the v0.6.81 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.80 relationship closeout exists.
* Confirm evidence-interface handback readiness is selected as the next gap.
* Confirm evidence-interface handback readiness planning is not started.
* Confirm AAEF main handback material is not prepared.
* Confirm no AAEF main handback work is started or submitted.
* Confirm no public sample content is changed.
* Confirm no sanitized public sample content is refined.
* Confirm no validator behavior is modified.
* Confirm no validator output is added or changed.
* Confirm no validator output contract is created.
* Confirm no fixture metadata is changed.
* Confirm no negative fixtures are added.
* Confirm no JSON Schema is added.
* Confirm no new reviewer walkthrough is created.
* Confirm Applied Evidence implementation work is not started.
* Confirm no new Applied Evidence packages are generated.
* Confirm no private review records are generated.
* Confirm no public samples are promoted.
* Confirm current public negative fixture set remains retained.
* Confirm all 13 negative fixture categories are retained.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not start evidence-interface handback readiness planning.
* Do not prepare AAEF main handback material.
* Do not start AAEF main handback work.
* Do not modify validator behavior.
* Do not add validator failure category output.
* Do not create a validator output contract.
* Do not refine sanitized public sample content.
* Do not change public example text.
* Do not create a new reviewer walkthrough.
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
