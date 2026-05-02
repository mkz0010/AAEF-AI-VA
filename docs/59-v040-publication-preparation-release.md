# v0.4.0 Public Publication Preparation Release

Version: v0.4.0 candidate  
Status: publication-preparation release; does not create a remote repository

## Purpose

v0.4.0 consolidates the publication-readiness work completed in v0.3.5 through
v0.3.9 and prepares AAEF-AI-VA for a deliberate first GitHub publication.

This release does not:

- create a GitHub repository
- add `origin`
- push `main`
- push tags
- change repository visibility
- configure GitHub settings
- enable private vulnerability reporting
- enable branch protection or rulesets
- authorize runtime execution
- authorize scan execution
- authorize external network activity
- authorize credential injection
- authorize customer-target testing

## Publication-readiness stack

v0.4.0 summarizes the following completed checkpoints:

| Version | Checkpoint | Purpose |
| --- | --- | --- |
| v0.3.5 | Licensing and commercial-use boundary | Record AGPL-3.0, AAEF attribution, and commercial licensing posture |
| v0.3.6 | Public repository readiness checkpoint | Confirm repository-level readiness signals before publication |
| v0.3.7 | Publication hygiene and private artifact exclusion | Prevent private/generated/local artifacts from being tracked or published |
| v0.3.8 | Public security policy and vulnerability disclosure | Provide security-report posture without authorizing live testing |
| v0.3.9 | First-publication repository settings checklist | Record GitHub repository settings and first-push decisions as manual actions |

## Recommended publication path

Recommended path:

~~~text
1. Keep local repository clean.
2. Run all local checks.
3. Review README, LICENSE, SECURITY.md, and publication checkpoints.
4. Create GitHub repository as private first, or choose staged public explicitly.
5. Add remote manually only after final review.
6. Push main and tags manually.
7. Review rendered GitHub pages and repository settings.
8. Switch to public only when the author is comfortable with public visibility.
~~~

The recommended default is **staged public**:

~~~text
local-only -> private remote -> final rendered review -> public visibility
~~~

This gives the author a final GitHub-rendered review step without prematurely
publishing the repository.

## First-publication dry-run checklist

Before adding any remote:

~~~bash
cd /e/AAEF-AI-VA

git status
git remote -v
git log --oneline --decorate -12
py tools/run_all_local_checks.py
git ls-files private-not-in-git
git ls-files | grep -E '(__pycache__|\.pyc$)' || true
~~~

Expected state before publication:

- `git status` shows clean working tree
- `git remote -v` is empty or intentionally configured
- all local checks pass
- `private-not-in-git/` has no tracked files
- no Python cache files are tracked
- `LICENSE` exists
- `SECURITY.md` exists
- README explains the project without implying runtime execution is enabled

## Manual first-publication command candidate

Only after manual review:

~~~bash
cd /e/AAEF-AI-VA

# create the GitHub repository manually first
# select private-first or staged-public visibility intentionally
git remote add origin <REMOTE_URL>
git remote -v

git push -u origin main
git push origin --tags
~~~

These commands are intentionally documented, not automated.

## Repository settings review

After the first push, manually review:

| Area | Suggested initial choice |
| --- | --- |
| Visibility | Private-first or staged public |
| About description | Safety-first reference implementation for AI-assisted vulnerability assessment control boundaries |
| Topics | `ai-security`, `vulnerability-assessment`, `agentic-ai`, `security-automation`, `auditability`, `agpl` |
| License display | AGPL-3.0 |
| Issues | Enabled |
| Discussions | Disabled or optional initially |
| Wiki | Disabled initially |
| Security policy | Confirm `SECURITY.md` renders |
| Private vulnerability reporting | Consider enabling if repository is public |
| Branch protection/rulesets | Consider protecting `main` after first push |
| Releases | Consider publishing v0.4.0 after final rendered review |

## Public positioning

Candidate public positioning:

~~~text
AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability
assessment control boundaries. It demonstrates how an AI-assisted assessment workflow
can remain blocked by default until explicit authorization, preflight evidence,
review gates, and publication hygiene boundaries are satisfied.
~~~

Key claims allowed:

- safety-first reference implementation
- AI-assisted vulnerability assessment control boundaries
- evidence, preflight, approval, and review gates
- AGPL-3.0 code with separate commercial licensing path
- no live scanning authorization in the current release
- no customer target readiness in the current release

Claims to avoid:

- production-ready scanner
- autonomous vulnerability scanner
- customer-ready assessment platform
- compliance certification
- legal advice
- audit opinion
- permission to scan third-party systems
- proof that AI can safely run vulnerability assessments without human review

## Announcement draft

Candidate announcement:

~~~markdown
AAEF-AI-VA v0.4.0 is prepared as a public publication preparation release.

AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability
assessment control boundaries. The project focuses on keeping runtime execution,
scan execution, network activity, credential injection, and customer-target testing
blocked unless explicit authorization and evidence gates are satisfied.

This release consolidates the publication-readiness stack:

- AGPL-3.0 licensing and commercial-use boundary
- public repository readiness
- publication hygiene and private artifact exclusion
- public security policy and vulnerability disclosure posture
- first-publication repository settings checklist

This is not a production scanner and does not authorize live scanning.
The current value is the control model: evidence, preflight checks, fail-closed
negative examples, review gates, and publication safety boundaries.
~~~

## Runtime and scanning boundary

v0.4.0 does not change any runtime authorization boundary.

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

Before tagging v0.4.0, verify:

1. v0.4.0 publication-preparation document exists.
2. README links to the v0.4.0 publication-preparation document.
3. v0.3.5 through v0.3.9 checkpoints are referenced.
4. `LICENSE` exists.
5. `SECURITY.md` exists.
6. `.gitignore` excludes `private-not-in-git/`.
7. First-publication settings checklist exists.
8. `tools/run_all_local_checks.py` includes the v0.4.0 publication-preparation test.
9. No remote repository is created by this checkpoint.
10. No push command is executed by this checkpoint.
11. Runtime execution remains disabled.

## Follow-up candidates after v0.4.0

- Decide private-first vs staged-public publication.
- Create GitHub repository manually.
- Push `main` and tags manually.
- Review rendered README/SECURITY/LICENSE.
- Add GitHub Actions CI.
- Add dependency/license inventory.
- Add durable commercial contact channel.
- Add durable security reporting channel.
- Prepare public announcement post.
