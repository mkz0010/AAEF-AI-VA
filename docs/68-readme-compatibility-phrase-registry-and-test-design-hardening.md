# README Compatibility Phrase Registry and Test Design Hardening

Version: v0.5.2 candidate  
Status: README compatibility and test-design hardening; does not authorize runtime execution

## Purpose

This document records README compatibility phrases and README-facing test design rules
so future README rewrites do not accidentally break earlier checkpoint tests.

The v0.5.1 README public baseline cleanup exposed an important maintainability issue:
older checkpoint tests used README as a stable compatibility surface and expected
specific headings, attribution phrases, and safety-boundary wording.

This registry makes that dependency explicit.

## Design principle

README is both:

1. the public front door for the repository, and
2. a compatibility surface for earlier publication, licensing, security, metadata,
   release, and commercial-adoption checkpoint tests.

Future README rewrites should therefore preserve stable compatibility phrases or
intentionally update the relevant tests.

## Stable README headings

The following README headings should be treated as compatibility-sensitive:

| Heading | Reason |
| --- | --- |
| `## Current public baseline` | Public entrypoint state |
| `## Core principle` | Authority-boundary message |
| `## What this is` | Positive project scope |
| `## What this is not` | Negative claim boundary |
| `## Commercial adoption entrypoint` | Business-facing entrypoint |
| `## Publication Hygiene and Private Artifact Boundary` | Publication hygiene compatibility |
| `## Security Policy` | Security policy compatibility |
| `## Public Repository Metadata` | Metadata announcement compatibility |
| `## License and commercial-use boundary` | License/commercial boundary |
| `## Publication and release checkpoints` | Release/history navigation |
| `## Commercial Adoption Preparation` | Commercial adoption checkpoint link |

## Stable README phrases

The following README phrases should be preserved unless the related checkpoint tests
are intentionally updated:

| Phrase | Reason |
| --- | --- |
| `AI output is not authority to perform assessment actions.` | Core authority-boundary principle |
| `AI may request assessment actions, but execution is decided by the AAEF Authorization Gateway, Tool Gateway, contractual scope, and human review.` | Execution-authority separation |
| `Runtime execution remains disabled.` | Runtime safety boundary |
| `Live scanning | Not authorized` | Scan authorization boundary |
| `Customer-target operation | Not authorized` | Customer-target boundary |
| `private-not-in-git/` | Private artifact boundary |
| `SECURITY.md` | Security policy link |
| `.github/workflows/validate.yml` | CI workflow link |
| `tools/run_all_local_checks.py` | Local validation entrypoint |
| `GNU Affero General Public License v3.0` | Code license |
| `CC BY 4.0` | Parent AAEF short-form attribution |
| `Creative Commons Attribution 4.0 International` | Parent AAEF full attribution |
| `https://github.com/mkz0010/agentic-authority-evidence-framework` | Parent AAEF repository attribution |
| `commercial licensing inquiries` | Commercial inquiry compatibility phrase |

## Stable README links

The following README links are compatibility-sensitive:

| Link | Reason |
| --- | --- |
| `LICENSE` | AGPL-3.0 license |
| `SECURITY.md` | Security reporting |
| `docs/54-licensing-and-commercial-use-boundary.md` | License boundary |
| `docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md` | Publication hygiene |
| `docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md` | Security policy |
| `docs/62-public-facing-repository-metadata-and-announcement-pack.md` | Metadata pack |
| `docs/63-public-repository-launch-checkpoint.md` | Public launch |
| `docs/64-public-release-notes-and-launch-announcement-package.md` | Release notes package |
| `docs/65-github-release-publication-checkpoint.md` | GitHub Release checkpoint |
| `docs/66-commercial-adoption-preparation-checkpoint.md` | Commercial adoption |
| `docs/67-readme-public-baseline-and-commercial-entrypoint-cleanup.md` | README cleanup |

## Forbidden positive claims

README-facing tests should avoid broad substring bans.

Tests should reject unsafe positive claims such as:

- `runtime execution enabled`
- `network activity allowed`
- `scan execution allowed`
- `credential injection permitted`
- `customer target operation allowed`
- `is a production scanner`
- `is a production-ready scanner`
- `is an autonomous vulnerability scanner`
- `is a customer-ready assessment platform`
- `is a customer-ready managed assessment platform`
- `certified compliant`
- `legal approval granted`
- `audit opinion issued`

## Allowed negative boundary statements

README-facing tests should allow negative boundary statements in sections such as
`What this is not` and `Claims to avoid`.

Allowed negative boundary examples include:

- `not a production scanner`
- `not an autonomous vulnerability scanner`
- `not a customer-ready managed assessment platform`
- `permission to scan third-party systems` when listed as something the repository does not grant
- `permission to inject credentials` when listed as something the repository does not grant
- `permission to operate against customer targets` when listed as something the repository does not grant

The test-design rule is:

~~~text
Reject unsafe positive claims.
Allow explicit negative boundary statements.
~~~

## Test design requirements

README-facing tests should:

1. check required headings and links,
2. check license and attribution phrases,
3. check security and private vulnerability reporting phrases,
4. check publication hygiene and private artifact boundaries,
5. check commercial entrypoint boundaries,
6. reject forbidden positive claims,
7. allow negative boundary statements,
8. avoid broad substring bans that fail on `What this is not` sections.

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

## Required local checks

Before tagging v0.5.2, verify:

1. README links to this registry.
2. Registry records stable README headings.
3. Registry records stable README phrases.
4. Registry records stable README links.
5. Registry distinguishes forbidden positive claims from allowed negative boundary statements.
6. Registry preserves runtime and scanning boundaries.
7. `tools/run_all_local_checks.py` includes the registry test.

## Out of scope

This checkpoint does not:

- rewrite README again,
- change repository visibility,
- create or edit a GitHub Release,
- publish an announcement,
- create a commercial contact channel,
- provide legal advice,
- authorize runtime execution,
- authorize scan execution,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
