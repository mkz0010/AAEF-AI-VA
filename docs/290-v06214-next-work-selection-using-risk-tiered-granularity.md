# v0.6.214 Next Work Selection Using Risk-Tiered Granularity

Status: Accepted direction-selection checkpoint

## Purpose

This checkpoint records the next work selection after v0.6.213 using risk-tiered granularity.

v0.6.214 is intentionally narrow. It selects the first implementation work item under the accepted Gateway Core Safety Integration Plan. It does not implement the selected work item.

## Baseline carried forward

The latest completed checkpoint before this document is v0.6.213.

v0.6.213 accepted the Gateway Core Safety Integration Plan for implementation planning only.

The following boundaries remain in force:

- gateway core safety controls are not implemented in this checkpoint
- Tool Gateway behavior is not changed in this checkpoint
- adapter behavior is not changed in this checkpoint
- execution statuses are not renamed in this checkpoint
- schemas are not changed in this checkpoint
- validator behavior is not changed in this checkpoint
- fixture semantics are not changed in this checkpoint
- runtime behavior is not changed in this checkpoint
- scanner behavior is not changed in this checkpoint
- runtime demo remains necessary but deferred
- publication remains deferred
- no scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence is claimed

## Selected next work item

The selected next work item is recorded as follows:

- selected_next_work_item = mock_dry_run_completed_status_terminology_cleanup
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.215 Mock/Dry-run Completed Status Terminology Cleanup Candidate
- selected_followup_checkpoint = v0.6.216 Mock/Dry-run Completed Status Terminology Cleanup Review and Decision

## Why this work item is selected

The accepted Gateway Core Safety Integration Plan identifies mock/dry-run completed status terminology cleanup as the first staging item.

The external review identified that mapping `allow` to `completed` can imply real execution, even when the current path is mock, dry-run, or non-execution oriented.

This issue should be handled before deeper Gateway core enforcement work because status wording shapes how reviewers interpret generated outputs, evidence records, local checks, and public repository claims.

## Why the risk tier is high

This work is high-risk because execution status terminology can affect:

- generated example outputs
- result schema expectations
- evidence or review trace wording
- local checks
- README and public interpretation
- backward compatibility for existing fixtures and examples
- downstream implementation work under the Gateway Core Safety Integration Plan

The selected work must be split into candidate and review/decision checkpoints.

## Why the work is split into two checkpoints

The selected work item is split into two checkpoints:

1. v0.6.215 creates the terminology cleanup candidate.
2. v0.6.216 reviews the terminology cleanup candidate, accepts or rejects it, and records the decision.

This preserves a review boundary before terminology changes are treated as accepted.

## Scope of the selected v0.6.215 candidate

The v0.6.215 candidate may inspect and propose narrow terminology changes for mock/dry-run result statuses.

The candidate may cover:

- `decision_to_execution_status` behavior if applicable
- generated mock Tool Gateway outputs
- result status wording
- evidence or review trace wording
- examples and tests that currently expect `completed`
- documentation explaining mock/dry-run/non-execution result status

The candidate must explicitly separate:

- authorization decision
- mock/dry-run result recording
- external process execution
- network activity
- real scanner execution

## Required v0.6.215 constraints

The v0.6.215 candidate must preserve the following constraints:

- do not imply real tool execution when none occurred
- do not approve runtime execution
- do not approve scanner readiness
- do not approve external PoC readiness
- do not claim production readiness
- do not claim certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence
- do not introduce live scanner behavior
- do not introduce external target authorization
- preserve fail-closed behavior
- preserve evidence or review trace linkage
- update tests and examples together if terminology changes are proposed
- explicitly document any backward compatibility or migration decision

## Candidate terminology options

The v0.6.215 candidate should evaluate safer terms, such as:

- `dry_run_result_recorded`
- `mock_result_recorded`
- `authorized_but_not_executed`
- `fixture_result_recorded`

The candidate may choose one of these or propose a better term, but it must explain why the chosen term does not imply real execution.

## Explicit non-goals for v0.6.214

v0.6.214 does not:

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

Runtime demo remains necessary but deferred.

The project should not advance to closed runtime demo readiness until Gateway core safety integration has been planned, implemented, and reviewed.

## Publication boundary retained

Publication remains deferred.

This direction-selection checkpoint does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Acceptance criteria

This checkpoint is accepted when:

- the selected next work item is explicitly recorded
- the selected risk tier is recorded as high
- the two-checkpoint split is recorded
- v0.6.215 is identified as the candidate checkpoint
- v0.6.216 is identified as the review and decision checkpoint
- the checkpoint states that execution statuses are not renamed in v0.6.214
- runtime demo remains necessary but deferred
- publication remains deferred
- no Tool Gateway behavior changes are applied in v0.6.214
