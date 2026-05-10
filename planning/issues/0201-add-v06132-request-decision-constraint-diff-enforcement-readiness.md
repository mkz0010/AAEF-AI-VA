# Issue 0201: Add v0.6.132 request/decision constraint-diff enforcement readiness

## Summary

Prepare request/decision constraint-diff enforcement readiness as checkpoint 1 of 3 for the High-risk gate-semantics work item selected in v0.6.131.

## Acceptance criteria

* Add `docs/208-v06132-request-decision-constraint-diff-enforcement-readiness.md`.
* Add `planning/decisions/ADR-0202-add-v06132-request-decision-constraint-diff-enforcement-readiness.md`.
* Add this issue note.
* Add `tools/test_v06132_request_decision_constraint_diff_enforcement_readiness.py`.
* Register the v0.6.132 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.131 selected request/decision constraint-diff enforcement as High risk with three checkpoints.
* Identify comparison inputs, target discovery, expected behavior, diff categories, fail-closed boundary, expected tests, evidence boundary, and non-goals.
* Confirm no constraint-diff behavior, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, AAEF main issue, AAEF main PR, issue command, issue URL, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not implement request/decision constraint-diff enforcement in this checkpoint.
* Do not modify constraint-diff behavior.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
