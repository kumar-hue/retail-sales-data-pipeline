# Retail Sales Data Pipeline

## Project Overview

This project focuses on processing and analyzing retail sales data using Python, SQL, PySpark, and Databricks.

The BigMart Sales dataset was used to perform data cleaning, transformation, exploratory data analysis, and business-oriented sales analysis.

## Objectives

- Clean and validate retail sales data.
- Handle missing values and standardize categorical data.
- Perform exploratory data analysis using SQL.
- Process and transform data using PySpark.
- Analyze sales across products, outlets, and locations.
- Generate business-oriented insights from the dataset.

## Technologies Used

- Python
- SQL
- PySpark
- Databricks

## Dataset

The project uses the BigMart Sales dataset containing information about:

- Products
- Item types
- Item weight
- Item visibility
- Item MRP
- Outlet information
- Outlet size
- Outlet location
- Outlet type
- Item outlet sales

## Project Workflow

```text
Raw Dataset
     ↓
Data Loading
     ↓
Data Cleaning
     ↓
Data Validation
     ↓
SQL Exploratory Data Analysis
     ↓
PySpark Transformations
     ↓
PySpark Aggregations
     ↓
PySpark Joins
     ↓
Window Functions & Ranking
     ↓
Final Business Analysis


## Data Cleaning

The following cleaning operations were performed:

* Standardized `Item_Fat_Content` values.
* Filled missing `Item_Weight` values using the average item weight.
* Filled missing `Outlet_Size` values with `Unknown`.
* Checked for duplicate records.
* Verified the cleaned dataset.

The cleaned data was stored as:

`workspace.default.bigmart_sales_cleaned`

## SQL Analysis

SQL was used for:

* Data exploration
* Aggregations
* Sales analysis
* Grouping by item and outlet attributes
* Identifying top and low-selling products
* Analyzing sales by outlet type, size, and location
* Generating overall dataset summaries

## PySpark Analysis

PySpark DataFrames were used for:

* Selecting required columns
* Filtering records
* Creating new columns using `withColumn()`
* Applying conditional logic using `when()` and `otherwise()`
* Grouping and aggregating data
* Sorting results
* Joining DataFrames
* Applying Window Functions
* Ranking products by sales
* Identifying top 3 products within each item type
The PySpark notebooks used for the analysis are available in the `notebooks/` folder.

## Project Structure

RetailSalesProject/
│
├── data/
│
├── sql/
│   ├── day1_queries.sql
│   ├── day2_queries.sql
│   ├── day3_queries.sql
│   ├── day4_queries.sql
│   └── day5_queries.sql
│
├── screenshots/
│
├── documentation/
│   ├── day1_notes.md
│   ├── day2_notes.md
│   ├── day3_notes.md
│   ├── day4_notes.md
│   ├── day5_notes.md
│   ├── day6_notes.md
│   ├── day7_notes.md
│   ├── day8_notes.md
│   ├── day9_notes.md
│   ├── day10_notes.md
│   ├── day11_notes.md
│   ├── day12_notes.md
│   └── day13_notes.md
│
├── notebooks/
│   ├── day6_pyspark_basics.py
│   ├── day7_pyspark_transformations.py
│   ├── day8_pyspark_aggregations.py
│   ├── day9_pyspark_joins.py
│   ├── day10_pyspark_advanced.py
│   ├── day11_pyspark_window_functions.py
│   ├── day12_pyspark_ranking.py
│   └── day13_final_analysis.py
│
├── output/
│
└── README.md


## Key PySpark Concepts

The project includes practical use of:

* `select()`
* `filter()`
* `withColumn()`
* `when()`
* `otherwise()`
* `groupBy()`
* `agg()`
* `count()`
* `sum()`
* `avg()`
* `orderBy()`
* `join()`
* Window Functions
* `row_number()`
* `rank()`
* `dense_rank()`

## Final Analysis

The final analysis examined:

* Overall sales performance
* Sales by outlet type
* Sales by item type
* Sales by outlet location
* Top-selling products
* Sales by item type and outlet type
* Product rankings within item categories

## Learning Outcomes

Through this project, I gained practical experience in:

* SQL-based data analysis
* Data cleaning and validation
* PySpark DataFrame operations
* Data transformation and aggregation
* Joining datasets
* Window Functions and ranking
* Working with Databricks
* Performing business-oriented analysis




