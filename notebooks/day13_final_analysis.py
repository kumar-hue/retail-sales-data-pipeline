# Databricks notebook source
from pyspark.sql.functions import sum, avg, count, round

df = spark.table("workspace.default.bigmart_sales_cleaned")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Overall business summary

# COMMAND ----------

df.agg(
    count("*").alias("Total_Records"),
    count("Item_Type").alias("Total_Products"),
    round(sum("Item_Outlet_Sales"), 2).alias("Total_Sales"),
    round(avg("Item_Outlet_Sales"), 2).alias("Average_Sales")
).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sales by outlet type

# COMMAND ----------

outlet_analysis = (
    df.groupBy("Outlet_Type")
      .agg(
          count("*").alias("Product_Count"),
          round(sum("Item_Outlet_Sales"), 2).alias("Total_Sales"),
          round(avg("Item_Outlet_Sales"), 2).alias("Average_Sales")
      )
      .orderBy("Total_Sales", ascending=False)
)

outlet_analysis.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sales by item type

# COMMAND ----------

item_analysis = (
    df.groupBy("Item_Type")
      .agg(
          count("*").alias("Product_Count"),
          round(sum("Item_Outlet_Sales"), 2).alias("Total_Sales"),
          round(avg("Item_Outlet_Sales"), 2).alias("Average_Sales")
      )
      .orderBy("Total_Sales", ascending=False)
)

item_analysis.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sales By Outlet  Location

# COMMAND ----------

location_analysis = (
    df.groupBy("Outlet_Location_Type")
      .agg(
          count("*").alias("Product_Count"),
          round(sum("Item_Outlet_Sales"), 2).alias("Total_Sales"),
          round(avg("Item_Outlet_Sales"), 2).alias("Average_Sales")
      )
      .orderBy("Total_Sales", ascending=False)
)

location_analysis.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Top 10 products

# COMMAND ----------

top_products = (
    df.select(
        "Item_Identifier",
        "Item_Type",
        "Item_Outlet_Sales",
        "Outlet_Identifier"
    )
    .orderBy(
        "Item_Outlet_Sales",
        ascending=False
    )
)

top_products.show(10)

# COMMAND ----------

# MAGIC %md
# MAGIC ### How do item categories perform across different outlet types?

# COMMAND ----------

final_analysis = (
    df.groupBy("Item_Type", "Outlet_Type")
      .agg(
          count("*").alias("Product_Count"),
          round(sum("Item_Outlet_Sales"), 2).alias("Total_Sales"),
          round(avg("Item_Outlet_Sales"), 2).alias("Average_Sales")
      )
      .orderBy("Total_Sales", ascending=False)
)

final_analysis.show(20)