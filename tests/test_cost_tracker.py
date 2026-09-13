from docforge.manifest.cost_tracker import InferenceCostTracker
from docforge.eval.run_benchmark import run_benchmark

def test_cost_calculation():
    tracker = InferenceCostTracker()
    m = tracker.generate_manifest("doc-123", pages=5, prompt_tokens=2000, completion_tokens=500)
    assert m["document_id"] == "doc-123"
    assert m["estimated_cost_usd"] > 0
    assert m["cost_per_page_usd"] < 0.01

def test_benchmark_metrics():
    res = run_benchmark()
    assert res["f1_score_pct"] == 91.4
    assert res["human_review_reduction_pct"] > 70.0
