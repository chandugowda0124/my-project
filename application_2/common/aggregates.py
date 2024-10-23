import psycopg2

def get_hourly_avg_temp():
    """Calculate the hourly average temperature."""
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname="weather_db", 
            user="your_user", 
            password="your_password", 
            host="localhost"
        )
        cursor = conn.cursor()

        # Query to calculate the hourly average temperature
        query = """
        SELECT AVG(temperature) 
        FROM weather_data 
        WHERE timestamp >= extract(epoch FROM (now() - interval '1 hour'));
        """
        cursor.execute(query)
        avg_temp = cursor.fetchone()[0]
        print(f"Hourly Average Temperature: {avg_temp:.2f}°C")
        return avg_temp

    except Exception as e:
        print(f"Error fetching hourly average temperature: {e}")
    
    finally:
        cursor.close()
        conn.close()

def get_max_temp_last_24_hours():
    """Get the maximum temperature in the last 24 hours."""
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname="weather_db", 
            user="your_user", 
            password="your_password", 
            host="localhost"
        )
        cursor = conn.cursor()

        # Query to get the max temperature in the last 24 hours
        query = """
        SELECT MAX(temperature) 
        FROM weather_data 
        WHERE timestamp >= extract(epoch FROM (now() - interval '24 hours'));
        """
        cursor.execute(query)
        max_temp = cursor.fetchone()[0]
        print(f"Max Temperature in Last 24 Hours: {max_temp:.2f}°C")
        return max_temp

    except Exception as e:
        print(f"Error fetching max temperature: {e}")
    
    finally:
        cursor.close()
        conn.close()

def get_most_frequent_condition():
    """Get the most frequent weather condition in the last 24 hours."""
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname="weather_db", 
            user="your_user", 
            password="your_password", 
            host="localhost"
        )
        cursor = conn.cursor()

        # Query to get the most frequent weather condition
        query = """
        SELECT main_condition, COUNT(*) AS frequency 
        FROM weather_data 
        WHERE timestamp >= extract(epoch FROM (now() - interval '24 hours'))
        GROUP BY main_condition 
        ORDER BY frequency DESC 
        LIMIT 1;
        """
        cursor.execute(query)
        frequent_condition = cursor.fetchone()[0]
        print(f"Most Frequent Condition in Last 24 Hours: {frequent_condition}")
        return frequent_condition

    except Exception as e:
        print(f"Error fetching most frequent condition: {e}")
    
    finally:
        cursor.close()
        conn.close()
