# Changelog

## Unreleased

### Added

- Added operator readiness review summary for real execution blockers and next actions.

- Added real execution readiness gate and tests to keep real tool execution disabled until explicit prerequisites are satisfied.

- Added scope registry and target alias resolution controls for command plans and dry-run executor validation.

- Added dry-run controlled executor policy and tests before real tool execution.

- Added dry-run ZAP adapter command plan support without executing ZAP or external processes.

- Documented internal adapter artifact policy and clarified that adapter output remains private/internal by default.
- Added Tool Gateway adapter stubs and adapter registry for ZAP, Nmap, nuclei, and browser automation.
- Routed completed mock Tool Gateway actions through adapter stubs before real tool integration.


- Added v0.1.10 stability checkpoint documentation and a single local validation runner.

- Fixed remaining escaped Python docstring sequences that prevented Tool Gateway runner validation after v0.1.9.

### Fixed

- Fixed Tool Gateway mock runner syntax error introduced during mock Vault credential_ref validation.

- Added mock Vault metadata validation for credential_ref target, scope, tool, operation, expiry, and revocation constraints.
- Added credential_ref mock Vault negative tests.

- Added Tool Gateway runner self-tests for positive scenarios, generated outputs, and fail-closed negative cases.
- Added documentation and ADR for Tool Gateway negative tests.

- Added standard-library Tool Gateway mock runner for allowed, denied, and human-approval-required scenarios.
- Added Tool Gateway mock runner documentation and ADR.


- Added Tool Gateway prototype scaffold and example contract flows for allowed, denied, and human-approval-required actions.
- Added MVP example validation script.

- Added MVP schema contracts for tool action requests, authorization decisions, tool execution results, and evidence records.
- Added lightweight schema validation script.

- Defined Tool Gateway MVP design as the trusted execution control boundary.
- Added ADR for treating Tool Gateway as a trusted control boundary rather than a generic command executor.

- Defined credential_ref lifecycle, visibility boundaries, and Tool Gateway/Vault responsibilities.
- Added credential_ref flow document and ADR for secretless AI tool execution lifecycle.

- Defined initial MVP scope for controlled Web/API/NW assessment assistance.
- Added MVP scope document and ADR for initial tool and assessment boundaries.

- Initial local project scaffold.
- Local-first project management structure.
- Draft documents for business planning, architecture, AAEF controls, credential_ref, AI data handling, and exit strategy.
