# Issue 0184: Add v0.6.115 narrow public-safe AAEF main handback exact issue submission or pause decision

## Summary

Add a v0.6.115 decision checkpoint after v0.6.114 reviewed the internal exact AAEF main issue text candidate and marked it close-ready.

## Acceptance criteria

* Add `docs/191-v06115-narrow-public-safe-aaef-main-handback-exact-issue-submission-or-pause-decision.md`.
* Add `planning/decisions/ADR-0185-add-v06115-narrow-public-safe-aaef-main-handback-exact-issue-submission-or-pause-decision.md`.
* Add this issue note.
* Add `tools/test_v06115_narrow_public_safe_aaef_main_handback_exact_issue_submission_or_pause_decision.py`.
* Register the v0.6.115 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.114 exact issue text candidate review and close-readiness exists.
* Select human-maintainer-only submission checklist preparation as the next checkpoint.
* Confirm direct submission is not selected.
* Confirm pause is not selected.
* Confirm the close-ready exact issue text candidate remains internal-only and not submitted.
* Confirm no exact PR text, AAEF main issue, AAEF main PR, release note, document change, handback package, handback draft, issue URL, issue command, or checklist is created.
* Preserve public-safe evidence/interface lesson boundaries.
* Preserve the two-layer public/private boundary.
* Preserve no AAEF Core/Profile/Practical Package promotion.
* Preserve no public sample, validator, fixture, package, private review, public sample promotion, runtime, scanner, Docker, credential, customer, or delivery changes.

## Non-goals

* Do not submit anything to AAEF main.
* Do not open an AAEF main issue or PR.
* Do not create a human submission checklist in this checkpoint.
* Do not draft exact AAEF main PR content.
* Do not draft AAEF main release notes or document changes.
* Do not create a handback package or handback draft.
* Do not approve AAEF Core/Profile/Practical Package promotion.
* Do not modify validator behavior.
* Do not run scanners, run Docker, enable runtime execution, inject credentials, authorize customer targets, or authorize delivery.
