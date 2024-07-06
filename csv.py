import pandas as pd
import numpy as np
import os

# Define number of records and columns
num_records = 100000
num_columns = 30

# Generate random data
data = np.random.rand(num_records, num_columns)

# Create a DataFrame
columns = [f"col{i+1}" for i in range(num_columns)]
df = pd.DataFrame(data, columns=columns)

# Define CSV file path (relative path)
csv_file_path = 'dummy_data.csv'

# Save to CSV
df.to_csv(csv_file_path, index=False)

# Get the absolute path of the CSV file
absolute_csv_file_path = os.path.abspath(csv_file_path)
print(f"CSV file with {num_records} records and {num_columns} columns created at {absolute_csv_file_path}")
