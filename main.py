import subprocess
import sys
import os

def run_pipeline():
    print("🚀 Initializing Cloud-Native Lakehouse Pipeline...")
    
    # Retrieve the current Python interpreter path to ensure Virtual Environment consistency
    python_exe = sys.executable

    try:
        # Phase 2: Data Ingestion (Raw to Bronze)
        print("\n--- Phase 2: Ingesting Data to Bronze Layer ---")
        subprocess.run([python_exe, "scripts/ingest_to_bronze.py"], check=True)
        
        # Phase 3: Data Transformation (Bronze to Silver)
        print("\n--- Phase 3: Transforming Data to Silver Layer ---")
        subprocess.run([python_exe, "scripts/transform_to_silver.py"], check=True)
        
        # Phase 4: Data Aggregation & Analytics (Silver to Gold)
        print("\n--- Phase 4: Creating Gold Layer Analytical Views ---")
        subprocess.run([python_exe, "scripts/transform_to_gold.py"], check=True)
        
        print("\n✅ End-to-End Pipeline execution completed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Pipeline execution failed at a critical stage. Error Details: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()