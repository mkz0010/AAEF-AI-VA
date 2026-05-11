# Issue 0217: Add v0.6.148 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.147, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/224-v06148-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0218-add-v06148-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06148_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.148 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.147 closed the Technical Due Diligence Summary work item.
* Select Safe PoC Boundary Template as the next work item.
* Classify the selected work item as Medium risk.
* Assign two checkpoints to the selected work item.
* Confirm no Safe PoC Boundary Template, customer PoC authorization, commercial contract, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, AAEF main issue, AAEF main PR, issue command, issue URL, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not create the Safe PoC Boundary Template in this checkpoint.
* Do not authorize a customer PoC in this checkpoint.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
