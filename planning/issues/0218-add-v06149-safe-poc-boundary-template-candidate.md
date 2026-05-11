# Issue 0218: Add v0.6.149 Safe PoC Boundary Template candidate

## Summary

Create the Safe PoC Boundary Template candidate as checkpoint 1 of 2 for the Medium-risk work item selected in v0.6.148.

## Acceptance criteria

* Add `docs/safe-poc-boundary-template.md`.
* Add `docs/225-v06149-safe-poc-boundary-template-candidate.md`.
* Add `planning/decisions/ADR-0219-add-v06149-safe-poc-boundary-template-candidate.md`.
* Add this issue note.
* Add `tools/test_v06149_safe_poc_boundary_template_candidate.py`.
* Register the v0.6.149 test in `tools/run_all_local_checks.py`.
* Include target reader, purpose, non-authorizing notice, boundary summary, written authorization fields, parties/responsibilities, target scope, exclusions, time window, tool/action limits, AI request/gate boundary, credential/data handling, evidence retention/deletion, human review, stop conditions, communications/escalation, deliverables boundary, commercial/license boundary, pre-PoC checklist, not-allowed section, and claim boundaries.
* Confirm no customer PoC authorization, commercial contract, runtime/scanner/Docker/credential/customer/delivery authorization, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not authorize a customer PoC.
* Do not create a commercial contract.
* Do not modify runtime behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
