# Issue 0264: Add v0.6.195 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.194, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/271-v06195-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0265-add-v06195-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06195_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.195 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.194 closed the Safe Demo Fixture Set Creation work item.
* Select Repository Landing and Demo Path Clarity as the next work item.
* Classify the selected work item as Medium risk.
* Assign two checkpoints to the selected work item.
* Confirm no landing/demo clarity candidate artifact creation, additional fixture creation, public sample creation, safe demo creation, public demo creation, executable demo creation, runtime/scanner readiness creation, real scanner execution selection, runtime execution selection, customer PoC intake selection, AAEF main publication, AAEF main issue/PR, issue command/URL, customer PoC approval, commercial contract, paid engagement approval, commercial license terms, customer-specific material, validator behavior, schema, runtime, scanner, Docker, sensitive value, customer, delivery, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not create landing/demo clarity candidate content in this checkpoint.
* Do not create new fixture files.
* Do not create public samples.
* Do not create a public demo.
* Do not create an executable demo.
* Do not authorize runtime or scanner execution.
* Do not authorize customer PoC intake.
* Do not create a commercial contract or commercial license terms.
* Do not reopen the AAEF main handback sequence.
