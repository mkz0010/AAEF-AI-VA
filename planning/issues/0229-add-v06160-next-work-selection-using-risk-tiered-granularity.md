# Issue 0229: Add v0.6.160 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.159, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/236-v06160-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0230-add-v06160-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06160_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.160 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.159 closed the External Review Package Integration work item.
* Select Public Review Entry Point Polish as the next work item.
* Classify the selected work item as Medium risk.
* Assign two checkpoints to the selected work item.
* Confirm no README/public-entry modification, External Review Package modification, customer PoC approval, commercial contract, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, AAEF main issue, AAEF main PR, issue command, issue URL, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not modify the public review entry point in this checkpoint.
* Do not authorize a customer PoC in this checkpoint.
* Do not create a commercial contract.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
