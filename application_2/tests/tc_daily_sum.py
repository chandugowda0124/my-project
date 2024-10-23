def test_daily_summary():
    calculate_daily_summary()
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM daily_summary')
    summary = cursor.fetchall()
    assert len(summary) > 0, "Daily summary should have entries"
    print("Daily summary test passed")
