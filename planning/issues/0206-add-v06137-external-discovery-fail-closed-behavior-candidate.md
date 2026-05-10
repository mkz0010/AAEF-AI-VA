# Issue 0206: Add v0.6.137 external discovery fail-closed behavior candidate

## Summary

Implement the external_discovery=true fail-closed behavior candidate as checkpoint 2 of 3 for the High-risk gate-semantics work item selected in v0.6.135.

## Acceptance criteria

* Add `tools/external_discovery_fail_closed.py`.
* Add `tools/test_external_discovery_fail_closed_behavior.py`.
* Add `docs/213-v06137-external-discovery-fail-closed-behavior-candidate.md`.
* Add `planning/decisions/ADR-0207-add-v06137-external-discovery-fail-closed-behavior-candidate.md`.
* Add this issue note.
* Add `tools/test_v06137_external_discovery_fail_closed_behavior_candidate.py`.
* Register candidate tests in `tools/run_all_local_checks.py`.
* Support deterministic evidence-safe external discovery comparison.
* Fail closed for missing explicit decision allowance, local-only/local-lab-only target boundary, missing/malformed destination binding, missing scope support, ambiguous target boundary, expired or invalid authorization, and malformed external_discovery flags.
* Continue existing checks for external_discovery=false, missing/not-required external_discovery, and explicitly allowed boundary-compatible external discovery.
* Return evidence-safe decision fields without raw secrets, raw credentials, tokens, private customer material, scanner output, private artifacts, full raw payloads, or live third-party target details.
* Confirm no runtime/scanner/Docker/credential/customer/delivery authorization, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
