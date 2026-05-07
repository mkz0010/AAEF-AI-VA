# Issue 0119: Add v0.6.49 public validator negative fixture metadata contract readiness review

## Summary

Add a v0.6.49 readiness review for a future public validator negative fixture metadata contract.

## Acceptance criteria

* Add `docs/126-v0649-public-validator-negative-fixture-metadata-contract-readiness-review.md`.
* Add `planning/decisions/ADR-0120-add-v0649-public-validator-negative-fixture-metadata-contract-readiness-review.md`.
* Add this issue note.
* Add `tools/test_v0649_public_validator_negative_fixture_metadata_contract_readiness_review.py`.
* Register the v0.6.49 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.48 hardening planning exists.
* Confirm the existing v0.6.46 fixture metadata has enough information to support a future contract.
* Confirm required candidate fields and boundary flags are documented.
* Confirm no metadata contract is implemented yet.
* Confirm no fixture metadata is rewritten.
* Confirm validator behavior remains unchanged.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not implement the metadata contract.
* Do not add schemas.
* Do not rewrite fixture metadata.
* Do not add negative fixtures.
* Do not modify validator behavior.
* Do not run scanners.
* Do not run Docker.
* Do not enable runtime execution.
* Do not inject credentials.
* Do not authorize customer targets.
* Do not authorize delivery.
