# Issue 0233: Add v0.6.164 Buyer-Facing Commercial Inquiry Boundary candidate

## Summary

Create the Buyer-Facing Commercial Inquiry Boundary candidate as checkpoint 1 of 2 for the Medium-risk work item selected in v0.6.163.

## Acceptance criteria

* Add `docs/buyer-facing-commercial-inquiry-boundary.md`.
* Add a commercial inquiry boundary entry to `README.md`.
* Add `docs/240-v06164-buyer-facing-commercial-inquiry-boundary-candidate.md`.
* Add `planning/decisions/ADR-0234-add-v06164-buyer-facing-commercial-inquiry-boundary-candidate.md`.
* Add this issue note.
* Add `tools/test_v06164_buyer_facing_commercial_inquiry_boundary_candidate.py`.
* Register the v0.6.164 test in `tools/run_all_local_checks.py`.
* Select email-based inquiry as the contact model without committing an unapproved email address.
* Include allowed inquiry topics and topics requiring separate agreement.
* Include not-a-contract, no-paid-engagement, no-customer-PoC, no-runtime/scanner, no-credential/customer/delivery authorization language.
* Include relationship to External Review Package, Safe PoC Boundary Template, licensing/commercial-use boundaries, public/private material boundaries, and claim boundaries.
* Confirm no customer PoC approval, commercial contract creation, commercial license terms, paid engagement approval, customer-specific material, runtime/scanner/Docker/credential/customer/delivery approval, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not commit an unapproved public email address.
* Do not create commercial license terms.
* Do not approve a paid engagement.
* Do not authorize a customer PoC.
* Do not create a commercial contract.
* Do not modify runtime behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
