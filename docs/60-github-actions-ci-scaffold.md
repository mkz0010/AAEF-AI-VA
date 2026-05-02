# GitHub Actions CI Scaffold

Version: v0.4.1 candidate  
Status: CI scaffold; does not authorize runtime execution

## Purpose

This checkpoint adds a minimal GitHub Actions workflow for repository validation.

The workflow is intentionally narrow. It exists to show that the repository's
source-level checks can run in CI after the repository is pushed to GitHub.

It does not:

- create a remote repository
- push code to GitHub
- configure GitHub repository settings
- enable private vulnerability reporting
- enable branch protection or rulesets
- authorize runtime execution
- authorize scan execution
- authorize external network activity
- authorize credential injection
- authorize customer-target testing

## Workflow file

The workflow is defined at:

~~~text
.github/workflows/validate.yml
~~~

Workflow behavior:

| Trigger | Purpose |
| --- | --- |
| `push` to `main` | Validate committed changes on the main branch |
| `pull_request` to `main` | Validate proposed changes before merge |
| `workflow_dispatch` | Allow manual validation from GitHub UI |

## Validation job

The initial job performs only repository validation:

~~~text
check out repository
set up Python
show Python version
run python tools/run_all_local_checks.py
~~~

No dependency installation is included because the current validation suite uses the
standard library and repository-local scripts.

If future dependencies are added, the dependency installation step should be
introduced deliberately and reviewed for license, security, and reproducibility
impact.

## CI is not runtime readiness

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

## Design constraints

The CI scaffold should remain:

- read-only with respect to repository contents
- free of secrets
- free of credentials
- free of external target configuration
- free of ZAP execution
- free of network scan execution
- limited to local validation scripts

## Expected workflow permissions

The workflow uses:

~~~yaml
permissions:
  contents: read
~~~

This keeps the initial CI posture minimal.

## Required local checks

Before tagging v0.4.1, verify:

1. `.github/workflows/validate.yml` exists.
2. The workflow uses checkout and Python setup actions.
3. The workflow runs `python tools/run_all_local_checks.py`.
4. The workflow does not reference secrets.
5. The workflow does not run ZAP.
6. The workflow does not run scan commands.
7. The workflow does not use credentials.
8. README links to the CI scaffold document.
9. `tools/run_all_local_checks.py` includes the CI scaffold validation test.
10. Runtime execution remains disabled.

## Out of scope

This checkpoint does not:

- create a GitHub repository
- add `origin`
- push `main`
- push tags
- configure branch protection
- configure repository rulesets
- configure private vulnerability reporting
- create release notes
- publish an announcement
- authorize scanning or runtime execution

## Follow-up candidates

- Add branch protection or ruleset checklist after first remote push.
- Add dependency/license inventory if dependencies are introduced.
- Add release notes for the first public release.
- Add a public announcement draft after rendered README review.
- Add a CI badge after the repository URL is stable.
