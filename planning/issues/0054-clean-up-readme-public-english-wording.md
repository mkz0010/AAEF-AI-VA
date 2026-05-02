# Issue 0054: Clean up README public English wording

Status: Completed by v0.4.2 candidate  
Type: README / public presentation / repository polish

## Goal

Clean up README wording so the public repository entry point is English-first and
does not contain internal Japanese local-management phrasing.

## Acceptance criteria

- [x] Remove or replace Japanese local-management wording from README.
- [x] Replace Japanese AI authority statement with English wording.
- [x] Preserve the AAEF authority boundary.
- [x] Add documentation for the README wording cleanup.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Confirm runtime execution remains disabled.

## Non-goals

- Translate all repository docs.
- Add a Japanese README.
- Change repository visibility.
- Create a GitHub release.
- Enable runtime execution.
- Enable ZAP, scans, external process execution, credential injection, or network activity.
