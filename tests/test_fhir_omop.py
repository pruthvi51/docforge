from docforge.converters.fhir_omop import to_fhir_condition, to_fhir_observation, to_omop_condition_occurrence

def test_fhir_condition_resource():
    res = to_fhir_condition("p-001", "E11.9", "Type 2 Diabetes")
    assert res["resourceType"] == "Condition"
    assert res["subject"]["reference"] == "Patient/p-001"
    assert res["code"]["coding"][0]["code"] == "E11.9"

def test_omop_condition_occurrence():
    res = to_omop_condition_occurrence(person_id=101, concept_id=201826, start_date="2024-01-15")
    assert res["person_id"] == 101
    assert res["condition_concept_id"] == 201826
