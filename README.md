# AAEF-controlled AI Vulnerability Assessment Platform

AAEF制御型AI脆弱性診断基盤のローカル管理リポジトリ。

This repository is local-first and private by default.

## Core Principle

Model output is not authority.

AIの出力は診断行為の権限ではない。AIは診断行為を要求できるが、実行可否はAAEF Authorization Gateway、Tool Gateway、契約スコープ、人間レビューによって決定される。

## Repository Rule


## Local Validation

Run the complete local validation set before committing, merging, or tagging implementation changes:

~~~bash
py tools/run_all_local_checks.py
~~~

As of `v0.1.10`, the Tool Gateway mock runner baseline is the current stable local checkpoint.

Do not commit raw customer materials, credentials, scan artifacts, personal data, secrets, or confidential client data.
