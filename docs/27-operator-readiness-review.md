# Operator Readiness Review

## Purpose

This document defines the operator readiness review layer for the AAEF-controlled AI Vulnerability Assessment Platform.

The real execution readiness gate produces machine-readable blockers. Operators need those blockers translated into a reviewable summary that supports approval, rejection, or remediation.

## Core Principle

A blocker list is not enough.

Execution readiness must be reviewable by a human operator before future bounded execution can be considered.

## What This Adds

v0.1.19 adds:

- operator-readable readiness summary,
- blocker categorization,
- next-action guidance,
- generated JSON review output,
- generated Markdown review output,
- tests for the review summary.

## Review Inputs

The operator review is derived from:

- command plan,
- controlled executor result,
- real execution readiness gate result,
- blockers reported by the readiness gate.

## Review Output

The generated review includes:

- review status,
- decision recommendation,
- real execution permission status,
- command plan ID,
- tool,
- operation,
- target ID,
- scope ID,
- blocker count,
- blockers,
- blocker categories,
- next actions,
- operator decision checklist,
- operator notes section.

## Default Recommendation

The current MVP recommendation is:

~~~text
do_not_execute
~~~

This is expected because real execution remains disabled and command plans remain dry-run-only.

## Generated Files

The operator review generator writes ignored/private outputs under:

~~~text
private-not-in-git/operator-reviews/real-execution-readiness/
~~~

Generated files:

- `operator-readiness-review.generated.json`
- `operator-readiness-review.generated.md`

## Example Command

~~~bash
py tools/generate_operator_readiness_review.py
~~~

## Relationship to Real Execution Readiness Gate

The readiness gate answers:

~~~text
Can this command plan move toward real execution?
~~~

The operator review answers:

~~~text
Why or why not, and what should the operator do next?
~~~

## Future Use

Before real execution is introduced, the operator review should be extended to include:

- reviewer identity,
- approval timestamp,
- approval scope,
- approval expiration,
- required remediation owner,
- evidence link,
- runtime approval link,
- customer authorization reference.
