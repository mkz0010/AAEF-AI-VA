# Issue 0228: Add v0.6.159 External Review Package Integration review and decision

## Summary

Review and accept the External Review Package Integration candidate as checkpoint 2 of 2 for the Medium-risk work item selected in v0.6.157.

## Acceptance criteria

* Add `docs/235-v06159-external-review-package-integration-review-and-decision.md`.
* Add `planning/decisions/ADR-0229-add-v06159-external-review-package-integration-review-and-decision.md`.
* Add this issue note.
* Add `tools/test_v06159_external_review_package_integration_review_and_decision.py`.
* Register the v0.6.159 test in `tools/run_all_local_checks.py`.
* Confirm `docs/external-review-package.md` exists and contains required package sections.
* Confirm reader, purpose, non-authorizing notice, document inventory, recommended entry points, reviewer paths, evidence/test-family index, boundary/non-goal summary, package-level claim-boundary summary, can/cannot-answer questions, Safe PoC guidance, when-not-to-request-PoC guidance, outside-public-package boundary, explicit non-goals, and claim boundaries.
* Confirm the Medium-risk work item is closed.
* Confirm no customer PoC approval, commercial contract creation, runtime/scanner/Docker/credential/customer/delivery approval, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not create a deployment guide, scanner operation guide, audit package, certification package, production readiness package, or external-framework equivalence mapping.
* Do not approve a customer PoC.
* Do not create a commercial contract.
* Do not approve runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
