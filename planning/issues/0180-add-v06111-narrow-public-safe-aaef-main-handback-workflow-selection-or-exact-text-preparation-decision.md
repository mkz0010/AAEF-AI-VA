# Issue 0180: Add v0.6.111 narrow public-safe AAEF main handback workflow selection or exact text preparation decision

## Summary

Add a v0.6.111 decision checkpoint after v0.6.110 planned the narrow public-safe AAEF main handback submission workflow boundary.

## Acceptance criteria

* Add `docs/187-v06111-narrow-public-safe-aaef-main-handback-workflow-selection-or-exact-text-preparation-decision.md`.
* Add `planning/decisions/ADR-0181-add-v06111-narrow-public-safe-aaef-main-handback-workflow-selection-or-exact-text-preparation-decision.md`.
* Add this issue note.
* Add `tools/test_v06111_narrow_public_safe_aaef_main_handback_workflow_selection_or_exact_text_preparation_decision.py`.
* Register the v0.6.111 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.110 submission workflow planning exists.
* Select AAEF main issue workflow for planning.
* Select exact issue text preparation planning as the next checkpoint.
* Confirm no exact issue text, exact PR text, AAEF main issue, AAEF main PR, release note, document change, handback package, or handback draft is created.
* Preserve public-safe evidence/interface lesson boundaries.
* Preserve the two-layer public/private boundary.
* Preserve no AAEF Core/Profile/Practical Package promotion.
* Preserve no public sample, validator, fixture, package, private review, public sample promotion, runtime, scanner, Docker, credential, customer, or delivery changes.

## Non-goals

* Do not submit anything to AAEF main.
* Do not open or draft exact AAEF main issue or PR content.
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
