# Public FAQ and Reviewer Objections Handling

Version: v0.5.10 candidate  
Status: public FAQ and reviewer-objection handling; does not authorize runtime execution

## Purpose

This document answers likely first-time reviewer questions about AAEF-AI-VA.

The repository may be reviewed before a direct commercial conversation. In that
situation, reviewers may bring practical objections such as:

- Is this just another vulnerability scanner?
- Does this run scans?
- Can this be used against customer targets?
- What is actually implemented?
- What does the AGPL-3.0 license mean for commercial use?
- Why would a company talk to the author instead of just using the repository?
- What evidence supports the claims?
- What remains intentionally blocked?

This checkpoint answers those questions conservatively and directly.

This checkpoint is explanatory material only.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Short answer

AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability
assessment control boundaries.

It is not a live scanner.

It does not authorize third-party scanning.

It does not authorize customer-target operation.

It demonstrates how AI-assisted assessment workflows can be placed behind
authorization, scope, evidence, review, and delivery gates so that model output is
treated as a request rather than execution authority.

## FAQ

### Is AAEF-AI-VA a vulnerability scanner?

No.

AAEF-AI-VA is not a production vulnerability scanner and not an autonomous
vulnerability scanner.

It is a reference implementation for control boundaries around AI-assisted
vulnerability assessment workflows.

### Does AAEF-AI-VA run live scans?

No.

Runtime execution remains disabled.

Live scanning is not authorized.

The repository currently demonstrates local validation, gate behavior, evidence
models, review boundaries, governance boundaries, and publication boundaries.

### Can this be used against customer targets?

Not from the public repository alone.

Customer-target operation is not authorized.

External network testing is not authorized.

Any future customer-target operation would require separate contractual scope,
authorization, operational design, safety review, and explicit implementation work.

### What does the project actually demonstrate?

The project demonstrates:

- Tool Gateway behavior,
- controlled executor policy,
- real execution readiness blocking,
- operator readiness review,
- human approval gates,
- evidence chain linkage,
- evidence reconstruction reporting,
- sanitizer redaction policy,
- finding candidate modeling,
- finding review gates,
- report finding promotion,
- report review gates,
- report packet review gates,
- delivery authorization gates,
- lifecycle checkpointing,
- runtime readiness blocking,
- local target lab boundary planning,
- runtime destination binding boundary planning,
- bounded execution transition planning,
- preflight validation scaffolding,
- preflight evidence examples and validation rules,
- licensing and commercial-use boundaries,
- public repository readiness,
- publication hygiene,
- security disclosure governance,
- GitHub Actions validation,
- README compatibility,
- repository governance,
- release governance,
- public trust navigation,
- public evidence and capability boundary explanation.

### What does the project not demonstrate?

The project does not demonstrate:

- live vulnerability scanning,
- external network testing,
- customer-target testing,
- credential injection against real systems,
- production service deployment,
- multi-tenant SaaS operation,
- managed security service operation,
- compliance certification,
- legal approval,
- audit opinion,
- external framework equivalence,
- customer-ready managed assessment platform operation.

### Why is runtime execution intentionally blocked?

Runtime execution is intentionally blocked because the project's core principle is:

> AI output is not authority to perform assessment actions.

The project is building control boundaries before enabling execution. That means
authorization, scope, preflight evidence, review, and delivery gates are represented
before live actions are authorized.

### Why does the repository include generated outputs under `private-not-in-git/`?

Local tests generate example outputs under `private-not-in-git/`.

Those outputs demonstrate local pipeline behavior. They are not public customer
evidence and they are not proof of production operation.

`private-not-in-git/` is intentionally excluded from tracked public artifacts.

### Is the project safe to use as-is in production?

No production deployment approval is provided by this repository.

AAEF-AI-VA should be reviewed as a reference implementation and control-boundary
demonstration, not as a production deployment approval.

### Is this compliance certification?

No.

AAEF-AI-VA does not provide compliance certification, legal approval, audit opinion,
or external framework equivalence.

### Is this legal advice?

No.

Licensing, commercial-use, and project-name usage documents are project-boundary
statements. They are not legal advice.

Organizations should consult qualified counsel for licensing or commercial decisions.

### Why AGPL-3.0?

AAEF-AI-VA is publicly licensed under GNU Affero General Public License v3.0.

AGPL-3.0 preserves public-source transparency and helps distinguish public use from
separate commercial licensing discussions.

### Can a company use the public repository commercially?

Organizations may review, use, modify, and redistribute the project under the terms
of AGPL-3.0.

Organizations that want a different commercial arrangement should request a separate
commercial licensing discussion.

No commercial license is granted without a separate written agreement.

### Why would a company talk to the author instead of just using the repository?

A company may want to talk to the author if it needs:

- a non-AGPL commercial licensing discussion,
- controlled proof-of-concept planning,
- integration guidance,
- scope and safety-boundary design,
- governance mapping,
- review of operational readiness,
- support for adapting the control model to a specific environment.

The public repository does not create a commercial contract or managed-service
approval.

### Are commercial inquiries the same as vulnerability reports?

No.

Commercial licensing inquiries are separate from vulnerability reports.

Security reports should follow `SECURITY.md`.

Sensitive vulnerability details should not be posted publicly.

### Does this replace human security professionals?

No.

AAEF-AI-VA is designed around human review, authorization, and governance boundaries.

It does not replace professional security judgment.

### Does this make AI output trustworthy?

Not by itself.

The project does not try to make model output inherently authoritative. It treats
model output as a request and requires independent authorization, scope, evidence,
review, and delivery boundaries before assessment actions can proceed.

### What should a technical reviewer inspect first?

A technical reviewer should inspect:

1. `README.md`
2. `tools/run_all_local_checks.py`
3. `.github/workflows/validate.yml`
4. `docs/75-public-evidence-and-capability-boundary-summary.md`
5. `docs/73-public-trust-and-reviewer-navigation-checkpoint.md`

### What should a commercial reviewer inspect first?

A commercial reviewer should inspect:

1. `README.md`
2. `COMMERCIAL-LICENSE.md`
3. `NOTICE`
4. `TRADEMARKS.md`
5. `docs/66-commercial-adoption-preparation-checkpoint.md`
6. `docs/75-public-evidence-and-capability-boundary-summary.md`

### What should a security reviewer inspect first?

A security reviewer should inspect:

1. `SECURITY.md`
2. `docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md`
3. `docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md`
4. `docs/75-public-evidence-and-capability-boundary-summary.md`

## Reviewer objections and direct responses

| Objection | Conservative response |
| --- | --- |
| "This is not a real scanner yet." | Correct. The repository demonstrates control boundaries and intentionally blocks live scanning. |
| "Why should I care if it does not scan?" | The value is in making AI-assisted assessment actions governable before execution is enabled. |
| "Can I use this directly in customer work?" | Not as customer-target operation from the public repository alone. Separate scope, authorization, safety review, and implementation work would be required. |
| "Is AGPL-3.0 a barrier?" | It may be for some commercial models; that is why separate commercial licensing discussions are explicitly separated. |
| "Can someone fork it?" | The public license allows use under AGPL-3.0 terms; separate commercial, naming, and endorsement boundaries remain documented. |
| "Does this prove compliance?" | No. It is not certification, legal approval, audit opinion, or external framework equivalence. |
| "Is this safe?" | It is designed with safety boundaries, but no safety guarantee is claimed. Runtime and scanning remain blocked. |
| "What is the strongest current evidence?" | Local validation, gate behavior, evidence linkage, review gates, delivery authorization, governance checkpoints, and release operations. |

## Evidence-backed answer pattern

Public answers should follow this pattern:

1. State what is demonstrated.
2. State what remains blocked.
3. Link to the supporting artifact.
4. Avoid unsupported production, certification, legal, audit, or scan-authorization claims.

Example:

~~~text
AAEF-AI-VA demonstrates local validation of control gates and evidence/review
boundaries. Runtime execution and live scanning remain blocked. See
docs/75-public-evidence-and-capability-boundary-summary.md and
tools/run_all_local_checks.py.
~~~

## Relationship to evidence and capability summary

This FAQ builds on:

- `docs/75-public-evidence-and-capability-boundary-summary.md`

The evidence and capability summary explains what is demonstrated. This FAQ answers
likely objections about that boundary.

## Relationship to public front page polish

This FAQ builds on:

- `docs/74-public-front-page-and-repository-landing-polish-checkpoint.md`

The front page polish checkpoint explains how the repository should introduce
itself. This FAQ explains how to respond when reviewers challenge that introduction.

## Relationship to public trust navigation

This FAQ builds on:

- `docs/73-public-trust-and-reviewer-navigation-checkpoint.md`

The reviewer navigation checkpoint explains where different reviewers should go.
This FAQ explains how to answer likely reviewer questions.

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

Before tagging v0.5.10, verify:

1. README links to this FAQ.
2. Short answer is recorded.
3. FAQ answers are recorded.
4. Reviewer objections and direct responses are recorded.
5. Evidence-backed answer pattern is recorded.
6. Relationships to evidence summary, front page polish, and public trust navigation are recorded.
7. Runtime and scanning boundaries remain disabled.
8. Claims to avoid are recorded.
9. `tools/run_all_local_checks.py` includes the public FAQ reviewer objections test.

## Out of scope

This checkpoint does not:

- enable runtime execution,
- enable scanning,
- create private sales material,
- publish pricing,
- create a target customer list,
- create a commercial contract,
- provide legal advice,
- configure GitHub branch protection,
- configure GitHub rulesets,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
