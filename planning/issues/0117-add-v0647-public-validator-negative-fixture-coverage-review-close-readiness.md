# Issue 0117: Add v0.6.47 public validator negative fixture coverage review and close-readiness

## Summary

Add a v0.6.47 checkpoint that reviews the v0.6.46 public validator negative fixture implementation candidate and closes the first negative fixture track.

## Acceptance criteria

* Add `docs/124-v0647-public-validator-negative-fixture-coverage-review-close-readiness.md`.
* Add `planning/decisions/ADR-0118-add-v0647-public-validator-negative-fixture-coverage-review-close-readiness.md`.
* Add this issue note.
* Add `tools/test_v0647_public_validator_negative_fixture_coverage_review_close_readiness.py`.
* Register the v0.6.47 test in `tools/run_all_local_checks.py`.
* Confirm the v0.6.46 fixture set contains 13 expected categories.
* Confirm fixture metadata remains static, synthetic, public-safe, and non-authorizing.
* Confirm positive control preservation.
* Confirm validator behavior is not modified.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not add new negative fixtures.
* Do not modify validator behavior.
* Do not run scanners.
* Do not run Docker.
* Do not enable runtime execution.
* Do not inject credentials.
* Do not authorize customer targets.
* Do not authorize delivery.
