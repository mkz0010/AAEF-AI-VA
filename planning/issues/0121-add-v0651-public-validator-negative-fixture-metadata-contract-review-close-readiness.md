# Issue 0121: Add v0.6.51 public validator negative fixture metadata contract review and close-readiness

## Summary

Add a v0.6.51 checkpoint that reviews the v0.6.50 public validator negative fixture metadata contract candidate and records close-readiness.

## Acceptance criteria

* Add `docs/128-v0651-public-validator-negative-fixture-metadata-contract-review-close-readiness.md`.
* Add `planning/decisions/ADR-0122-add-v0651-public-validator-negative-fixture-metadata-contract-review-close-readiness.md`.
* Add this issue note.
* Add `tools/test_v0651_public_validator_negative_fixture_metadata_contract_review_close_readiness.py`.
* Register the v0.6.51 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.50 candidate contract exists.
* Confirm v0.6.50 contract test exists.
* Re-run the v0.6.50 contract test.
* Confirm metadata contract close-readiness flags are documented.
* Confirm no JSON Schema is added.
* Confirm no fixture metadata is rewritten.
* Confirm no fixtures are added.
* Confirm validator behavior remains unchanged.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not add JSON Schema.
* Do not rewrite fixture metadata.
* Do not add negative fixtures.
* Do not modify validator behavior.
* Do not start validator failure category mapping implementation.
* Do not run scanners.
* Do not run Docker.
* Do not enable runtime execution.
* Do not inject credentials.
* Do not authorize customer targets.
* Do not authorize delivery.
