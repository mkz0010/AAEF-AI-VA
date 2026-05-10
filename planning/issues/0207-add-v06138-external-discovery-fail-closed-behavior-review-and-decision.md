# Issue 0207: Add v0.6.138 external discovery fail-closed behavior review and decision

## Summary

Review and accept the external_discovery=true fail-closed behavior candidate as checkpoint 3 of 3 for the High-risk gate-semantics work item selected in v0.6.135.

## Acceptance criteria

* Add `docs/214-v06138-external-discovery-fail-closed-behavior-review-and-decision.md`.
* Add `planning/decisions/ADR-0208-add-v06138-external-discovery-fail-closed-behavior-review-and-decision.md`.
* Add this issue note.
* Add `tools/test_v06138_external_discovery_fail_closed_behavior_review_and_decision.py`.
* Register the v0.6.138 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.137 helper and tests exist.
* Confirm deterministic external discovery comparison.
* Confirm fail-closed behavior for missing explicit decision allowance, allowance=false, local-only/local-lab-only target boundaries, missing/malformed destination binding, missing scope support, ambiguous target boundary, expired/invalid authorization, and malformed external_discovery flags.
* Confirm external_discovery=false, missing/not-required external_discovery, and explicitly allowed boundary-compatible external discovery continue existing checks.
* Confirm evidence-safe result fields avoid raw secrets, raw credentials, tokens, private customer material, scanner output, private artifacts, full raw payloads, and live third-party target details.
* Confirm the High-risk work item is closed.
* Confirm no runtime/scanner/Docker/credential/customer/delivery authorization, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
