import pandas as pd
import numpy as np

# Generate dummy data
num_records = 100000
data = {
    'column1': np.random.randint(0, 100, size=num_records)
}

# Add 29 more columns with random string data
for i in range(2, 31):
    column_name = f'column{i}'
    data[column_name] = np.random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], size=num_records)

df = pd.DataFrame(data)

# Save to Excel
excel_file = 'excel_data.xlsx'
df.to_excel(excel_file, index=False)

print(f"Successfully generated {num_records} records with 30 columns and saved to {excel_file}.")
