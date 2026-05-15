# ADR-0297: Add v0.6.227 Next Work Selection Using Risk-Tiered Granularity

Status: Accepted

## Context

v0.6.226 accepted the Minimum Flow Scenario Matrix for future evidence linkage planning.

The next step is to decide which concrete artifact should be planned after the accepted scenario matrix.

## Decision

Add v0.6.227 as a direction-selection checkpoint.

v0.6.227 selects:

- selected_next_work_item = evidence_linkage_table
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.228 Evidence Linkage Table Candidate
- selected_followup_checkpoint = v0.6.229 Evidence Linkage Table Review and Decision

## Rationale

The accepted scenario matrix defines the four scenario rows.

An evidence linkage table should be reviewed before creating package records, fixtures, request records, decision records, dispatch records, walkthroughs, mappings, or handback material.

## Consequences

v0.6.227 does not create the evidence linkage table.

v0.6.227 does not create fixtures, change Gateway behavior, change runtime behavior, rewrite README, apply public cleanup, or approve publication.

Runtime demo remains necessary but deferred.

Publication remains deferred.
