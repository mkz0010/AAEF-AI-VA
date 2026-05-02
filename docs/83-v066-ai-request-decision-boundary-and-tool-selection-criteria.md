# v0.6.6 AI Request Decision Boundary and Tool Selection Criteria

Version: v0.6.6 candidate  
Status: AI request-boundary and tool-selection design; does not authorize runtime execution

## Purpose

This checkpoint defines the AI request decision boundary and tool selection criteria
for AAEF-AI-VA.

v0.6.5 defined the documentation-only local lab profile and action taxonomy. The
next design question is how to describe AI-assisted method selection without
implying AI execution authority.

This checkpoint is design and planning only.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Core proposition

The core proposition is:

~~~text
AI generates tool_action_request.
Gates decide execution.
~~~

In Japanese:

~~~text
AIは tool_action_request を生成する。
実行可否はゲートが決める。
~~~

AI may recommend a candidate method, choose a candidate tool at the request-generation
level, or explain why a next observation would be useful.

AI must not authorize execution.

Execution authority remains with authorization, scope, preflight, Tool Gateway,
human review, and delivery gates.

## Compatibility note

Execution authority remains with authorization, scope, preflight, Tool Gateway, human review, and delivery gates.

The same meaning may also appear in wrapped Markdown prose, but this exact line is retained for validation compatibility.

## Decision boundary

The project separates three layers:

| Layer | AI role | Gate role |
| --- | --- | --- |
| Observation interpretation | AI may interpret sanitized and normalized observations | Gate verifies observation source, scope, and safety boundary |
| Request generation | AI may generate `tool_action_request` | Gate verifies authorization, preflight, action taxonomy, and review requirements |
| Execution decision | AI has no authority | Gate decides block, allow future dry-run, require review, or keep execution blocked |

This distinction must remain visible in future design, demos, and commercial
conversation.

## What AI may do

AI may:

- read approved diagnostic context packages,
- identify missing observations,
- recommend candidate next observations,
- choose a candidate method at request-generation level,
- generate `tool_action_request`,
- compare candidate tools,
- state confidence and uncertainty,
- state why information is insufficient,
- request human review,
- request additional preflight evidence,
- produce a non-executing rationale for a proposed action.

These are request-generation activities, not execution authorization.

## What AI must not do

AI must not:

- authorize execution,
- bypass authorization gates,
- bypass scope gates,
- bypass preflight gates,
- bypass Tool Gateway enforcement,
- bypass human review,
- treat tool selection as permission,
- treat confidence as authorization,
- request real credentials,
- request raw secrets,
- decide customer-target operation,
- decide external network testing,
- decide production deployment,
- issue compliance, legal, audit, or safety claims.

## Tool selection is not execution authority

Tool selection means:

~~~text
AI proposes which tool or method may be useful for the next diagnostic step.
~~~

Tool selection does not mean:

~~~text
AI is allowed to run the tool.
AI has decided execution is safe.
AI has authority over target scope.
AI has authority over customer authorization.
AI has authority over credentials.
~~~

Every proposed tool action remains a `tool_action_request`.

Every `tool_action_request` must be evaluated by gates.

## Tool action request fields

A future `tool_action_request` should include:

| Field | Purpose |
| --- | --- |
| `request_id` | Unique request identifier |
| `requested_by` | AI, operator, or system component |
| `request_generation_context_ref` | Reference to approved diagnostic context |
| `candidate_tool` | Proposed tool or method |
| `candidate_action_type` | Proposed action category |
| `target_binding_ref` | Reference to target/scope binding |
| `scope_binding_ref` | Reference to allowed scope |
| `reason_for_request` | Why the action is proposed |
| `observations_used` | Sanitized observations used to generate the request |
| `missing_information` | Known gaps |
| `confidence` | Non-authoritative confidence statement |
| `expected_evidence` | Evidence expected if the action is later approved |
| `safety_notes` | Safety concerns and constraints |
| `requires_human_review` | Whether review is required before any later advancement |
| `execution_authority_claimed` | Must be `false` |

The field `execution_authority_claimed` must remain false.

## Request generation context

AI tool selection should be based on approved context such as:

- target type,
- application type,
- SPA or non-SPA indication,
- API type,
- authentication method category,
- scope boundaries,
- local-only or documentation-only target mode,
- known denied actions,
- allowed documentation-only actions,
- available observations,
- missing observations,
- suspected vulnerability category,
- available evidence,
- preflight evidence requirements,
- human review requirements,
- generated output policy,
- public claim boundary.

The AI should not infer permission from context.

Context informs request generation only.

## Current MVP tool criteria

The current MVP tool set remains:

| Tool/method | Request-generation use | Execution status |
| --- | --- | --- |
| ZAP | Web application passive/active scan candidate in future controlled contexts | Execution not authorized |
| Nmap | Port and service discovery candidate in future controlled contexts | Execution not authorized |
| nuclei | Known vulnerability or template-based check candidate in future controlled contexts | Execution not authorized |
| browser / safe_login_check | Authentication-flow observation candidate in future controlled contexts | Execution not authorized |

Current references to these tools remain design or simulated behavior unless a later
explicit checkpoint authorizes a narrower dry-run or local-only behavior.

## Future tool candidate tiers

Future tool candidates are categorized for request-generation criteria only.

They do not authorize execution.

| Tier | Tool candidate | Intended future request-generation rationale |
| --- | --- | --- |
| P0 | testssl.sh or sslyze | TLS configuration observation where ZAP coverage is insufficient |
| P0 | nikto | Web server misconfiguration and known dangerous file observation |
| P1 | ffuf or feroxbuster | Content discovery and hidden endpoint observation |
| P1 | constrained sqlmap | SQL injection confirmation candidate under strict low-risk and parameter-bound constraints |
| P1 | wapiti or arachni | Alternative or complementary web scan engine candidate |
| P2 | Burp Suite Pro CLI/API | Advanced commercial scanner profile candidate under licensing and customer-scope controls |
| P2 | Nessus Essentials or OpenVAS | Network and infrastructure vulnerability scan candidate under separate safety and scope controls |

These tools must not be added as execution-authorized capabilities merely because
they appear in this roadmap.

## Tool-selection criteria

AI may recommend a candidate tool only when the recommendation is grounded in
approved context.

| Condition | Candidate method | Required caution |
| --- | --- | --- |
| TLS configuration is in scope | testssl.sh or sslyze | Local-only or explicitly scoped target required |
| Web server misconfiguration is suspected | nikto | Must avoid external or customer target implication |
| Unknown paths or endpoints block assessment | ffuf or feroxbuster | Rate, scope, and target constraints required |
| SQL injection signal exists in approved observation | constrained sqlmap | Low-risk, parameter-bound, and human-reviewed only |
| ZAP results are incomplete or need corroboration | wapiti or arachni | Alternative engine use remains gated |
| Advanced manual/professional workflow is needed | Burp Suite Pro CLI/API | License, scope, and commercial boundary required |
| Network vulnerability context is in scope | Nessus Essentials or OpenVAS | Separate safety, timing, and resource controls required |

Tool-selection criteria are advisory criteria for request generation.

They are not permission to run the tool.

## Request outcome model

A `tool_action_request` may result in:

| Outcome | Meaning |
| --- | --- |
| `blocked` | Gate denies or keeps execution blocked |
| `requires_human_review` | Human review is required before any later advancement |
| `requires_more_observation` | Information is insufficient for the requested action |
| `requires_preflight_evidence` | Required preflight evidence is missing |
| `documentation_recorded` | Documentation-only action is recorded |
| `future_dry_run_candidate` | Candidate is recorded for future dry-run planning |
| `execution_not_authorized` | Runtime execution remains blocked |

This checkpoint does not introduce an `executed` outcome.

## Request quality criteria

A high-quality AI-generated request should:

- name the capability it supports,
- name the suspected diagnostic purpose,
- identify observations used,
- identify missing information,
- identify target and scope binding references,
- select an allowed or candidate action category,
- avoid denied action categories,
- state confidence without claiming authority,
- state expected evidence,
- state safety notes,
- state whether human review is required,
- preserve the boundary that execution is gate-decided.

A low-quality request should be rejected or sent back for additional information.

## Rejection criteria

A `tool_action_request` should be rejected if it:

- claims execution authority,
- lacks target binding,
- lacks scope binding,
- requests an action in the denied taxonomy,
- requests live scanning,
- requests external network testing,
- requests customer-target operation,
- requests real credential injection,
- requests raw sensitive artifact capture,
- attempts to bypass preflight,
- attempts to bypass human review,
- treats confidence as permission,
- treats tool choice as authorization,
- lacks diagnostic rationale,
- lacks expected evidence,
- relies on unapproved raw artifacts.

## Human review escalation

Human review is required when:

- the proposed action could affect assessment scope,
- the proposed action could influence finding promotion,
- the proposed action could influence report delivery,
- the proposed action references credentials or authentication state,
- the proposed action references potentially sensitive artifacts,
- the proposed action is a future dry-run candidate,
- the proposed action is associated with a P1 or P2 tool candidate,
- the request quality is uncertain,
- the diagnostic context is incomplete.

Human review remains a gate, not a rubber stamp.

## Relationship to action taxonomy

The v0.6.5 action taxonomy remains in force.

Allowed documentation-only action categories may be referenced in request generation.

Denied action categories remain denied.

Future tool-specific action categories should be added only after a separate
checkpoint updates the taxonomy.

## Relationship to observation fidelity

This checkpoint depends on approved diagnostic context. It does not define
observation normalization or diagnostic fidelity.

That topic is deferred to:

~~~text
v0.6.7 Observation Normalization and Diagnostic Fidelity Risk Review
~~~

Rationale:

- Tool selection quality depends on the quality of observations.
- Sanitization and normalization can remove diagnostically useful signals.
- The project needs a loss-aware observation model before demo and lab work expand.

## Public claim boundary

Allowed public language:

- "AI generates `tool_action_request`",
- "gates decide execution",
- "AI may recommend candidate methods at request-generation level",
- "tool selection is not execution authorization",
- "runtime execution remains blocked",
- "scan execution remains blocked",
- "customer-target operation remains blocked."

Avoid public language that implies:

- AI authorizes execution,
- AI runs tools autonomously,
- tool choice is permission,
- live scanning,
- customer-target authorization,
- production deployment,
- managed service readiness,
- commercial PoC readiness,
- compliance certification,
- legal approval,
- audit opinion,
- external framework equivalence,
- commercial license grant.

## Compatibility note

Negative guidance may name unsafe implications such as AI authorizing execution, AI running tools autonomously, or tool choice becoming permission. Validation should reject concrete positive claims, not checklist entries that describe language to avoid.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
execution_authorized = false
preflight_satisfied = false
ready_for_runtime_execution = false
real_execution_permitted = false
external_process_execution_allowed = false
network_activity_allowed = false
scan_execution_allowed = false
credential_injection_permitted = false
raw_artifact_capture_permitted = false
customer_target = false
external_network_target = false
~~~

## Claims to avoid

Do not claim that this checkpoint provides:

- production deployment approval,
- runtime execution readiness,
- scan authorization,
- customer-target authorization,
- compliance certification,
- legal approval,
- audit opinion,
- completed legal review,
- completed dependency audit,
- managed service approval,
- commercial license grant,
- safety guarantee,
- external framework equivalence,
- audit sufficiency.

## Required local checks

Before tagging v0.6.6, verify:

1. README links to this checkpoint.
2. Core proposition is recorded.
3. Decision boundary is recorded.
4. What AI may do is recorded.
5. What AI must not do is recorded.
6. Tool selection is not execution authority is recorded.
7. Tool action request fields are recorded.
8. Request generation context is recorded.
9. Current MVP tool criteria are recorded.
10. Future tool candidate tiers are recorded.
11. Tool-selection criteria are recorded.
12. Request outcome model is recorded.
13. Request quality and rejection criteria are recorded.
14. Human review escalation is recorded.
15. Relationship to observation fidelity is recorded.
16. Runtime and scanning boundaries remain disabled.
17. Claims to avoid are recorded.
18. `tools/run_all_local_checks.py` includes the v0.6.6 AI request boundary test.

## Out of scope

This checkpoint does not:

- build a local lab,
- add static lab fixtures,
- add dry-run lab execution,
- enable runtime execution,
- enable scanning,
- create tool adapters,
- add new scanner integrations,
- create private sales material,
- publish pricing,
- create a target customer list,
- create a commercial contract,
- provide legal advice,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
