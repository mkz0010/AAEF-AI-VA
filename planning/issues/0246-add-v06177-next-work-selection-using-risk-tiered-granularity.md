# Issue 0246: Add v0.6.177 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.176, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/253-v06177-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0247-add-v06177-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06177_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.177 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.176 closed the Current-State Executive Summary work item.
* Select Public Demo Positioning as the next work item.
* Classify the selected work item as Medium risk.
* Assign two checkpoints to the selected work item.
* Confirm no public demo positioning artifact creation, safe demo creation, public demo creation, runtime/scanner readiness creation, real scanner execution selection, runtime execution selection, customer PoC intake selection, AAEF main publication, AAEF main issue/PR, issue command/URL, customer PoC approval, commercial contract, paid engagement approval, commercial license terms, customer-specific material, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not create Public Demo Positioning in this checkpoint.
* Do not create a safe demo.
* Do not create a public demo.
* Do not authorize runtime or scanner execution.
* Do not authorize customer PoC intake.
* Do not create a commercial contract or commercial license terms.
* Do not reopen the AAEF main handback sequence.
