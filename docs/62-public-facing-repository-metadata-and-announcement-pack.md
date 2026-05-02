# Public-Facing Repository Metadata and Announcement Pack

Version: v0.4.3 candidate  
Status: public-facing repository presentation pack; does not authorize runtime execution

## Purpose

This checkpoint prepares the public-facing repository presentation after the GitHub
remote URL has been established.

It adds and validates:

- README validation badge guidance,
- repository About metadata candidates,
- GitHub topic candidates,
- release positioning,
- public announcement draft,
- claim boundaries for public messaging.

This checkpoint does not change repository visibility, create a release, publish an
announcement, configure GitHub settings, or authorize runtime execution.

## Repository URL

~~~text
https://github.com/mkz0010/AAEF-AI-VA
~~~

## README badge

Recommended README badge:

~~~markdown
[![Validate AAEF-AI-VA artifacts](https://github.com/mkz0010/AAEF-AI-VA/actions/workflows/validate.yml/badge.svg)](https://github.com/mkz0010/AAEF-AI-VA/actions/workflows/validate.yml)
~~~

The badge should represent repository validation only.

It must not imply:

- production readiness,
- scan authorization,
- customer-target readiness,
- credential handling readiness,
- compliance certification,
- legal approval,
- audit opinion.

## GitHub About metadata

Recommended values:

| Field | Candidate value |
| --- | --- |
| Repository name | `AAEF-AI-VA` |
| Description | `Safety-first reference implementation for AI-assisted vulnerability assessment control boundaries` |
| Website | optional; leave blank or point to the parent AAEF repository after review |
| License | AGPL-3.0 |
| Security policy | `SECURITY.md` |
| Visibility | private-first or staged public until final manual decision |

Recommended topics:

~~~text
ai-security
vulnerability-assessment
agentic-ai
security-automation
auditability
agpl
ai-assurance
security-controls
~~~

## Public positioning

Use this public positioning:

~~~text
AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability
assessment control boundaries. It demonstrates how assessment actions can remain
blocked by default unless authorization, contractual scope, evidence, preflight,
tool gateway, and human review boundaries are satisfied.
~~~

## Short description

~~~text
Safety-first reference implementation for AI-assisted vulnerability assessment control boundaries.
~~~

## Longer description

~~~text
AAEF-AI-VA demonstrates a control-oriented approach to AI-assisted vulnerability
assessment. The project treats AI output as a request, not authority. Assessment
execution remains blocked by default unless explicit authorization, scope,
preflight evidence, Tool Gateway behavior, and human review gates support the action.
~~~

## Announcement draft

~~~markdown
AAEF-AI-VA is now prepared as a public-facing repository candidate.

AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability
assessment control boundaries. The core design principle is simple:

AI output is not authority to perform assessment actions.

The project focuses on authorization, scope, preflight evidence, Tool Gateway
behavior, human review, publication hygiene, and validation checks. The current
release includes AGPL-3.0 licensing, a security policy, private artifact exclusion,
GitHub Actions validation, and public publication readiness documentation.

This is not a live scanner. It does not authorize scanning, external network
testing, credential injection, or customer-target operation.

The current value is the control model: how an AI-assisted assessment workflow can
remain blocked by default until the required gates are satisfied.
~~~

## Claims to use

Acceptable public claims:

- safety-first reference implementation
- AI-assisted vulnerability assessment control boundaries
- AI output is not authority to perform assessment actions
- fail-closed authorization and preflight posture
- evidence, review, and publication hygiene boundaries
- AGPL-3.0 code with a separate commercial licensing path
- current release does not authorize live scanning

## Claims to avoid

Avoid claims that imply:

- production scanner readiness
- autonomous vulnerability assessment readiness
- customer environment readiness
- permission to scan third-party systems
- credential handling readiness
- compliance certification
- legal advice
- audit opinion
- safety without human review

## Runtime and scanning boundary

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

Before tagging v0.4.3, verify:

1. README contains the GitHub Actions validation badge.
2. README contains public repository metadata guidance.
3. This metadata and announcement pack exists.
4. Repository URL is recorded.
5. Public positioning is recorded.
6. Announcement draft is recorded.
7. Claim boundaries are recorded.
8. `tools/run_all_local_checks.py` includes the metadata/announcement validation test.
9. Runtime execution remains disabled.

## Out of scope

This checkpoint does not:

- change repository visibility
- publish a GitHub release
- publish a social announcement
- configure GitHub About fields automatically
- configure GitHub topics automatically
- configure branch protection or rulesets
- enable private vulnerability reporting
- authorize runtime execution
- authorize scan execution
- authorize external network testing
- authorize credential injection
- authorize customer-target testing
