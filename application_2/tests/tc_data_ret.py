def test_data_retrieval():
    data = get_weather_data()
    assert len(data) == 6, "Should fetch weather data for 6 cities"
    print("Data retrieval test passed")
