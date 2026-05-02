# Release Governance and Maintainer Operations Checklist

Version: v0.5.6 candidate  
Status: release operations checklist; does not configure GitHub settings

## Purpose

This checkpoint records the maintainer release workflow for AAEF-AI-VA.

The goal is to make the current release process explicit before changing repository
administration settings such as branch protection or rulesets.

This checkpoint is an operations checklist only.

This checkpoint does not configure GitHub branch protection.

This checkpoint does not configure GitHub rulesets.

This checkpoint does not configure tag protection.

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

## Standard release workflow

The standard release workflow is:

1. Start from clean `main`.
2. Pull latest `origin/main` with fast-forward only.
3. Create a scoped feature branch.
4. Apply the narrow planned change.
5. Run the targeted test.
6. Run `tools/run_all_local_checks.py`

Compatibility phrase: `python tools/run_all_local_checks.py`.
7. Inspect `git status` and `git diff --stat`.
8. Commit only after all local checks pass.
9. Switch back to `main`.
10. Fast-forward merge the feature branch.
11. Delete the local feature branch.
12. Create a semantic version tag.
13. Push `main`.
14. Push the semantic version tag.
15. Verify GitHub Actions after push.
16. Confirm working tree is clean.
17. Review the latest log entry.

## Pre-release checklist

Before creating a release commit, verify:

- the branch name is scoped to the change,
- the change has a narrow checkpoint purpose,
- the new documentation has a matching ADR and planning issue,
- the new targeted test is registered in `tools/run_all_local_checks.py`,
- `tools/run_all_local_checks.py` passes locally,
- `private-not-in-git/` remains untracked,
- no secrets, credentials, customer materials, pricing notes, or generated private artifacts are staged,
- runtime and scanning boundaries remain disabled,
- public claims do not imply production readiness, certification, legal approval, audit opinion, or scan authorization.

## Commit and merge checklist

Before merging to `main`, verify:

- `git status` shows only intended tracked/untracked files,
- `git diff --stat` matches the expected scope,
- the commit message is concise and scoped,
- the feature branch contains only the intended checkpoint,
- all local checks passed before the commit,
- fast-forward merge is possible,
- the feature branch can be deleted after merge.

## Tag and push checklist

Before pushing a release tag, verify:

- the tag follows semantic versioning,
- the tag is not already present locally or remotely,
- `main` points to the intended release commit,
- the release commit is the current `HEAD`,
- the tag points to the intended release commit,
- `git push origin main` completes successfully,
- `git push origin <tag>` completes successfully,
- GitHub Actions are checked after push.

## GitHub Actions verification checklist

After push, verify:

- GitHub Actions started for the pushed commit,
- the validation workflow completed successfully,
- the workflow corresponds to the intended commit,
- no unrelated failing workflow is ignored without review,
- any failure is investigated before further release steps,
- the final repository state is recorded in the conversation or local notes.

## Private artifact checklist

Before and after release, verify:

- `private-not-in-git/` is not tracked,
- generated local test outputs remain under `private-not-in-git/`,
- private sales materials remain under `private-not-in-git/`,
- release-note drafts under `private-not-in-git/` are not staged unless intentionally public,
- no customer-specific material is committed,
- no secrets or credentials are committed,
- no sensitive vulnerability details are committed.

Suggested check:

~~~bash
git ls-files private-not-in-git
~~~

The expected result is no tracked files.

## Emergency exception checklist

Emergency exceptions should be rare.

If normal release governance cannot be followed, record:

- what happened,
- why normal workflow could not be followed,
- who approved the exception,
- what files changed,
- what tests were run,
- whether `tools/run_all_local_checks.py` was skipped or failed,
- what remediation is required,
- whether a follow-up checkpoint is needed,
- whether any public release note or tag needs correction.

Emergency exceptions do not authorize runtime execution, scanning, credential
injection, or customer-target operation.

## Post-release review checklist

After each release, verify:

- `git status` is clean,
- `main` is up to date with `origin/main`,
- the new tag exists locally,
- the new tag exists remotely,
- the latest log shows `HEAD -> main`, the new tag, and `origin/main`,
- GitHub Actions passed for the pushed commit,
- README links remain valid,
- CHANGELOG and ROADMAP include the new checkpoint,
- no private artifacts were tracked,
- the next-step recommendation is documented.

## Relationship to existing checkpoints

This checkpoint builds on:

- `docs/60-github-actions-ci-scaffold.md`,
- `docs/65-github-release-publication-checkpoint.md`,
- `docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md`,
- `docs/69-licensing-trademark-authorship-protection-checkpoint.md`,
- `docs/70-dependency-and-repository-governance-readiness-checkpoint.md`,
- `docs/71-github-repository-ruleset-and-branch-protection-planning-checkpoint.md`.

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

Before tagging v0.5.6, verify:

1. README links to this checklist.
2. Standard release workflow is recorded.
3. Pre-release checklist is recorded.
4. Commit and merge checklist is recorded.
5. Tag and push checklist is recorded.
6. GitHub Actions verification checklist is recorded.
7. Private artifact checklist is recorded.
8. Emergency exception checklist is recorded.
9. Post-release review checklist is recorded.
10. Runtime and scanning boundaries remain disabled.
11. Claims to avoid are recorded.
12. `tools/run_all_local_checks.py` includes the release governance maintainer operations test.

## Out of scope

This checkpoint does not:

- configure GitHub branch protection,
- configure GitHub rulesets,
- configure tag protection,
- require pull requests immediately,
- create a commercial contract,
- publish pricing,
- provide legal advice,
- authorize runtime execution,
- authorize scan execution,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
