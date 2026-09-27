# Databricks notebook source
df=spark.table("workspace.default.bigmart_sales_cleaned")

# COMMAND ----------

display(df.limit(10))

# COMMAND ----------

df.count()

# COMMAND ----------

df.columns

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.select("Item_Fat_Content"
          ,"Item_Type"
          ,"Item_MRP"
          ,"Item_Outlet_Sales"

).show(10)

# COMMAND ----------

df.filter(
    df.Outlet_Type=="Supermarket Type1"
).show(10)

# COMMAND ----------

df.groupBy("Item_Type")\
    .count()  \
    .orderBy("count",ascending=False)\
    .show(10)


# COMMAND ----------

from pyspark.sql.functions import avg
df.groupBy("Item_Type")\
   .agg(avg("Item_Outlet_Sales").alias("Average_Sales"))\
   .orderBy("Average_Sales",ascending=False)\
   .show()
