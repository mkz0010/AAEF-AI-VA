# Issue 0177: Add v0.6.108 narrow public-safe AAEF main handback submittable text preparation candidate review and close-readiness

## Summary

Add a v0.6.108 checkpoint that reviews and closes the v0.6.107 internal narrow public-safe AAEF main handback submittable text preparation candidate.

## Acceptance criteria

* Add `docs/184-v06108-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate-review-close-readiness.md`.
* Add `planning/decisions/ADR-0178-add-v06108-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate-review-close-readiness.md`.
* Add this issue note.
* Add `tools/test_v06108_narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate_review_close_readiness.py`.
* Register the v0.6.108 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.107 submittable text preparation candidate exists.
* Confirm the submittable text preparation candidate is retained and close-ready.
* Confirm candidate text remains internal and non-submitted.
* Confirm no AAEF main issue, PR, release note, document change, submittable workflow, handback package, or handback draft is created.
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
