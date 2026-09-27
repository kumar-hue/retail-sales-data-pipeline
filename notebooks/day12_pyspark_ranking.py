# Databricks notebook source
from pyspark.sql.functions import rank, dense_rank
from pyspark.sql.window import Window

df = spark.table("workspace.default.bigmart_sales_cleaned")

# COMMAND ----------

window_spec = Window.partitionBy("Item_Type") \
    .orderBy(df.Item_Outlet_Sales.desc())

# COMMAND ----------

# MAGIC %md
# MAGIC ### use rank()
# MAGIC that gives gap after a tie

# COMMAND ----------

df_ranked = df.withColumn(
    "Sales_Rank",
    rank().over(window_spec)
)

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
# MAGIC ### Use dense_rank()
# MAGIC does not leave gaps-1 2 2 3...

# COMMAND ----------

df_dense_ranked = df.withColumn(
    "Sales_Rank",
    dense_rank().over(window_spec)
)

df_dense_ranked.select(
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
# MAGIC ### Find top 3 using dense_rank()
# MAGIC This can return more than 3 products for an item type if there are ties.

# COMMAND ----------

df_dense_ranked.filter(
    df_dense_ranked.Sales_Rank <= 3
).select(
    "Item_Type",
    "Item_Identifier",
    "Item_Outlet_Sales",
    "Sales_Rank"
).orderBy(
    "Item_Type",
    "Sales_Rank"
).show(50)