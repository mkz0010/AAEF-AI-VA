# ADR-0428: Remove Plaintext Commercial Draft Terms from Current Public Tree

Status: accepted emergency cleanup
Date: 2026-05-19
Version: v0.6.353

## Context

v0.6.352 removed draft product and pricing files from the current public repository tree. Follow-up review showed that the cleanup test still included exact commercial draft terms as plaintext strings.

## Decision

Remove plaintext commercial draft terms from the current tracked tree and add a hash-based current-tree test to prevent their reintroduction.

## Decision record

~~~text
public_commercial_term_cleanup_completed = true
current_public_tree_exact_commercial_draft_terms_removed = true
v06352_cleanup_test_plaintext_commercial_terms_removed = true
current_public_tree_product_pricing_files_absent = true
history_rewrite_performed = false
git_history_exposure_may_remain = true
separate_history_exposure_review_still_required = true
commercial_packaging_publication_deferred = true
pricing_draft_publication_deferred = true
commercial_offer_approval = false
gateway_core_integration_still_required = true
public_status_terminology_cleanup_still_required = true
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
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
public commercial term cleanup is not publication approval
public commercial term cleanup is not customer demo readiness
public commercial term cleanup is not commercial offer approval
public commercial term cleanup is not runtime wiring
public commercial term cleanup is not runtime application
public commercial term cleanup is not execution authorization
public commercial term cleanup is not real execution permission
public commercial term cleanup is not external target authorization
public commercial term cleanup is not scanner readiness
public commercial term cleanup is not production readiness
No private generated outputs are moved public in v0.6.353.
~~~

## Consequences

The current public tree exposes less commercial draft detail. Git history may still expose prior contents, so a separate public history exposure review remains required.

## Boundaries

- This is current-tree cleanup only.
- This does not rewrite Git history.
- This does not approve publication.
- This does not approve commercial offers.
- This does not create customer demo readiness.
- This does not change runtime wiring or execution behavior.
