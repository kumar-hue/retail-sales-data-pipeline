# Databricks notebook source
# MAGIC %md
# MAGIC ### Load our cleaned data

# COMMAND ----------

from pyspark.sql.functions import sum,avg,count,min,max
df=spark.table("workspace.default.bigmart_sales_cleaned")

# COMMAND ----------

df.show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create a small outlet DataFrame for praticing real joins

# COMMAND ----------

outlet_data=[
    ("OUT049","Tier1"),
    ("OUT018","Tier2"),
    ("OUT010","Tier3"),
    ("OUT013","Tier1"),
    ("OUT027","Tier2")
]
outlet_df=spark.createDataFrame(
    outlet_data,["Outlet_Identifier", "Market_Tier"]
)
outlet_df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### inner join - df and outlet_df datafarmes

# COMMAND ----------

joined_df=df.join(outlet_df,on="Outlet_Identifier",how="inner")
joined_df.show(10)

# COMMAND ----------

joined_df.columns

# COMMAND ----------

# MAGIC %md
# MAGIC ### Analyse sales by Market Tier
# MAGIC How do sales differ across market tiers?

# COMMAND ----------

joined_df.groupBy("Market_Tier") \
    .agg(
        count("*").alias("product_count"),
        sum("Item_Outlet_Sales").alias("Total_Sales"),
        avg("Item_Outlet_Sales").alias("Average_Sales")      
    )\
    .orderBy("Total_Sales",ascending=False)\
    .show()      