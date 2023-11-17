def display(cur):
    # Fetch all the rows from the query result
    select_data_sql = "SELECT * FROM PhoneBook;"
    cur.execute(select_data_sql)
    rows = cur.fetchall()

    # Display the retrieved data
    if not rows:
        print("Rubrica vuota.\n")
    else:
        for row in rows:
            print("PersonID:", row[0])
            print("Nome:", row[1])
            print("Numero:", row[2])
            print("Mail:", row[3])
            print()

def insert(cur):
    while True:
        #Select input
        name = input("Nome: ")
        phone = input("Numero:" )
        mail = input("Mail: ")
        print(f"Nome: {name}, numero:: {phone}, mail: {mail}.")
        value = input("Info corrette? (Y/N): ").strip().lower()
        # Check for valid input
        if value in ("y", "yes"):  
            break

    # Define the SQL query with placeholders for parameters
    insert_data_sql = """
    INSERT INTO PhoneBook (Nome, Numero, Mail)
    VALUES (?, ?, ?)
    """
    # Execute the SQL query with parameter values
    cur.execute(insert_data_sql, (name, phone, mail))
    
    # Commit the transaction to save the changes to the database
    cur.connection.commit()
    print("Dati salvati con successo!\n")

def delete(cur):
    #Check if there something to delete
    select_data_sql = "SELECT * FROM PhoneBook;"
    cur.execute(select_data_sql)
    check = cur.fetchall()
    if not check:
        print("Nessun dato da cancellare.\n")
    
    #Else, proceed with deletion
    else: 
        while True:
            del_ID = input("Seleziona il PersonID da cancellare (numero intero): ")
        
            # Check if the input can be converted to an integer
            try:
                del_ID = int(del_ID)
            except ValueError:
                print("Serve un numero intero!")
                continue

            # Execute a SELECT query to check if the specified PersonID exists
            select_data_sql = "SELECT * FROM PhoneBook WHERE PersonID = ?;"
            cur.execute(select_data_sql, (del_ID,))
        
            # Fetch the row with the specified PersonID
            row = cur.fetchone()
        
            if row is None:
                print("Nessun record con il PersonID specificato.")
            else:
                print("Ecco il record che desideri eliminare:")
                print("PersonID:", row[0])
                print("Nome:", row[1])
                print("Numero:", row[2])
                print("Mail:", row[3])

                # Ask the user for confirmation
                confirmation = input("Vuoi davvero cancellare questo record? (Y/N): ").strip().lower()
                if confirmation in ("y","yes"):
                    # Execute the DELETE query to remove the specified record
                    delete_data_sql = "DELETE FROM PhoneBook WHERE PersonID = ?;"
                    cur.execute(delete_data_sql, (del_ID,))
                    cur.connection.commit()
                    print("Dati cancellati.\n")
                else:
                    print("Cancellazione annullata.\n")
        
                break  # Exit the loop after processing the input