# Issue 0249: Add v0.6.180 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.179, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/256-v06180-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0250-add-v06180-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06180_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.180 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.179 closed the Public Demo Positioning work item.
* Select Commercial Inquiry Response Boundary as the next work item.
* Classify the selected work item as Medium risk.
* Assign two checkpoints to the selected work item.
* Confirm no commercial inquiry response boundary artifact creation, commercial response template creation, safe demo creation, public demo creation, runtime/scanner readiness creation, real scanner execution selection, runtime execution selection, customer PoC intake selection, AAEF main publication, AAEF main issue/PR, issue command/URL, customer PoC approval, commercial contract, paid engagement approval, commercial license terms, customer-specific material, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not create Commercial Inquiry Response Boundary in this checkpoint.
* Do not create a commercial inquiry response template.
* Do not create a safe demo.
* Do not create a public demo.
* Do not authorize runtime or scanner execution.
* Do not authorize customer PoC intake.
* Do not create a commercial contract or commercial license terms.
* Do not reopen the AAEF main handback sequence.
