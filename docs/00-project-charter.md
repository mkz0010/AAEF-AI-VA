# Project Charter

## Project Name

AAEF-controlled AI Vulnerability Assessment Platform

## Japanese Name

AAEF制御型AI脆弱性診断基盤

## Purpose

AIに脆弱性診断を任せるのではなく、AIによる診断計画、ツール実行要求、結果整理、報告書作成を、契約スコープ・認可・実行制御・機密情報保護・証跡・人間レビューの下で実施するための統制型診断基盤を構築する。

## Core Principle

Model output is not authority.

AIの出力は診断行為の権限ではない。AIは診断行為を要求できるが、実行可否はAAEF Authorization Gateway、Tool Gateway、契約スコープ、人間レビューによって決定される。

## Initial Positioning

This project is not a fully autonomous AI penetration testing service.

It is a controlled execution and evidence layer for AI-assisted vulnerability assessment.

## Initial Business Direction

The project may be developed as:

- an internal AI-assisted vulnerability assessment service,
- a platform licensed to vulnerability assessment companies,
- a PoC offered to MSSPs, SIers, or security consulting firms,
- or a commercial implementation that can later be sold separately from the public AAEF framework.
