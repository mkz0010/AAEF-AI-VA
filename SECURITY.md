# Security Policy

AAEF-AI-VA is an implementation project for AI-assisted vulnerability assessment
control boundaries. It is currently a safety-first reference implementation and
does not authorize live scanning, external network activity, credential injection,
or customer-target execution.

## Supported versions

The latest tagged local release is the primary review target.

| Version | Security support posture |
| --- | --- |
| v0.3.x | Public-review candidate; security reports accepted after a durable reporting channel is published |
| Earlier versions | Historical local development snapshots |

## Reporting a vulnerability

A durable security reporting channel has not yet been published.

Until a durable contact channel is added, do not disclose sensitive vulnerability
details in public issues, public discussions, screenshots, logs, or social posts.

Once a durable reporting channel is published, vulnerability reports should include:

- affected version or commit
- affected file or component
- concise description of the issue
- reproduction steps that do not require attacking third-party systems
- whether the issue affects repository publication safety, evidence integrity,
  authorization boundaries, private artifact exclusion, or runtime-execution controls

## Scope

In scope:

- authorization, preflight, and execution-blocking logic
- evidence record, evidence validation, and negative evidence examples
- private artifact exclusion and publication hygiene checks
- license/commercial-use boundary text that could mislead users about obligations
- README, SECURITY.md, and public documentation claims that could imply unsafe execution
- tests that fail to preserve safety, evidence, or publication boundaries

Out of scope:

- requests to run scans against third-party systems
- requests to validate live customer targets
- exploit development against real services
- credential collection, credential injection, or secret handling against real systems
- ZAP execution, active scanning, external network testing, or authenticated crawling
- generated artifacts under `private-not-in-git/`
- legal advice about AGPL-3.0, CC BY 4.0, or commercial contracts

## Runtime and scanning boundary

Repository publication does not authorize runtime execution.

The following must remain false unless future explicit implementation work changes
the authorization model and all required gates are satisfied:

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

## Safe testing expectations

Security reports should use local source review, local unit tests, or isolated
demonstrations that do not contact third-party systems.

Do not:

- scan external systems
- test against customer environments
- submit credentials
- submit secrets
- attach private generated artifacts
- attach raw logs containing tokens, credentials, personal data, or customer data

## Disclosure handling

Until a durable channel exists, this policy records the intended handling model:

1. A report is received through a non-public channel.
2. The issue is triaged for safety, publication hygiene, evidence integrity, and
   authorization-boundary impact.
3. Reproduction is performed locally without external scanning.
4. A fix is prepared without weakening runtime-execution boundaries.
5. Public disclosure is coordinated after a safe fix or mitigation is available.

## Commercial and legal boundary

Commercial licensing inquiries are separate from vulnerability reports.

This policy does not provide legal advice, contract terms, audit opinions, compliance
certification, or authorization to use the project against third-party targets.

## Reporting channel and scope clarification

Use GitHub Security Advisories / private vulnerability reporting for sensitive reports about this repository when that channel is available.

If the private reporting channel is unavailable, open a public GitHub issue only for non-sensitive coordination and do not include exploit details, secrets, credentials, target-specific data, private customer material, scanner output, or other sensitive information.

Security reports for this repository should concern the AAEF-AI-VA implementation, documentation, examples, release process, or repository configuration.

This repository is not an authorization to test third-party systems. Do not use this repository, its examples, or its documentation as permission to scan, attack, probe, exploit, or otherwise test systems that you do not own or do not have explicit written authorization to assess.

Do not submit live third-party vulnerability details, customer target data, credentials, tokens, private scan output, exploit chains, or operationally sensitive diagnostics through public issues.

AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability assessment control boundaries. It is not a production vulnerability scanner, not a managed vulnerability disclosure program, not a bug bounty program, not an emergency response service, not a certification scheme, not a legal compliance claim, not an audit opinion, and not an authorization service.

For questions about commercial licensing, paid evaluation, or NDA-based adoption discussions, use the commercial contact path described in the repository documentation rather than the vulnerability reporting channel.
