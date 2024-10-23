def test_alerting_thresholds():
    check_thresholds("Delhi", 36, "Clear", temp_threshold=35)
    print("Alerting thresholds test passed")
