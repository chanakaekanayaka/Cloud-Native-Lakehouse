# Cloud-Native Data Lakehouse Pipeline
### End-to-End Medallion Architecture Implementation

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS_S3-569A31?style=flat-square&logo=amazons3&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black" />
</div>

---

## Project Overview
This repository showcases a professional implementation of a **Cloud-Native Data Lakehouse**. By leveraging the **Medallion Architecture**, the system automates the lifecycle of sales data—from raw ingestion into a containerized S3 environment to the generation of high-performance analytical insights. The project focuses on data integrity, schema evolution, and storage optimization using columnar formats.

## System Architecture
The pipeline is designed with a three-tier refinement strategy to ensure data reliability and accessibility:

<p align="center">
  <img src="screenshots/architecture.png" width="900" alt="System Architecture">
</p>

### The Medallion Standard
*   **Bronze Layer (Raw Storage):** Acts as the landing zone for immutable raw datasets. Data is ingested directly into MinIO S3 buckets without modification to preserve the original state.
*   **Silver Layer (Refined Data):** Focuses on data quality. This stage involves cleaning headers, enforcing data types, and converting files into **Apache Parquet** format for superior compression and query speed.
*   **Gold Layer (Analytical Insights):** The final stage where data is aggregated into business-ready KPIs and summaries, optimized for visualization and reporting.

---

## Technical Stack

| Category | Technology | Implementation |
| :--- | :--- | :--- |
| **Infrastructure** | **Docker** | Containerization of the MinIO S3 object storage environment. |
| **Object Storage** | **MinIO** | S3-compatible cloud-native storage for hosting Medallion tiers. |
| **Orchestration** | **Python** | Centralized control through `main.py` for automated ETL execution. |
| **Data Processing** | **Pandas** | Comprehensive data cleaning, transformation, and schema enforcement. |
| **OLAP Engine** | **DuckDB** | Lightning-fast SQL execution for complex analytical aggregations. |

---

## Directory Structure
```text
cloud-native-lakehouse/
├── data/                   # Local cache for raw and processed layers
│   ├── gold_layer/         # Final aggregated summaries
│   └── silver_sales/       # Refined Parquet datasets
├── docker/                 # Infrastructure as Code (docker-compose.yml)
├── scripts/                # Modular ETL components
│   ├── ingest_to_bronze.py
│   ├── transform_to_silver.py
│   ├── transform_to_gold.py
│   └── view_data.py        # Data validation and preview utility
└── main.py                 # Master pipeline orchestrator