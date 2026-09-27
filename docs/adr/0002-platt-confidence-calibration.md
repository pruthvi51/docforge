# ADR 0002: Platt Scaling Confidence Calibration

## Status: Accepted
## Context
Raw model extraction confidence is poorly calibrated, sending too many correct extractions for manual review.

## Decision
Apply Platt logistic scaling to calibrate probabilities, routing only <85% confidence extractions to clinicians.

## Consequences
- 73% reduction in clinician review burden.
