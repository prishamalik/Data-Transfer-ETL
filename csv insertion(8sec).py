import pandas as pd
from sqlalchemy import create_engine
import time

# Database credentials and configuration
db_username = 'sa'
db_password = 'sasa'
db_server = 'DESKTOP-BF8PELR\\SQLEXPRESS'
db_database = 'dummy'

# Database URI
DATABASE_URI = f"mssql+pyodbc://{db_username}:{db_password}@{db_server}/{db_database}?driver=ODBC+Driver+17+for+SQL+Server"
start_time = time.time()
# Read data from Excel
csv_file = r'C:\Users\Prisha Malik\OneDrive\Desktop\intern\dummy_data.csv'
df_csv = pd.read_csv(csv_file)

# Create database engine
engine = create_engine(DATABASE_URI)

table_name_csv = 'csvtable'
df_csv.to_sql(table_name_csv, engine, if_exists='append', index=False)

end_time = time.time()

print(f"Successfully inserted records from {csv_file} into the {table_name_csv} table.")
print(f"Total execution time: {end_time - start_time} seconds")

