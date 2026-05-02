# AAEF Control Model Draft

## Control Targets

- AI provider usage
- AI input data classification
- Tool action requests
- Authorization decisions
- Credential reference usage
- Tool execution
- Evidence generation
- Human review

## Key Principle

AI output is a request, not authorization.

## Initial Control Areas

### AIUSE: AI Use Controls

- AIUSE-01: AI Provider Use Authorization
- AIUSE-02: Sensitive Data Exclusion
- AIUSE-03: Prompt Data Minimization
- AIUSE-04: Provider Policy Binding
- AIUSE-05: AI Output Non-Authority
- AIUSE-06: Customer AI Preference Enforcement
- AIUSE-07: AI Input/Output Evidence Logging

### TOOL: Tool Execution Controls

- Tool actions must be requested through Tool Gateway.
- Tools must not be executed directly by AI.
- Tool actions must reference approved targets and scopes.
- Destructive or high-risk tests require explicit human approval.

### CRED: Credential Reference Controls

- AI receives credential_ref only.
- Raw credentials are stored in Vault.
- Tool Gateway injects secrets only into approved tool runtimes.
- Evidence must record credential_ref usage without exposing raw secrets.
