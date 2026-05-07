# Issue 0128: Add v0.6.58 public validator behavior hardening scope review and close-readiness

## Summary

Add a v0.6.58 checkpoint that reviews the v0.6.57 documentation-only public validator behavior hardening scope and records close-readiness.

## Acceptance criteria

* Add `docs/135-v0658-public-validator-behavior-hardening-scope-review-close-readiness.md`.
* Add `planning/decisions/ADR-0129-add-v0658-public-validator-behavior-hardening-scope-review-close-readiness.md`.
* Add this issue note.
* Add `tools/test_v0658_public_validator_behavior_hardening_scope_review_close_readiness.py`.
* Register the v0.6.58 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.57 scope planning exists.
* Confirm v0.6.56 readiness review exists.
* Confirm the documentation-only scope is retained.
* Confirm all 13 negative fixture categories are retained in scope.
* Confirm the scope-planning track is close-ready.
* Confirm no validator behavior is modified.
* Confirm no validator output is added.
* Confirm no validator output contract is created.
* Confirm no metadata-level `expected_failure_category` field is added.
* Confirm no JSON Schema is added.
* Confirm no fixture metadata is rewritten.
* Confirm no fixtures are added.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not modify validator behavior.
* Do not add validator failure category output.
* Do not create a validator output contract.
* Do not add metadata-level failure category fields.
* Do not add JSON Schema.
* Do not rewrite fixture metadata.
* Do not add negative fixtures.
* Do not start validator behavior hardening implementation.
* Do not run scanners.
* Do not run Docker.
* Do not enable runtime execution.
* Do not inject credentials.
* Do not authorize customer targets.
* Do not authorize delivery.
