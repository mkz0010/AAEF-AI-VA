# First-Publication Repository Settings Checklist

Version: v0.3.9 candidate  
Status: repository publication settings checklist; does not create a remote repository

## Purpose

This checklist prepares AAEF-AI-VA for the first GitHub repository publication.

It does not create a remote repository, push code, change repository visibility, or
authorize runtime execution.

The goal is to make the first publication deliberate and reversible until the author
chooses a final publication path.

## Recommended publication posture

Recommended approach:

~~~text
Initial remote: private or staged private-first
Review state: complete local checks, inspect repository contents, verify README rendering
Publication target: public after final manual review
Commercial service implementation: separate private repository
~~~

AAEF-AI-VA can eventually be public because it is intended to demonstrate the
reference implementation boundary, safety gates, evidence flow, and AGPL/commercial
licensing posture.

However, the first remote can be private while final repository settings and public
presentation are reviewed.

## Visibility decision

Before first publication, decide one of:

| Option | Use when | Notes |
| --- | --- | --- |
| Private-first | final review is still in progress | Safest initial GitHub import path |
| Public | ready to publish immediately | Best for signaling and proof-of-work |
| Staged public | start private, then switch to public | Recommended default |

Repository visibility must be a manual author decision.

## Repository metadata checklist

Before publication, prepare:

| Setting | Candidate value |
| --- | --- |
| Repository name | `AAEF-AI-VA` |
| Description | `Safety-first reference implementation for AI-assisted vulnerability assessment control boundaries` |
| Website | optional; can point to AAEF or a later project page |
| Topics | `ai-security`, `vulnerability-assessment`, `agentic-ai`, `security-automation`, `auditability`, `agpl` |
| License display | AGPL-3.0 from `LICENSE` |
| README | Confirm rendered public wording |
| Security policy | `SECURITY.md` present |
| Releases/tags | Push tags through at least `v0.3.9` if publishing history |

## Feature settings checklist

Suggested initial state:

| Feature | Suggested setting | Reason |
| --- | --- | --- |
| Issues | Enabled | Track public review and roadmap items |
| Discussions | Optional / disabled initially | Avoid unsupported support burden |
| Wiki | Disabled initially | Keep documentation in versioned source |
| Projects | Optional | Not needed for first publication |
| Pull requests | Enabled | Useful for review after publication |
| Sponsorship/Funding | Optional later | Not needed for first publication |

## Security settings checklist

Before public publication:

1. Confirm `SECURITY.md` renders correctly.
2. Decide whether to enable private vulnerability reporting.
3. Keep sensitive vulnerability reports out of public issues.
4. Keep commercial licensing inquiries separate from vulnerability reports.
5. Do not imply permission to scan third-party systems.
6. Do not imply permission to test customer targets.
7. Do not imply permission to inject credentials.
8. Do not attach generated private artifacts from `private-not-in-git/`.

## Branch protection / ruleset checklist

After the first push, consider protecting `main`.

Candidate initial controls:

- prevent force pushes to `main`
- prevent deletion of `main`
- require pull request review for non-trivial external changes
- require local checks or CI checks before merge once CI exists
- preserve fast-forward or explicit merge policy according to project needs
- protect release tags after public publication policy is defined

This is a repository setting decision, not a source-code change.

## Initial remote setup checklist

Manual-only candidate command sequence:

~~~bash
cd /e/AAEF-AI-VA

git status
py tools/run_all_local_checks.py
git log --oneline --decorate -10

# create the GitHub repository manually first
# then add the selected remote URL explicitly
git remote add origin <REMOTE_URL>
git remote -v

# choose whether to push only main or main plus tags
git push -u origin main
git push origin --tags
~~~

Do not run these commands until:

- repository visibility is selected,
- README/SECURITY/LICENSE are reviewed,
- `private-not-in-git/` exclusion has been verified,
- commercial contact placeholder posture is acceptable,
- the author is ready for the repository to leave local-only state.

## Publication settings are not runtime readiness

This checklist does not change any runtime authorization boundary.

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

## Required local checks

Before completing this checkpoint, verify:

1. First-publication checklist exists.
2. README links to this checklist.
3. Security policy exists.
4. Publication hygiene checkpoint exists.
5. Licensing/commercial-use boundary exists.
6. `private-not-in-git/` remains excluded.
7. `tools/run_all_local_checks.py` includes this checklist validation.
8. No remote repository is created by the checkpoint.
9. No push command is executed by the checkpoint.
10. Public wording does not authorize runtime execution.

## Out of scope

This checkpoint does not:

- create a GitHub repository
- add `origin`
- push `main`
- push tags
- change repository visibility
- configure GitHub settings through an API
- enable private vulnerability reporting
- enable branch protection or rulesets
- authorize runtime execution
- authorize scanning, external network testing, credential injection, or customer-target testing
- finalize commercial licensing terms
- replace legal review

## Follow-up candidates

- Add GitHub Actions CI after first remote publication.
- Add dependency/license inventory.
- Add durable commercial contact channel.
- Add durable security reporting channel.
- Add first-publication announcement draft.
- Add public README polish pass.
