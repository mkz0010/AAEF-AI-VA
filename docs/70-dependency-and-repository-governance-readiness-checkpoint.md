# Dependency and Repository Governance Readiness Checkpoint

Version: v0.5.4 candidate  
Status: repository governance readiness; does not authorize runtime execution

## Purpose

This checkpoint strengthens the public repository foundation for future adoption and
commercial discussions.

It records lightweight governance expectations for:

- dependency and license inventory,
- branch protection and ruleset planning,
- release and tag governance,
- security reporting and private vulnerability reporting,
- public repository administration,
- private artifact boundaries,
- runtime and scanning prohibitions.

This checkpoint does not claim legal review, production readiness, compliance
certification, audit opinion, or runtime safety approval.

## Repository state

~~~text
Repository: https://github.com/mkz0010/AAEF-AI-VA
Visibility: public
Public license: AGPL-3.0
Parent framework attribution: AAEF / CC BY 4.0
Security policy: SECURITY.md
Private vulnerability reporting: enabled
Runtime execution: disabled
Live scanning: not authorized
Customer-target operation: not authorized
~~~

## Dependency and license inventory expectations

The repository should maintain a conservative dependency posture.

Current expectations:

- identify direct runtime dependencies before production-oriented use,
- identify test-only and development-only dependencies,
- record license compatibility review as a future explicit step,
- avoid claiming a completed legal dependency review unless actually performed,
- avoid committing secrets, credentials, private customer materials, or generated private run outputs,
- keep generated local artifacts under `private-not-in-git/`.

This checkpoint records readiness planning. It is not a completed legal dependency audit.

## Current dependency posture

The current repository is primarily Python standard-library oriented and local-test
oriented.

Before any commercial deployment, service-provider use, managed-service use, or
customer-target operation, the dependency posture should be reviewed again.

Suggested future inventory categories:

| Category | Examples | Treatment |
| --- | --- | --- |
| Runtime dependencies | Packages required by executable runtime components | Review before runtime enablement |
| Development dependencies | Test, lint, formatting, validation tools | Review before release hardening |
| Documentation dependencies | Docs generation or publishing tools | Review before publication automation |
| External tools | ZAP, scanners, browsers, shells, APIs | Require explicit runtime and scope review |
| Generated outputs | Evidence, review records, local demo artifacts | Keep under `private-not-in-git/` |

## Branch protection and ruleset planning

The repository should consider GitHub branch protection or rulesets when the project
moves from solo-maintained public reference implementation toward broader
collaboration or commercial adoption.

Recommended future settings:

- require pull request before merge,
- require status checks to pass before merge,
- require the validation workflow before merge,
- restrict force pushes to protected branches,
- protect release tags or document tag creation authority,
- require review for high-risk runtime, scanning, credential, or customer-target changes,
- keep vulnerability reports separate from public issues.

This checkpoint does not configure branch protection by itself.

## Release and tag governance

Release and tag governance should preserve the current style:

- semantic version tags,
- small scoped checkpoints,
- local checks before tagging,
- GitHub Actions validation after push,
- release notes for public milestones,
- safety-boundary wording preserved in public releases.

Suggested release checklist:

1. Work on a scoped feature branch.
2. Run the new targeted test.
3. Run `tools/run_all_local_checks.py`.
4. Commit after all local checks pass.
5. Fast-forward merge into `main`.
6. Tag the version.
7. Push `main` and the tag.
8. verify GitHub Actions.
9. Keep `private-not-in-git/` untracked.

## Security and disclosure governance

The repository already includes:

- `SECURITY.md`,
- private vulnerability reporting,
- public warning against sensitive public disclosure,
- publication hygiene and private artifact exclusion,
- commercial inquiry separation from vulnerability reports.

Security reports must not be mixed with commercial licensing inquiries.

Sensitive vulnerability details should not be posted in public issues.

## Commercial-readiness relationship

This checkpoint supports commercial readiness by showing that the repository is not
only a code dump.

It records that the project has considered:

- dependency boundaries,
- public/private artifact boundaries,
- release governance,
- repository settings,
- security disclosure,
- license and authorship,
- project-name usage,
- commercial-use boundaries.

This checkpoint does not create a commercial contract.

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

- completed legal dependency review,
- full software bill of materials,
- production deployment approval,
- branch protection configuration,
- compliance certification,
- legal approval,
- audit opinion,
- runtime execution readiness,
- scan authorization,
- customer-target authorization.

## Required local checks

Before tagging v0.5.4, verify:

1. README links to this checkpoint.
2. Dependency and license inventory expectations are recorded.
3. Branch protection and ruleset planning is recorded.
4. Release and tag governance is recorded.
5. Security and disclosure governance is recorded.
6. Commercial-readiness relationship is recorded.
7. Runtime and scanning boundaries remain disabled.
8. Claims to avoid are recorded.
9. `tools/run_all_local_checks.py` includes the governance readiness test.

## Out of scope

This checkpoint does not:

- configure GitHub branch protection,
- configure GitHub rulesets,
- complete a legal dependency review,
- generate a full SBOM,
- create a commercial contract,
- publish pricing,
- provide legal advice,
- authorize runtime execution,
- authorize scan execution,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
