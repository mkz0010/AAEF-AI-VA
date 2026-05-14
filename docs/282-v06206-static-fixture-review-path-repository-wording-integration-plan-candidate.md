# v0.6.206 Static Fixture Review Path Repository Wording Integration Plan Candidate

Status: Candidate only

## Purpose

This checkpoint creates a candidate repository wording integration plan for the `Static Fixture Review Path` wording accepted in v0.6.204 for repository wording use.

This document is a plan candidate only. It does not apply wording changes to the selected repository surfaces.

This checkpoint is not a publication approval, not a public announcement, not a release announcement, not a social-post instruction, not a customer PoC invitation, not a runtime-readiness approval, and not a scanner-readiness approval.

## Source decision

v0.6.205 selected the next work item:

- selected_next_work_item = static_fixture_review_path_repository_wording_integration_plan
- selected_next_work_item_risk_tier = medium
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.206 Static Fixture Review Path Repository Wording Integration Plan Candidate
- selected_followup_checkpoint = v0.6.207 Static Fixture Review Path Repository Wording Integration Plan Review and Decision

## Candidate plan status

This candidate plan is:

- candidate only
- not accepted
- not applied
- not published
- not a publication approval
- not a social-post instruction
- subject to v0.6.207 review and decision

## Candidate integration objective

The objective is to plan how v0.6.204 accepted wording may be integrated into repository-facing documentation without expanding the project boundary.

The integration plan should make the current review path easier to find and understand while preserving these constraints:

- the path remains a `Static Fixture Review Path`
- the path remains static, mock, fixture-only, non-execution, and reviewer-facing
- AI output remains a request, not authority
- execution remains decided by gates
- evidence remains linked to request, gate decision, execution or non-execution result, and review
- publication remains deferred
- no runtime, scanner, customer PoC, production, certification, legal, audit, diagnostic-completeness, or external-framework-equivalence claim is added

## Candidate target surfaces

The candidate integration plan may cover the following repository-facing surfaces:

1. `README.md`
   - Purpose: keep the front page wording aligned with the accepted `Static Fixture Review Path` phrase.
   - Candidate action type: wording alignment only.
   - Boundary: do not turn README into a public announcement, demo page, sales page, customer PoC offer, scanner capability statement, or production-readiness statement.

2. `docs/repository-landing-demo-path-clarity.md`
   - Purpose: align existing repository landing and review-path clarity wording with the accepted `Static Fixture Review Path` phrase.
   - Candidate action type: wording alignment and boundary reinforcement only.
   - Boundary: do not introduce Public Demo, Executable Demo, Scanner Demo, Working Demo, PoC Demo, or Production Demo labels.

3. `docs/examples/safe-demo/blocked-tool-action-request-review/reviewer-walkthrough.md`
   - Purpose: ensure reviewer-facing path language remains static, mock, fixture-only, and non-execution.
   - Candidate action type: small wording alignment only if needed.
   - Boundary: do not change fixture semantics, evidence semantics, schema behavior, or validator behavior.

4. `docs/examples/safe-demo/blocked-tool-action-request-review/`
   - Purpose: confirm the fixture set remains findable as a static reviewer-facing path.
   - Candidate action type: index or pointer review only if existing repository structure supports it.
   - Boundary: do not create new fixture files in this checkpoint.

5. `ROADMAP.md`
   - Purpose: ensure future direction language does not imply publication approval or runtime/scanner readiness.
   - Candidate action type: roadmap wording alignment only.
   - Boundary: do not select runtime execution, scanner readiness, or customer PoC intake.

## Candidate non-target surfaces

The candidate integration plan should not target:

- GitHub Release publication text
- external social posts
- AAEF main repository issues, PRs, commands, or URLs
- commercial contract terms
- paid engagement materials
- customer-specific documents
- runtime/scanner configuration
- Docker or runtime execution artifacts
- JSON Schema changes
- validator behavior changes
- new public fixture files

## Candidate wording reuse rules

Repository wording integration should reuse v0.6.204 accepted wording only under these rules:

- Use `Static Fixture Review Path` as the preferred label.
- Use `publicly reviewable static fixture set` only when the text also says static, mock, fixture-only, and non-execution.
- Use `safe` only to describe the review boundary, not production readiness.
- Do not use `Public Demo` as the active project label.
- Do not use demo language that suggests executable behavior.
- Keep `AI output is a request, not authority` near any explanation of proposed tool actions.
- Keep gate decision and execution separate in wording.
- Keep non-execution evidence visible in reviewer-facing wording.

## Candidate required boundary checklist

Any future integration checkpoint based on this plan should verify that changed text includes or preserves these boundary statements:

- AAEF-AI-VA is a safety-first reference implementation, not a live scanner.
- The current review path is static, mock, fixture-only, and non-execution.
- AI output is treated as a request, not authority.
- Execution is decided by gates.
- Evidence links the request, gate decision, execution or non-execution result, and review.
- The repository does not provide third-party testing authorization, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.
- Publication remains deferred unless a separate explicit publication checkpoint approves it.

## Candidate review requirements for v0.6.207

v0.6.207 should review this candidate plan and decide whether it is accepted, revised, or rejected.

The review should check:

- whether target surfaces are appropriate
- whether non-target surfaces are excluded
- whether accepted v0.6.204 wording is reused conservatively
- whether the plan avoids public announcement or social-post approval
- whether the plan avoids runtime/scanner/customer PoC readiness claims
- whether a later integration implementation checkpoint is required before any actual wording changes are applied

## Candidate next step if accepted

If v0.6.207 accepts this plan, a later checkpoint may select or create a repository wording integration implementation candidate.

That later checkpoint should be separate from this plan candidate and should still avoid publication approval, runtime execution, scanner readiness, and customer PoC readiness.

## Explicit non-goals for v0.6.206

v0.6.206 does not:

- apply accepted wording to repository-facing documents
- publish a public announcement
- approve a social post
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

- the candidate integration objective is recorded
- candidate target surfaces are recorded
- candidate non-target surfaces are recorded
- candidate wording reuse rules are recorded
- candidate required boundary checklist is recorded
- v0.6.207 review requirements are recorded
- the document states that wording changes are not applied in v0.6.206
- the document preserves publication-deferred boundaries
