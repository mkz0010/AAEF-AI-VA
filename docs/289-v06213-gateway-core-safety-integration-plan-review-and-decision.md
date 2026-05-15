# v0.6.213 Gateway Core Safety Integration Plan Review and Decision

Status: Accepted for implementation planning; not implemented

## Purpose

This checkpoint reviews the v0.6.212 `Gateway Core Safety Integration Plan Candidate`.

The decision is narrow: the candidate plan is accepted as the Gateway Core Safety Integration Plan for future implementation planning.

This checkpoint does not implement Gateway core safety controls.

This checkpoint does not change Tool Gateway behavior, adapter behavior, execution status terminology, schemas, validators, fixtures, runtime behavior, scanner behavior, public release posture, or commercial terms.

## Reviewed source

Reviewed candidate:

- v0.6.212 Gateway Core Safety Integration Plan Candidate

Source reassessment:

- v0.6.211 External Review Intake and Priority Reassessment

## Decision

The v0.6.212 candidate plan is accepted as the Gateway Core Safety Integration Plan for future implementation planning.

Decision fields:

- gateway_core_safety_integration_plan_accepted = true
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
- production_readiness_claim = false
- certification_claim = false
- legal_compliance_claim = false
- audit_opinion_claim = false
- diagnostic_completeness_claim = false
- external_framework_equivalence_claim = false

## Accepted problem statement

The project has a maturity gap between controls that are documented or helper-tested and controls that are enforced in the Tool Gateway core path.

Future work must distinguish these states:

- documented control pattern
- schema or fixture representation
- helper implementation
- local check coverage
- Tool Gateway core-path enforcement
- core-path negative test coverage

Documented or helper-tested controls must not be described as equivalent to Gateway core-path enforcement.

## Accepted integration objective

The accepted objective is to integrate safety controls into the mock Tool Gateway core path through later narrow implementation checkpoints.

The future integration should make the Gateway core path fail closed when mandatory safety checks fail, while preserving the current project boundary:

- reference implementation
- mock / dry-run / fixture-oriented behavior
- no live scanner
- no external target authorization
- no runtime demo approval
- no publication approval
- no production, certification, legal, audit, diagnostic-completeness, or external-framework-equivalence claim

## Accepted mandatory Gateway core sequence

Future implementation work should use this accepted candidate ordering as the target sequence:

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

The sequence is accepted for implementation planning only. It is not yet implemented in this checkpoint.

## Accepted priority controls

The following controls are accepted as the priority set for later implementation planning.

### 1. Mock / dry-run completed status terminology cleanup

The plan accepts that `completed` is risky in mock or dry-run result paths because it can imply real execution.

Future work should review and replace or narrow mock/dry-run use of `completed`, with candidate alternatives such as:

- `dry_run_result_recorded`
- `mock_result_recorded`
- `authorized_but_not_executed`

### 2. Authorization current-time expiry integration

The plan accepts that current-time authorization expiry must be enforced in the Gateway core path before adapter behavior.

Expired authorization should fail closed and should be covered by negative tests.

### 3. Request / decision constraint-diff integration

The plan accepts that request/decision constraint drift must be enforced in the Gateway core path before adapter behavior.

Future work should prioritize constraints including:

- `external_discovery`
- `destructive_tests`
- `evidence_required`
- `rate_limit`
- target and scope related constraints

### 4. External discovery fail-closed integration

The plan accepts that external discovery should fail closed in the mock/public path unless a separately reviewed exception model exists.

No exception model is accepted in this checkpoint.

### 5. Common target / scope / tool / operation binding

The plan accepts that target, scope, tool, and operation binding should be enforced in the common Gateway pre-adapter path rather than left to individual adapters.

### 6. Adapter consistency review

The plan accepts that adapter maturity must be reviewed by adapter and that uniform adapter maturity should not be claimed until tested.

The review should cover at least ZAP, Nmap, nuclei, and browser paths.

### 7. Implementation maturity matrix

The plan accepts that an implementation maturity matrix should distinguish documented, helper implemented, fixture covered, local test covered, gateway core integrated, and core-path tested states.

### 8. Evidence wording cleanup

The plan accepts that evidence wording should avoid audit-grade proof implications.

Current evidence records should be positioned as evidence records, review traces, or reconstruction traces, not immutable audit logs, legal proof, audit opinions, or certification evidence.

### 9. Public / private commercial material boundary review

The plan accepts that public commercial-facing materials should be reviewed for maturity-overstatement and strategy-exposure risk.

### 10. Safe demo / mock runtime / controlled runtime PoC separation

The plan accepts that future work should keep these tiers separate:

1. Static Fixture Review Path
2. Mock Runtime Demonstration
3. Controlled Runtime PoC

Runtime demo remains necessary but deferred.

## Accepted implementation staging

If future work proceeds, it should be split into narrow checkpoints.

Accepted staging:

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

## Accepted definition of done for future implementation work

Future implementation checkpoints should not be treated as done unless they include:

- core-path positive tests
- core-path negative tests
- fail-closed behavior for unsafe inputs
- explicit generated result status
- evidence or review trace linkage
- README or maturity matrix update if public expectations change
- preservation of no-runtime and no-scanner-readiness boundaries unless separately reviewed

## Review notes

The v0.6.212 candidate plan is acceptable because it:

- directly responds to the external review maturity-gap concern
- keeps planning separate from implementation
- prioritizes Gateway core-path enforcement before runtime demo readiness
- preserves the distinction between documented controls, helper implementation, local checks, and core-path enforcement
- avoids publication, runtime, scanner, external PoC, production, certification, legal, audit, diagnostic-completeness, and external-framework-equivalence claims

## Next recommended checkpoint

The recommended next checkpoint is:

- v0.6.214 Next Work Selection Using Risk-Tiered Granularity

That checkpoint should select the first implementation work item under the accepted Gateway Core Safety Integration Plan.

The expected first implementation work item is mock/dry-run completed status terminology cleanup, but the final selection should be recorded in v0.6.214.

## Runtime demo position retained

runtime demo remains necessary but deferred.

The project should not advance to closed runtime demo readiness until Gateway core safety integration has been planned, implemented, and reviewed.

## Publication boundary retained

publication remains deferred.

This review-and-decision checkpoint does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Explicit non-goals for v0.6.213

v0.6.213 does not:

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

## Acceptance criteria

This review-and-decision checkpoint is accepted when:

- the v0.6.212 candidate plan is reviewed
- the plan is accepted for implementation planning
- the mandatory Gateway core sequence is accepted for implementation planning
- priority controls are accepted for implementation planning
- implementation staging is accepted
- the definition of done for future implementation work is accepted
- runtime demo remains necessary but deferred
- publication remains deferred
- no Tool Gateway behavior changes are applied in v0.6.213
- v0.6.214 is identified as the next recommended checkpoint
