# 0046: Add negative preflight evidence examples

Status: addressed in v0.3.4

## Problem

The project has positive generated preflight evidence examples and validation rules, but it also needs representative invalid evidence claims to prove that unsafe claims fail closed.

## Scope

Add negative examples for:

- missing input evidence
- mismatched runtime-target binding
- stale runtime readiness state
- false `execution_authorized = true`
- false `preflight_satisfied = true`
- AI-visible raw evidence
- raw artifact capture permitted
- example/live evidence confusion
- no-egress verified spoofing
- sanitizer boundary verified spoofing

## Acceptance criteria

- Negative examples are recorded.
- Negative examples are validated.
- All examples are non-live examples.
- All examples fail closed.
- No negative example satisfies preflight.
- No negative example authorizes execution.
- No negative example permits runtime execution.
- No negative example permits network activity.
- No negative example permits raw artifact capture.
- Local checks pass.

## Runtime boundary

This issue does not enable ZAP startup, ZAP API calls, spidering, active scanning, authenticated crawling, external process execution, network activity, credential injection, live evidence generation, or raw artifact capture.
