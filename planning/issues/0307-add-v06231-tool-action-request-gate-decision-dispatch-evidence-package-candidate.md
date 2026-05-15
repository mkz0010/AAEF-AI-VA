# 0307 - Add v0.6.231 Tool Action Request Gate Decision Dispatch Evidence Package Candidate

Status: completed by v0.6.231  
Version: v0.6.231  
Type: planning / package candidate checkpoint

## Objective

Create a documentation-only candidate package shape for the selected work item:

~~~text
tool_action_request_gate_decision_dispatch_evidence_package
~~~

## Acceptance criteria

- `package_candidate_created = true` is recorded.
- `package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231` is recorded.
- `package_candidate_status = candidate_not_applied` is recorded.
- `package_candidate_scope = documentation_only_package_shape` is recorded.
- The candidate package shape includes model output reference, tool action request, gate decision, dispatch or non-dispatch decision, execution or non-execution result, evidence event, reviewer reconstruction path, and AAEF five questions mapping reference.
- The candidate package shape covers:
  - `SCN-001 permitted safe diagnostic`
  - `SCN-002 denied out-of-scope request`
  - `SCN-003 held / requires human approval`
  - `SCN-004 expired-not-executed`
- No minimum flow package, fixtures, evidence linkage records, request records, decision records, dispatch records, result records, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.
- No runtime behavior, scanner behavior, Tool Gateway behavior, adapter behavior, schema behavior, or validator behavior is changed, except registration of the v0.6.231 structural test.
- No production readiness, scanner readiness, runtime demo readiness, external PoC readiness, publication approval, legal compliance, audit sufficiency, audit opinion, certification, diagnostic completeness, automated risk acceptance, or external-framework equivalence claim is made.

## Out of scope

- Accepting the candidate package shape.
- Creating package-level records.
- Creating or modifying fixtures.
- Creating evidence linkage records.
- Creating runtime behavior.
- Changing Tool Gateway or adapter behavior.
- Changing schema behavior.
- Changing validator behavior, except registration of the v0.6.231 structural test.
- Moving private generated outputs public.
- Publishing announcements or social posts.
- Creating commercial terms.

## Next

Proceed to v0.6.232 Tool Action Request Gate Decision Dispatch Evidence Package Review and Decision after v0.6.231 is merged and tagged.
