# Issue 0154: Add v0.6.85 applied evidence handback preparation decision

## Summary

Add a v0.6.85 decision checkpoint after v0.6.84 closed the evidence-interface handback readiness candidate.

## Acceptance criteria

* Add `docs/161-v0685-applied-evidence-handback-preparation-decision.md`.
* Add `planning/decisions/ADR-0155-add-v0685-applied-evidence-handback-preparation-decision.md`.
* Add this issue note.
* Add `tools/test_v0685_applied_evidence_handback_preparation_decision.py`.
* Register the v0.6.85 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.84 readiness closeout exists.
* Select narrow public-safe AAEF main handback preparation planning as the next checkpoint.
* Confirm no AAEF main handback material is prepared.
* Confirm no AAEF main issue, PR, release note, document change, or handback text is created.
* Preserve public-safe evidence/interface lesson boundaries.
* Preserve no public sample, validator, fixture, package, private review, public sample promotion, runtime, scanner, Docker, credential, customer, or delivery changes.

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
* Do not generate packages or private review records.
* Do not promote public samples.
* Do not run scanners, run Docker, enable runtime execution, inject credentials, authorize customer targets, or authorize delivery.
