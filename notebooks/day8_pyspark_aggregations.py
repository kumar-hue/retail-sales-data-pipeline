# Databricks notebook source
df=spark.table("workspace.default.bigmart_sales_cleaned")

# COMMAND ----------

df.show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ## How do outlet type and outlet size relate to sales?
# MAGIC #### Which combination of outlet type and outlet size generates the highest total sales?

# COMMAND ----------

from pyspark.sql.functions import sum,avg,count
df.groupBy("Outlet_Type","Outlet_Size")\
.agg(
    count("*").alias("Total_Products"),
    sum("Item_Outlet_Sales").alias("Total_Sales"),
    avg("Item_Outlet_Sales").alias("Average_Sales")
) \
.orderBy("Total_Sales",ascending=False) \
.show()


# COMMAND ----------

# MAGIC %md
# MAGIC ### multiple aggregations by Outlet_Type

# COMMAND ----------

df.groupBy("Outlet_Type")\
.agg(
    count("*").alias("Total_Products"),
    sum("Item_Outlet_Sales").alias("Total_Sales"),
    avg("Item_Outlet_Sales").alias("Average_Sales")
)\
.orderBy("Total_Sales",ascending=False) \
.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create a summary DataFrame

# COMMAND ----------

outlet_summary = df.groupBy("Outlet_Type") \
    .agg(
        count("*").alias("Product_Count"),
        sum("Item_Outlet_Sales").alias("Total_Sales"),
        avg("Item_Outlet_Sales").alias("Average_Sales")
    )

outlet_summary.show()

# COMMAND ----------

outlet_summary.orderBy("Total_Sales",ascending=False).show()

# COMMAND ----------

outlet_summary.show()

# COMMAND ----------

outlet_summary.orderBy(
    "Total_Sales",
    ascending=False
).show()