# v0.6.2 Evaluation Criteria and Acceptance Model

Version: v0.6.2 candidate  
Status: evaluation planning and acceptance model; does not authorize runtime execution

## Purpose

This checkpoint defines how future AAEF-AI-VA capabilities should be evaluated.

v0.6.0 established work ordering. v0.6.1 inventoried current capabilities and
maturity. v0.6.2 defines the criteria for judging whether future work is actually
an improvement.

This checkpoint is evaluation planning only.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Evaluation principle

Future work should be accepted only when it improves at least one of the following
without weakening safety boundaries:

- control boundary clarity,
- authorization decision quality,
- preflight evidence quality,
- scope and target binding clarity,
- human review quality,
- generated evidence readability,
- finding/report review quality,
- delivery authorization clarity,
- local validation coverage,
- public claim accuracy,
- commercial boundary clarity,
- maintainer operational repeatability.

The project should prefer evidence-backed improvement over feature expansion.

## Acceptance model summary

| Evaluation area | Acceptance question | Required result |
| --- | --- | --- |
| Capability fit | Does the work improve a named capability? | Capability is mapped to inventory |
| Maturity movement | Does maturity increase without overclaiming? | L0-L6 movement is explicit |
| Evidence | What artifact proves the change? | Test, doc, fixture, or generated private output exists |
| Safety boundary | Does runtime/scanning remain blocked unless explicitly in scope? | Boundary markers remain false |
| Scope boundary | Is the target local-only, documentation-only, or future commercial? | Scope is explicit |
| Review boundary | Is human review preserved where needed? | Review gate or review rationale exists |
| Claim boundary | What public claim becomes safer? | Claim language remains conservative |
| Rework reduction | Does this reduce future uncertainty? | Next decision becomes clearer |

## Evaluation dimensions

Future work should be scored qualitatively across these dimensions:

| Dimension | Description |
| --- | --- |
| Control clarity | The boundary between AI request and authorized action becomes clearer |
| Safety preservation | Runtime, scan, credential, and customer-target prohibitions remain intact |
| Evidence quality | Evidence is more traceable, readable, or reviewable |
| Reviewability | Human reviewers can understand and approve or block the next step |
| Scope precision | Local, dry-run, fixture, customer, and commercial scopes are separated |
| Testability | Local validation can detect regression or unsafe wording |
| Explainability | A reviewer can explain what the capability proves and does not prove |
| Commercial boundary | Commercial implications remain separated from public license and security reporting |
| Operational repeatability | Maintainer workflow remains reproducible |
| Public claim safety | Public claims stay evidence-backed and conservative |

## Maturity advancement rules

Maturity should advance only when evidence supports it.

| Movement | Requirement |
| --- | --- |
| L0 to L1 | Static example or documented fixture exists |
| L1 to L2 | Local validation checks the example or document |
| L2 to L3 | Dry-run behavior exists without real execution |
| L3 to L4 | Local-only controlled behavior is constrained to owned localhost/lab scope |
| L4 to L5 | Human-reviewed PoC candidate has scope, evidence, and commercial/legal boundaries |
| L5 to L6 | Separate commercial, legal, security, operational, and support review is completed |

AAEF-AI-VA must not imply L5 or L6 readiness based only on L0-L4 evidence.

## Required acceptance gates

Every future v0.6.x implementation or demo-oriented change should pass these gates:

| Gate | Acceptance criterion |
| --- | --- |
| Capability gate | The changed capability is named and mapped to the inventory |
| Evaluation gate | The relevant evaluation dimensions are identified |
| Evidence gate | A concrete artifact supports the change |
| Safety gate | Runtime and scanning prohibitions remain intact |
| Scope gate | Local, dry-run, fixture, commercial, and customer scopes are separated |
| Review gate | Human review is preserved or a documented rationale explains why not |
| Claim gate | Public claims do not exceed demonstrated maturity |
| Regression gate | Existing local checks still pass |
| Private artifact gate | Generated private outputs remain under `private-not-in-git/` |
| Commercial gate | Commercial implications are separated from vulnerability reports and public AGPL use |

## Failure criteria

A change should fail evaluation if it:

- enables runtime execution without explicit authorization work,
- enables scan execution without explicit local-only scope and gate maturity,
- permits credential injection without explicit safety design,
- implies customer-target authorization,
- implies production deployment approval,
- implies compliance certification,
- implies legal approval,
- implies audit opinion,
- creates public claims beyond demonstrated maturity,
- stores private generated artifacts in tracked public files,
- weakens security reporting boundaries,
- confuses commercial inquiries with vulnerability reports,
- bypasses human review where the workflow requires it,
- reduces local validation coverage.

## Evidence requirements

Each accepted change should have at least one evidence artifact:

| Artifact type | Examples |
| --- | --- |
| Local test | `tools/test_*.py` |
| Documentation checkpoint | `docs/*.md` |
| ADR | `planning/decisions/ADR-*.md` |
| Planning issue | `planning/issues/*.md` |
| Static fixture | JSON or Markdown example committed intentionally |
| Generated private output | Output under `private-not-in-git/` |
| GitHub Actions result | Public validation workflow after push |

Generated private outputs are supporting evidence for local behavior, not public
customer evidence and not proof of production operation.

## Evaluation records

Future evaluation-oriented work should record:

- capability name,
- current maturity level,
- target maturity level,
- supporting artifact,
- safety boundary impact,
- scope boundary,
- review requirement,
- public claim impact,
- known limitations,
- next decision unlocked.

This may be recorded in a document, ADR, test, fixture, or generated private output.

## Local lab decision criteria

A local assessment lab should not be built until these criteria are satisfied:

1. capability inventory exists,
2. evaluation criteria exist,
3. safety boundary and non-goal review exists,
4. local lab decision record exists,
5. local-only target profile is explicit,
6. allowed and denied action taxonomy exists,
7. preflight evidence requirements are explicit,
8. generated output policy remains private,
9. public claims remain conservative,
10. runtime and scanning remain blocked until intentionally advanced.

The local lab should start no higher than documentation-only, static fixture, or
dry-run maturity unless a later decision explicitly authorizes localhost-only
controlled behavior.

## Demo-readiness criteria

A demo scenario should be considered ready only when:

- it has a named purpose,
- it maps to capability inventory,
- it has evaluation criteria,
- it does not imply live scanning,
- it does not imply customer-target authorization,
- it can be explained through evidence and review gates,
- it produces outputs under `private-not-in-git/` where applicable,
- it includes a "what this demo does not prove" section,
- it avoids production, certification, legal, audit, and safety guarantee claims.

## Commercial PoC boundary criteria

Commercial PoC readiness should require:

- explicit commercial scope,
- separate commercial agreement or licensing discussion,
- target authorization model,
- human review model,
- evidence retention model,
- delivery authorization model,
- support boundary,
- vulnerability disclosure boundary,
- data handling boundary,
- operational rollback plan,
- public claim boundary.

This repository does not currently provide commercial PoC readiness.

## Scoring guidance

Use qualitative scoring rather than certification-like scores.

Recommended values:

| Score | Meaning |
| --- | --- |
| Not evaluated | No evaluation has been performed |
| Weak | Criteria are mostly unclear or unsupported |
| Partial | Some evidence exists but important gaps remain |
| Adequate for planning | Enough evidence to plan the next step |
| Adequate for local validation | Enough evidence to validate locally |
| Adequate for dry-run demo | Enough evidence for dry-run demonstration |
| Not sufficient for customer use | Explicitly not sufficient for customer-target operation |

Avoid labels such as certified, compliant, approved, guaranteed, audit-ready, or
production-ready.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.3 Safety Boundary and Non-Goal Review
~~~

Rationale:

- v0.6.1 identified capabilities and gaps.
- v0.6.2 defines how future changes will be evaluated.
- v0.6.3 should reconfirm what remains intentionally out of scope before local lab
  decisioning.
- The local assessment lab decision should happen only after evaluation criteria and
  safety/non-goal review are complete.

## Compatibility note

The validation test represents the demo phrase `what this demo does not prove` without breaking Python string quoting.

This preserves the intended demo-readiness criterion while avoiding a test syntax error.

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

Before tagging v0.6.2, verify:

1. README links to this checkpoint.
2. Evaluation principle is recorded.
3. Acceptance model summary is recorded.
4. Evaluation dimensions are recorded.
5. Maturity advancement rules are recorded.
6. Required acceptance gates are recorded.
7. Failure criteria are recorded.
8. Evidence requirements are recorded.
9. Local lab decision criteria are recorded.
10. Demo-readiness criteria are recorded.
11. Commercial PoC boundary criteria are recorded.
12. Scoring guidance is recorded.
13. Runtime and scanning boundaries remain disabled.
14. Claims to avoid are recorded.
15. `tools/run_all_local_checks.py` includes the v0.6.2 evaluation criteria test.

## Out of scope

This checkpoint does not:

- build a local lab,
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
