# Issue 0197: Add v0.6.128 authorization expiry current-time check readiness

## Summary

Prepare authorization expiry current-time check readiness as checkpoint 1 of 3 for the High-risk gate-semantics work item selected in v0.6.127.

## Acceptance criteria

* Add `docs/204-v06128-authorization-expiry-current-time-check-readiness.md`.
* Add `planning/decisions/ADR-0198-add-v06128-authorization-expiry-current-time-check-readiness.md`.
* Add this issue note.
* Add `tools/test_v06128_authorization_expiry_current_time_check_readiness.py`.
* Register the v0.6.128 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.127 selected authorization expiry checked against current time as High risk with three checkpoints.
* Identify target discovery, expected behavior, tests to add or update, fail-closed boundary, current-time source boundary, and non-goals.
* Confirm no authorization behavior, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, AAEF main issue, AAEF main PR, issue command, issue URL, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not implement the authorization expiry current-time check in this checkpoint.
* Do not modify authorization behavior.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
