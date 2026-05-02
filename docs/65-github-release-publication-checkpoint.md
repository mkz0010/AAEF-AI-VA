# GitHub Release Publication Checkpoint

Version: v0.4.6 candidate  
Status: release publication checkpoint; does not authorize runtime execution

## Purpose

This checkpoint records that the GitHub Release for `v0.4.5` was published after the
public repository launch and launch announcement package were completed.

It captures the release-level facts that were verified manually:

- release tag,
- release title,
- release URL,
- latest release status,
- release note source path,
- release note safety boundaries,
- continued runtime-execution prohibition.

This checkpoint does not create the GitHub Release. It records the release state
after the manual GitHub Release publication step was completed.

## Repository

~~~text
Repository: https://github.com/mkz0010/AAEF-AI-VA
Visibility: PUBLIC
Latest repository checkpoint before release publication: v0.4.5
~~~

## Published release

~~~text
Release tag: v0.4.5
Release title: AAEF-AI-VA v0.4.5 Public Launch Communication Package
Release URL: https://github.com/mkz0010/AAEF-AI-VA/releases/tag/v0.4.5
Release type: Latest
Release status: published
~~~

## Release notes source

The release notes were prepared locally under:

~~~text
private-not-in-git/release-notes/v0.4.5-release-notes.md
~~~

This path is intentionally under `private-not-in-git/`.

The source release-note file is a local generated/review artifact and is not intended
to be tracked as a repository source artifact.

## Release note safety boundaries

The published release notes record that:

- AAEF-AI-VA is a public safety-first reference implementation for AI-assisted vulnerability assessment control boundaries.
- AI output is treated as a request, not authority.
- Assessment actions remain blocked unless authorization, contractual scope, Tool Gateway behavior, preflight evidence, and human review boundaries support the action.
- The repository includes AGPL-3.0 licensing.
- The repository includes `SECURITY.md`.
- Private vulnerability reporting is enabled.
- GitHub Actions validation is active.
- Publication hygiene and private artifact exclusion are documented.
- Runtime and scanning boundaries are documented as disabled.
- The release is not a live scanner.
- The release does not authorize third-party scanning, external network testing, credential injection, or customer-target operation.

## Manual release commands used

The release was created from the existing pushed `v0.4.5` tag using a manually reviewed
release notes file.

Command shape:

~~~bash
gh release create v0.4.5 \
  --repo mkz0010/AAEF-AI-VA \
  --title "AAEF-AI-VA v0.4.5 Public Launch Communication Package" \
  --notes-file private-not-in-git/release-notes/v0.4.5-release-notes.md \
  --verify-tag \
  --latest
~~~

Verification command shape:

~~~bash
gh release view v0.4.5 --repo mkz0010/AAEF-AI-VA
gh release list --repo mkz0010/AAEF-AI-VA --limit 5
~~~

## Release publication is not runtime readiness

GitHub Release publication does not authorize vulnerability scanning, live assessment,
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

Acceptable release claims:

- GitHub Release `v0.4.5` was published.
- The release is marked as Latest.
- The public repository has GitHub Actions validation.
- The public repository has private vulnerability reporting enabled.
- The release notes preserve the authority-boundary message.
- Runtime execution remains disabled.
- Live scanning remains unauthorized.

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
- replacement for professional security judgment

## Required local checks

Before tagging v0.4.6, verify:

1. GitHub Release publication checkpoint exists.
2. README links to the release publication checkpoint.
3. Repository URL is recorded.
4. Release URL is recorded.
5. Release title is recorded.
6. Release tag `v0.4.5` is recorded.
7. Release status is recorded as published.
8. Release type is recorded as Latest.
9. Release notes source is recorded under `private-not-in-git/`.
10. Release note safety boundaries are recorded.
11. Runtime and scanning boundaries remain disabled.
12. `tools/run_all_local_checks.py` includes the release publication checkpoint test.

## Out of scope

This checkpoint does not:

- create a GitHub Release
- edit a GitHub Release
- publish a social announcement
- create a commercial contract
- provide legal advice
- configure branch protection or rulesets
- authorize runtime execution
- authorize scan execution
- authorize external network testing
- authorize credential injection
- authorize customer-target testing

## Follow-up candidates

- Prepare LinkedIn launch post from the launch announcement package.
- Prepare Zenn/Qiita technical article draft.
- Add branch protection / ruleset planning.
- Add dependency/license inventory.
- Add durable commercial contact channel.
- Add commercialization-oriented service packaging.
