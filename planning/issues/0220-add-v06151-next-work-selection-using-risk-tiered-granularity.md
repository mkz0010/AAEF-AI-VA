# Issue 0220: Add v0.6.151 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.150, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/227-v06151-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0221-add-v06151-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06151_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.151 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.150 closed the Safe PoC Boundary Template work item.
* Select Control Matrix as the next work item.
* Classify the selected work item as Medium risk.
* Assign two checkpoints to the selected work item.
* Confirm no Control Matrix, customer PoC approval, commercial contract, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, AAEF main issue, AAEF main PR, issue command, issue URL, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not create the Control Matrix in this checkpoint.
* Do not authorize a customer PoC in this checkpoint.
* Do not create a commercial contract.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
