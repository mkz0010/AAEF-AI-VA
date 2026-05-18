# ADR-0427: Remove Public Product/Pricing Draft Files from Current Tree

Status: accepted emergency cleanup
Date: 2026-05-19
Version: v0.6.352

## Context

The current public repository tree contained product/personas.md and product/pricing-draft.md. Those files expose draft commercial packaging and pricing-related material before an explicit commercial publication decision.

The README preserves the boundary that this repository is not a customer-ready managed assessment platform. Keeping draft product and pricing files in the public tree creates avoidable confusion and competitive exposure.

## Decision

Remove product/personas.md and product/pricing-draft.md from the current public repository tree.

## Decision record

~~~text
public_product_pricing_tree_removal_completed = true
public_product_personas_removed_from_public_tree = true
public_product_pricing_draft_removed_from_public_tree = true
product_pricing_public_tree_exposure_closed_for_current_tree = true
current_public_tree_contains_product_personas_md = false
current_public_tree_contains_product_pricing_draft_md = false
commercial_persona_detail_publication_deferred = true
pricing_draft_publication_deferred = true
commercial_packaging_publication_deferred = true
history_rewrite_performed = false
git_history_exposure_may_remain = true
separate_history_exposure_review_required = true
public_repo_should_not_include_pricing_draft = true
public_repo_should_not_include_commercial_persona_pack = true
README_commercial_readiness_consistency_preserved = true
not_customer_ready_managed_assessment_platform_boundary_preserved = true
gateway_core_integration_still_required = true
external_review_p0_gateway_core_integration_not_completed = true
completed_public_status_cleanup_still_required = true
readme_maturity_matrix_still_required = true
safe_local_only_demo_execution_boundary_runtime_applied = false
minimal_runtime_wiring_changed = false
tool_gateway_behavior_changed = false
runtime_behavior_changed = false
scanner_behavior_changed = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
publication_approval = false
public_announcement = deferred
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
recommended_next_work_item = public_history_exposure_review
public_history_exposure_review_recommended = true
safe_local_only_demo_minimal_runtime_wiring_implementation_closeout_review_deferred = true
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
public product/pricing tree removal is not publication approval
public product/pricing tree removal is not customer demo readiness
public product/pricing tree removal is not commercial offer approval
public product/pricing tree removal is not runtime wiring
public product/pricing tree removal is not runtime application
public product/pricing tree removal is not execution authorization
public product/pricing tree removal is not real execution permission
public product/pricing tree removal is not external target authorization
public product/pricing tree removal is not scanner readiness
public product/pricing tree removal is not production readiness
No private generated outputs are moved public in v0.6.352.
~~~

## Consequences

The current public tree no longer carries those draft product and pricing files. Git history may still expose prior contents, so a separate history exposure review is required next.

The previously planned safe local-only demo minimal runtime wiring implementation closeout review is deferred. The urgent public-tree cleanup takes priority.

## Boundaries

- This is current-tree cleanup only.
- This does not rewrite Git history.
- This does not approve publication.
- This does not approve commercial offers.
- This does not create customer demo readiness.
- This does not change runtime wiring or execution behavior.
