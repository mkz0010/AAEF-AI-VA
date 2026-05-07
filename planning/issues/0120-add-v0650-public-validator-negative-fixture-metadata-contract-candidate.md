# Issue 0120: Add v0.6.50 public validator negative fixture metadata contract candidate

## Summary

Add a v0.6.50 candidate metadata contract for public validator negative fixtures.

## Acceptance criteria

* Add `docs/127-v0650-public-validator-negative-fixture-metadata-contract-candidate.md`.
* Add `planning/decisions/ADR-0121-add-v0650-public-validator-negative-fixture-metadata-contract-candidate.md`.
* Add this issue note.
* Add `tools/test_v0650_public_validator_negative_fixture_metadata_contract_candidate.py`.
* Register the v0.6.50 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.49 readiness review exists.
* Confirm required metadata fields are documented.
* Confirm required runtime boundary flags are documented.
* Confirm all existing v0.6.46 negative fixture metadata files satisfy the candidate contract.
* Confirm no metadata is rewritten.
* Confirm no fixtures are added.
* Confirm validator behavior remains unchanged.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not add JSON Schema.
* Do not rewrite fixture metadata.
* Do not add negative fixtures.
* Do not modify validator behavior.
* Do not run scanners.
* Do not run Docker.
* Do not enable runtime execution.
* Do not inject credentials.
* Do not authorize customer targets.
* Do not authorize delivery.
