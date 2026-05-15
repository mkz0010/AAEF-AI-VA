# v0.6.236 Next Work Selection Using Risk-Tiered Granularity

Status: selected next work checkpoint  
Scope: AAEF-AI-VA applied implementation planning  
Previous checkpoint: v0.6.235 Future Record Planning Review and Decision  
Selection result: `record_candidate_planning`  
Application status: selection only; no record candidate artifacts created

## Purpose

This checkpoint uses the risk-tiered granularity policy to select the next AAEF-AI-VA work item after v0.6.235 accepted the Future Record Planning Candidate for future fixture planning and record candidate planning.

The selected next work item is:

~~~text
record_candidate_planning
~~~

This selection is intentionally narrow. v0.6.236 selects record candidate planning as the next work item, but it does not create record candidate artifacts, actual records, fixtures, a minimum flow package, reviewer walkthrough, AAEF five questions mapping, AAEF handback summary, runtime behavior, scanner behavior, Tool Gateway behavior, adapter behavior, schema behavior, publication approval, or public announcement.

No private generated outputs are moved public in v0.6.236.

## Inputs

The selection uses the following current-state inputs:

- v0.6.220 accepted AAEF Applied Evidence Minimum Flow Plan.
- v0.6.223 accepted Existing Element Inventory.
- v0.6.226 accepted Minimum Flow Scenario Matrix.
- v0.6.229 accepted Evidence Linkage Table Review and Decision.
- v0.6.230 selected `tool_action_request_gate_decision_dispatch_evidence_package`.
- v0.6.232 accepted the package boundary for future fixture and record planning.
- v0.6.233 selected `future_record_planning`.
- v0.6.234 created the Future Record Planning Candidate.
- v0.6.235 accepted the Future Record Planning Candidate for future fixture planning and record candidate planning.
- Current AAEF-AI-VA public-safety, applied-implementation, and evidence-boundary constraints.
- Current principle: Model output is not authority.
- Current principle: AI rationale is not authorization.
- Current principle: gate decision is not AI self-approval.
- Current principle: evidence supports reconstruction; it does not prove legal truth.

## Selection rationale

`record_candidate_planning` is selected because the future record model has been accepted, but actual record candidate artifacts should not be created before a planning checkpoint defines their boundaries.

Record candidate planning should come before fixture planning because fixtures should instantiate a known record candidate shape rather than forcing record semantics to emerge from examples.

This preserves the sequence:

~~~text
accepted package boundary
  -> accepted future record planning
  -> record candidate planning
  -> record candidate artifacts
  -> fixture planning
  -> fixture artifacts
  -> reviewer walkthrough planning
  -> AAEF five questions mapping planning
~~~

The sequence reduces the risk of treating fixture examples as authoritative schema, treating static artifacts as runtime behavior, or treating mock/dry-run evidence as live scanner execution.

## Risk-tiered granularity review

| Candidate work item | Risk | Granularity assessment | Selection decision |
| --- | --- | --- | --- |
| `record_candidate_planning` | medium | narrow enough to plan record candidate artifacts before creating them | selected |
| `future_fixture_planning` | medium | useful, but should follow record candidate planning | deferred |
| `reviewer_walkthrough_planning` | medium | useful, but should follow record candidate planning or fixture planning | deferred |
| `aaef_five_questions_mapping_planning` | medium | useful, but depends on stable record candidate and reviewer path planning | deferred |
| actual record candidate creation | higher | premature before record candidate planning candidate and review | deferred |
| actual record creation | higher | premature before record candidate artifacts and review | deferred |
| fixture creation or fixture modification | medium | premature before record candidate planning | deferred |
| runtime demo work | high | still requires separate readiness, preflight, and safety-gate work | deferred |
| publication or announcement work | high | premature before records, fixtures, and review exist | deferred |

## Selected record candidate planning scope

The next checkpoint should create a documentation-only planning candidate for future record candidate artifacts. It should not create actual record candidate artifacts or actual records.

The future planning scope should cover candidate artifact planning for these record groups:

- `model_output_reference_record_candidate`
- `tool_action_request_record_candidate`
- `gate_decision_record_candidate`
- `dispatch_decision_record_candidate`
- `non_dispatch_decision_record_candidate`
- `execution_result_record_candidate`
- `non_execution_result_record_candidate`
- `evidence_event_record_candidate`
- `reviewer_reconstruction_reference_record_candidate`
- `aaef_five_questions_mapping_reference_record_candidate`

The next checkpoint should preserve permitted, denied, held, and expired-not-executed paths as first-class future record candidate paths.

## Explicit non-artifact boundary

This checkpoint selects record candidate planning only. It does not create any actual record candidate artifacts or actual records.

The following remain not created:

- actual model output reference record candidates
- actual tool action request record candidates
- actual gate decision record candidates
- actual dispatch decision record candidates
- actual non-dispatch decision record candidates
- actual execution result record candidates
- actual non-execution result record candidates
- actual evidence event record candidates
- actual reviewer reconstruction reference record candidates
- actual AAEF five questions mapping reference record candidates
- actual records
- fixtures

## Decision fields

~~~text
next_work_selection_completed = true
selected_work_item = record_candidate_planning
selected_work_item_status = selected_for_next_candidate_checkpoint
selected_work_item_reason = accepted_future_record_planning_requires_record_candidate_planning_before_fixture_creation
selection_applied_to_record_candidates = false
record_candidate_planning_selected = true
future_fixture_planning_selected = false
reviewer_walkthrough_planning_selected = false
aaef_five_questions_mapping_planning_selected = false
record_candidate_planning_candidate_created = false
record_candidate_artifacts_created = false
record_candidates_created = false
actual_records_created = false
records_created = false
minimum_flow_package_created = false
package_implementation_created = false
fixtures_created = false
fixtures_modified = false
fixture_planning_created = false
evidence_linkage_records_created = false
model_output_reference_record_candidates_created = false
tool_action_request_record_candidates_created = false
gate_decision_record_candidates_created = false
dispatch_decision_record_candidates_created = false
non_dispatch_decision_record_candidates_created = false
execution_result_record_candidates_created = false
non_execution_result_record_candidates_created = false
evidence_event_record_candidates_created = false
reviewer_reconstruction_reference_record_candidates_created = false
aaef_five_questions_mapping_reference_record_candidates_created = false
model_output_reference_records_created = false
tool_action_request_records_created = false
gate_decision_records_created = false
dispatch_decision_records_created = false
non_dispatch_decision_records_created = false
dispatch_evidence_records_created = false
non_dispatch_evidence_records_created = false
execution_result_records_created = false
non_execution_result_records_created = false
evidence_event_records_created = false
reviewer_reconstruction_reference_records_created = false
aaef_five_questions_mapping_reference_records_created = false
reviewer_walkthrough_created = false
aaef_five_questions_mapping_created = false
aaef_handback_summary_created = false
private_generated_outputs_moved_public = false
public_exposure_cleanup_applied = false
readme_front_page_rewritten = false
gateway_core_safety_controls_implemented = false
tool_gateway_behavior_changed = false
adapter_behavior_changed = false
execution_status_renamed = false
schema_changed = false
validator_behavior_changed = false
fixture_semantics_changed = false
runtime_behavior_changed = false
scanner_behavior_changed = false
runtime_demo_ready = false
scanner_readiness_claim = false
external_poc_readiness_claim = false
publication_approval = false
public_announcement = deferred
social_post_publication = deferred
commercial_terms_created = false
production_readiness_claim = false
certification_claim = false
legal_compliance_claim = false
audit_opinion_claim = false
diagnostic_completeness_claim = false
external_framework_equivalence_claim = false
~~~

## Claim boundaries

This checkpoint preserves the following boundaries:

- runtime demo remains necessary but deferred
- publication remains deferred
- evidence supports reconstruction; it does not prove legal truth
- validator success is structural only
- model output is not authority
- AI rationale is not authorization
- gate decision is not AI self-approval
- generated private run output is not public-safe by default
- human approval is not risk acceptance
- mock flow is not live scanner execution
- static fixture is not runtime behavior
- record candidate planning selection is not record candidate creation
- record candidate planning is not actual record creation
- future record planning is not schema implementation
- accepted package boundary is not an implemented package
- accepted package boundary is not a minimum flow package

No production readiness, scanner readiness, external PoC readiness, customer PoC approval, paid engagement approval, legal compliance, audit sufficiency, audit opinion, certification, diagnostic completeness, automated risk acceptance, or external-framework equivalence claim is made.

## Next checkpoint

The likely next checkpoint is:

~~~text
v0.6.237 Record Candidate Planning Candidate
~~~

The next checkpoint should create a documentation-only candidate plan for future record candidate artifacts under the accepted future record planning model. It should still avoid actual record candidate creation, actual record creation, fixture creation, runtime behavior, scanner behavior, live execution, publication approval, or public announcement claims.
