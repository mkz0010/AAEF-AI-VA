# Issue 0208: Add v0.6.139 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.138, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/215-v06139-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0209-add-v06139-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06139_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.139 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.138 closed the external_discovery=true fail-closed behavior work item.
* Select mock/dry-run `completed` status terminology cleanup as the next work item.
* Classify the selected work item as Medium risk.
* Assign two checkpoints to the selected work item.
* Confirm no mock/dry-run status wording, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, AAEF main issue, AAEF main PR, issue command, issue URL, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not rename mock/dry-run `completed` status in this checkpoint.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
