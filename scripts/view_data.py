import pandas as pd
import os

def view_layers():
    # Define file paths for the Silver and Gold layers
    silver_path = "data/silver_sales.parquet"
    gold_path = "data/gold_layer/sales_summary.parquet"

    print("--- 🥈 Silver Layer: Cleaned Data Overview ---")
    if os.path.exists(silver_path):
        # Load Silver Layer data for verification
        df_silver = pd.read_parquet(silver_path)
        print(f"Schema (Columns): {df_silver.columns.tolist()}")
        print(df_silver.head(10))  # Previewing the first 10 records
    else:
        print("Alert: Silver Layer Parquet file not found. Ensure the transformation script has run successfully.")

    print("\n" + "="*60 + "\n")

    print("---  Gold Layer: Aggregated Business Insights ---")
    if os.path.exists(gold_path):
        # Load Gold Layer data for business logic verification
        df_gold = pd.read_parquet(gold_path)
        print(df_gold)
    else:
        print("Alert: Gold Layer Parquet file not found. Ensure the analytical aggregation script has run successfully.")

if __name__ == "__main__":
    view_layers()