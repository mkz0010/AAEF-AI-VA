# v0.6.216 Public Exposure Hygiene Plan Candidate

Status: Candidate only

## Purpose

This checkpoint creates a candidate plan for public exposure hygiene after v0.6.215.

v0.6.215 selected `public_exposure_hygiene_plan` as the next high-risk work item and deferred, but did not reject, `mock_dry_run_completed_status_terminology_cleanup`.

This checkpoint is a plan candidate only. It does not remove contact routes, move pricing materials, move business-plan materials, rewrite README, delete documents, change Gateway behavior, rename execution statuses, create runtime demo material, approve publication, or approve commercial terms.

## Source decision

v0.6.215 selected the next work item:

- selected_next_work_item = public_exposure_hygiene_plan
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.216 Public Exposure Hygiene Plan Candidate
- selected_followup_checkpoint = v0.6.217 Public Exposure Hygiene Plan Review and Decision

The previously selected Gateway implementation work remains deferred, not rejected:

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = interposed_public_exposure_and_commercial_boundary_hygiene_review
- deferred_return_condition = public_exposure_hygiene_plan_reviewed_and_decided

## Candidate plan status

This candidate plan is:

- candidate only
- not accepted
- not applied
- not a public cleanup
- not a publication approval
- not a commercial offer
- subject to v0.6.217 review and decision

## Problem statement

The public repository currently has several surfaces that can weaken external trust or reveal commercial strategy if left unmanaged.

The external review raised the following concerns:

- README may lead with too many prohibitions before a clear value proposition.
- Direct personal contact information can weaken enterprise credibility if framed as the commercial route.
- Pricing drafts can weaken negotiation posture.
- Business-plan materials can expose strategy.
- Candidate and draft labels can make external-facing materials appear unfinished.
- Current/latest version wording can confuse readers.
- Historical checkpoint documents can overwhelm first-time reviewers.
- Static fixture review can look like a non-running document pile unless public navigation is curated.

This plan candidate turns those concerns into a staged public exposure hygiene plan.

## Candidate principles

The public exposure hygiene plan should follow these principles:

1. Prefer public/private boundary repair over broad deletion.
2. Keep public reviewability where it supports trust.
3. Remove or de-emphasize negotiation-sensitive commercial detail from public surfaces.
4. Keep defensive architecture descriptions public only at a boundary-safe level.
5. Lead with value proposition before non-goal lists.
6. Preserve claim boundaries and avoid maturity overstatement.
7. Separate public review path, commercial inquiry path, and runtime demo path.
8. Treat runtime demo as necessary but deferred.
9. Treat publication as deferred unless a separate checkpoint approves it.
10. Avoid rewriting project history in a way that hides prior public claims.

## Candidate workstreams

### 1. README front-page value proposition and reader path

Candidate action:

- rewrite the top of README so first-time readers understand what the project does before they encounter long boundary lists
- explain the problem: AI may suggest diagnostic actions, but execution authority must be gate-controlled
- explain what reviewers can inspect today
- link to the Static Fixture Review Path
- link to selected review documents rather than every historical checkpoint
- keep a compact "What this is not" section

Candidate target wording direction:

- "AI-assisted vulnerability assessment with explicit execution control"
- "AI output is a request, not authority"
- "The gate decides whether a proposed action can proceed"
- "This repository currently provides a static fixture review path and safety-first reference implementation boundaries"

Constraints:

- do not claim live scanner readiness
- do not claim production readiness
- do not claim customer PoC readiness
- do not imply certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence

### 2. Public contact route hygiene

Candidate action:

- inventory all public surfaces that expose a personal email address or imply a direct commercial route
- replace direct personal-email-first wording with a safer public inquiry route
- consider GitHub Issues, GitHub Discussions, or a request-for-contact process
- reserve future domain-based contact for later explicit review

Candidate replacement direction:

- "For review, collaboration, or commercial inquiries, open a GitHub Issue or Discussion with the appropriate inquiry label. Direct contact may be provided after initial maintainer review."

Required disclaimer:

- inquiry does not create a contract
- inquiry does not approve a PoC
- inquiry does not authorize scanning
- inquiry does not authorize customer targets
- inquiry does not approve runtime execution
- inquiry does not approve delivery

Constraints:

- do not create a new contact route in this plan candidate
- do not remove contact routes in this plan candidate
- do not publish a new email address in this plan candidate

### 3. Pricing and commercial draft exposure hygiene

Candidate action:

- inventory public product, pricing, persona, proposal, and sales-strategy materials
- identify materials that should be moved to private-not-in-git or a private repository
- identify public-safe replacement summaries where useful
- preserve only minimal public commercial inquiry boundary language

Likely high-risk public surfaces to review:

- product pricing drafts
- persona documents
- proposal story materials
- sales strategy notes
- detailed commercial positioning materials
- negotiation-sensitive assumptions

Candidate decision direction:

- keep AGPL and commercial-license boundary public
- keep a minimal commercial inquiry boundary public
- move detailed pricing and sales drafts out of public repository surfaces

Constraints:

- do not move files in this plan candidate
- do not create commercial terms in this plan candidate
- do not publish price bands in public cleanup unless separately reviewed

### 4. Business plan exposure hygiene

Candidate action:

- inventory public business-plan materials
- identify strategy-sensitive content, including target customer strategy, partner strategy, exit strategy, negotiation posture, and commercialization assumptions
- move strategy-sensitive material to private-not-in-git or a private repository in a later candidate if accepted

Candidate decision direction:

- public repository should not expose exit strategy or negotiation-sensitive business plan content
- public repository may keep a high-level project overview if it is boundary-safe and not strategy-sensitive

Constraints:

- do not move business-plan files in this plan candidate
- do not delete history in this plan candidate
- do not publish new commercial strategy in this plan candidate

### 5. Current/latest version clarity

Candidate action:

- inventory README, ROADMAP, CHANGELOG, and review documents for confusing current/latest wording
- distinguish latest repository checkpoint from any older baseline labels
- clearly state runtime status, publication status, and static fixture review status

Candidate wording model:

- Latest repository checkpoint: v0.6.216 or later
- Current public review path: Static Fixture Review Path
- Runtime status: no runtime execution approval
- Scanner status: no live scanner readiness claim
- Publication status: deferred unless separately approved

Constraints:

- do not imply active baseline changes unless explicitly reviewed
- do not imply runtime or scanner readiness
- do not imply publication approval

### 6. External-facing candidate and draft label hygiene

Candidate action:

- inventory external-facing materials that use `candidate`, `draft_candidate`, `draft`, or similar status labels
- decide whether each label should remain, be explained, or be replaced
- distinguish internal process status from external document readiness

Candidate decision direction:

- internal process records may keep candidate/draft labels
- external-facing review guides should either use accepted review status or explain their status clearly
- sales-facing or buyer-facing documents should not look unfinished unless they are explicitly marked as internal drafts and not linked from public entry points

Constraints:

- do not blindly remove all candidate labels
- do not overstate maturity by replacing labels without review
- do not claim finalized commercial material unless accepted separately

### 7. Public documentation curation

Candidate action:

- create a curated public reader path
- separate current review documents from historical checkpoint records
- keep historical checkpoint records accessible if appropriate, but do not force first-time readers through them
- identify archive/index improvements
- identify public-safe core docs

Candidate curation buckets:

1. Start here
2. Static Fixture Review Path
3. Control Boundary and Evidence
4. Enterprise Review / Due Diligence
5. Licensing and Commercial Boundary
6. Historical Checkpoints / Archive
7. Private or removed-from-public candidates

Constraints:

- do not delete historical docs in this plan candidate
- do not move docs in this plan candidate
- do not hide safety boundaries
- do not expose private commercial strategy

### 8. Demo and motion-evidence positioning

Candidate action:

- define whether a later mock execution recording, screenshot, or asciinema should be prepared
- ensure any recording demonstrates mock/non-execution behavior rather than scanner readiness
- keep closed runtime demo separate from public mock walkthrough

Candidate tiering:

1. Static Fixture Review Path
2. Mock Execution Walkthrough
3. Closed Runtime Demo
4. Controlled Runtime PoC

Constraints:

- no runtime demo approval in this plan candidate
- no scanner execution
- no external target authorization
- no customer PoC readiness
- no publication approval

## Candidate sequencing

If this plan is accepted in v0.6.217, later work should proceed in narrow checkpoints.

Candidate sequencing:

1. Contact route and commercial exposure inventory candidate
2. Contact route and commercial exposure cleanup review and decision
3. Pricing and business-plan public exposure cleanup candidate
4. Pricing and business-plan public exposure cleanup review and decision
5. README front-page value proposition and version clarity candidate
6. README front-page value proposition and version clarity review and decision
7. External-facing candidate/draft label hygiene candidate
8. External-facing candidate/draft label hygiene review and decision
9. Public documentation curation candidate
10. Public documentation curation review and decision
11. Mock walkthrough recording readiness review
12. Return to Gateway Core Safety Integration next work selection

## Candidate definition of done for future cleanup work

Future cleanup checkpoints should not be treated as done unless they include:

- explicit inventory of affected public surfaces
- exact files changed or intentionally left unchanged
- public/private boundary rationale
- no hidden publication approval
- no hidden runtime demo approval
- no hidden customer or external target authorization
- no new commercial terms unless separately reviewed
- tests preventing reintroduction of unsafe public claims where practical
- README/ROADMAP/CHANGELOG updates when public expectations change

## Treatment of existing public history

This plan candidate recognizes that previously public material may remain visible in Git history.

Therefore, later cleanup should focus on:

- current public surfaces
- current README entry paths
- current repository navigation
- future-facing public claims
- minimizing further exposure

The plan should not pretend that deletion from the working tree removes prior public exposure from Git history.

## Explicit non-goals for v0.6.216

v0.6.216 does not:

- remove public contact routes
- move pricing materials
- move business-plan materials
- rewrite the README front page
- delete historical docs
- create a curated documentation index
- create a mock execution recording
- create a runtime demo
- create an executable demo
- implement Gateway core safety controls
- change Tool Gateway behavior
- change adapter behavior
- rename execution statuses
- change execution result schemas
- change evidence schemas
- change validator behavior
- change fixture semantics
- apply runtime changes
- approve scanner readiness
- authorize real scanner execution
- authorize external PoC intake
- publish a public announcement
- approve a social post
- create a release announcement
- create AAEF main publication material
- create an AAEF main issue, PR, command, or URL
- create commercial contract terms
- create paid engagement approval
- create external-specific material
- promote this project into AAEF Core, Profile, or Practical Package

## Runtime demo position retained

Runtime demo remains necessary but deferred.

The project should not advance to closed runtime demo readiness until Gateway core safety integration and public exposure hygiene have both been planned and reviewed.

## Publication boundary retained

Publication remains deferred.

This plan candidate does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Acceptance criteria

This candidate checkpoint is accepted when:

- the Public Exposure Hygiene Plan Candidate is recorded
- the public exposure hygiene principles are recorded
- README front-page value proposition review is included
- public contact route hygiene is included
- pricing and commercial draft exposure hygiene is included
- business plan exposure hygiene is included
- current/latest version clarity is included
- external-facing candidate and draft label hygiene is included
- public documentation curation is included
- demo and motion-evidence positioning is included
- future cleanup sequencing is recorded
- v0.6.217 is identified as the review and decision checkpoint
- the checkpoint states that no cleanup is applied in v0.6.216
- runtime demo remains necessary but deferred
- publication remains deferred
