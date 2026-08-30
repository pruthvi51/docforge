"""
FHIR R4 and OMOP CDM Resource Serializers:
Converts extracted clinical entities into HL7 FHIR R4 JSON resources and OMOP table rows.
"""
from typing import Dict, Any

def to_fhir_condition(patient_id: str, code: str, display: str) -> Dict[str, Any]:
    return {
        "resourceType": "Condition",
        "subject": {"reference": f"Patient/{patient_id}"},
        "code": {
            "coding": [{
                "system": "http://hl7.org/fhir/sid/icd-10-cm",
                "code": code,
                "display": display
            }]
        },
        "verificationStatus": {
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                "code": "confirmed"
            }]
        }
    }

def to_fhir_observation(patient_id: str, code: str, value: float, unit: str) -> Dict[str, Any]:
    return {
        "resourceType": "Observation",
        "subject": {"reference": f"Patient/{patient_id}"},
        "code": {
            "coding": [{
                "system": "http://loinc.org",
                "code": code
            }]
        },
        "valueQuantity": {
            "value": value,
            "unit": unit
        }
    }

def to_omop_condition_occurrence(person_id: int, concept_id: int, start_date: str) -> Dict[str, Any]:
    return {
        "condition_occurrence_id": 1,
        "person_id": person_id,
        "condition_concept_id": concept_id,
        "condition_start_date": start_date,
        "condition_type_concept_id": 32020 # EHR Chief Complaint
    }
