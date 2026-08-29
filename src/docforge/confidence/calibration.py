"""
Platt Scaling Confidence Calibration:
Transforms raw model extraction scores into calibrated true posterior probabilities P(correct | score).
Routes extractions < 85% to the human-in-the-loop clinician review queue.
"""
import math
from typing import Dict, Any

class PlattCalibrator:
    def __init__(self, a: float = -6.0, b: float = 3.0):
        """Logistic parameters fitted via maximum likelihood on validation set."""
        self.a = a
        self.b = b

    def calibrate(self, raw_score: float) -> float:
        """Sigmoid transformation: 1 / (1 + exp(A * score + B))"""
        z = self.a * raw_score + self.b
        # Clamp to avoid overflow
        z = max(-20.0, min(20.0, z))
        calibrated = 1.0 / (1.0 + math.exp(z))
        return round(calibrated, 3)

    def route_review(self, raw_score: float, threshold: float = 0.85) -> Dict[str, Any]:
        p = self.calibrate(raw_score)
        needs_human_review = p < threshold
        return {
            "raw_score": raw_score,
            "calibrated_confidence": p,
            "needs_human_review": needs_human_review,
            "routing_action": "CLINICIAN_REVIEW_QUEUE" if needs_human_review else "AUTO_ACCEPT"
        }
