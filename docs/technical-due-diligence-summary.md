# Technical Due Diligence Summary

Status: candidate
Version: v0.6.146
Date: 2026-05-10

## Reader

This summary is for technical due-diligence reviewers, security architects, vulnerability assessment engineers, enterprise security reviewers, and commercial evaluation teams reviewing AAEF-AI-VA after the Enterprise Review Guide.

## Purpose

The purpose of this summary is to describe the technical review surface of AAEF-AI-VA without expanding claims, creating deployment approval, or granting permission to test any real system.

Core technical proposition:

~~~text
AI output is a request; gates decide execution.
~~~

The summary helps reviewers inspect how the repository separates AI-request generation, gate decisions, evidence records, non-execution records, and reviewer-facing interpretation.

## Technical positioning

AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability assessment control boundaries.

It should be reviewed as a technical control-boundary example, not as a live scanner.

The project is useful for technical review because it demonstrates how an AI-assisted diagnostic workflow can represent:

* proposed action,
* authorization and scope checks,
* gate outcome,
* execution or non-execution status,
* evidence linkage,
* reviewer interpretation,
* claim boundaries.

## Control surface overview

The technical control surface includes these review areas:

| Area | What to review |
| --- | --- |
| AI request boundary | Whether AI output is treated as a request, not execution authority. |
| Gate decision boundary | Whether a gate decides allowed, blocked, or human-review-required outcomes. |
| Scope and target boundary | Whether target mode, destination binding, and scope support are explicit. |
| Authorization time boundary | Whether authorization expiry can be evaluated against the relevant current time. |
| Request/decision drift boundary | Whether request constraints and decision constraints can be compared. |
| External discovery boundary | Whether external discovery fails closed unless explicitly allowed and boundary-compatible. |
| Mock/dry-run status boundary | Whether mock/dry-run completion is separated from real execution completion. |
| Evidence boundary | Whether request, decision, execution/non-execution, and result are linked for review. |
| Private artifact boundary | Whether raw/private artifacts stay out of public documentation. |
| Delivery boundary | Whether report and delivery authorization remain separate review stages. |

## Repository review surface

A technical reviewer should inspect:

* `README.md` for public positioning and baseline language,
* `docs/enterprise-review-guide.md` for reviewer framing,
* gate-related tests under `tools/`,
* generated-output validation tests,
* authorization expiry helper and tests,
* request/decision constraint-diff helper and tests,
* external discovery fail-closed helper and tests,
* mock/dry-run status terminology helper and tests,
* evidence chain, reconstruction, finding, report, packet, and delivery gate tests,
* publication hygiene and private artifact exclusion tests,
* licensing and commercial-use boundary tests.

The review should focus on what the repository proves locally and what remains explicitly out of scope.

## Evidence paths

Reviewers should trace at least these evidence paths:

1. AI request or proposed action.
2. Gate input.
3. Gate decision outcome.
4. Execution or non-execution record.
5. Evidence chain linkage.
6. Reconstruction or reviewer-facing summary.
7. Finding or report promotion gate, when applicable.
8. Delivery authorization gate, when applicable.

The important question is not whether model text sounds plausible.

The important question is whether the repository can show evidence-linked review points.

## Gate-semantics checks

A due-diligence review should verify that the repository contains checks or tests for:

* authorization expiry compared to relevant current time,
* request/decision constraint drift,
* external discovery fail-closed behavior,
* localhost-only and local-lab-only target boundary handling,
* destination binding handling,
* scope support handling,
* ambiguous target boundary handling,
* invalid or expired authorization handling,
* mock/dry-run completed terminology,
* non-execution evidence,
* human approval preservation.

These checks support reviewability. They do not grant operational permission.

## Non-execution boundaries

The project repeatedly records blocked, mock, dry-run, or review-required states.

A reviewer should confirm that:

* non-execution is represented explicitly,
* blocked outcomes are not treated as execution success,
* mock/dry-run completed terminology is disambiguated,
* real execution permission remains false unless separately authorized,
* customer target authorization is not implied,
* delivery authorization remains separately gated.

## Runtime boundary

AAEF-AI-VA should not be reviewed as a production runtime.

Reviewers should treat runtime-related artifacts as boundary demonstrations unless a later scoped implementation explicitly changes that.

Questions to ask:

* What runtime behavior is actually implemented?
* What is scaffold, candidate, review record, or documentation?
* Which tests prove non-execution?
* Which tests prove fail-closed handling?
* Which code paths remain demonstration-only?

## Credential and data boundary

A technical review should confirm that credentials and private data are not exposed to AI output or public artifacts.

Reviewers should inspect whether:

* credential references are used instead of raw secrets,
* redaction tests exist,
* private artifacts remain under private-not-in-git paths,
* public examples avoid customer-specific or secret material,
* evidence-safe result models avoid copying raw credentials, tokens, or private customer data.

## Public/private artifact boundary

AAEF-AI-VA relies on a public/private split.

Public artifacts may show safe patterns, docs, sanitized examples, and tests.

Private artifacts may contain generated local run outputs, raw artifacts, private review outputs, or local-only evidence.

Reviewers should verify that public artifacts do not accidentally include private outputs, secrets, customer data, or operational playbooks that should remain outside public materials.

## Due-diligence questions

Technical reviewers should ask:

* What exact action did the AI request?
* What gate made the execution decision?
* What evidence supported the gate outcome?
* What was blocked, mocked, or routed for review?
* What was actually executed, if anything?
* Was authorization current at the relevant time?
* Did request constraints drift from decision constraints?
* Was external discovery explicitly allowed and boundary-compatible?
* Are target and destination bindings explicit?
* Are mock/dry-run statuses disambiguated?
* Are private artifacts excluded from public docs?
* Are claim boundaries conservative?

## Review artifacts to inspect

Recommended review artifacts:

| Artifact | Review purpose |
| --- | --- |
| `docs/enterprise-review-guide.md` | Overall reviewer framing and claim boundaries. |
| `docs/technical-due-diligence-summary.md` | Technical review surface and evidence paths. |
| `tools/run_all_local_checks.py` | Local validation entry point. |
| Authorization expiry tests | Current-time authorization review. |
| Request/decision constraint-diff tests | Constraint drift review. |
| External discovery fail-closed tests | External target expansion review. |
| Mock/dry-run status terminology tests | Status interpretation review. |
| Evidence chain and reconstruction tests | Review traceability. |
| Report and delivery gate tests | Finding/report/delivery separation. |
| Publication hygiene tests | Public/private artifact boundary. |

## Follow-on PoC considerations

A controlled PoC should be separate from this summary.

A future PoC plan should define:

* written authorization,
* target inventory,
* excluded systems,
* network boundaries,
* tool set,
* credential handling,
* logging and evidence retention,
* human review responsibility,
* stop conditions,
* data retention and deletion,
* delivery boundary,
* commercial and license boundary.

This summary does not create that plan.

## Claim boundaries

This summary must remain conservative.

This summary is not a certification scheme.

This summary is not a legal compliance statement.

This summary is not an audit opinion.

This summary does not grant permission to test third-party systems.

This summary does not assert deployment sufficiency.

This summary does not assert equivalence with external frameworks.

Do not interpret this summary as:

* certification,
* legal compliance determination,
* audit opinion,
* audit sufficiency determination,
* deployment approval,
* complete vulnerability assessment capability,
* permission for testing third-party systems,
* equivalence mapping to external frameworks,
* proof that gate-free AI tool execution is acceptable,
* promotion of AAEF-AI-VA into AAEF Core, Profile, or Practical Package status.

Allowed interpretation:

~~~text
AAEF-AI-VA is a safety-first reference implementation and technical control-boundary example for reviewable AI-assisted vulnerability assessment action requests.
~~~
