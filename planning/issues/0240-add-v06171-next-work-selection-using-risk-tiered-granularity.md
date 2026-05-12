# Issue 0240: Add v0.6.171 next work selection using risk-tiered granularity

## Summary

Apply the v0.6.120 checkpoint granularity policy by selecting the next work item after v0.6.170, assigning its risk tier, and assigning its checkpoint count.

## Acceptance criteria

* Add `docs/247-v06171-next-work-selection-using-risk-tiered-granularity.md`.
* Add `planning/decisions/ADR-0241-add-v06171-next-work-selection-using-risk-tiered-granularity.md`.
* Add this issue note.
* Add `tools/test_v06171_next_work_selection_using_risk_tiered_granularity.py`.
* Register the v0.6.171 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.170 closed the Public Entry and Inquiry Route Consistency Review work item.
* Select AAEF Team Inquiry Address Reflection Proposal as the next work item.
* Classify the selected work item as Medium risk.
* Assign two checkpoints to the selected work item.
* Confirm no proposal creation, proposal sending, AAEF main repository modification, AAEF main contact publication change, AAEF main issue/PR, issue command/URL, AAEF main handback reopening, customer PoC approval, commercial contract, paid engagement approval, commercial license terms publication, customer-specific materials, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not create the AAEF Team Inquiry Address Reflection Proposal in this checkpoint.
* Do not send a proposal to the AAEF team in this checkpoint.
* Do not modify AAEF main in this checkpoint.
* Do not publish or modify AAEF main contact information in this checkpoint.
* Do not open an AAEF main issue or PR.
* Do not generate an issue command or issue URL.
* Do not reopen the AAEF main handback sequence.
* Do not authorize a customer PoC.
* Do not create a commercial contract or commercial license terms.
* Do not approve a paid engagement.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
