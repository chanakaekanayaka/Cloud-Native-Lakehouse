import pandas as pd
import os
import boto3
from botocore.client import Config

def transform_to_silver():
    try:
        # 1. Load raw data from the local CSV source
        df = pd.read_csv("data/sales_data.csv")
        
        # 2. Clean column headers by removing leading/trailing whitespaces to ensure schema consistency
        df.columns = [c.strip() for c in df.columns]
        
        print(f"✅ Schema Cleaned. Verified Columns: {df.columns.tolist()}")

        # 3. Persist the cleaned data locally in Parquet format (optimized for analytical workloads)
        os.makedirs("data/silver_sales", exist_ok=True)
        silver_file = "data/silver_sales.parquet"
        df.to_parquet(silver_file)

        # 4. Synchronize the local Parquet file with the MinIO Silver Bucket
        s3 = boto3.resource('s3',
                            endpoint_url="http://localhost:9000",
                            aws_access_key_id="admin",
                            aws_secret_access_key="password123",
                            config=Config(signature_version='s3v4'),
                            region_name='us-east-1')
        s3.Bucket("silver").upload_file(silver_file, "sales_cleaned.parquet")
        
        print("✅ Silver Layer Transformation Successful!")

    except Exception as e:
        print(f"❌ Silver Layer Processing Error: {e}")

if __name__ == "__main__":
    transform_to_silver()