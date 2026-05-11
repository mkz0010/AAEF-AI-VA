# Issue 0221: Add v0.6.152 Control Matrix candidate

## Summary

Create the Control Matrix candidate as checkpoint 1 of 2 for the Medium-risk work item selected in v0.6.151.

## Acceptance criteria

* Add `docs/control-matrix.md`.
* Add `docs/228-v06152-control-matrix-candidate.md`.
* Add `planning/decisions/ADR-0222-add-v06152-control-matrix-candidate.md`.
* Add this issue note.
* Add `tools/test_v06152_control_matrix_candidate.py`.
* Register the v0.6.152 test in `tools/run_all_local_checks.py`.
* Include target reader, purpose, non-authorizing notice, row design, matrix rows, interpretation limits, and claim boundaries.
* Include matrix rows for AI request, gate decision, authorization expiry, constraint drift, external discovery, mock/dry-run status, non-execution evidence, human approval, credential/data handling, public/private artifact boundary, report/delivery boundary, PoC non-authorization, commercial/license boundary, and conservative claim boundaries.
* Confirm no customer PoC approval, commercial contract creation, runtime/scanner/Docker/credential/customer/delivery approval, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not create a compliance matrix, audit checklist, or certification checklist.
* Do not authorize a customer PoC.
* Do not create a commercial contract.
* Do not modify runtime behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
