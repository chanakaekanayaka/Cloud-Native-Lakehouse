import boto3
from botocore.client import Config
import os

# MinIO Connection Configuration
MINIO_URL = "http://localhost:9000"
ACCESS_KEY = "admin"
SECRET_KEY = "password123"
BUCKET_NAME = "bronze"

def upload_raw_data():
    # Initialize MinIO (S3) resource client
    s3 = boto3.resource('s3',
                        endpoint_url=MINIO_URL,
                        aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY,
                        config=Config(signature_version='s3v4'),
                        region_name='us-east-1')

    # Define the local file path
    local_file = os.path.join("data", "sales_data.csv")
    
    # Define the destination object name in MinIO
    s3_object_name = "sales_raw.csv"

    try:
        print(f"🚀 Uploading data to '{BUCKET_NAME}' bucket...")
        
        # Execute the file upload to the specified bucket
        s3.Bucket(BUCKET_NAME).upload_file(local_file, s3_object_name)
        
        print(f"✅ Success! '{s3_object_name}' is now available in the Bronze Layer.")
    except Exception as e:
        print(f"❌ An error occurred during ingestion: {e}")

if __name__ == "__main__":
    upload_raw_data()