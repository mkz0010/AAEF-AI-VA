# ADR-0291: Add v0.6.221 Next Work Selection Using Risk-Tiered Granularity

Status: Accepted

## Context

v0.6.220 accepted the AAEF Applied Evidence Minimum Flow Plan for future minimum flow planning.

The accepted plan requires existing element inventory before creating new minimum flow package artifacts, fixtures, evidence linkage records, reviewer walkthrough material, or handback material.

## Decision

Add v0.6.221 as a direction-selection checkpoint.

v0.6.221 selects:

- selected_next_work_item = existing_element_inventory
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.222 Existing Element Inventory Candidate
- selected_followup_checkpoint = v0.6.223 Existing Element Inventory Review and Decision

## Rationale

The repository already contains relevant Tool Gateway runner, mock flow, evidence chain, reconstruction, runtime scaffold, safe demo, and reviewer materials.

Those elements must be inventoried and classified before new minimum flow package artifacts are created.

## Consequences

v0.6.221 does not create the existing element inventory.

v0.6.221 does not create fixtures, change Gateway behavior, change runtime behavior, rewrite README, apply public cleanup, or approve publication.

Runtime demo remains necessary but deferred.

Publication remains deferred.
