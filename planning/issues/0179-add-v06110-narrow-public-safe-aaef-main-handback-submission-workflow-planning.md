# Issue 0179: Add v0.6.110 narrow public-safe AAEF main handback submission workflow planning

## Summary

Add a v0.6.110 planning checkpoint after v0.6.109 selected narrow public-safe AAEF main handback submission workflow planning.

## Acceptance criteria

* Add `docs/186-v06110-narrow-public-safe-aaef-main-handback-submission-workflow-planning.md`.
* Add `planning/decisions/ADR-0180-add-v06110-narrow-public-safe-aaef-main-handback-submission-workflow-planning.md`.
* Add this issue note.
* Add `tools/test_v06110_narrow_public_safe_aaef_main_handback_submission_workflow_planning.py`.
* Register the v0.6.110 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.109 submission-or-pause decision exists.
* Confirm submission workflow planning is documentation-only.
* Confirm no workflow is selected or executed.
* Confirm no exact issue text, exact PR text, release note text, document-change text, or handback package is created.
* Preserve public-safe evidence/interface lesson boundaries.
* Preserve the two-layer public/private boundary.
* Preserve no AAEF Core/Profile/Practical Package promotion.
* Preserve no public sample, validator, fixture, package, private review, public sample promotion, runtime, scanner, Docker, credential, customer, or delivery changes.

## Non-goals

* Do not submit anything to AAEF main.
* Do not open or draft AAEF main issue or PR content.
* Do not draft AAEF main release notes or document changes.
* Do not create a handback package or handback draft.
* Do not approve AAEF Core/Profile/Practical Package promotion.
* Do not decide lesson promotion to AAEF main.
* Do not modify validator behavior.
* Do not add validator failure category output.
* Do not create a validator output contract.
* Do not refine sanitized public sample content.
* Do not change public example text.
* Do not generate packages or private review records.
* Do not promote public samples.
* Do not run scanners, run Docker, enable runtime execution, inject credentials, authorize customer targets, or authorize delivery.
