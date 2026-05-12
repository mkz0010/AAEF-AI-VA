# ADR-0250: Add v0.6.180 next work selection using risk-tiered granularity

Status: Accepted
Date: 2026-05-12

## Context

v0.6.179 reviewed and accepted Public Demo Positioning and closed the Medium-risk work item. The next safe step is to define how inbound commercial or buyer-facing inquiries should be answered without creating contract, PoC, runtime, scanner, customer-target, delivery, certification, legal, audit, or production-readiness implications.

## Decision

Select Commercial Inquiry Response Boundary as the next work item.

Classify the selected work item as Medium risk because it will create buyer-facing boundary language that can influence external interpretation of commercial inquiry, PoC, contracts, demo access, runtime execution, scanner execution, customer scope, and delivery.

Use two checkpoints: candidate implementation, then review and decision.

This v0.6.180 decision itself is a Low-risk direction-selection record and is completed in one checkpoint.

## Consequences

v0.6.181 should create the Commercial Inquiry Response Boundary candidate and tests. No commercial inquiry response boundary artifact is created by this v0.6.180 checkpoint.
