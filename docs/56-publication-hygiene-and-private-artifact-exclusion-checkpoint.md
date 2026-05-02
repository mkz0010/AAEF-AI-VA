# Publication Hygiene and Private Artifact Exclusion Checkpoint

Version: v0.3.7 candidate  
Status: publication hygiene checkpoint; does not authorize runtime execution

## Purpose

This checkpoint records the minimum hygiene checks that should pass before the
AAEF-AI-VA repository is pushed to any remote repository or made public.

It follows the public repository readiness checkpoint and focuses on accidental
publication risks:

- generated evidence records,
- local run outputs,
- private review artifacts,
- Python cache files,
- local environment files,
- editor/system noise,
- future customer or target-specific material.

## Why this matters

AAEF-AI-VA intentionally generates local evidence, review, gate, and report artifacts
under `private-not-in-git/`.

Those artifacts are useful for local validation, but they are not intended to be
published as source artifacts.

Publication hygiene is therefore a separate boundary from:

- runtime readiness,
- preflight readiness,
- execution authorization,
- scan authorization,
- customer target readiness,
- commercial service readiness.

## Expected `.gitignore` posture

The repository should exclude at least:

~~~text
private-not-in-git/
*.generated.json
*.generated.md
__pycache__/
*.py[cod]
.env
.env.*
*.local
*.log
.vscode/
.idea/
.DS_Store
Thumbs.db
~~~

## Publication hygiene is not runtime readiness

This checkpoint does not change any runtime authorization boundary.

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

Before publication, verify:

1. `.gitignore` excludes `private-not-in-git/`.
2. `.gitignore` excludes generated JSON and Markdown outputs.
3. `.gitignore` excludes Python cache files.
4. `.gitignore` excludes local environment files and logs.
5. `git ls-files` does not show tracked files under `private-not-in-git/`.
6. `git ls-files` does not show tracked Python cache files.
7. `tools/run_all_local_checks.py` includes the publication hygiene test.
8. README mentions the private artifact boundary.
9. Public text does not imply runtime execution is enabled.

## Suggested command sequence

~~~bash
cd /e/AAEF-AI-VA

git status
git ls-files private-not-in-git
git ls-files | grep -E '(__pycache__|\.pyc$)' || true
py tools/run_all_local_checks.py
~~~

## Out of scope

This checkpoint does not:

- create a remote repository
- push code to GitHub
- decide repository visibility
- authorize runtime execution
- authorize ZAP execution
- authorize network activity
- review all third-party dependency licenses
- finalize commercial contract wording
- replace legal review

## Follow-up candidates

- Add `SECURITY.md`.
- Add public vulnerability disclosure guidance.
- Add dependency/license inventory.
- Add repository settings checklist for the first GitHub publication.
- Add a first-publication dry-run command set.
