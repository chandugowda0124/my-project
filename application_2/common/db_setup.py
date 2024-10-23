import psycopg2

def store_weather_data(main_condition, temperature, feels_like, timestamp):
    """Store weather data in PostgreSQL."""
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname="weather_db", 
            user="your_user", 
            password="your_password", 
            host="localhost"
        )
        cursor = conn.cursor()

        # SQL query to insert weather data
        insert_query = """
        INSERT INTO weather_data (main_condition, temperature, feels_like, timestamp)
        VALUES (%s, %s, %s, %s);
        """
        cursor.execute(insert_query, (main_condition, temperature, feels_like, timestamp))
        
        # Commit the transaction
        conn.commit()

    except Exception as e:
        print(f"Error inserting data: {e}")
    
    finally:
        cursor.close()
        conn.close()
