# Issue 0252: Add v0.6.183 Safe Demo Scenario Definition candidate

## Summary

Create the Safe Demo Scenario Definition candidate as checkpoint 1 of 2 for the Medium-risk work item selected in v0.6.182.

## Acceptance criteria

* Add `docs/safe-demo-scenario-definition.md`.
* Add `docs/259-v06183-safe-demo-scenario-definition-candidate.md`.
* Add `planning/decisions/ADR-0253-add-v06183-safe-demo-scenario-definition-candidate.md`.
* Add this issue note.
* Add `tools/test_v06183_safe_demo_scenario_definition_candidate.py`.
* Register the v0.6.183 test in `tools/run_all_local_checks.py`.
* Confirm the scenario defines request, gate decision, evidence trace, blocked/non-execution outcome, and reviewer questions.
* Confirm the scenario is mock/fixture-only and documentation-only at this checkpoint.
* Confirm the review/decision is deferred to v0.6.184.
* Confirm no executable demo, safe demo, public demo, runtime/scanner readiness, real scanner execution, runtime execution, customer PoC intake, AAEF main publication, AAEF main issue/PR, issue command/URL, customer PoC approval, commercial contract, paid engagement approval, commercial license terms, customer-specific material, validator behavior, schema, public sample, runtime, scanner, Docker, credential, customer, delivery, certification claim, legal compliance claim, audit opinion claim, production readiness claim, external-framework equivalence claim, diagnostic completeness claim, third-party testing authorization claim, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not create an executable demo.
* Do not create a safe demo artifact.
* Do not create a public demo artifact.
* Do not authorize runtime or scanner execution.
* Do not authorize customer PoC intake.
* Do not create a commercial contract or commercial license terms.
* Do not reopen the AAEF main handback sequence.
