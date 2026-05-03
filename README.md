# 🌊 Cloud-Native Data Lakehouse Pipeline
### *End-to-End Medallion Architecture with MinIO, Pandas, and DuckDB*

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS_S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black" />
</div>

---

## 📌 Overview
This project implements a robust **Cloud-Native Data Lakehouse** using the **Medallion Architecture**. It automates the process of raw data ingestion into S3-compatible storage (MinIO), followed by systematic cleaning and high-performance analytical aggregation.

## 🏗️ System Architecture
The data flows through three distinct layers to ensure high quality and reliability:

<p align="center">
  <img src="screenshots/architecture.png" width="900" alt="Architecture Diagram">
</p>

- **Bronze Layer:** Raw data ingestion from local sources to immutable S3 storage.
- **Silver Layer:** Schema enforcement, header cleaning, and Parquet optimization.
- **Gold Layer:** Business-ready KPIs and aggregations for reporting.

---

## 🛠️ Implementation Details

### **1. Data Ingestion (Bronze)**
- **Tool:** `Boto3` (AWS SDK for Python)
- **Action:** Seamlessly uploads local CSV datasets to the MinIO raw bucket.

### **2. Transformation & Refinement (Silver)**
- **Tool:** `Pandas`
- **Action:** Handles missing values, cleans column headers, and converts data into **Parquet** format to optimize storage and query performance.

### **3. Advanced Analytics (Gold)**
- **Tool:** `DuckDB`
- **Action:** Executes complex SQL-based aggregations to generate metrics like Total Revenue and Order counts per Region.

---

## 🚀 Execution & Visuals

### **Pipeline Performance**
To run the entire automated pipeline:
```bash
python main.py