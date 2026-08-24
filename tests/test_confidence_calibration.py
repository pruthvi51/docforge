from docforge.confidence.calibration import PlattCalibrator

def test_platt_calibration_high_confidence():
    cal = PlattCalibrator()
    res = cal.route_review(0.98, threshold=0.85)
    assert res["calibrated_confidence"] >= 0.85
    assert res["needs_human_review"] is False
    assert res["routing_action"] == "AUTO_ACCEPT"

def test_platt_calibration_low_confidence_routes_hitl():
    cal = PlattCalibrator()
    res = cal.route_review(0.40, threshold=0.85)
    assert res["calibrated_confidence"] < 0.85
    assert res["needs_human_review"] is True
    assert res["routing_action"] == "CLINICIAN_REVIEW_QUEUE"
