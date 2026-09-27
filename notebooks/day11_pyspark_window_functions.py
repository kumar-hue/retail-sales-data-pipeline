# Databricks notebook source
# MAGIC %md
# MAGIC ### Load the cleaned table

# COMMAND ----------

from pyspark.sql.functions import row_number
from pyspark.sql.window import Window

df = spark.table("workspace.default.bigmart_sales_cleaned")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create a window
# MAGIC ### The ranking starts again for each Item_Type.

# COMMAND ----------

window_spec = Window.partitionBy("Item_Type") \
    .orderBy(df.Item_Outlet_Sales.desc())

# COMMAND ----------

# MAGIC %md
# MAGIC ###Add ranking with row_number
# MAGIC df_ranked contains all your original columns plus

# COMMAND ----------

df_ranked=df.withColumn(
    "Sales_Rank",row_number().over(window_spec)
)


# COMMAND ----------

# MAGIC %md
# MAGIC ### Display the results

# COMMAND ----------

df_ranked.select(
    "Item_Type",
    "Item_Identifier",
    "Item_Outlet_Sales",
    "Sales_Rank"
).orderBy(
    "Item_Type",
    "Sales_Rank"
).show(20)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Find the top 3 products in each Item Type

# COMMAND ----------

df_ranked.filter(
    df_ranked.Sales_Rank<=3
).select(
    "Item_Type",
    "Item_Identifier",
    "Item_Outlet_Sales",
    "Sales_Rank"
).orderBy(
    "Item_Type",
    "Sales_Rank"
).show(50)

# COMMAND ----------

df_ranked.filter(df_ranked.Sales_Rank <= 3)