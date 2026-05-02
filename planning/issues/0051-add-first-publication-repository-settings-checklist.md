# Issue 0051: Add first-publication repository settings checklist

Status: Completed by v0.3.9 candidate  
Type: repository publication / governance / release preparation

## Goal

Add a first-publication checklist for GitHub repository settings and manual initial
publication decisions.

## Acceptance criteria

- [x] Add first-publication repository settings checklist.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Confirm repository visibility decision is treated as manual.
- [x] Confirm remote creation and push are not performed by the checkpoint.
- [x] Confirm branch protection/ruleset planning is documented but not configured.
- [x] Confirm runtime execution remains disabled.

## Non-goals

- Create a GitHub repository.
- Add `origin`.
- Push `main` or tags.
- Change repository visibility.
- Enable GitHub private vulnerability reporting.
- Configure branch protection or rulesets.
- Enable runtime execution.
- Enable ZAP, scans, external process execution, credential injection, or network activity.
