"""
RapidFuzz Clinical Ontology Matcher:
Normalizes colloquial disease/medication strings into canonical ICD-10 and RxNorm terms.
"""
from typing import Any, Dict, Optional

from rapidfuzz import fuzz, process

CLINICAL_ONTOLOGY = {
    "type 2 diabetes": {"code": "E11.9", "type": "DIAGNOSIS"},
    "essential hypertension": {"code": "I10", "type": "DIAGNOSIS"},
    "asthma": {"code": "J45.909", "type": "DIAGNOSIS"},
    "metformin 500mg": {"code": "860975", "type": "MEDICATION"},
    "lisinopril 10mg": {"code": "316049", "type": "MEDICATION"},
    "blood pressure": {"code": "8480-6", "type": "VITAL_OBSERVATION"},
}

class OntologyMatcher:
    def __init__(self, cutoff_score: float = 75.0):
        self.cutoff_score = cutoff_score
        self.choices = list(CLINICAL_ONTOLOGY.keys())

    def match_entity(self, text: str) -> Optional[Dict[str, Any]]:
        match = process.extractOne(text.lower().strip(), self.choices, scorer=fuzz.token_sort_ratio)
        if match and match[1] >= self.cutoff_score:
            matched_term = match[0]
            info = CLINICAL_ONTOLOGY[matched_term]
            return {
                "matched_term": matched_term,
                "confidence": round(match[1] / 100.0, 3),
                "code": info["code"],
                "type": info["type"],
            }
        return None
