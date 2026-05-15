# v0.6.212 Gateway Core Safety Integration Plan Candidate

Status: Candidate only

## Purpose

This checkpoint creates a candidate plan for Gateway Core Safety Integration after the v0.6.211 external review intake and priority reassessment.

This is a plan candidate only. It does not change Tool Gateway behavior, adapter behavior, execution status terminology, schemas, validators, fixtures, runtime behavior, or scanner behavior.

The goal is to make the next implementation work explicit before touching the Gateway core path.

## Source decision

v0.6.211 selected the next work item:

- selected_next_work_item = gateway_core_safety_integration_plan
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.212 Gateway Core Safety Integration Plan Candidate
- selected_followup_checkpoint = v0.6.213 Gateway Core Safety Integration Plan Review and Decision

## Candidate plan status

This candidate plan is:

- candidate only
- not accepted
- not implemented
- not gateway-integrated
- not runtime-ready
- not scanner-ready
- subject to v0.6.213 review and decision

## Problem statement

The external review identified a maturity gap between controls that are documented or helper-tested and controls that are enforced in the Tool Gateway core path.

The project must distinguish these states:

- documented control pattern
- schema or fixture representation
- helper implementation
- local check coverage
- Tool Gateway core-path enforcement
- core-path negative test coverage

The plan must avoid implying that documented or helper-tested controls are already enforced by the Gateway core path.

## Candidate integration objective

The objective is to plan how safety controls should be integrated into the mock Tool Gateway core path before any runtime demo or commercial presentation advances.

The accepted future integration should make the Gateway core path fail closed when mandatory safety checks fail, while preserving the current project boundary:

- reference implementation
- mock / dry-run / fixture-oriented behavior
- no live scanner
- no external target authorization
- no runtime demo approval
- no publication approval
- no production, certification, legal, audit, diagnostic-completeness, or external-framework-equivalence claim

## Candidate mandatory Gateway core sequence

The candidate plan proposes the following mandatory Gateway core sequence:

1. Schema validation
2. Request / decision binding validation
3. Authorization current-time expiry validation
4. Request / decision constraint-diff validation
5. External discovery fail-closed validation
6. Target / scope / tool / operation binding validation
7. Credential_ref validation against mock Vault metadata
8. Adapter command-plan generation
9. Controlled executor dry-run validation
10. Tool result / evidence record generation

The sequence should be treated as a candidate target ordering for later implementation work.

## Candidate priority controls

The Gateway Core Safety Integration Plan should cover these controls in priority order.

### 1. Mock / dry-run completed status terminology cleanup

Problem:

- `allow` currently maps to `completed` in some mock Gateway output paths.
- The word `completed` can imply real tool execution.

Candidate direction:

- replace or narrow mock/dry-run use of `completed`
- prefer wording such as `dry_run_result_recorded`, `mock_result_recorded`, or `authorized_but_not_executed`
- preserve backward compatibility only if explicitly justified
- update tests and examples together

### 2. Authorization current-time expiry integration

Problem:

- helper coverage exists, but Gateway core-path enforcement must be explicit.
- Expired authorization should not continue through the Gateway path.

Candidate direction:

- call current-time expiry validation near the start of the Gateway core path
- fail closed if authorization is expired or expiry is missing where required
- include negative tests for expired authorization
- record the check result in the generated result and evidence trace

### 3. Request / decision constraint-diff integration

Problem:

- request/decision constraint drift must be blocked in the Gateway core path.
- Helper-only validation is not enough for the main control boundary.

Candidate direction:

- compare request constraints and decision constraints before adapter behavior
- fail closed on unauthorized widening or mismatch
- prioritize `external_discovery`, `destructive_tests`, `evidence_required`, `rate_limit`, and target/scope-related constraints
- include positive and negative core-path tests

### 4. External discovery fail-closed integration

Problem:

- external discovery must be blocked by default in the mock/public path.
- Helper-only validation is insufficient for security-sensitive review.

Candidate direction:

- fail closed whenever external discovery is requested or appears in effective constraints unless a later separately reviewed exception model exists
- keep any future exception model out of this checkpoint
- include negative tests for request-side and decision-side external discovery

### 5. Common target / scope / tool / operation binding

Problem:

- adapter behavior should not individually decide whether scope is safe.
- the common Gateway pre-adapter path should enforce target and scope binding.

Candidate direction:

- resolve target binding before adapter command-plan generation
- enforce allowed tool and operation binding before adapter behavior
- apply common checks to ZAP, Nmap, nuclei, and browser paths
- avoid claiming full adapter parity until tested

### 6. Adapter consistency review

Problem:

- ZAP appears more strongly bound to scope registry behavior than other adapters.
- Tool Gateway claims should not imply uniform maturity if adapters differ.

Candidate direction:

- document adapter maturity by adapter
- require common pre-adapter checks for all adapters
- add adapter-specific gaps to implementation maturity matrix
- avoid claiming all adapters enforce identical controls until tested

### 7. Implementation maturity matrix

Problem:

- external readers may confuse documented/helper-tested controls with Gateway-integrated controls.

Candidate direction:

- add a matrix distinguishing documented, helper implemented, fixture covered, local test covered, gateway core integrated, and core-path tested
- place the matrix near README current status or in a linked document
- ensure the matrix is conservative and easy to update

### 8. Evidence wording cleanup

Problem:

- evidence records can sound like audit-grade proof if not constrained.

Candidate direction:

- use `review trace` or `evidence record / reconstruction trace` language where appropriate
- state that current evidence records are not immutable audit logs, legal proof, audit opinions, or certification evidence
- record limitations explicitly

### 9. Public / private commercial material boundary review

Problem:

- public product, pricing, or persona materials may overstate maturity or reveal sales strategy.

Candidate direction:

- inventory public commercial-facing materials
- decide whether pricing/persona details belong in public repository surfaces
- move sensitive or premature material to private-not-in-git if needed
- preserve simple commercial inquiry boundary language publicly

### 10. Safe demo / mock runtime / controlled runtime PoC separation

Problem:

- static fixture review, mock runtime demonstration, and controlled runtime PoC must not be mixed.

Candidate direction:

- define three tiers: Static Fixture Review Path, Mock Runtime Demonstration, Controlled Runtime PoC
- keep runtime demo necessary but deferred
- require separate readiness review before any closed runtime demo work begins

## Candidate implementation staging

If this plan is accepted in v0.6.213, later work should be split into narrow checkpoints.

Candidate staging:

1. completed status terminology cleanup candidate and review
2. authorization current-time expiry Gateway integration candidate and review
3. request/decision constraint-diff Gateway integration candidate and review
4. external discovery fail-closed Gateway integration candidate and review
5. common target/scope/tool/operation binding candidate and review
6. adapter consistency and maturity matrix candidate and review
7. evidence wording and review-trace limitation cleanup candidate and review
8. public/private commercial material boundary candidate and review
9. safe demo / mock runtime / controlled runtime PoC separation candidate and review
10. closed runtime demo readiness track selection only after core integration work is reviewed

## Explicit non-goals for v0.6.212

v0.6.212 does not:

- implement Gateway core safety controls
- change Tool Gateway behavior
- change adapter behavior
- rename execution statuses
- change execution result schemas
- change evidence schemas
- change validator behavior
- change fixture semantics
- apply runtime changes
- create a runtime demo
- create an executable demo
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

runtime demo remains necessary but deferred.

The project should not advance to closed runtime demo readiness until Gateway core safety integration has been planned, implemented, and reviewed.

## Publication boundary retained

publication remains deferred.

This candidate plan does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Acceptance criteria

This candidate checkpoint is accepted when:

- the Gateway Core Safety Integration Plan Candidate is recorded
- the mandatory Gateway core sequence is recorded
- priority controls are recorded
- candidate implementation staging is recorded
- the implementation maturity matrix requirement is recorded
- runtime demo remains necessary but deferred
- publication remains deferred
- no Tool Gateway behavior changes are applied in v0.6.212
- v0.6.213 is identified as the review and decision checkpoint
