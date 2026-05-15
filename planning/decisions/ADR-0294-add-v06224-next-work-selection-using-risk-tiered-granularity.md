# ADR-0294: Add v0.6.224 Next Work Selection Using Risk-Tiered Granularity

Status: Accepted

## Context

v0.6.223 accepted the Existing Element Inventory for future AAEF Applied Evidence Minimum Flow planning.

The next step is to decide which concrete artifact should be planned after the accepted inventory.

## Decision

Add v0.6.224 as a direction-selection checkpoint.

v0.6.224 selects:

- selected_next_work_item = minimum_flow_scenario_matrix
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.225 Minimum Flow Scenario Matrix Candidate
- selected_followup_checkpoint = v0.6.226 Minimum Flow Scenario Matrix Review and Decision

## Rationale

The accepted inventory shows partially present coverage across the required minimum flow and scenarios.

A scenario matrix should be reviewed before creating any fixtures, linkage records, request/decision/dispatch records, walkthroughs, mappings, or handback material.

## Consequences

v0.6.224 does not create the scenario matrix.

v0.6.224 does not create fixtures, change Gateway behavior, change runtime behavior, rewrite README, apply public cleanup, or approve publication.

Runtime demo remains necessary but deferred.

Publication remains deferred.
