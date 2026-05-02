# Commercial Adoption Preparation Checkpoint

Version: v0.5.0 candidate  
Status: commercial adoption preparation; does not authorize runtime execution

## Purpose

This checkpoint prepares AAEF-AI-VA for business-facing adoption conversations without
turning the public repository into a sales deck.

The intended audience is:

- vulnerability assessment companies,
- MSSPs,
- security consulting firms,
- AI security teams,
- security automation teams,
- organizations evaluating AI-assisted assessment workflows.

The public repository should remain a credible technical reference implementation.
Commercial outreach, pricing, customer-specific proposals, and sales sequencing should
remain private.

## Commercial positioning

AAEF-AI-VA is not positioned as "AI performs vulnerability assessment by itself."

The intended positioning is:

~~~text
AAEF-AI-VA helps demonstrate how AI-assisted vulnerability assessment actions can be
controlled, blocked, reviewed, and evidenced before execution authority is granted.
~~~

The differentiator is not raw model capability.

The differentiator is the control boundary:

~~~text
AI output is not authority to perform assessment actions.
~~~

## Buyer problem

The target buyer often has this concern:

~~~text
We want to use AI in vulnerability assessment, but we are worried about unsafe
execution, scope violations, uncontrolled scanning, credential misuse, unreliable
AI findings, and auditability.
~~~

AAEF-AI-VA provides a concrete reference model for discussing that concern.

## Difference from generic AI vulnerability assessment tools

Many AI-security or AI-assessment offerings emphasize:

- faster finding generation,
- automated scanning,
- report drafting,
- triage acceleration,
- vulnerability explanation,
- agentic operation.

AAEF-AI-VA emphasizes:

- authorization before action,
- contractual scope boundaries,
- Tool Gateway control,
- preflight evidence,
- fail-closed negative examples,
- human review gates,
- report review gates,
- delivery authorization,
- publication hygiene,
- private artifact exclusion,
- evidence-linked lifecycle checkpoints.

## Public vs private material boundary

Public repository material may include:

- reference implementation code,
- safety boundaries,
- evidence models,
- preflight examples,
- review gates,
- licensing and commercial-use boundary,
- SECURITY.md,
- GitHub Actions validation,
- public launch checkpoints,
- high-level commercial adoption boundary.

Private material should include:

- pricing assumptions,
- target company lists,
- outreach sequences,
- negotiation notes,
- customer-specific risks,
- customer-specific scope examples,
- real target profiles,
- real scan workflows,
- service packaging,
- proposal drafts,
- contract negotiation notes,
- commercial license draft terms.

## Commercial paths

Potential commercial paths:

| Path | Description | Public repository role |
| --- | --- | --- |
| Advisory engagement | Help a company design AI-assisted assessment control boundaries | Evidence of expertise and reference model |
| PoC / pilot design | Build a controlled internal PoC for an assessment team | Baseline architecture and gates |
| Commercial license discussion | Separate license for organizations that cannot use AGPL-3.0 as-is | License boundary and contact path |
| Integration support | Help adapt the model to an existing assessment workflow | Shared vocabulary and safety model |
| Training / workshop | Teach AI execution-boundary risk in assessment workflows | Public reference material |

This checkpoint does not set prices or contract terms.

## Target customer profiles

Strong-fit targets:

1. Vulnerability assessment companies that want AI-assisted workflows but fear unsafe automation.
2. MSSPs considering agentic security operations.
3. Security SaaS vendors adding AI workflow features.
4. Consulting firms building AI security advisory practices.
5. Internal security teams evaluating controlled AI-assisted assessment tooling.

Lower-fit targets:

- buyers looking only for a turnkey scanner,
- buyers wanting fully autonomous exploitation,
- buyers wanting to bypass authorization or scope controls,
- buyers expecting compliance certification from this repository alone.

## Suggested enterprise conversation flow

1. Start with the buyer risk:
   - AI can generate useful assessment actions.
   - AI output alone cannot safely authorize assessment actions.
2. Show the core boundary:
   - AI output is a request, not authority.
3. Map the control layers:
   - authorization,
   - contractual scope,
   - Tool Gateway,
   - preflight evidence,
   - human review,
   - report review,
   - delivery authorization.
4. Explain the business value:
   - safer AI adoption,
   - reduced unauthorized action risk,
   - better evidence trail,
   - clearer accountability,
   - easier internal review.
5. Propose a limited PoC:
   - no live customer scanning,
   - no credential injection,
   - local or controlled lab target only,
   - review-focused evidence flow.
6. Discuss commercial path:
   - advisory,
   - integration support,
   - commercial license discussion if needed.

## Commercial inquiry wording

Suggested public wording:

~~~text
AAEF-AI-VA is licensed under AGPL-3.0. Organizations interested in commercial
licensing, integration support, or advisory work may contact the project author
through a separately published commercial contact channel.

Commercial inquiries are separate from vulnerability reports and do not authorize
runtime execution, scanning, credential injection, or customer-target operation.
~~~

## Repository wording boundary

The public repository should not overclaim.

Allowed public claims:

- safety-first reference implementation,
- AI-assisted vulnerability assessment control boundaries,
- AGPL-3.0 licensed implementation,
- separate commercial licensing discussion may be possible,
- GitHub Actions validation is active,
- private vulnerability reporting is enabled,
- runtime execution remains disabled.

Avoid public claims:

- production scanner,
- autonomous vulnerability scanner,
- customer-ready assessment platform,
- commercial license terms are finalized,
- compliance certification,
- legal approval,
- audit opinion,
- guaranteed safe AI assessment,
- permission to scan third-party systems,
- replacement for professional security judgment.

## Private local sales pack

A private local draft may be generated at:

~~~text
private-not-in-git/commercial-adoption/v0.5.0-enterprise-sales-pack.md
~~~

That file is intentionally not tracked.

The public repository records that such private planning material may exist, but it
does not publish pricing, target accounts, customer-specific proposal text, or
negotiation details.

## Runtime and scanning boundary

Commercial adoption preparation does not authorize vulnerability scanning, live
assessment, external network testing, credential injection, customer-target
operation, or any other runtime execution.

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

## Required local checks

Before tagging v0.5.0, verify:

1. Commercial adoption preparation checkpoint exists.
2. README links to the checkpoint.
3. Public/private sales-material boundary is recorded.
4. Commercial inquiry wording is recorded.
5. Target customer profiles are recorded.
6. Differentiation from generic AI vulnerability assessment tools is recorded.
7. Runtime and scanning boundaries remain disabled.
8. `private-not-in-git/` remains excluded from tracked files.
9. `tools/run_all_local_checks.py` includes the commercial adoption test.
10. The public repository does not contain customer-specific pricing or target-account details.

## Out of scope

This checkpoint does not:

- publish a LinkedIn post,
- publish a Zenn or Qiita article,
- create a commercial contract,
- publish pricing,
- publish target account lists,
- provide legal advice,
- authorize runtime execution,
- authorize scan execution,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.

## Follow-up candidates

- Add commercial contact channel once selected.
- Prepare a private enterprise briefing deck.
- Prepare a private outreach list.
- Prepare a private PoC proposal template.
- Add dependency/license inventory.
- Add branch protection / ruleset planning.
- Add a public "Commercial licensing inquiries" section after contact channel is ready.
