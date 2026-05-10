# Issue 0193: Add v0.6.124 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.123, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/200-v06124-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0194-add-v06124-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06124_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.124 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.123 closed the README current/latest baseline clarity work item.
* Select SECURITY.md reporting-channel consistency as the next work item.
* Classify the selected work item as Medium risk.
* Assign two checkpoints to the selected work item.
* Confirm no SECURITY.md wording, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, AAEF main issue, AAEF main PR, issue command, issue URL, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not implement the SECURITY.md change in this checkpoint.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
