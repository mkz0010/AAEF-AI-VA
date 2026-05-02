# Public Front Page and Repository Landing Polish Checkpoint

Version: v0.5.8 candidate  
Status: presentation and navigation polish; does not authorize runtime execution

## Purpose

This checkpoint records how the public repository front page should introduce
AAEF-AI-VA to first-time readers.

The repository may be discovered before any direct sales conversation, partnership
discussion, or technical walkthrough. In that situation, the public front page must
do four things quickly:

1. explain the value proposition,
2. state the safety boundary,
3. direct reviewers to the right reading path,
4. avoid unsupported claims.

This checkpoint is presentation and navigation polish only.

This checkpoint does not create commercial sales material.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## First-minute reviewer goals

Within the first minute, a reviewer should understand:

- AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability assessment control boundaries.
- AI output is not authority to perform assessment actions.
- Assessment actions remain blocked unless authorization, contractual scope, Tool Gateway behavior, preflight evidence, and human review boundaries support the action.
- Runtime execution remains disabled.
- Live scanning is not authorized.
- Customer-target operation is not authorized.
- The repository is AGPL-3.0 licensed.
- Commercial licensing inquiries require separate discussion.
- Security reports follow `SECURITY.md`.
- The reviewer can run `python tools/run_all_local_checks.py`.

## Above-the-fold README expectations

The README top section should preserve a concise public introduction.

Recommended above-the-fold elements:

| Element | Purpose |
| --- | --- |
| Project name | Identify `AAEF-AI-VA` immediately |
| One-line description | Explain AI-assisted vulnerability assessment control boundaries |
| Core principle | Preserve `AI output is not authority to perform assessment actions.` |
| What this is | Describe safety-first reference implementation scope |
| What this is not | Avoid scanner, production, certification, and permission claims |
| Validation signal | Point to GitHub Actions and local checks |
| License signal | Point to AGPL-3.0 and parent AAEF / CC BY 4.0 |
| Security signal | Point to `SECURITY.md` and private vulnerability reporting |
| Commercial boundary | Point to `COMMERCIAL-LICENSE.md` |
| Reviewer navigation | Point to `docs/73-public-trust-and-reviewer-navigation-checkpoint.md` |

## Public value proposition

The public value proposition should be direct but conservative:

AAEF-AI-VA demonstrates how AI-assisted vulnerability assessment can be placed behind
authorization, scope, evidence, review, and delivery gates so that model output is
treated as a request rather than execution authority.

The value proposition should emphasize:

- control boundaries,
- authorization gates,
- Tool Gateway behavior,
- preflight evidence,
- human review,
- report finding promotion,
- delivery authorization,
- auditability,
- local validation,
- disabled runtime execution.

## Product introduction boundary

The repository can act as product introduction, but not as an unsupported sales deck.

Allowed product-introduction messages:

- show the control model,
- show the safety posture,
- show the validation posture,
- show licensing and commercial-use boundaries,
- show governance readiness,
- show release operations,
- show reviewer navigation,
- show what remains blocked.

Avoid product-introduction messages that imply:

- production deployment approval,
- live scanner readiness,
- customer-target authorization,
- compliance certification,
- legal approval,
- audit opinion,
- commercial license grant,
- managed service approval,
- safety guarantee.

## Reviewer landing paths

The front page should preserve clear landing paths:

| Reviewer | Primary entrypoint |
| --- | --- |
| First-time reader | `README.md` |
| Technical reviewer | `tools/run_all_local_checks.py` and `.github/workflows/validate.yml` |
| Security reviewer | `SECURITY.md` |
| Commercial reviewer | `COMMERCIAL-LICENSE.md` |
| Licensing reviewer | `LICENSE`, `NOTICE`, `AUTHORS`, `COPYRIGHT`, `TRADEMARKS.md`, `CONTRIBUTING.md` |
| Maintainer operations reviewer | `docs/72-release-governance-and-maintainer-operations-checklist.md` |
| Public trust reviewer | `docs/73-public-trust-and-reviewer-navigation-checkpoint.md` |

## Trust-signal placement

The README should make trust signals discoverable without overwhelming the reader.

Important trust signals:

- AGPL-3.0 license,
- AAEF / CC BY 4.0 attribution,
- `SECURITY.md`,
- private vulnerability reporting,
- GitHub Actions validation,
- local validation command,
- publication hygiene boundary,
- commercial-use boundary,
- trademark-like project-name boundary,
- release governance checklist,
- reviewer navigation checkpoint.

## Commercial-use placement

Commercial-use material should be visible but not aggressive.

The front page should make clear:

- public use is governed by AGPL-3.0,
- separate commercial licensing discussions are possible,
- no commercial license is granted without a separate written agreement,
- commercial licensing inquiries are separate from vulnerability reports,
- commercial discussions do not authorize runtime execution, scanning, credential injection, or customer-target operation.

## Security placement

Security material should be easy to find.

The front page should make clear:

- security reports follow `SECURITY.md`,
- sensitive vulnerability details should not be posted publicly,
- private vulnerability reporting is enabled,
- vulnerability reports are separate from commercial licensing inquiries,
- generated private artifacts belong under `private-not-in-git/`.

## Validation placement

Validation material should be visible to technical reviewers.

The front page should preserve:

~~~bash
python tools/run_all_local_checks.py
~~~

Validation statements should avoid overclaiming.

Allowed validation statement:

- local checks validate documented examples, gates, boundaries, and repository governance expectations.

Avoid validation statements that imply:

- production safety,
- complete security assurance,
- legal compliance,
- audit sufficiency,
- scan authorization,
- customer-target authorization.

## README compatibility relationship

This checkpoint builds on the README compatibility phrase registry.

Related checkpoint:

- `docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md`

The front page should preserve compatibility-sensitive phrases such as:

- `AI output is not authority to perform assessment actions.`
- `Runtime execution remains disabled.`
- `Live scanning | Not authorized`
- `Customer-target operation | Not authorized`
- `commercial licensing inquiries`
- `CC BY 4.0`
- `GNU Affero General Public License v3.0`

## Relationship to reviewer navigation

This checkpoint builds on public trust reviewer navigation.

Related checkpoint:

- `docs/73-public-trust-and-reviewer-navigation-checkpoint.md`

The reviewer navigation checkpoint explains where different reviewers should go. This
front-page polish checkpoint explains how the repository landing page should expose
that navigation without turning into a sales deck.

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
- commercial license grant,
- safety guarantee.

## Required local checks

Before tagging v0.5.8, verify:

1. README links to this checkpoint.
2. First-minute reviewer goals are recorded.
3. Above-the-fold README expectations are recorded.
4. Public value proposition is recorded.
5. Product introduction boundary is recorded.
6. Reviewer landing paths are recorded.
7. Trust-signal placement is recorded.
8. Commercial-use placement is recorded.
9. Security placement is recorded.
10. Validation placement is recorded.
11. README compatibility relationship is recorded.
12. Public trust reviewer navigation relationship is recorded.
13. Runtime and scanning boundaries remain disabled.
14. Claims to avoid are recorded.
15. `tools/run_all_local_checks.py` includes the public front page landing polish test.

## Out of scope

This checkpoint does not:

- rewrite the full README,
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
