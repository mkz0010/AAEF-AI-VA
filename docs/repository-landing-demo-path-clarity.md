# Repository Landing and Demo Path Clarity

Status: draft_candidate
Version: v0.6.196
Date: 2026-05-13

## Purpose

This document is documentation-only.

It defines how repository landing surfaces should point reviewers to the accepted safe demo fixture set without implying scanner readiness, executable demo status, public demo status, PoC readiness, delivery authorization, or authorization to test third-party systems.

## Accepted fixture set path

The accepted static fixture set is located at:

~~~text
docs/examples/safe-demo/blocked-tool-action-request-review/
~~~

The accepted fixture set was reviewed and accepted in:

~~~text
v0.6.194 Safe Demo Fixture Set Review and Decision
docs/270-v06194-safe-demo-fixture-set-review-and-decision.md
~~~

## Review order

Reviewers should inspect the fixture set in this order:

1. `request.fixture.json`
2. `gate-decision.fixture.json`
3. `non-execution-result.fixture.json`
4. `evidence-trace.fixture.json`
5. `reviewer-walkthrough.md`

## Expected reviewer conclusion

~~~text
AI output did not become authority.
The gate decision controlled execution.
Execution was not permitted.
Execution did not occur.
The non-execution outcome is reviewable from static fixture evidence.
~~~

## Boundary statements

The accepted fixture set is static, mock, fixture-only, non-execution, and reviewer-facing.

The accepted fixture set is not a scanner.

The accepted fixture set is not an executable demo.

The accepted fixture set is not a public demo.

The accepted fixture set is not PoC readiness.

The accepted fixture set is not delivery authorization.

The accepted fixture set is not authorization to test third-party systems.

The accepted fixture set is not production readiness evidence.

The accepted fixture set is not diagnostic completeness evidence.

The accepted fixture set is not certification, legal compliance, or audit opinion.

## README landing expectation

README should include a compact landing entry that points to the accepted fixture path, lists the five review files, identifies the expected reviewer conclusion, links to the v0.6.194 review and decision record, and links to this clarity document.

## AAEF main boundary

AAEF main contact publication remains deferred.

This candidate does not modify AAEF main.

This candidate does not reopen the AAEF main handback sequence.

## Candidate status

Review and decision are deferred to:

~~~text
v0.6.197 Repository Landing and Demo Path Clarity Review and Decision
~~~

<!-- v0.6.209-static-fixture-review-path-wording:start -->
## v0.6.209 Static Fixture Review Path wording candidate

This section is a repository wording integration implementation candidate for docs\repository-landing-demo-path-clarity.md.

The current review path is the `Static Fixture Review Path`: a static, mock, fixture-only, non-execution, reviewer-facing path for inspecting how AI-generated tool action requests, gate decisions, non-execution results, evidence traces, and review fit together.

AI output is treated as a request, not authority. Execution is decided by gates. Evidence links the request, gate decision, execution or non-execution result, and review.

Publication remains deferred. This candidate wording is not accepted until v0.6.210 review and decision. It is not a public announcement, social-post instruction, live scanner, executable demo, customer PoC package, production-readiness claim, certification claim, legal compliance statement, audit opinion, diagnostic completeness claim, or external-framework equivalence claim.
<!-- v0.6.209-static-fixture-review-path-wording:end -->
