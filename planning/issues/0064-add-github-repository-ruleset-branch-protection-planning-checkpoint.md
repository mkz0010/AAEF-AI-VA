# Issue 0064: Add GitHub repository ruleset and branch protection planning checkpoint

Status: Completed by v0.5.5 candidate  
Type: repository governance / branch protection planning / release governance

## Goal

Plan GitHub repository rulesets and branch protection before changing repository
administration settings.

## Acceptance criteria

- [x] Add GitHub repository ruleset and branch protection planning documentation.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Record planned `main` branch protections.
- [x] Record planned required checks.
- [x] Record planned release tag protections.
- [x] Record high-risk change review expectations.
- [x] Record emergency exception planning.
- [x] Record maintainer responsibility planning.
- [x] Record GitHub administration checklist.
- [x] Confirm runtime execution remains disabled.

## Non-goals

- Configure GitHub branch protection.
- Configure GitHub rulesets.
- Configure tag protection.
- Require pull requests immediately.
- Create a commercial contract.
- Publish pricing.
- Provide legal advice.
- Enable runtime execution.
- Enable ZAP, scans, external process execution, credential injection, or network activity.
