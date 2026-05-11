# Issue 0224: Add v0.6.155 Reviewer Walkthrough candidate

## Summary

Create the Reviewer Walkthrough candidate as checkpoint 1 of 2 for the Medium-risk work item selected in v0.6.154.

## Acceptance criteria

* Add `docs/reviewer-walkthrough.md`.
* Add `docs/231-v06155-reviewer-walkthrough-candidate.md`.
* Add `planning/decisions/ADR-0225-add-v06155-reviewer-walkthrough-candidate.md`.
* Add this issue note.
* Add `tools/test_v06155_reviewer_walkthrough_candidate.py`.
* Register the v0.6.155 test in `tools/run_all_local_checks.py`.
* Include target reader, purpose, non-authorizing notice, suggested reading sequence, first-pass review path, technical due-diligence path, PoC-boundary path, Control Matrix path, evidence/test-family path, claim-boundary path, questions before PoC, reviewer outputs, interpretation limits, explicit non-goals, and claim boundaries.
* Confirm no customer PoC approval, commercial contract creation, runtime/scanner/Docker/credential/customer/delivery approval, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not create a deployment guide, scanner operation guide, audit checklist, certification package, or production readiness review.
* Do not authorize a customer PoC.
* Do not create a commercial contract.
* Do not modify runtime behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
