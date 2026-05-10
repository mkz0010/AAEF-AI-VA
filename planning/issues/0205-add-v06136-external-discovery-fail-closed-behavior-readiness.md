# Issue 0205: Add v0.6.136 external discovery fail-closed behavior readiness

## Summary

Prepare external_discovery=true fail-closed behavior readiness as checkpoint 1 of 3 for the High-risk gate-semantics work item selected in v0.6.135.

## Acceptance criteria

* Add `docs/212-v06136-external-discovery-fail-closed-behavior-readiness.md`.
* Add `planning/decisions/ADR-0206-add-v06136-external-discovery-fail-closed-behavior-readiness.md`.
* Add this issue note.
* Add `tools/test_v06136_external_discovery_fail_closed_behavior_readiness.py`.
* Register the v0.6.136 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.135 selected external_discovery=true fail-closed behavior as High risk with three checkpoints.
* Identify current semantics to inspect, target discovery, target-boundary inputs, expected behavior, fail-closed boundary, expected tests, evidence boundary, and non-goals.
* Confirm no external_discovery behavior, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, AAEF main issue, AAEF main PR, issue command, issue URL, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not implement external_discovery fail-closed behavior in this checkpoint.
* Do not modify external_discovery behavior.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
