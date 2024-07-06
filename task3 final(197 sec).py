import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import configparser
import logging
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Extract connection details from the configuration file
driver = config.get('database', 'driver')
server = config.get('database', 'server')
database = config.get('database', 'database')
trusted_connection = config.get('database', 'trusted_connection')

source_username = config.get('source_database', 'username')
source_password = config.get('source_database', 'password')
source_server = config.get('source_database', 'server')
source_database = config.get('source_database', 'database')

destination_username = config.get('destination_database', 'username')
destination_password = config.get('destination_database', 'password')
destination_server = config.get('destination_database', 'server')
destination_database = config.get('destination_database', 'database')

# Create the connection string for initial connection
conn_str = (
    f'DRIVER={{{driver}}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection={trusted_connection};'
)

# Establish initial connection
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


# Close initial connection
cursor.close()
conn.close()

# Define connection strings for SQLAlchemy
source_conn_str = f"mssql+pyodbc://{source_username}:{source_password}@{source_server}/{source_database}?driver=ODBC+Driver+17+for+SQL+Server"
dest_conn_str = f"mssql+pyodbc://{destination_username}:{destination_password}@{destination_server}/{destination_database}?driver=ODBC+Driver+17+for+SQL+Server"

# Create SQLAlchemy engines
source_engine = create_engine(source_conn_str)
dest_engine = create_engine(dest_conn_str)

def fetch_data():
    query = "SELECT * FROM YourTable"
    df = pd.read_sql(query, source_engine)
    logging.info("Data fetched successfully from the source database.")
    return df

def transform_data(df):
    df = df.applymap(lambda x: str(x).upper())
    logging.info("Data transformed successfully.")
    return df

def load_data(df):
    df.to_sql('destination', dest_engine, if_exists='append', index=False)
    logging.info("Data loaded successfully into the destination database.")

def etl_process():
    start_time = time.time()
    df = fetch_data()
    df = transform_data(df)
    load_data(df)
    end_time = time.time()
    total_duration = end_time - start_time
    logging.info(f"ETL process completed successfully in {total_duration:.2f} seconds.")


if __name__ == "__main__":
    etl_process()


