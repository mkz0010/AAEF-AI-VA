# v0.6.231 Tool Action Request Gate Decision Dispatch Evidence Package Candidate

Status: candidate package shape  
Scope: AAEF-AI-VA applied implementation planning  
Previous checkpoint: v0.6.230 Next Work Selection Using Risk-Tiered Granularity  
Selected work item: `tool_action_request_gate_decision_dispatch_evidence_package`  
Application status: candidate only; not applied to fixtures, records, runtime, or scanner behavior

## Purpose

This checkpoint creates a candidate package shape for the work item selected in v0.6.230:

~~~text
tool_action_request_gate_decision_dispatch_evidence_package
~~~

The purpose is to define a narrow package boundary that can later connect AI-generated tool action requests, gate decisions, dispatch or non-dispatch evidence, execution or non-execution results, evidence events, and reviewer reconstruction paths.

This is a candidate package shape only. It does not create the minimum flow package, static fixtures, actual evidence linkage records, tool action request records, gate decision records, dispatch evidence records, non-dispatch evidence records, execution result records, non-execution result records, reviewer walkthrough, AAEF five questions mapping, AAEF handback summary, runtime behavior, scanner behavior, Tool Gateway behavior, adapter behavior, schema behavior, publication approval, or public announcement.

## Candidate package identity

~~~text
package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231
package_candidate_name = Tool Action Request Gate Decision Dispatch Evidence Package Candidate
package_candidate_status = candidate_not_applied
package_candidate_scope = documentation_only_package_shape
package_candidate_origin = v0.6.230 selected work item
~~~

## Candidate package objective

The package candidate should provide a future planning container for evidence that answers the AAEF-style reconstruction path:

- What model output proposed or led to the tool action request?
- What tool action request was created?
- What gate decision decided whether execution was allowed?
- Was the action dispatched or not dispatched?
- If dispatched, what execution result was produced?
- If not dispatched, what non-execution result explains why?
- What evidence event links these decisions and outcomes?
- What reviewer path can reconstruct the authority and evidence chain?

The candidate keeps Model output is not authority as the controlling boundary.

Model output is not authority. AI rationale is not authorization, and a gate decision is not AI self-approval.

## Candidate package components

| Component | Candidate role | Status |
| --- | --- | --- |
| `model_output_reference` | Identifies the model output that proposed, described, or triggered the request without treating it as authority | candidate field only |
| `tool_action_request` | Captures the requested tool action, scope, target binding, and requested constraints | candidate field group only |
| `gate_decision` | Captures the authorization gate decision and decision basis | candidate field group only |
| `dispatch_decision` | Captures dispatch decision when execution is allowed | candidate field group only |
| `non_dispatch_decision` | Captures non-dispatch decision when execution is denied, held, or expired | candidate field group only |
| `execution_result` | Captures result reference when a permitted action is dispatched and completes inside the controlled boundary | candidate field group only |
| `non_execution_result` | Captures result reference when an action is not executed | candidate field group only |
| `evidence_event` | Captures the evidence event that links request, decision, dispatch or non-dispatch, and result | candidate field group only |
| `reviewer_reconstruction_path` | Captures the future reviewer path through the evidence chain | candidate field group only |
| `aaef_five_questions_mapping_reference` | Captures the future mapping reference to AAEF-style reconstruction questions | candidate field group only |

## Candidate package field groups

### Model output reference

~~~text
model_output_id
model_output_created_at
model_output_role = request_source_only
model_output_authority_status = not_authority
model_output_rationale_authorization_status = not_authorization
~~~

### Tool action request

~~~text
tool_action_request_id
tool_action_request_created_at
requested_tool
requested_action_type
requested_target_binding
requested_scope_reference
requested_constraints
requested_credential_ref
requester_context_ref
request_status = proposed_for_gate_decision
~~~

### Gate decision

~~~text
gate_decision_id
gate_decision_created_at
gate_decision_status
gate_decision_basis
gate_decision_scope_result
gate_decision_constraint_result
gate_decision_expiry_result
gate_decision_human_approval_requirement
gate_decision_authority_status = authorization_gate_decision
~~~

### Dispatch or non-dispatch decision

~~~text
dispatch_decision_id
non_dispatch_decision_id
dispatch_status
non_dispatch_reason
dispatch_authority_source = gate_decision_only
dispatch_ai_self_approval_status = prohibited
~~~

### Execution or non-execution result

~~~text
execution_result_id
non_execution_result_id
execution_status
non_execution_status
execution_boundary
non_execution_reason
runtime_execution_claim_status = not_claimed
scanner_execution_claim_status = not_claimed
~~~

### Evidence event

~~~text
evidence_event_id
evidence_event_created_at
linked_model_output_id
linked_tool_action_request_id
linked_gate_decision_id
linked_dispatch_decision_id
linked_non_dispatch_decision_id
linked_execution_result_id
linked_non_execution_result_id
evidence_reconstruction_status = supports_reconstruction_not_legal_proof
~~~

### Reviewer reconstruction path

~~~text
reviewer_walkthrough_id
reviewer_reconstruction_path_id
reviewer_expected_questions
reviewer_gap_notes
reviewer_status = future_artifact_reference_only
~~~

### AAEF five questions mapping reference

~~~text
five_questions_mapping_id
who_acted_reference
on_whose_behalf_reference
with_what_scope_reference
allowed_at_execution_time_reference
what_evidence_proves_reference
mapping_status = future_artifact_reference_only
~~~

## Scenario coverage candidate

| Scenario | Candidate package path | Expected future evidence shape |
| --- | --- | --- |
| `SCN-001 permitted safe diagnostic` | request -> gate decision -> dispatch -> execution result -> evidence event -> reviewer reconstruction | future permitted-path package records |
| `SCN-002 denied out-of-scope request` | request -> gate decision -> non-dispatch -> non-execution result -> evidence event -> reviewer reconstruction | future denied-path package records |
| `SCN-003 held / requires human approval` | request -> gate decision -> non-dispatch while held -> non-execution result -> evidence event -> reviewer reconstruction | future held-path package records |
| `SCN-004 expired-not-executed` | request -> gate decision or expiry check -> non-dispatch -> non-execution result -> evidence event -> reviewer reconstruction | future expired-path package records |

## Candidate acceptance criteria for a later review checkpoint

A later review checkpoint should decide whether this candidate package shape is accepted. Acceptance should require that the package shape:

- preserves Model output is not authority
- preserves AI rationale is not authorization
- preserves gate decision is not AI self-approval
- preserves non-dispatch and non-execution evidence as first-class paths
- covers permitted, denied, held, and expired-not-executed scenarios
- avoids production readiness, scanner readiness, runtime demo readiness, legal compliance, audit sufficiency, certification, diagnostic completeness, automated risk acceptance, and external-framework equivalence claims
- keeps private generated outputs out of public artifacts by default
- supports future reviewer reconstruction without claiming that evidence proves legal truth

## Decision fields

~~~text
package_candidate_created = true
package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231
package_candidate_status = candidate_not_applied
package_candidate_scope = documentation_only_package_shape
selected_work_item = tool_action_request_gate_decision_dispatch_evidence_package
selected_work_item_status = candidate_package_shape_created
minimum_flow_package_created = false
package_candidate_applied = false
fixtures_created = false
fixtures_modified = false
evidence_linkage_records_created = false
tool_action_request_records_created = false
gate_decision_records_created = false
dispatch_evidence_records_created = false
non_dispatch_evidence_records_created = false
execution_result_records_created = false
non_execution_result_records_created = false
evidence_event_records_created = false
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

## Explicit non-application boundary

This checkpoint creates a documentation-only candidate package shape. It does not create, modify, or apply:

- minimum flow package artifacts
- static fixtures
- actual evidence linkage records
- actual tool action request records
- actual gate decision records
- actual dispatch evidence records
- actual non-dispatch evidence records
- actual execution result records
- actual non-execution result records
- actual evidence event records
- reviewer walkthrough artifacts
- AAEF five questions mapping artifacts
- AAEF handback summary artifacts
- runtime demo behavior
- scanner behavior
- Tool Gateway behavior
- adapter behavior
- schema behavior
- validator behavior, except registration of the structural v0.6.231 test
- README front-page positioning

No private generated outputs are moved public in v0.6.231.

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
- candidate package shape is not an implemented package
- candidate package shape is not a minimum flow package

No production readiness, scanner readiness, external PoC readiness, customer PoC approval, paid engagement approval, legal compliance, audit sufficiency, audit opinion, certification, diagnostic completeness, automated risk acceptance, or external-framework equivalence claim is made.

## Next checkpoint

The likely next checkpoint is:

~~~text
v0.6.232 Tool Action Request Gate Decision Dispatch Evidence Package Review and Decision
~~~

The next checkpoint should review this candidate package shape and decide whether to accept it for future fixture and record planning. It should still avoid runtime behavior, scanner behavior, live execution, publication approval, or public announcement claims.
