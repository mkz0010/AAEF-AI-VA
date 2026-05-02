# Sanitizer and Redaction Policy

## Purpose

This document defines the first sanitizer and redaction policy scaffold for the AAEF-controlled AI Vulnerability Assessment Platform.

The project is moving toward real tool integration. Before raw ZAP, Burp, Nmap, nuclei, or browser artifacts are ever shown to AI, the platform needs a sanitizer boundary.

## Core Principle

Raw adapter output must not be AI-visible.

Only sanitized artifacts may become AI-visible or report-draft input.

## Why This Matters

Real diagnostic tools can emit sensitive material such as:

- Authorization headers,
- cookies,
- Set-Cookie headers,
- bearer tokens,
- API keys,
- CSRF tokens,
- session identifiers,
- passwords,
- private IP addresses,
- internal hostnames,
- raw request and response bodies,
- screenshots,
- stack traces.

The sanitizer is the boundary between raw tool output and AI-visible content.

## Current MVP Behavior

v0.1.23 adds:

- sanitizer module,
- redaction policy JSON,
- generated sanitized artifact demo,
- sanitizer tests,
- fail-closed checks for unsafe artifact paths,
- validation that obvious sensitive literals are not left in sanitized output.

## Generated Files

The demo generator writes ignored/private outputs under:

~~~text
private-not-in-git/sanitized-artifacts/demo/
~~~

Generated files:

- `raw-artifact.demo.json`
- `sanitized-artifact.generated.json`

## Example Command

~~~bash
py tools/generate_sanitized_artifact_demo.py
~~~

## Redaction Categories

The MVP policy includes initial categories for:

- credential or token material,
- session material,
- internal network values.

## AI-visible Rule

The sanitizer output may set:

~~~text
ai_visible_allowed: true
~~~

only after sanitizer completion.

It must also keep:

~~~text
secret_exposed_to_ai: false
~~~

## Relationship to Evidence Reconstruction

Evidence reconstruction explains whether secrets were exposed to AI.

The sanitizer provides the future technical boundary that makes that claim stronger when real tool outputs are introduced.

## Future Work

Future versions should add:

- structured HTTP request/response redaction,
- screenshot classification,
- allowlist-based field extraction,
- finding normalizer,
- sanitized finding candidate model,
- redaction coverage reporting,
- customer-specific retention settings,
- policy version binding to evidence records.

## Relationship to Finding Candidates

Sanitized artifacts may be converted into finding candidates.

A finding candidate is not a confirmed vulnerability and must require human review before report use.

See `docs/32-sanitized-finding-candidate-model.md`.
