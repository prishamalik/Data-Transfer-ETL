import pyodbc

connection_string = (
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-BF8PELR\SQLEXPRESS;'
     'DATABASE-dummy;'
     'TRUSTED_CONNECTION-yes;'
    
)


conn = pyodbc.connect(connection_string)
cursor = conn.cursor()
cursor.execute('use dummy')

columns = [f"Column{i} VARCHAR(50)" if i > 1 else "Column1 INT" for i in range(1, 31)]

# SQL query to create table
create_table_query = f"""
CREATE TABLE YourTable (
    {", ".join(columns)}
);
"""

# Execute the query and commit
cursor.execute(create_table_query)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Table created successfully!")

