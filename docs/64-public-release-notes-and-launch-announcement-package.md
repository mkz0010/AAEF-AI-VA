# Public Release Notes and Launch Announcement Package

Version: v0.4.5 candidate  
Status: public communication package; does not publish a GitHub Release or announcement

## Purpose

This package prepares public communication materials for AAEF-AI-VA after the public
repository launch checkpoint.

It provides reusable text for:

- GitHub Release notes,
- short repository descriptions,
- longer launch announcements,
- LinkedIn-style posts,
- Zenn/Qiita-style technical article leads,
- commercial inquiry wording,
- claim boundaries.

This checkpoint does not publish a GitHub Release, social post, article, or sales
material. It prepares text for manual review.

## Repository

~~~text
Repository: https://github.com/mkz0010/AAEF-AI-VA
Visibility: PUBLIC
License: AGPL-3.0
Security policy: SECURITY.md
Private vulnerability reporting: enabled
GitHub Actions validation: active and passing
Latest launch checkpoint: v0.4.4
~~~

## Core message

~~~text
AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability
assessment control boundaries.

The core principle is:

AI output is not authority to perform assessment actions.

AI may request assessment actions, but execution is decided by authorization,
contractual scope, Tool Gateway behavior, preflight evidence, and human review.
~~~

## GitHub Release notes draft

Title:

~~~text
AAEF-AI-VA v0.4.5 Public Launch Communication Package
~~~

Body:

~~~markdown
AAEF-AI-VA is now available as a public safety-first reference implementation for
AI-assisted vulnerability assessment control boundaries.

The project demonstrates a control-oriented approach to AI-assisted security work:
AI output is treated as a request, not authority. Assessment actions remain blocked
unless authorization, contractual scope, Tool Gateway behavior, preflight evidence,
and human review boundaries support the action.

This release adds public communication material for the launch phase:

- GitHub Release notes draft
- short and long public descriptions
- LinkedIn-style announcement draft
- Zenn/Qiita-style technical article lead
- commercial inquiry wording
- public claim boundaries

The repository already includes:

- AGPL-3.0 license
- SECURITY.md
- private vulnerability reporting enabled
- GitHub Actions validation
- publication hygiene and private artifact exclusion
- runtime and scanning boundaries documented as disabled

This is not a live scanner and does not authorize third-party scanning, external
network testing, credential injection, or customer-target operation.
~~~

## Short public introduction

~~~text
AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability
assessment control boundaries. It shows how AI-assisted assessment workflows can
remain blocked by default until authorization, scope, evidence, Tool Gateway, and
human review gates are satisfied.
~~~

## Longer public announcement

~~~markdown
AAEF-AI-VA has been launched as a public repository.

AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability
assessment control boundaries. It is built around a simple principle:

AI output is not authority to perform assessment actions.

In an AI-assisted vulnerability assessment workflow, an AI system may propose or
request an assessment action. But the decision to execute that action should be made
by explicit authorization, contractual scope, Tool Gateway behavior, preflight
evidence, and human review.

The repository currently focuses on the control model rather than live scanning:

- authorization and execution-blocking gates
- Tool Gateway behavior
- preflight evidence model and validation rules
- negative evidence examples
- human review and report review gates
- publication hygiene and private artifact exclusion
- SECURITY.md and private vulnerability reporting
- GitHub Actions validation

The current release does not authorize live scanning, external network testing,
credential injection, or customer-target operation.

The goal is to make AI-assisted vulnerability assessment safer by making execution
authority explicit, reviewable, and evidence-bound.
~~~

## LinkedIn-style announcement draft

~~~text
I have published AAEF-AI-VA, a safety-first reference implementation for
AI-assisted vulnerability assessment control boundaries.

The core idea is simple:

AI output is not authority to perform assessment actions.

AI may request an assessment action, but execution should be decided by explicit
authorization, contractual scope, Tool Gateway behavior, preflight evidence, and
human review.

This repository is not a live scanner. It is a control-boundary reference
implementation: how to keep AI-assisted assessment workflows blocked by default
until the required gates are satisfied.

Repository:
https://github.com/mkz0010/AAEF-AI-VA
~~~

## Zenn/Qiita-style technical article lead

~~~markdown
# AIに脆弱性診断を任せる前に、「実行権限」を分離する

AI-assisted vulnerability assessment is not only a model capability problem.
It is an authority and execution-boundary problem.

AAEF-AI-VA is a safety-first reference implementation that explores this boundary.
The central principle is:

> AI output is not authority to perform assessment actions.

The project shows how AI-generated assessment requests can remain blocked until
authorization, contractual scope, Tool Gateway behavior, preflight evidence, and
human review gates support the action.
~~~

## Commercial inquiry wording

Recommended wording:

~~~text
AAEF-AI-VA is licensed under AGPL-3.0. Organizations that want to embed, modify, or
operate the platform in a way that does not align with AGPL-3.0 obligations may
request a separate commercial license discussion.

Commercial licensing inquiries are separate from vulnerability reports and do not
authorize runtime execution or third-party scanning.
~~~

## Security reporting wording

Recommended wording:

~~~text
Security reports should follow SECURITY.md. Sensitive vulnerability details should
not be posted publicly. Private vulnerability reporting is enabled for this public
repository.
~~~

## Claims to use

Acceptable claims:

- safety-first reference implementation
- AI-assisted vulnerability assessment control boundaries
- AI output is not authority to perform assessment actions
- execution authority is explicit, reviewable, and evidence-bound
- current release keeps runtime execution disabled
- current release does not authorize live scanning
- GitHub Actions validation is active
- private vulnerability reporting is enabled
- AGPL-3.0 with potential separate commercial licensing discussion

## Claims to avoid

Avoid claims that imply:

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

## Manual publication checklist

Before publishing any announcement:

1. Confirm GitHub Actions is passing.
2. Confirm README badge is green.
3. Confirm SECURITY.md is visible.
4. Confirm private vulnerability reporting remains enabled.
5. Confirm no generated artifacts under `private-not-in-git/` are tracked.
6. Confirm release text does not imply live scanning or customer-target readiness.
7. Confirm commercial inquiry wording does not sound like legal advice.
8. Confirm the announcement links to the public repository.
9. Confirm any Japanese article distinguishes AAEF-AI-VA from the parent AAEF framework.
10. Confirm runtime execution remains disabled.

## Out of scope

This checkpoint does not:

- publish a GitHub Release
- publish a LinkedIn post
- publish a Zenn or Qiita article
- create a commercial contract
- provide legal advice
- authorize runtime execution
- authorize scan execution
- authorize external network testing
- authorize credential injection
- authorize customer-target testing

## Follow-up candidates

- Create GitHub Release from the release notes draft.
- Prepare a LinkedIn launch post.
- Prepare a Zenn article explaining the authority-boundary model.
- Add a durable commercial contact channel.
- Add dependency/license inventory.
- Add branch protection / ruleset planning.
