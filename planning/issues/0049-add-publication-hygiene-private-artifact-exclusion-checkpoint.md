# Issue 0049: Add publication hygiene and private artifact exclusion checkpoint

Status: Completed by v0.3.7 candidate  
Type: publication hygiene / repository governance

## Goal

Add a publication hygiene checkpoint that prevents private/generated/local artifacts
from being accidentally tracked or published.

## Acceptance criteria

- [x] Add `.gitignore` coverage for private/generated/local artifacts.
- [x] Add publication hygiene documentation.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Confirm `private-not-in-git/` is excluded.
- [x] Confirm generated JSON/Markdown outputs are excluded.
- [x] Confirm Python caches are excluded.
- [x] Confirm publication hygiene does not imply runtime readiness.

## Non-goals

- Create a GitHub repository.
- Push to a remote.
- Decide public vs private repository visibility.
- Enable runtime execution.
- Enable ZAP, scans, external process execution, credential injection, or network activity.
- Complete third-party dependency license inventory.
