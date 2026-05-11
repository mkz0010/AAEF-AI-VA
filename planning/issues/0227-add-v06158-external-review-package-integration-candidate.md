# Issue 0227: Add v0.6.158 External Review Package Integration candidate

## Summary

Create the External Review Package Integration candidate as checkpoint 1 of 2 for the Medium-risk work item selected in v0.6.157.

## Acceptance criteria

* Add `docs/external-review-package.md`.
* Add `docs/234-v06158-external-review-package-integration-candidate.md`.
* Add `planning/decisions/ADR-0228-add-v06158-external-review-package-integration-candidate.md`.
* Add this issue note.
* Add `tools/test_v06158_external_review_package_integration_candidate.py`.
* Register the v0.6.158 test in `tools/run_all_local_checks.py`.
* Include target reader, purpose, non-authorizing notice, document inventory, recommended entry points, reviewer paths, evidence/test-family index, boundary/non-goal summary, package-level claim-boundary summary, questions the package can/cannot answer, Safe PoC Boundary Template guidance, when not to request a PoC, outside-public-package boundary, explicit non-goals, and claim boundaries.
* Confirm no customer PoC approval, commercial contract creation, runtime/scanner/Docker/credential/customer/delivery approval, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not create a deployment guide, scanner operation guide, customer PoC authorization package, audit package, certification package, production readiness package, or external-framework equivalence mapping.
* Do not authorize a customer PoC.
* Do not create a commercial contract.
* Do not modify runtime behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
