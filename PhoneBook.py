import sqlite3
from methods import *

# Create a connection to the SQLite database (or create a new one)
conn = sqlite3.connect("phonebook.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL statement to create the "PhoneBook" table
create_table_sql = """
CREATE TABLE IF NOT EXISTS PhoneBook (
    PersonID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nome NVARCHAR(50) NOT NULL,
    Numero NVARCHAR(50) NOT NULL,
    Mail NVARCHAR(50) NOT NULL
);
"""
# Execute the SQL statement to create the table
cursor.execute(create_table_sql)

while True:
#User interaction
    value = input("cosa vuoi fare? (Display / Inserisci / Cancella / Esci): ")
    if value.lower() == "display":
        display(cursor)
    elif value.lower() == "inserisci":
        insert(cursor)
    elif value.lower() == "cancella":
        delete(cursor)
    elif value.lower() == "esci":
        break
    else:
        print("Errore. Forse hai sbagliato a digitare?\n")
    
# Close the database connection
conn.close()
