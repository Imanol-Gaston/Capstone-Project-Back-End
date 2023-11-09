import os
import psycopg2

conn = psycopg2.connect(
    host="localhost", 
    database="sitework", 
    user="postgres", 
    password="12341234"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# # Execute a command: this creates a new table
# cur.execute("DROP TABLE IF EXISTS users")
# cur.execute(
#     "CREATE TABLE users (id serial PRIMARY KEY,"
#     "email varchar (50) NOT NULL,"
#     "password varchar (50) NOT NULL,"
#     "type varchar (50) NOT NULL,"
#     "created_at date DEFAULT CURRENT_TIMESTAMP);"
# )


# Insert data into the table

cur.execute(
    "SELECT * from inspectors"
)

registro=cur.fetchall()
print(registro)


conn.commit()

cur.close()
conn.close()
