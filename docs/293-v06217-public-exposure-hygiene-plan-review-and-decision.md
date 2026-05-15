# v0.6.217 Public Exposure Hygiene Plan Review and Decision

Status: Accepted for cleanup planning; not applied

## Purpose

This checkpoint reviews the v0.6.216 `Public Exposure Hygiene Plan Candidate`.

The decision is narrow: the candidate plan is accepted as the Public Exposure Hygiene Plan for future cleanup planning.

This checkpoint does not apply public-facing cleanup.

This checkpoint does not remove contact routes, move pricing materials, move business-plan materials, rewrite README, delete documents, create a mock execution recording, create runtime demo material, approve publication, create commercial terms, or change Tool Gateway behavior.

## Reviewed source

Reviewed candidate:

- v0.6.216 Public Exposure Hygiene Plan Candidate

Source reassessment:

- v0.6.215 External Review Public Exposure and Commercial Boundary Reassessment

## Decision

The v0.6.216 candidate plan is accepted as the Public Exposure Hygiene Plan for future cleanup planning.

Decision fields:

- public_exposure_hygiene_plan_accepted = true
- public_exposure_cleanup_applied = false
- public_contact_route_removed = false
- pricing_materials_moved = false
- business_plan_moved = false
- readme_front_page_rewritten = false
- historical_docs_deleted = false
- mock_execution_recording_created = false
- gateway_core_safety_controls_implemented = false
- tool_gateway_behavior_changed = false
- adapter_behavior_changed = false
- execution_status_renamed = false
- schema_changed = false
- validator_behavior_changed = false
- fixture_semantics_changed = false
- runtime_behavior_changed = false
- scanner_behavior_changed = false
- runtime_demo_ready = false
- scanner_readiness_claim = false
- external_poc_readiness_claim = false
- publication_approval = false
- public_announcement = deferred
- social_post_publication = deferred
- commercial_terms_created = false
- production_readiness_claim = false
- certification_claim = false
- legal_compliance_claim = false
- audit_opinion_claim = false
- diagnostic_completeness_claim = false
- external_framework_equivalence_claim = false

## Accepted problem statement

The project has public surfaces that can weaken external trust or expose commercial strategy if left unmanaged.

The accepted concern set includes:

- README may lead with too many prohibitions before a clear value proposition.
- Direct personal contact information can weaken enterprise credibility if framed as a commercial route.
- Pricing drafts can weaken negotiation posture.
- Business-plan materials can expose strategy.
- Candidate and draft labels can make external-facing materials appear unfinished.
- Current/latest version wording can confuse readers.
- Historical checkpoint documents can overwhelm first-time reviewers.
- Static fixture review can look like a non-running document pile unless public navigation is curated.

## Accepted principles

The Public Exposure Hygiene Plan is accepted with these principles:

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

## Accepted workstreams

The following workstreams are accepted for future cleanup planning.

### 1. README front-page value proposition and reader path

Future cleanup should make the README easier for first-time readers.

The top of README should explain:

- what AAEF-AI-VA is
- who should care
- what can be reviewed today
- what the current static fixture path demonstrates
- what this is not

The rewrite must preserve claim boundaries and must not imply live scanner, production, customer PoC, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence readiness.

### 2. Public contact route hygiene

Future cleanup should inventory all public surfaces that expose a personal email address or imply a direct commercial route.

The accepted direction is to replace direct personal-email-first wording with a safer public inquiry route, such as GitHub Issues, GitHub Discussions, or a request-for-contact process, unless a later review approves a domain-based address.

Any inquiry language must state that an inquiry does not create:

- a contract
- a PoC approval
- scanning authorization
- customer target authorization
- runtime execution approval
- delivery approval

### 3. Pricing and commercial draft exposure hygiene

Future cleanup should inventory public product, pricing, persona, proposal, and sales-strategy materials.

The accepted direction is:

- keep AGPL and commercial-license boundary public
- keep minimal commercial inquiry boundary language public
- move detailed pricing and sales drafts out of public repository surfaces where appropriate
- avoid publishing price bands unless separately reviewed

### 4. Business plan exposure hygiene

Future cleanup should inventory public business-plan materials and identify strategy-sensitive content.

Strategy-sensitive content includes:

- target customer strategy
- partner strategy
- exit strategy
- negotiation posture
- commercialization assumptions

The accepted direction is to move or replace strategy-sensitive public business-plan material through later explicit cleanup checkpoints.

### 5. Current/latest version clarity

Future cleanup should distinguish:

- latest repository checkpoint
- current public review path
- active runtime readiness status
- static fixture review path status
- publication status

Version clarity work must not imply active runtime or scanner readiness.

### 6. External-facing candidate and draft label hygiene

Future cleanup should inventory external-facing materials that use `candidate`, `draft_candidate`, `draft`, or similar status labels.

The accepted direction is:

- internal process records may keep candidate/draft labels
- external-facing review guides should either use accepted review status or explain their status clearly
- sales-facing or buyer-facing documents should not look unfinished unless they are explicitly internal drafts and not linked from public entry points

### 7. Public documentation curation

Future cleanup should create a curated public reader path.

The accepted curation buckets are:

1. Start here
2. Static Fixture Review Path
3. Control Boundary and Evidence
4. Enterprise Review / Due Diligence
5. Licensing and Commercial Boundary
6. Historical Checkpoints / Archive
7. Private or removed-from-public candidates

Historical documents should not be blindly deleted. The first objective is to reduce first-time reader overload and repair public/private boundaries.

### 8. Demo and motion-evidence positioning

Future cleanup should define whether a later mock execution recording, screenshot, or asciinema should be prepared.

The accepted tiers are:

1. Static Fixture Review Path
2. Mock Execution Walkthrough
3. Closed Runtime Demo
4. Controlled Runtime PoC

This checkpoint does not approve any runtime demo, scanner execution, external target authorization, customer PoC readiness, or publication.

## Accepted sequencing

If future work proceeds, it should be split into narrow checkpoints.

Accepted sequencing:

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

## Accepted definition of done for future cleanup work

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

The accepted plan recognizes that previously public material may remain visible in Git history.

Later cleanup should focus on:

- current public surfaces
- current README entry paths
- current repository navigation
- future-facing public claims
- minimizing further exposure

Cleanup should not pretend that deletion from the working tree removes prior public exposure from Git history.

## Review notes

The v0.6.216 candidate plan is acceptable because it:

- responds directly to the external review's public exposure and commercial boundary concerns
- avoids broad deletion as the default remedy
- preserves transparency where public reviewability supports trust
- separates public review path, commercial inquiry path, runtime demo path, and controlled PoC path
- preserves conservative claim boundaries
- keeps cleanup planning separate from cleanup application

## Next recommended checkpoint

The recommended next checkpoint is:

- v0.6.218 Next Work Selection Using Risk-Tiered Granularity

That checkpoint should select the first cleanup work item under the accepted Public Exposure Hygiene Plan.

The expected first cleanup work item is contact route and commercial exposure inventory, but the final selection should be recorded in v0.6.218.

## Deferred Gateway implementation work

The previously selected Gateway implementation work remains deferred, not rejected:

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = interposed_public_exposure_and_commercial_boundary_hygiene_review
- deferred_return_condition = public_exposure_hygiene_cleanup_track_reviewed_or_explicitly_paused

## Explicit non-goals for v0.6.217

v0.6.217 does not:

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

This review-and-decision checkpoint does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Acceptance criteria

This review-and-decision checkpoint is accepted when:

- the v0.6.216 candidate plan is reviewed
- the plan is accepted for cleanup planning
- accepted principles are recorded
- accepted workstreams are recorded
- accepted sequencing is recorded
- accepted definition of done is recorded
- the treatment of existing public history is recorded
- v0.6.218 is identified as the next recommended checkpoint
- the checkpoint states that no cleanup is applied in v0.6.217
- the checkpoint states that no Gateway implementation changes are applied in v0.6.217
- runtime demo remains necessary but deferred
- publication remains deferred
