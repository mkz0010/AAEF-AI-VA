# ADR-0429: Defer History Rewrite After Public History Exposure Review

Status: accepted
Date: 2026-05-19
Version: v0.6.354

## Context

v0.6.352 removed public product/pricing draft files from the current tree. v0.6.353 removed exact commercial draft terms left in the current tree by the cleanup test. The remaining question is whether to rewrite Git history, recreate the repository, or continue with current-tree cleanup and recorded boundaries.

## Decision

Do not rewrite Git history and do not recreate the repository at this checkpoint.

The current-tree cleanup is accepted as sufficient for now. Prior Git history exposure may remain and is treated as prior removed commercial draft material, not as credential, customer, NDA, or patent-sensitive exposure based on the current review record.

## Decision record

~~~text
public_history_exposure_review_completed = true
public_history_exposure_review_id = public_history_exposure_review_v06354
current_tree_cleanup_completed = true
current_tree_product_pricing_files_absent = true
current_tree_exact_commercial_draft_terms_absent = true
current_tree_plaintext_commercial_draft_terms_absent = true
prior_git_history_exposure_confirmed = true
history_exposure_category = prior_removed_commercial_draft_material
history_exposure_severity = competitive_draft_exposure_not_secret_credential_exposure
history_rewrite_required = false
history_rewrite_deferred = true
repo_recreation_required = false
repo_recreation_deferred = true
history_rewrite_performed = false
repo_recreated = false
git_history_exposure_may_remain = true
public_history_exposure_accepted_with_current_tree_cleanup = true
commercial_material_publication_deferred = true
commercial_packaging_publication_deferred = true
pricing_draft_publication_deferred = true
commercial_offer_approval = false
publication_approval = false
public_announcement = deferred
customer_demo_approval = false
gateway_core_integration_still_required = true
authorization_expiry_gateway_core_integration_still_required = true
constraint_diff_gateway_core_integration_still_required = true
external_discovery_fail_closed_gateway_core_integration_still_required = true
public_status_terminology_cleanup_still_required = true
readme_maturity_matrix_still_required = true
readme_front_page_simplification_still_required = true
evidence_trace_strengthening_still_required = true
safe_local_only_demo_execution_boundary_runtime_applied = false
minimal_runtime_wiring_changed = false
tool_gateway_behavior_changed = false
runtime_behavior_changed = false
scanner_behavior_changed = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
recommended_next_work_item = gateway_core_safety_integration_status_and_priority_review
gateway_core_safety_integration_status_and_priority_review_recommended = true
public_history_exposure_review_recommended = false
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
public history exposure review is not history rewrite
public history exposure review is not repository recreation
public history exposure review is not publication approval
public history exposure review is not customer demo readiness
public history exposure review is not commercial offer approval
public history exposure review is not runtime wiring
public history exposure review is not runtime application
public history exposure review is not execution authorization
public history exposure review is not real execution permission
public history exposure review is not external target authorization
public history exposure review is not scanner readiness
public history exposure review is not production readiness
No private generated outputs are moved public in v0.6.354.
~~~

## Consequences

The project preserves repository continuity, tags, and review trace. If later review finds secrets, customer-specific material, NDA-assumed material, patent-sensitive implementation detail, or concrete private commercial terms in public history, this decision must be revisited.

## Boundaries

- This is a history exposure review only.
- This does not rewrite Git history.
- This does not recreate the repository.
- This does not approve publication.
- This does not approve commercial offers.
- This does not create customer demo readiness.
- This does not change runtime wiring or execution behavior.
