# Public Trust and Reviewer Navigation Checkpoint

Version: v0.5.7 candidate  
Status: public navigation aid; does not authorize runtime execution

## Purpose

This checkpoint makes AAEF-AI-VA easier to evaluate as a public repository.

The project may be reviewed before any direct commercial conversation exists. In
that situation, the repository itself becomes a product introduction, technical
credibility artifact, safety-boundary statement, and reviewer navigation surface.

This checkpoint provides role-based reading paths for:

- technical reviewers,
- security reviewers,
- commercial reviewers,
- licensing reviewers,
- maintainer operations reviewers,
- public first-time readers.

This checkpoint is a public navigation aid only.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Public trust signals

AAEF-AI-VA should be evaluated through public trust signals that are visible in the
repository.

Current public trust signals include:

| Trust signal | Public artifact |
| --- | --- |
| Public source repository | `https://github.com/mkz0010/AAEF-AI-VA` |
| Public license | `LICENSE` / AGPL-3.0 |
| Parent framework attribution | AAEF / CC BY 4.0 |
| Security reporting | `SECURITY.md` |
| Private vulnerability reporting | Enabled on GitHub |
| Validation workflow | `.github/workflows/validate.yml` |
| Local validation entry point | `python tools/run_all_local_checks.py` |
| Notice and authorship | `NOTICE`, `AUTHORS`, `COPYRIGHT` |
| Commercial-use boundary | `COMMERCIAL-LICENSE.md` |
| Project-name usage boundary | `TRADEMARKS.md` |
| Contribution boundary | `CONTRIBUTING.md` |
| Repository governance | `docs/70-dependency-and-repository-governance-readiness-checkpoint.md` |
| Branch protection planning | `docs/71-github-repository-ruleset-and-branch-protection-planning-checkpoint.md` |
| Release operations | `docs/72-release-governance-and-maintainer-operations-checklist.md` |

## Public first-time reader path

A first-time reader should start here:

1. `README.md`
2. `SECURITY.md`
3. `LICENSE`
4. `NOTICE`
5. `COMMERCIAL-LICENSE.md`
6. `docs/66-commercial-adoption-preparation-checkpoint.md`
7. `docs/72-release-governance-and-maintainer-operations-checklist.md`

This path explains what the project is, what it is not, how it is licensed, how
security reporting works, and how releases are governed.

## Technical reviewer path

A technical reviewer should read:

1. `README.md`
2. `tools/run_all_local_checks.py`
3. `.github/workflows/validate.yml`
4. `docs/60-github-actions-ci-scaffold.md`
5. `docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md`
6. `docs/70-dependency-and-repository-governance-readiness-checkpoint.md`
7. `docs/71-github-repository-ruleset-and-branch-protection-planning-checkpoint.md`

Technical reviewers should verify:

- tests are local and reproducible,
- runtime execution remains disabled,
- generated outputs remain under `private-not-in-git/`,
- README compatibility tests avoid broad false positives,
- branch protection is planned before being enforced,
- release governance is documented before stricter GitHub administration changes.

## Security reviewer path

A security reviewer should read:

1. `SECURITY.md`
2. `docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md`
3. `docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md`
4. `docs/69-licensing-trademark-authorship-protection-checkpoint.md`
5. `docs/70-dependency-and-repository-governance-readiness-checkpoint.md`
6. `docs/72-release-governance-and-maintainer-operations-checklist.md`

Security reviewers should verify:

- sensitive vulnerability details are not posted publicly,
- private vulnerability reporting is enabled,
- private artifacts remain untracked,
- no credential injection is authorized,
- no customer-target operation is authorized,
- no live scanning is authorized,
- release operations include private artifact checks.

## Commercial reviewer path

A commercial reviewer should read:

1. `README.md`
2. `COMMERCIAL-LICENSE.md`
3. `NOTICE`
4. `TRADEMARKS.md`
5. `docs/66-commercial-adoption-preparation-checkpoint.md`
6. `docs/69-licensing-trademark-authorship-protection-checkpoint.md`
7. `docs/70-dependency-and-repository-governance-readiness-checkpoint.md`

Commercial reviewers should verify:

- public AGPL-3.0 licensing is explicit,
- separate commercial licensing discussion is possible,
- no commercial license is granted without a separate written agreement,
- commercial inquiries are separate from vulnerability reports,
- project-name usage boundaries are documented,
- the repository is not presented as a live service or production scanner.

## Licensing reviewer path

A licensing reviewer should read:

1. `LICENSE`
2. `NOTICE`
3. `AUTHORS`
4. `COPYRIGHT`
5. `COMMERCIAL-LICENSE.md`
6. `TRADEMARKS.md`
7. `CONTRIBUTING.md`
8. `docs/54-licensing-and-commercial-use-boundary.md`
9. `docs/69-licensing-trademark-authorship-protection-checkpoint.md`

Licensing reviewers should verify:

- AGPL-3.0 is the public code license,
- parent AAEF attribution is preserved,
- AAEF / CC BY 4.0 attribution is preserved,
- inbound contribution expectations are documented,
- project-name usage does not overclaim registered trademark status,
- commercial-license discussions are not confused with security reports.

## Maintainer operations reviewer path

A maintainer operations reviewer should read:

1. `docs/70-dependency-and-repository-governance-readiness-checkpoint.md`
2. `docs/71-github-repository-ruleset-and-branch-protection-planning-checkpoint.md`
3. `docs/72-release-governance-and-maintainer-operations-checklist.md`
4. `tools/run_all_local_checks.py`
5. `.github/workflows/validate.yml`
6. `CHANGELOG.md`
7. `ROADMAP.md`

Maintainer operations reviewers should verify:

- scoped branches are used,
- local checks run before commit,
- fast-forward merge is documented,
- semantic version tags are used,
- GitHub Actions are checked after push,
- emergency exception handling is documented,
- private artifact checks are part of the release process.

## Recommended review questions

A reviewer can use these questions:

1. What does the project claim to be?
2. What does the project explicitly refuse to claim?
3. What actions remain blocked?
4. What evidence shows that runtime execution remains disabled?
5. What tests can be run locally?
6. What happens to generated private outputs?
7. How are vulnerability reports handled?
8. How are commercial inquiries separated from vulnerability reports?
9. How are project names and related phrases controlled?
10. How is release governance recorded?

## Product introduction boundary

The public repository may function as a product introduction.

However, the repository should introduce the product through boundaries and evidence,
not through unsupported claims.

The product introduction boundary is:

- show the control model,
- show the safety posture,
- show the validation posture,
- show licensing and commercial-use boundaries,
- show governance readiness,
- show release operations,
- avoid claiming production readiness,
- avoid claiming certification,
- avoid claiming legal approval,
- avoid claiming audit opinion,
- avoid claiming scan authorization.

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

- production deployment approval,
- runtime execution readiness,
- scan authorization,
- customer-target authorization,
- compliance certification,
- legal approval,
- audit opinion,
- completed legal review,
- completed dependency audit,
- managed service approval,
- commercial license grant.

## Required local checks

Before tagging v0.5.7, verify:

1. README links to this checkpoint.
2. Public trust signals are recorded.
3. Public first-time reader path is recorded.
4. Technical reviewer path is recorded.
5. Security reviewer path is recorded.
6. Commercial reviewer path is recorded.
7. Licensing reviewer path is recorded.
8. Maintainer operations reviewer path is recorded.
9. Recommended review questions are recorded.
10. Product introduction boundary is recorded.
11. Runtime and scanning boundaries remain disabled.
12. Claims to avoid are recorded.
13. `tools/run_all_local_checks.py` includes the public trust reviewer navigation test.

## Out of scope

This checkpoint does not:

- create commercial sales material,
- publish pricing,
- create a target customer list,
- create a commercial contract,
- provide legal advice,
- configure GitHub branch protection,
- configure GitHub rulesets,
- authorize runtime execution,
- authorize scan execution,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
