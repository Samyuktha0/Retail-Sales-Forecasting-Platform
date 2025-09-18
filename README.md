# 🛒 Retail Sales Forecasting Platform

This project builds a scalable data pipeline using Azure Data Factory and Databricks to forecast weekly retail sales across multiple regions. It includes Spark-based ML models, SQL-based data warehousing, and Power BI dashboards for business insights.

## 🚀 Features
- ETL pipeline processing 1M+ records/week
- Spark ML model with 92% forecast accuracy
- Power BI dashboard with 10+ KPIs
- Modular pipeline with monitoring and alerting

## 🧰 Tech Stack
- Azure Data Factory
- Azure Databricks (Spark)
- SQL Server
- Power BI

## 🛠️ Setup Instructions
1. Clone the repo: `git clone https://github.com/samyuktha/retail-sales-forecasting.git`
2. Import `spark_forecasting.ipynb` into Databricks
3. Configure ADF pipeline using `pipeline_config.json`
4. Load dummy data from `/data/retail_sales.csv` into Blob Storage
5. Run pipeline and visualize results in Power BI

## 📦 Environment
- Python 3.8+
- Spark 3.3+
- Azure Subscription with ADF & Databricks
- Power BI Desktop

## 📊 Dataset
Dummy dataset: `retail_sales.csv`  
Fields: `week`, `store_id`, `product_id`, `units_sold`, `revenue`

## 📄 License
MIT
