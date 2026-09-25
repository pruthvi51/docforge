# ADR 0005: Execution Manifest and Token Accounting

## Status: Accepted
## Context
Production scale requires tracking per-document inference expenses and page-level cost accounting.

## Decision
Emit detailed JSON execution manifests recording token consumption and estimated dollar costs.
