# Issue 0237: Add v0.6.168 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.167, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/244-v06168-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0238-add-v06168-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06168_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.168 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.167 closed the Maintainer Inquiry Address Publication work item.
* Select Public Entry and Inquiry Route Consistency Review as the next work item.
* Classify the selected work item as Medium risk.
* Assign two checkpoints to the selected work item.
* Confirm no consistency review creation, README public-entry modification, commercial inquiry modification, inquiry address publication modification, customer PoC approval, commercial contract, paid engagement approval, commercial license terms, customer-specific materials, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, AAEF main issue, AAEF main PR, issue command, issue URL, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not create the Public Entry and Inquiry Route Consistency Review in this checkpoint.
* Do not modify README public/commercial inquiry language in this checkpoint.
* Do not modify the inquiry address publication in this checkpoint.
* Do not authorize a customer PoC in this checkpoint.
* Do not create a commercial contract or commercial license terms.
* Do not approve a paid engagement.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
