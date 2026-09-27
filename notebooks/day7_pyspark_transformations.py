# Databricks notebook source
df=spark.table("workspace.default.bigmart_sales_cleaned")

# COMMAND ----------

df2=df.withColumn("Sales_Per_Weight",df.Item_Outlet_Sales/df.Item_Weight).show(10)

# COMMAND ----------

from pyspark.sql.functions import when
df2=df.withColumn("Sales_Category",when(df.Item_Outlet_Sales>=2000,"High").otherwise("Low")
)
display(df2.select("Item_Identifier","Item_Outlet_Sales","Sales_Category"
).limit(10))          