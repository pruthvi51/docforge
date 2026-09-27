# ADR 0004: Topological DAG Pipeline Compilation

## Status: Accepted
## Context
Multi-stage extraction steps require explicit dependency ordering without circular references.

## Decision
Compile pipeline step dependencies using topological sort.
