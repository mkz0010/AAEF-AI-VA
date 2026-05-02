# Evidence Store Design Draft

## Purpose

診断アクション、認可判断、ツール実行結果、Finding候補、人間レビュー結果を紐づける。

## Initial Evidence Fields

- evidence_id
- authorization_decision_id
- action_request_id
- target_id
- tool
- operation
- timestamp
- result_summary
- raw_artifact_ref
- sanitized_artifact_ref
- credential_ref_used
- human_review_status
- report_finding_id

## Rule

## credential_ref Evidence Requirements

Evidence records may include `credential_ref_used`, but must not include raw secret values.

Evidence should preserve traceability between:

- tool_action_request_id,
- authorization_decision_id,
- credential_ref_used,
- tool execution metadata,
- sanitized artifact reference,
- human review status.


Evidence must support reconstruction of what was requested, what was authorized, what was executed, what was observed, and what was finally reported.
