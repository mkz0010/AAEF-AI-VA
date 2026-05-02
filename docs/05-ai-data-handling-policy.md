# AI Data Handling Policy Draft

## Purpose

AI利用時の顧客情報、診断情報、秘密情報の取り扱いを制御する。

## Data Classification

| Level | Description | External AI Use |
|---|---|---|
| L0 | Public information | Allowed |
| L1 | Low sensitivity / anonymized data | Conditionally allowed |
| L2 | Confidential customer data | Requires customer approval and policy controls |
| L3 | High sensitivity data | Prohibited by default |
| L4 | Specially controlled data | External AI prohibited or dedicated environment only |

## Prohibited Inputs to External AI

- Passwords
- API keys
- Secret keys
- Session cookies
- VPN credentials
- Raw personal data
- Cardholder data
- Production database contents
- Unredacted source code
- Unredacted high-risk vulnerability details

## Initial Rule

External AI may be used only with minimum necessary data, after classification, redaction, tokenization, or aliasing where practical.
