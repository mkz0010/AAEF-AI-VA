# Issue 0247: Add v0.6.178 Public Demo Positioning candidate

## Summary

Create the Public Demo Positioning candidate as checkpoint 1 of 2 for the Medium-risk work item selected in v0.6.177.

## Acceptance criteria

* Add `docs/public-demo-positioning.md`.
* Add `docs/254-v06178-public-demo-positioning-candidate.md`.
* Add `planning/decisions/ADR-0248-add-v06178-public-demo-positioning-candidate.md`.
* Add this issue note.
* Add `tools/test_v06178_public_demo_positioning_candidate.py`.
* Register the v0.6.178 test in `tools/run_all_local_checks.py`.
* Confirm the positioning distinguishes non-execution, mock, fixture, local-only, runtime execution, scanner execution, and customer PoC demo boundaries.
* Confirm blocked execution can be a valid demo outcome.
* Confirm evidence trace should be the demo focus.
* Confirm the review/decision is deferred to v0.6.179.
* Confirm no safe demo creation, public demo creation, runtime/scanner readiness creation, real scanner execution selection, runtime execution selection, customer PoC intake selection, AAEF main publication, AAEF main issue/PR, issue command/URL, customer PoC approval, commercial contract, paid engagement approval, commercial license terms, customer-specific material, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not create a safe demo.
* Do not create a public demo.
* Do not authorize runtime or scanner execution.
* Do not authorize customer PoC intake.
* Do not create a commercial contract or commercial license terms.
* Do not reopen the AAEF main handback sequence.
