# Issue 0176: Add v0.6.107 narrow public-safe AAEF main handback submittable text preparation candidate

## Summary

Add a v0.6.107 internal submittable text preparation candidate after v0.6.106 planned narrow public-safe AAEF main handback submittable text preparation controls.

## Acceptance criteria

* Add `docs/183-v06107-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate.md`.
* Add `planning/decisions/ADR-0177-add-v06107-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate.md`.
* Add this issue note.
* Add `tools/test_v06107_narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate.py`.
* Register the v0.6.107 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.106 submittable text preparation planning exists.
* Confirm the submittable text candidate is internal and documentation-only.
* Confirm the candidate is not submitted and not an opened AAEF main workflow.
* Confirm the two-layer public/private boundary is retained.
* Confirm no AAEF main issue, PR, release note, document change, handback package, or handback draft is created.
* Preserve public-safe evidence/interface lesson boundaries.
* Preserve no AAEF Core/Profile/Practical Package promotion.
* Preserve no public sample, validator, fixture, package, private review, public sample promotion, runtime, scanner, Docker, credential, customer, or delivery changes.

## Non-goals

* Do not prepare AAEF main handback material.
* Do not start AAEF main handback work.
* Do not open or draft AAEF main issue or PR content outside the internal candidate.
* Do not draft AAEF main release notes or document changes.
* Do not submit anything to AAEF main.
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
