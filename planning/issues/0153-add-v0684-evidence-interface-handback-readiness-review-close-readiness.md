# Issue 0153: Add v0.6.84 evidence-interface handback readiness review and close-readiness

## Summary

Add a v0.6.84 checkpoint that reviews and closes the v0.6.83 evidence-interface handback readiness candidate.

## Acceptance criteria

* Add `docs/160-v0684-evidence-interface-handback-readiness-review-close-readiness.md`.
* Add `planning/decisions/ADR-0154-add-v0684-evidence-interface-handback-readiness-review-close-readiness.md`.
* Add this issue note.
* Add `tools/test_v0684_evidence_interface_handback_readiness_review_close_readiness.py`.
* Register the v0.6.84 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.83 readiness candidate exists.
* Confirm the readiness candidate is retained and close-ready.
* Confirm `public_safe_evidence_interface_boundary_lessons` is retained.
* Confirm no AAEF main handback material is prepared.
* Confirm no AAEF main issue, PR, release note, or document change is opened or drafted.
* Confirm AAEF Core/Profile/Practical Package promotion remains false.
* Confirm only evidence/interface-level lessons are retained.
* Confirm model-output-is-not-authority and validator-output-is-not-authority are preserved.
* Confirm implementation details, patent-sensitive detail, private artifacts, scanner output, credentials, customer material, delivery material, and overclaims are excluded.
* Confirm no public sample, validator, fixture metadata, JSON Schema, package, private review, public sample promotion, or runtime/scanner/Docker/credential/customer/delivery change occurs.

## Non-goals

* Do not prepare AAEF main handback material.
* Do not start AAEF main handback work.
* Do not open or draft AAEF main issue or PR content.
* Do not draft AAEF main release notes or document changes.
* Do not write AAEF main handback text.
* Do not submit anything to AAEF main.
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
* Do not run scanners, run Docker, enable runtime execution, inject credentials, authorize customer targets, or authorize delivery.
