# v0.6.202 Static Fixture Review Path Public Communication Pack Candidate

Status: Candidate only

## Purpose

This checkpoint creates a candidate public communication pack for the `Static Fixture Review Path`.

This document is not a publication approval, announcement, release statement, sales page, customer PoC offer, or production-readiness claim.

The candidate wording in this document remains subject to v0.6.203 review and decision before it can be treated as accepted project wording.

## Source decision

v0.6.201 selected the next work item:

- selected_next_work_item = static_fixture_review_path_public_communication_pack
- selected_next_work_item_risk_tier = medium
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.202 Static Fixture Review Path Public Communication Pack Candidate
- selected_followup_checkpoint = v0.6.203 Static Fixture Review Path Public Communication Pack Review and Decision

## Candidate communication pack status

This candidate pack is:

- candidate-only
- not published
- not accepted
- not a public announcement
- not a demo release
- not a customer PoC invitation
- not a runtime or scanner readiness statement
- subject to v0.6.203 review and decision

## Candidate short public description

AAEF-AI-VA is a safety-first reference implementation showing how AI-assisted vulnerability assessment actions can be kept behind explicit gates.

Its current public review path is a `Static Fixture Review Path`: a static, mock, fixture-only, non-execution set of artifacts that lets reviewers inspect the request, gate decision, non-execution result, evidence trace, and reviewer walkthrough without running a scanner.

## Candidate medium public description

AAEF-AI-VA explores a controlled architecture for AI-assisted vulnerability assessment where AI output is a request, not authority.

The current externally reviewable path is the `Static Fixture Review Path`. It provides a static, mock, fixture-only, non-execution artifact set for reviewing how a proposed tool action is represented, how a gate decision is recorded, how non-execution is evidenced, and how a reviewer can trace the result.

This path is intended for architectural review and boundary discussion. It is not a live scanner, executable demo, production-ready scanner, customer PoC package, third-party testing authorization, certification, legal compliance statement, audit opinion, diagnostic completeness claim, or external-framework equivalence claim.

## Candidate README-compatible summary

The `Static Fixture Review Path` is the current safe public review path for AAEF-AI-VA.

It lets reviewers inspect a static, mock, fixture-only, non-execution example of the control boundary:

1. an AI-generated tool action request
2. a gate decision
3. a non-execution result
4. an evidence trace
5. a reviewer walkthrough

This path is for reviewing the architecture and evidence boundary. It does not run tools, authorize scanning, provide a production-ready workflow, or imply certification, legal compliance, audit sufficiency, diagnostic completeness, or equivalence with external frameworks.

## Candidate social-post-style draft

AAEF-AI-VA now has a safer public review phrase: `Static Fixture Review Path`.

The idea is simple:

AI can generate a proposed vulnerability-assessment action, but the AI does not become the authority to execute it.

The current review path is static, mock, fixture-only, and non-execution. It lets reviewers inspect the request, gate decision, non-execution result, evidence trace, and walkthrough without treating the repository as a scanner or live demo.

This is a candidate communication draft only. It is not published, not accepted, and remains subject to v0.6.203 review.

## Candidate wording to prefer

Prefer wording that says:

- `Static Fixture Review Path`
- `publicly reviewable static fixture set`
- `static, mock, fixture-only, non-execution review path`
- `reviewer-facing fixture walkthrough`
- `AI output is a request, not authority`
- `execution is decided by gates`
- `evidence links the request, gate decision, execution or non-execution result, and review`

## Candidate terms to avoid

Avoid using these phrases as project labels at this stage:

- `Public Demo`
- `Executable Demo`
- `Scanner Demo`
- `Working Demo`
- `PoC Demo`
- `Production Demo`
- `live scanner`
- `production-ready scanner`
- `customer PoC-ready package`

These terms can imply execution, scanning readiness, customer delivery readiness, or stronger assurance claims than the current repository supports.

## Candidate required boundary sentences

Public-facing descriptions should include at least one of the following boundary sentences, depending on context:

- AAEF-AI-VA is a safety-first reference implementation, not a live scanner.
- The current review path is static, mock, fixture-only, and non-execution.
- AI output is treated as a request, not authority.
- Execution is decided by gates, and evidence links the request, gate decision, execution or non-execution result, and review.
- The repository does not provide third-party testing authorization, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Candidate reviewer path summary

A reviewer should be directed to inspect the accepted static fixture set and read it in the following order:

1. `request.fixture.json`
2. `gate-decision.fixture.json`
3. `non-execution-result.fixture.json`
4. `evidence-trace.fixture.json`
5. `reviewer-walkthrough.md`

The reviewer should evaluate whether the fixture path clearly shows that the AI request is not execution authority, the gate decision is separately recorded, non-execution is evidenced, and the reviewer can reconstruct the boundary from the artifacts.

## Explicit non-goals for v0.6.202

v0.6.202 does not:

- publish any public announcement
- accept the communication pack as final project wording
- create a release announcement
- create a new fixture file
- create a public sample
- create an executable demo
- add runtime execution
- add scanner readiness
- authorize real scanner execution
- authorize customer PoC intake
- create AAEF main publication material
- create an AAEF main issue, PR, command, or URL
- create commercial contract terms
- create paid engagement approval
- create customer-specific material
- change validator behavior
- add a JSON Schema
- authorize runtime, scanner, Docker, sensitive-value, customer, or delivery activity
- promote this project into AAEF Core, Profile, or Practical Package

## Acceptance criteria for this candidate checkpoint

This checkpoint is complete when:

- the candidate short public description is recorded
- the candidate medium public description is recorded
- the candidate README-compatible summary is recorded
- the candidate social-post-style draft is recorded as not published
- preferred wording around `Static Fixture Review Path` is recorded
- terms to avoid are recorded
- required boundary sentences are recorded
- reviewer path summary is recorded
- the document states that v0.6.203 must review and decide before wording is accepted
