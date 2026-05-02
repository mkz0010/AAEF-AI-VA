# Contributing to AAEF-AI-VA

Thank you for considering a contribution.

AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability
assessment control boundaries.

## Ground rules

Contributions must preserve the core boundary:

> AI output is not authority to perform assessment actions.

Contributions must not enable runtime execution, live scanning, external network
testing, credential injection, customer-target operation, or unmanaged tool execution
without explicit maintainer review, documentation, tests, and a dedicated design
decision.

## Inbound contribution license

Unless separately agreed in writing, contributions are submitted under the same
license as the repository: GNU Affero General Public License v3.0.

By submitting a contribution, you represent that you have the right to submit it
under that license.

## Security reports

Do not submit sensitive vulnerability details through public issues or pull requests.

Use SECURITY.md for security reporting guidance.

## Commercial terms

A pull request, issue, discussion, fork, or contribution does not create a commercial
license, partnership, support agreement, endorsement, or managed-service approval.

Commercial licensing inquiries must be handled separately.

No commercial license grant is created by a pull request, issue, discussion, fork, contribution, or public repository interaction.

## Contribution boundaries

Allowed contributions may include:

- documentation improvements,
- tests,
- examples,
- validation hardening,
- safety-boundary clarifications,
- publication hygiene improvements,
- non-execution prototype scaffolding,
- local-only review artifacts.

High-risk contributions require special review, including anything that may affect:

- runtime execution,
- network activity,
- scanning,
- credential handling,
- target binding,
- customer-target operation,
- evidence capture of sensitive artifacts,
- report delivery authorization,
- commercial-use claims,
- legal or compliance claims.

## Claims to avoid

Contributions must not introduce claims that AAEF-AI-VA is:

- a production scanner,
- an autonomous vulnerability scanner,
- a customer-ready managed assessment platform,
- compliance certification,
- legal approval,
- audit opinion,
- permission to scan third-party systems,
- permission to inject credentials,
- replacement for professional security judgment.

## Private materials

Do not commit private customer materials, sales materials, pricing assumptions,
target account lists, credentials, secrets, generated run outputs, vulnerability
details, or local private notes.

Private local materials belong under `private-not-in-git/` and must remain untracked.
