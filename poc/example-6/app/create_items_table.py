import psycopg2

# Database connection details
host = "your_host"
port = "your_port"
database = "your_database"
user = "your_username"
password = "your_password"

def create_items_table():
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # SQL command to create the "items" table
    create_table_query = """
        CREATE TABLE items (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            price NUMERIC(10, 2)
        )
    """

    try:
        # Execute the SQL command to create the table
        cursor.execute(create_table_query)

        # Commit the changes to the database
        connection.commit()

        print("Table 'items' created successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        # Rollback the transaction in case of any error
        connection.rollback()
        print("Error creating table:", error)
    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_items_table()
