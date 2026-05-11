# Issue 0219: Add v0.6.150 Safe PoC Boundary Template review and decision

## Summary

Review and accept the Safe PoC Boundary Template candidate as checkpoint 2 of 2 for the Medium-risk work item selected in v0.6.148.

## Acceptance criteria

* Add `docs/226-v06150-safe-poc-boundary-template-review-and-decision.md`.
* Add `planning/decisions/ADR-0220-add-v06150-safe-poc-boundary-template-review-and-decision.md`.
* Add this issue note.
* Add `tools/test_v06150_safe_poc_boundary_template_review_and_decision.py`.
* Register the v0.6.150 test in `tools/run_all_local_checks.py`.
* Confirm `docs/safe-poc-boundary-template.md` exists and contains required PoC-boundary sections.
* Confirm non-authorizing notice, written authorization fields, parties/responsibilities, target scope, exclusions, time window, tool/action limits, AI request/gate boundary, credential/data handling, evidence retention/deletion, human review, stop conditions, communications/escalation, deliverables boundary, commercial/license boundary, pre-PoC checklist, not-allowed section, non-authorizing boundary, and claim boundaries.
* Confirm the Medium-risk work item is closed.
* Confirm no customer PoC approval, commercial contract creation, runtime/scanner/Docker/credential/customer/delivery approval, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not approve a customer PoC.
* Do not create a commercial contract.
* Do not approve runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
