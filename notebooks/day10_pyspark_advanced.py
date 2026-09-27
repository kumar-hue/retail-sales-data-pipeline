# Databricks notebook source
from pyspark.sql.functions import avg,sum,round,when,count
df=spark.table("workspace.default.bigmart_sales_cleaned")

# COMMAND ----------

# MAGIC %md
# MAGIC ### creates a sales category
# MAGIC classify each product based on its sales.

# COMMAND ----------

# MAGIC %md
# MAGIC ### df      → original cleaned data
# MAGIC ###df_sales → original data + Sales_Category

# COMMAND ----------

df_sales=df.withColumn(
    "Sales_Category",
    when(df.Item_Outlet_Sales>=3000,"Very High")
    .when(df.Item_outlet_sales>=2000,"High")
    .when(df.Item_outlet_sales>=1000,"Medium")
    .otherwise("Low")
)
df_sales.select(
    "Item_Identifier",
    "Item_Outlet_Sales",
    "Sales_Category"
).show(10)

# COMMAND ----------

# MAGIC %md
# MAGIC ### count products in each category

# COMMAND ----------

product_count=(
    df_sales.groupBy("Sales_Category")
    .count()
    .orderBy("count",ascending=False)
)
product_count.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Average sales by category

# COMMAND ----------

cat_avgsales=(
    df_sales.groupBy("Sales_Category")
    .agg(
        round(avg("Item_Outlet_Sales"),2).alias("Average_Sales")
    )
    .orderBy("Average_Sales",ascending=False)

)
cat_avgsales.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sales analysis by item type

# COMMAND ----------

df.groupBy("Item_Type") \
    .agg(
        count("*").alias("Product_Count"),
        round(sum("Item_Outlet_Sales"), 2).alias("Total_Sales"),
        round(avg("Item_Outlet_Sales"), 2).alias("Average_Sales")
    ) \
    .orderBy("Total_Sales", ascending=False) \
    .show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Filter high-selling products

# COMMAND ----------

df.filter(
    df.Item_Outlet_Sales >= 3000
).select(
    "Item_Identifier",
    "Item_Type",
    "Item_Outlet_Sales",
    "Outlet_Type"
).orderBy(
    "Item_Outlet_Sales",
    ascending=False
).show(20)