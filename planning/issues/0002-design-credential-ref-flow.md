# 0002: Design credential_ref flow

## Status

Open

## Priority

P0

## Type

Design

## Background

AIに認証情報を渡さず、credential_refのみで認証付き診断を実行する方式を設計する。

## Acceptance Criteria

- credential_ref lifecycle is defined
- Vault responsibility is defined
- Tool Gateway responsibility is defined
- AI-visible and AI-hidden fields are separated
- Evidence requirements are defined
- Sanitization requirements for tool output are defined
