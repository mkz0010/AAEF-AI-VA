# Sanitized Finding Candidate Model

## Purpose

This document defines the first sanitized finding candidate model for the AAEF-controlled AI Vulnerability Assessment Platform.

The sanitizer creates AI-visible-safe artifacts. The next step is to convert those sanitized artifacts into conservative finding candidates.

## Core Principle

A finding candidate is not a confirmed vulnerability.

A finding candidate is a review object derived from sanitized artifact metadata and summaries.

It must require human review before it can become a report finding.

## Current MVP Behavior

v0.1.24 adds:

- finding candidate module,
- finding candidate demo generator,
- finding candidate validation tests,
- conservative severity/confidence defaults,
- explicit human review requirement,
- report-ready blocking.

## Candidate Defaults

The MVP candidate uses:

~~~text
finding_candidate_status: candidate_requires_human_review
initial_severity: informational
initial_confidence: low
requires_human_review: true
report_ready: false
secret_exposed_to_ai: false
ai_visible_allowed: true
~~~

## Safety Boundary

Finding candidates must not include:

- raw adapter artifacts,
- raw artifact refs,
- Authorization headers,
- Cookie headers,
- Set-Cookie headers,
- raw passwords,
- CSRF tokens,
- session IDs,
- private IP addresses.

The candidate may include:

- sanitized artifact reference,
- redaction summary metadata,
- conservative observation summaries,
- limitations,
- review requirements.

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/finding-candidates/demo/
~~~

Generated files:

- `raw-artifact.demo.json`
- `sanitized-artifact.generated.json`
- `finding-candidate.generated.json`

## Example Command

~~~bash
py tools/generate_finding_candidate_demo.py
~~~

## Relationship to AI-assisted Analysis

AI may help analyze sanitized finding candidates, but AI must not confirm the vulnerability or make it report-ready by itself.

A human reviewer must validate:

- technical accuracy,
- exploitability,
- scope,
- false positive risk,
- severity,
- customer impact,
- remediation guidance.

## Future Work

Future versions should add:

- finding candidate schema,
- finding normalizer,
- CWE/OWASP/CVSS mapping candidates,
- duplicate finding grouping,
- evidence references,
- human validation workflow,
- report finding promotion gate.
