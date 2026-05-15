# ADR-0288: Add v0.6.218 AAEF Applied Evidence Minimum Flow Intake and Priority Reconciliation

Status: Accepted

## Context

v0.6.217 accepted the Public Exposure Hygiene Plan for cleanup planning.

AAEF main then confirmed that AAEF-AI-VA should prioritize a minimum applied evidence flow that helps answer the AAEF external review concern that implementation entry points, non-execution evidence, and evidence boundaries are not visible enough.

AAEF main emphasized that AAEF-AI-VA should not present itself as a production-ready vulnerability scanner. It should act as an applied implementation showing how AI-generated action requests are normalized, gate-decided, dispatched or not dispatched, and recorded as review-supporting evidence.

## Decision

Add v0.6.218 as an intake and priority reconciliation checkpoint.

The immediate next work item is changed to:

- selected_next_work_item = aaef_applied_evidence_minimum_flow_plan
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.219 AAEF Applied Evidence Minimum Flow Plan Candidate
- selected_followup_checkpoint = v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision

The accepted Public Exposure Hygiene Plan remains valid but deferred.

The previously selected mock/dry-run completed status terminology cleanup remains deferred, not rejected.

## Rationale

AAEF main needs a compact, reviewable applied evidence minimum flow more than new diagnostic capability.

The immediate priority is to reorganize existing AAEF-AI-VA elements into a minimum evidence package that supports AAEF's five questions and clearly states non-proof boundaries.

## Consequences

v0.6.218 does not create fixtures, change runtime behavior, rewrite README, move commercial materials, or change Tool Gateway behavior.

A separate v0.6.219 plan candidate is required before the minimum flow package is built.

Runtime demo remains necessary but deferred.

Publication remains deferred.
