# Evidence Reconstruction Report

## Purpose

This document defines the first evidence reconstruction report for the AAEF-controlled AI Vulnerability Assessment Platform.

v0.1.21 introduced evidence chain linkage. v0.1.22 turns that chain into a human-readable reconstruction report.

## Core Principle

Evidence is useful only if it can explain what happened.

The reconstruction report converts linked records into an explanation of:

- what was requested,
- what was authorized,
- what the Tool Gateway produced,
- what evidence was generated,
- why real execution is not permitted,
- what the operator reviewed,
- what human approval decision was recorded,
- whether secrets were exposed to AI,
- whether real execution was permitted.

## Generated Files

The generator writes ignored/private outputs under:

~~~text
private-not-in-git/reconstruction-reports/demo/
~~~

Generated files:

- `evidence-reconstruction-report.generated.json`
- `evidence-reconstruction-report.generated.md`

## Example Command

~~~bash
py tools/generate_evidence_reconstruction_report.py
~~~

You can also generate a report with an approved approval record for workflow testing:

~~~bash
py tools/generate_evidence_reconstruction_report.py approved
~~~

Even with an approved approval record, the report states that real execution is not permitted in the current MVP.

## Report Sections

The reconstruction report includes:

- summary,
- key IDs,
- safety assertions,
- readiness blockers,
- next actions,
- reconstruction narrative,
- chain nodes,
- chain links,
- review questions.

## Safety Assertions

The MVP report asserts:

- model output was not execution authority,
- real execution was not permitted,
- no external process was executed,
- no network activity was performed,
- secrets were not exposed to AI,
- evidence was required,
- adapter output was not embedded in public result objects,
- reconstruction is supported.

## Relationship to Evidence Chain

The evidence chain is the structural linkage.

The reconstruction report is the human-readable explanation built from that linkage.

## Future Use

Future versions may use reconstruction reports for:

- internal review,
- customer delivery packets,
- audit support,
- incident reconstruction,
- diagnostic run approval history,
- management reporting.

## Relationship to Sanitizer

The reconstruction report currently asserts that secrets were not exposed to AI based on generated result and evidence flags.

The sanitizer/redaction policy scaffold adds a technical boundary for future raw adapter outputs before they become AI-visible.

See `docs/31-sanitizer-redaction-policy.md`.

## Relationship to Finding Candidates

Future reconstruction reports may reference reviewed finding candidates.

The current MVP introduces finding candidates as non-report-ready review objects derived from sanitized artifacts.

See `docs/32-sanitized-finding-candidate-model.md`.
