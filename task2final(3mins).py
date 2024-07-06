import pyodbc
import random
import string
import datetime
import configparser

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Extract connection details from the configuration file
driver = config.get('database', 'driver')
server = config.get('database', 'server')
database = config.get('database', 'database')
trusted_connection = config.get('database', 'trusted_connection')

# Create the connection string
conn_str = (
    f'DRIVER={{{driver}}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection={trusted_connection};'
)

# Extract settings from the configuration file
total_rows = config.getint('settings', 'total_rows')
batch_size = config.getint('settings', 'batch_size')

# Establish connection
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Function to generate random integer
def generate_random_integer():
    return random.randint(1, 1000000)  # Adjust range as needed

# Function to generate random string
def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Insert dummy data using bulk insert
insert_query = '''
INSERT INTO YourTable(Column1, Column2, Column3, Column4, Column5, Column6, Column7, Column8, Column9, Column10,
                       Column11, Column12, Column13, Column14, Column15, Column16, Column17, Column18, Column19, Column20,
                       Column21, Column22, Column23, Column24, Column25, Column26, Column27, Column28, Column29, Column30)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''


total_batches = total_rows // batch_size

start_time = datetime.datetime.now()
print(f"Data insertion started at: {start_time}")

for i in range(total_batches):
    data = [[generate_random_integer()] + [generate_random_string() for _ in range(29)] for _ in range(batch_size)]
    cursor.fast_executemany = True  # Enable fast executemany
    cursor.executemany(insert_query, data)
    conn.commit()
   
    if (i + 1) % 5 == 0:
        print(f"{(i + 1) * batch_size} rows inserted so far...")

# Print the timestamp after completing
end_time = datetime.datetime.now()
print(f"Data insertion completed at: {end_time}")

# Calculate and print the total duration
duration = end_time - start_time
print(f"Total duration: {duration}")

print(f"All {total_rows} rows inserted successfully.")


