from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"Hello": "FastAPI with PostgreSQL"}

@app.post("/items/")
def create_item(item: Item):
    connection = psycopg2.connect(
        host="postgres-service",
        port="5432",
        database="your_database_name",
        user="your_username",
        password="your_password",
    )

    cursor = connection.cursor()

    query = "INSERT INTO items (name, price) VALUES (%s, %s);"
    values = (item.name, item.price)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Item created successfully"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    connection = psycopg2.connect(
        host="postgres-service",
        port="5432",
        database="your_database_name",
        user="your_username",
        password="your_password",
    )

    cursor = connection.cursor()

    query = "SELECT * FROM items WHERE id = %s;"
    values = (item_id,)

    cursor.execute(query, values)

    item = cursor.fetchone()

    cursor.close()
    connection.close()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item_dict = {
        "id": item[0],
        "name": item[1],
        "price": item[2]
    }

    return item_dict

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    connection = psycopg2.connect(
        host="postgres-service",
        port="5432",
        database="your_database_name",
        user="your_username",
        password="your_password",
    )

    cursor = connection.cursor()

    query = "UPDATE items SET name = %s, price = %s WHERE id = %s;"
    values = (item.name, item.price, item_id)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Item updated successfully"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    connection = psycopg2.connect(
        host="postgres-service",
        port="5432",
        database="your_database_name",
        user="your_username",
        password="your_password",
    )

    cursor = connection.cursor()

    query = "DELETE FROM items WHERE id = %s;"
    values = (item_id,)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Item deleted successfully"}




@app.get("/create-item-table")
def create_item_table():
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host="postgres-service",
        port="5432",
        database="your_database_name",
        user="your_username",
        password="your_password",
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

        return {"message": "Table 'items' created successfully!"}
    except (Exception, psycopg2.DatabaseError) as error:
        # Rollback the transaction in case of any error
        connection.rollback()
        return {"message": f"Error creating table: {error}"}
    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()


@app.get("/items")
def get_all_items():
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host="postgres-service",
        port="5432",
        database="your_database_name",
        user="your_username",
        password="your_password",
    )
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # SQL command to retrieve all items
    select_query = "SELECT * FROM items;"

    # Execute the SQL command
    cursor.execute(select_query)

    # Fetch all rows from the result set
    items = cursor.fetchall()

    # Transform the items into a list of dictionaries
    items_list = []
    for item in items:
        item_dict = {
            "id": item[0],
            "name": item[1],
            "price": item[2]
        }
        items_list.append(item_dict)

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    return {"items": items_list}