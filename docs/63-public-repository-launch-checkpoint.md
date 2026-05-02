# Public Repository Launch Checkpoint

Version: v0.4.4 candidate  
Status: public repository launch checkpoint; does not authorize runtime execution

## Purpose

This checkpoint records the public launch state of AAEF-AI-VA after the repository
was published on GitHub.

It captures the repository-level facts that were verified during launch:

- public repository visibility,
- `origin/main` publication,
- tag publication through v0.4.3 before this checkpoint,
- GitHub Actions validation,
- repository metadata,
- repository topics,
- private vulnerability reporting,
- repository feature settings,
- runtime-execution safety boundary.

This checkpoint does not create or configure the repository. It records the launch
state after the manual GitHub publication steps were completed.

## Repository

~~~text
Repository: https://github.com/mkz0010/AAEF-AI-VA
Visibility: PUBLIC
isPrivate: false
Default branch: main
origin: https://github.com/mkz0010/AAEF-AI-VA.git
~~~

## Launch state recorded

| Item | Recorded state |
| --- | --- |
| Repository URL | `https://github.com/mkz0010/AAEF-AI-VA` |
| Visibility | `PUBLIC` |
| Private repository flag | `false` |
| `origin/main` | Published |
| Latest pre-launch tag | `v0.4.3` |
| GitHub Actions workflow | `Validate AAEF-AI-VA artifacts` |
| GitHub Actions status | Passing |
| Manual workflow dispatch | Passing |
| Private vulnerability reporting | Enabled |
| Issues | Enabled |
| Discussions | Disabled |
| Wiki | Disabled |
| Projects | Disabled |
| License | AGPL-3.0 |
| Security policy | `SECURITY.md` present |
| Runtime execution | Disabled |

## Repository metadata

Description:

~~~text
Safety-first reference implementation for AI-assisted vulnerability assessment control boundaries
~~~

Topics:

~~~text
agentic-ai
agpl
ai-assurance
ai-security
auditability
security-automation
security-controls
vulnerability-assessment
~~~

## Verified GitHub Actions runs

The public launch review confirmed that the workflow named:

~~~text
Validate AAEF-AI-VA artifacts
~~~

was active and passing for recent `push` and `workflow_dispatch` runs.

The launch review observed a passing manual workflow dispatch run:

~~~text
workflow_dispatch run ID: 25254907292
result: passing
```

## Private vulnerability reporting

Private vulnerability reporting was enabled and verified with:

~~~text
enabled: true
~~~

This does not authorize testing against third-party systems. It only provides a
safer private reporting path for repository vulnerabilities.

## Launch is not runtime readiness

Public repository launch does not authorize vulnerability scanning, live assessment,
external network testing, credential injection, customer-target operation, or any
other runtime execution.

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

## Public claim boundary

Acceptable launch claims:

- public repository launch completed
- AGPL-3.0 licensed reference implementation
- safety-first AI-assisted vulnerability assessment control boundaries
- GitHub Actions validation is active and passing
- private vulnerability reporting is enabled
- runtime execution remains disabled
- scanning remains unauthorized

Claims to avoid:

- production scanner
- autonomous vulnerability scanner
- customer-ready assessment platform
- permission to scan third-party systems
- credential-handling readiness
- compliance certification
- legal approval
- audit opinion
- runtime safety without human review

## Required local checks

Before tagging v0.4.4, verify:

1. Public repository launch checkpoint exists.
2. README links to the launch checkpoint.
3. Repository URL is recorded.
4. Visibility is recorded as public.
5. Private vulnerability reporting is recorded as enabled.
6. GitHub Actions validation is recorded as active and passing.
7. Topics and description are recorded.
8. Feature settings are recorded.
9. Runtime and scanning boundaries remain disabled.
10. `tools/run_all_local_checks.py` includes the launch checkpoint test.

## Out of scope

This checkpoint does not:

- make the repository public
- configure repository metadata
- enable private vulnerability reporting
- create a GitHub Release
- publish a social announcement
- configure branch protection or rulesets
- authorize runtime execution
- authorize scan execution
- authorize external network testing
- authorize credential injection
- authorize customer-target testing

## Follow-up candidates

- Add GitHub Release notes for v0.4.4 or a later public launch release.
- Add branch protection / ruleset planning after observing public workflow behavior.
- Add dependency/license inventory.
- Add durable commercial contact channel.
- Add durable security reporting channel if GitHub private vulnerability reporting is not sufficient.
- Prepare public announcement post from the v0.4.3 announcement pack.
