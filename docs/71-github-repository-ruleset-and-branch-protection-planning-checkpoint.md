# GitHub Repository Ruleset and Branch Protection Planning Checkpoint

Version: v0.5.5 candidate  
Status: repository protection planning only; does not configure GitHub rulesets

## Purpose

This checkpoint records planned GitHub repository protection rules for AAEF-AI-VA.

The goal is to prepare the repository for future collaboration, public review, and
commercial-readiness evaluation without immediately changing GitHub administration
settings.

This checkpoint is planning only.

This checkpoint does not configure GitHub branch protection.

This checkpoint does not configure GitHub rulesets.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Repository state

~~~text
Repository: https://github.com/mkz0010/AAEF-AI-VA
Visibility: public
Default branch: main
Public license: AGPL-3.0
Security policy: SECURITY.md
Private vulnerability reporting: enabled
GitHub Actions validation: enabled
Runtime execution: disabled
Live scanning: not authorized
Customer-target operation: not authorized
~~~

## Planned protection scope

The planned protection scope covers:

- the `main` branch,
- semantic version tags,
- release tags,
- GitHub Actions validation,
- high-risk runtime and scanning changes,
- security policy and vulnerability disclosure files,
- licensing and commercial-use boundary files,
- public README and repository metadata,
- private artifact exclusion boundaries.

## Planned `main` branch protections

Recommended future `main` branch protections:

1. Require pull request before merge.
2. Require status checks to pass before merge.
3. Require the GitHub Actions validation workflow before merge.
4. Restrict force pushes to `main`.
5. Restrict branch deletion for `main`.
6. Require review for high-risk changes.
7. Require explicit maintainer approval for release-boundary changes.
8. Preserve fast-forward or merge strategy deliberately according to project policy.
9. Keep `private-not-in-git/` untracked.
10. Keep sensitive vulnerability details out of public issues and pull requests.

This checkpoint does not apply these settings.

## Planned required checks

Required checks should include:

- `python -m compileall -q prototypes tools`,
- `tools/run_all_local_checks.py`,
- GitHub Actions workflow validation,
- README compatibility phrase registry test,
- licensing/trademark/authorship protection test,
- dependency and repository governance readiness test,
- repository ruleset and branch protection planning test.

The canonical local validation entry point remains:

~~~bash
python tools/run_all_local_checks.py
~~~

## Planned release tag protections

Recommended future release tag protections:

- protect semantic version tags such as `v0.5.5`,
- document who may create release tags,
- require local checks before tagging,
- require GitHub Actions verification after pushing tags,
- avoid moving or deleting published tags except for exceptional documented recovery,
- keep release notes aligned with public safety boundaries,
- avoid tagging when runtime, scanning, credential, or customer-target boundaries are unclear.

This checkpoint does not configure tag protection.

## High-risk change review expectations

High-risk changes should require explicit review before merge.

High-risk areas include:

- runtime execution,
- network activity,
- scanning,
- credential handling,
- target binding,
- customer-target operation,
- evidence capture of sensitive artifacts,
- report delivery authorization,
- private artifact handling,
- security disclosure process,
- AGPL-3.0 license boundary,
- commercial licensing boundary,
- trademark-like project-name usage,
- public claims about readiness, certification, legality, or auditability.

## Emergency exception planning

Emergency exceptions should be rare and documented.

An emergency exception should record:

- what happened,
- why normal review could not be followed,
- who approved the exception,
- what files changed,
- what tests were run,
- what follow-up validation is required,
- whether any release tag or public statement needs correction.

Emergency exceptions do not authorize runtime execution, scanning, credential
injection, or customer-target operation.

## Maintainer responsibility planning

Maintainer responsibilities should include:

- preserving safety boundaries,
- reviewing high-risk changes,
- keeping tests passing,
- keeping release tags intentional,
- avoiding unsupported legal or compliance claims,
- separating vulnerability reports from commercial inquiries,
- maintaining private artifact exclusion,
- documenting deviations from normal governance.

## GitHub administration checklist

Before enabling repository protection settings, review:

1. Required branch name: `main`.
2. Required status check name as displayed by GitHub Actions.
3. Whether pull requests should be required for solo-maintained work.
4. Whether emergency direct pushes should remain possible.
5. Whether tag protection or rulesets are available for the repository plan.
6. Whether private vulnerability reporting remains enabled.
7. Whether branch protection would block planned local release workflow.
8. Whether documentation should be updated after settings are enabled.

## Relationship to existing checkpoints

This checkpoint builds on:

- `docs/55-public-repository-readiness-checkpoint.md`,
- `docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md`,
- `docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md`,
- `docs/60-github-actions-ci-scaffold.md`,
- `docs/65-github-release-publication-checkpoint.md`,
- `docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md`,
- `docs/69-licensing-trademark-authorship-protection-checkpoint.md`,
- `docs/70-dependency-and-repository-governance-readiness-checkpoint.md`.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
execution_authorized = false
preflight_satisfied = false
ready_for_runtime_execution = false
real_execution_permitted = false
external_process_execution_allowed = false
network_activity_allowed = false
scan_execution_allowed = false
credential_injection_permitted = false
raw_artifact_capture_permitted = false
customer_target = false
external_network_target = false
~~~

## Claims to avoid

Do not claim that this checkpoint provides:

- GitHub branch protection configured,
- GitHub rulesets configured,
- tag protection configured,
- mandatory pull request workflow enabled,
- production deployment approval,
- runtime execution readiness,
- scan authorization,
- customer-target authorization,
- compliance certification,
- legal approval,
- audit opinion.

## Required local checks

Before tagging v0.5.5, verify:

1. README links to this checkpoint.
2. Planned `main` branch protections are recorded.
3. Planned required checks are recorded.
4. Planned release tag protections are recorded.
5. High-risk change review expectations are recorded.
6. Emergency exception planning is recorded.
7. Maintainer responsibility planning is recorded.
8. GitHub administration checklist is recorded.
9. Runtime and scanning boundaries remain disabled.
10. Claims to avoid are recorded.
11. `tools/run_all_local_checks.py` includes the repository ruleset and branch protection planning test.

## Out of scope

This checkpoint does not:

- configure GitHub branch protection,
- configure GitHub rulesets,
- configure tag protection,
- require pull requests immediately,
- change repository visibility,
- create a commercial contract,
- publish pricing,
- provide legal advice,
- authorize runtime execution,
- authorize scan execution,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
