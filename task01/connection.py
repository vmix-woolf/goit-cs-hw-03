import psycopg2

def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="task_manager",
            user="viacheslav",
            password="ghj123YUI"
        )
        return connection
    except Exception as e:
        print(f"Error connection to the database: {e}")
        return None
