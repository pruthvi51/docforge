from docforge.extractors.ontology_matcher import OntologyMatcher

def test_exact_and_fuzzy_matches():
    matcher = OntologyMatcher()
    res1 = matcher.match_entity("Type 2 Diabetes")
    assert res1 is not None
    assert res1["code"] == "E11.9"
    assert res1["type"] == "DIAGNOSIS"

    # Fuzzy match with typo
    res2 = matcher.match_entity("hypertensn essential")
    assert res2 is not None
    assert res2["code"] == "I10"
