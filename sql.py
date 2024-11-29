import mysql.connector
from mysql.connector import Error

def update_data_in_table(host, user, password, database, table_name, column_name, new_value, condition):
    try:
        # Establish a database connection
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # SQL query to update data
            sql_query = f"UPDATE {table_name} SET {column_name} = %s WHERE {condition}"
            cursor.execute(sql_query, (new_value,))
            
            # Commit changes
            connection.commit()
            
            print(f"Rows affected: {cursor.rowcount}")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = ""
    database = "test_db"
    table_name = "employees"
    column_name = "salary"
    new_value = 5000
    condition = "id = 5"  

    update_data_in_table(host, user, password, database, table_name, column_name, new_value, condition)
