# Enterprise Review Guide

Status: candidate
Version: v0.6.143
Date: 2026-05-10

## Reader

This guide is for enterprise reviewers, vulnerability assessment company decision-makers, security architects, and technical reviewers evaluating AAEF-AI-VA as a safety-first reference implementation for AI-assisted vulnerability assessment control boundaries.

## Purpose

The purpose of this guide is to help reviewers understand what AAEF-AI-VA demonstrates, what it does not demonstrate, and what should be checked before any real deployment, customer evaluation, commercial evaluation, or internal adoption discussion.

AAEF-AI-VA should be reviewed as an applied implementation boundary example.

Core review proposition:

~~~text
AI output is a request; gates decide execution.
~~~

This means model output can propose or request a diagnostic action, but the authority to execute is represented by gate decisions, scope checks, evidence records, and reviewer-visible control boundaries.

## Decision-maker summary

AAEF-AI-VA is most useful when a reviewer wants to evaluate whether an AI-assisted vulnerability assessment workflow can keep these questions separate:

* What did the AI request?
* What authority existed at decision time?
* What gate allowed, blocked, or required human approval?
* What evidence links the request, decision, execution/non-execution, and result?
* What remains outside the current safe boundary?

AAEF-AI-VA should not be evaluated as a live vulnerability scanner.

It should be evaluated as a safety-first reference implementation for showing how AI-assisted diagnostic actions can be controlled, evidenced, blocked, and reviewed.

## What AAEF-AI-VA demonstrates

AAEF-AI-VA demonstrates a boundary pattern for AI-assisted vulnerability assessment workflows.

It demonstrates:

* separation between AI-generated request and execution authority,
* gate-mediated action decisions,
* scope and target-boundary review concepts,
* authorization expiry review concepts,
* request/decision constraint-diff review concepts,
* external discovery fail-closed review concepts,
* mock/dry-run status terminology clarification,
* evidence chain linkage for review,
* non-execution evidence,
* reviewer-readable decision records,
* private artifact separation,
* public claim-boundary discipline.

The project is strongest as a conversation artifact, reference implementation, and review scaffold for organizations that want AI assistance but need explicit control over tool execution.

## What AAEF-AI-VA does not demonstrate

This guide is not a certification scheme.

This guide is not a legal compliance statement.

This guide is not an audit opinion.

This guide does not authorize third-party testing.

This guide does not assert deployment sufficiency.

This guide does not assert equivalence with external frameworks.

AAEF-AI-VA does not by itself demonstrate:

* complete diagnostic coverage,
* customer target authorization,
* live scanner operation,
* operational approval for real environments,
* legal permission to test any system,
* audit sufficiency,
* regulatory sufficiency,
* enterprise deployment sufficiency,
* replacement of human review,
* replacement of contract scope review,
* replacement of security program governance.

## Review path

A practical enterprise review can use this sequence:

1. Confirm the project boundary.
2. Review the AI request / gate decision split.
3. Review target scope and destination binding behavior.
4. Review authorization expiry handling.
5. Review request/decision constraint-diff handling.
6. Review external discovery fail-closed handling.
7. Review mock/dry-run completed terminology.
8. Review evidence chain and reconstruction outputs.
9. Review private artifact and redaction boundaries.
10. Decide whether a separate controlled PoC plan is warranted.

This review path is only a review aid. It is not a deployment approval.

## Evidence review questions

Reviewers should ask:

* Can the project show what the AI requested?
* Can the project show whether the action was allowed, blocked, or routed for human approval?
* Can the project show the evidence that supported the gate outcome?
* Can the project distinguish execution from non-execution?
* Can the project explain why a mock/dry-run `completed` record is not the same as real execution completion?
* Can the project preserve reviewer traceability without exposing secrets or private customer material?
* Can the project show the difference between candidate finding, reviewed finding, report finding, report packet, and delivery authorization concepts?

A good answer should point to evidence artifacts, gate records, and status terminology rather than relying on model text alone.

## Gate-semantics review questions

Reviewers should inspect whether the gate-semantics work answers these questions:

* Is authorization evaluated against the relevant current time?
* Can a request drift from the authorization decision without being detected?
* Does external discovery fail closed unless explicitly allowed and boundary-compatible?
* Are ambiguous target-boundary inputs treated as review or block conditions rather than permissive defaults?
* Are credential references handled as references rather than raw secrets?
* Are reviewer-facing statuses clear enough to avoid confusing mock/dry-run results with real execution?

These checks support reviewability. They do not create permission to run tools against real targets.

## Demo boundary review

AAEF-AI-VA public demos and examples should be reviewed as safe demonstration artifacts.

A reviewer should verify:

* examples avoid raw secrets,
* private generated artifacts remain under private-not-in-git paths,
* public samples are sanitized,
* mock/dry-run outputs are clearly labeled,
* local target or lab boundaries are explicit,
* real execution remains gated and separately reviewed,
* no customer target is implied.

If a reviewer wants a real-world PoC, that should be handled as a separate controlled plan with written scope, authorization, environment, tool, credential, evidence-retention, and human-review terms.

## Deployment due-diligence prompts

Before any real internal use, the organization should separately review:

* legal authority to test,
* customer or asset-owner authorization,
* contract scope,
* target inventory and exclusions,
* network boundaries,
* credential handling,
* tool safety controls,
* logging and evidence retention,
* human review responsibilities,
* incident response path,
* data retention and deletion,
* third-party dependency review,
* license review,
* operational owner sign-off.

AAEF-AI-VA does not replace these reviews.

## Commercial evaluation boundary

For commercial evaluation, the safe question is not:

~~~text
Can this autonomously run vulnerability assessments?
~~~

The safer question is:

~~~text
Can this architecture make AI-assisted diagnostic requests reviewable, gated, and evidence-linked before any real action is allowed?
~~~

Enterprise reviewers should evaluate:

* whether the control boundary is understandable,
* whether evidence is sufficient for reviewer traceability,
* whether non-execution is explicitly represented,
* whether claim boundaries are conservative,
* whether a controlled PoC can be defined without expanding public claims.

## Claim boundaries

This guide must remain conservative.

Do not interpret this guide as:

* certification,
* legal compliance determination,
* audit opinion,
* audit sufficiency determination,
* deployment approval,
* complete vulnerability assessment capability,
* authorization for testing third-party systems,
* equivalence mapping to external frameworks,
* proof that AI can safely run tools without gates,
* promotion of AAEF-AI-VA into AAEF Core, Profile, or Practical Package status.

Allowed interpretation:

~~~text
AAEF-AI-VA is a safety-first reference implementation that demonstrates reviewable control boundaries for AI-assisted vulnerability assessment action requests.
~~~

## Suggested review outcome categories

Reviewers may classify their review outcome as:

| Outcome | Meaning |
| --- | --- |
| Understandable reference boundary | The project is understandable as a reference implementation and discussion artifact. |
| Needs more evidence | Reviewers need clearer artifacts or examples before deeper evaluation. |
| PoC candidate | A separate controlled PoC plan may be worth drafting. |
| Not suitable for current use | The project does not match the organization's needs or risk tolerance. |

These outcome categories are not certification results and are not deployment approvals.

## Reviewer notes

Useful reviewer notes should be evidence-linked.

Examples:

* Which artifact supported the conclusion?
* Which boundary remained unclear?
* Which real-world assumption would require separate authorization?
* Which claim must remain out of public materials?
* Which private operational detail should not be moved into public documentation?
