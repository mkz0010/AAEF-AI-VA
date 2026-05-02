# Issue 0048: Add public repository readiness checkpoint

Status: Completed by v0.3.6 candidate  
Type: publication-readiness / repository governance

## Goal

Add a repository-level checkpoint that can be run before first public publication.

## Acceptance criteria

- [x] Add public repository readiness documentation.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Confirm AGPL-3.0 license visibility.
- [x] Confirm AAEF / CC BY 4.0 attribution visibility.
- [x] Confirm commercial licensing placeholder visibility.
- [x] Confirm private generated artifacts remain separated.
- [x] Confirm public-readiness does not imply runtime-readiness.

## Non-goals

- Create a GitHub repository.
- Push to a remote.
- Enable runtime execution.
- Enable ZAP, scans, external process execution, credential injection, or network activity.
- Finalize commercial contract wording.
