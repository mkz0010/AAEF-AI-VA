# Issue 0077: Add v0.6.7 observation normalization and diagnostic fidelity risk review

Status: Completed by v0.6.7 candidate  
Type: v0.6.7 planning / observation normalization / diagnostic fidelity risk

## Goal

Define how AAEF-AI-VA should preserve diagnostic signal while preventing unsafe raw
responses and secrets from being sent directly to AI.

## Acceptance criteria

- [x] Add v0.6.7 observation normalization and diagnostic fidelity risk review.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Define Diagnostic Fidelity Risk.
- [x] Record observation handling pipeline.
- [x] Record raw artifact principle.
- [x] Record AI diagnostic context package.
- [x] Record signal-preserving extraction.
- [x] Record information that should not be sent directly to AI.
- [x] Record diagnostic sufficiency criteria.
- [x] Record normalization loss record.
- [x] Record AI behavior under insufficient information.
- [x] Record escalation paths.
- [x] Confirm runtime execution remains disabled.

## Non-goals

- Implement sanitizer changes.
- Implement normalizer changes.
- Implement signal extraction.
- Create new raw artifacts.
- Build a local lab.
- Add dry-run lab execution.
- Enable runtime execution.
- Enable scanning.
- Add new scanner integrations.
- Create private sales material.
- Publish pricing.
- Create a commercial contract.
- Provide legal advice.
