import duckdb
import pandas as pd
import boto3
from botocore.client import Config
import os

# 1. MinIO Connection Configuration
MINIO_URL = "http://localhost:9000"
ACCESS_KEY = "admin"
SECRET_KEY = "password123"
GOLD_BUCKET = "gold"

def create_gold_analytics():
    try:
        # Define the source path for the Silver Layer Parquet file
        silver_path = "data/silver_sales.parquet"
        
        print("📊 Starting Gold Layer Transformation and Aggregation...")

        # 2. DuckDB SQL Query - Aggregate Sales and Order metrics
        # Note: Identifiers with spaces (e.g., "Order ID") must be enclosed in double quotes.
        query = f"""
            SELECT 
                Region, 
                Category,
                SUM(CAST(Sales AS DOUBLE)) as Total_Revenue,
                COUNT(DISTINCT "Order ID") as Total_Orders,
                COUNT(*) as Total_Items_Sold
            FROM read_parquet('{silver_path}')
            GROUP BY Region, Category
            ORDER BY Total_Revenue DESC
        """
        
        # Execute the analytical query and convert the result set to a Pandas DataFrame
        gold_df = duckdb.query(query).to_df()

        # 3. Persist the aggregated Gold Layer data locally
        os.makedirs("data/gold_layer", exist_ok=True)
        local_gold_file = "data/gold_layer/sales_summary.parquet"
        gold_df.to_parquet(local_gold_file)

        # 4. Upload Business Insights to the MinIO 'gold' bucket
        print(f"🚀 Uploading Business Insights to MinIO '{GOLD_BUCKET}' bucket...")
        s3 = boto3.resource('s3',
                            endpoint_url=MINIO_URL,
                            aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_KEY,
                            config=Config(signature_version='s3v4'),
                            region_name='us-east-1')
        
        s3.Bucket(GOLD_BUCKET).upload_file(local_gold_file, "sales_summary.parquet")

        print("✅ Gold Layer Success! Business analytical reports are finalized.")
        print("\n--- Sales Summary Preview ---")
        print(gold_df.head()) 

    except Exception as e:
        print(f"❌ Gold Layer Error: {e}")

if __name__ == "__main__":
    create_gold_analytics()