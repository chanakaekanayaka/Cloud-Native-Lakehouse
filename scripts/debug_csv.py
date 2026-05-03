import pandas as pd

file_path = "data/sales_data.csv"

# 1. Inspecting raw file content to check for delimiters and encoding
print("--- 1. Raw File Preview (First 5 Rows) ---")
with open(file_path, 'r') as f:
    for i in range(5):
        print(f.readline().strip())

# 2. Verifying how Pandas interprets the headers
print("\n--- 2. Detected Column Names (via Pandas) ---")
df = pd.read_csv(file_path, nrows=5)
print(df.columns.tolist())

# 3. Quick data profile inspection
print("\n--- 3. Data Inspection (DataFrame Head) ---")
print(df.head())