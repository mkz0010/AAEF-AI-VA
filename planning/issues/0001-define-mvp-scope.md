# 0001: Define MVP scope

## Status

In Progress

## Priority

P0

## Type

Planning

## Background

AAEF制御型AI脆弱性診断基盤のMVP対象を明確にする必要がある。

初期MVPでは、AIによる完全自律ペネトレーションテストではなく、AAEFに基づく統制モデルを実証することを優先する。

## Decision Summary

Initial MVP scope is defined around controlled assistance for:

- Web application vulnerability assessment,
- API vulnerability assessment,
- small-scale network vulnerability assessment.

Initial tools:

- OWASP ZAP,
- Nmap,
- nuclei,
- simple browser automation where necessary.

Deferred tools:

- Burp Suite,
- Nessus / Tenable,
- cloud security posture tools,
- custom exploit validation scripts,
- advanced browser automation.

## Explicitly Out of Scope

- fully autonomous penetration testing,
- exploit chain automation,
- destructive testing,
- DoS or stress testing,
- brute force,
- credential spraying,
- password attacks,
- lateral movement,
- persistence,
- privilege escalation against real systems,
- production data modification,
- uncontrolled internet-wide scanning,
- unsupervised testing of customer production environments,
- AI access to raw credentials,
- external AI use with raw customer confidential materials.

## Acceptance Criteria

- MVP対象が明文化されている
- 初期対象外が明文化されている
- Phase 1 / Phase 2 の境界が明確である
- Business Plan and Architecture drafts are consistent
- credential_ref model is referenced
- Tool Gateway and AAEF Authorization Gateway roles are referenced
- Human review is required for final findings and reports

## Related Documents

- docs/11-mvp-scope.md
- docs/03-architecture.md
- docs/04-aaef-control-model.md
- docs/06-credential-ref-model.md
- planning/decisions/ADR-0005-define-initial-mvp-scope.md

## Remaining Work

- Confirm whether simple browser automation is included in Phase 1 or Phase 2.
- Define the first demo target application.
- Define the first evidence event shape for MVP execution.
- Define the first local prototype directory structure.
