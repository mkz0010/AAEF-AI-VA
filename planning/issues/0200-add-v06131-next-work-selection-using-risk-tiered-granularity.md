# Issue 0200: Add v0.6.131 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.130, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/207-v06131-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0201-add-v06131-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06131_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.131 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.130 closed the authorization expiry current-time check work item.
* Select request/decision constraint-diff enforcement as the next work item.
* Classify the selected work item as High risk.
* Assign three checkpoints to the selected work item.
* Confirm no constraint-diff behavior, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, AAEF main issue, AAEF main PR, issue command, issue URL, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not implement request/decision constraint-diff enforcement in this checkpoint.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
