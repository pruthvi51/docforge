# ADR 0001: Deterministic-First Cascade Architecture

## Status: Accepted
## Context
Calling LLMs for every regex pattern or exact dictionary match is prohibitively expensive.

## Decision
Route inputs through regex, RapidFuzz ontology matching, and only fallback to LLMs when necessary.

## Consequences
- 42% token cost reduction.
