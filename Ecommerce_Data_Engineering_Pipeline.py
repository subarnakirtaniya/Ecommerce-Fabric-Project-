#!/usr/bin/env python
# coding: utf-8

# ## Ecommerce_Data_Engineering_Pipeline
# 
# New notebook

# In[5]:


from pyspark.sql.functions import sum

gold_df = df_silver.groupBy("region") \
    .agg(sum("amount").alias("total_sales"))

gold_df.write.mode("overwrite").saveAsTable("gold_sales_by_region")


# In[3]:


from pyspark.sql.functions import col

# Read bronze table
df = spark.read.table("orders_table")

# Clean & transform
df_silver = df.withColumn("amount", col("amount").cast("int"))

# Save as silver table
df_silver.write.mode("overwrite").saveAsTable("silver_orders")


# In[2]:


# Welcome to your new notebook
# Type here in the cell editor to add code!

df = spark.read.option("header", "true").csv("Files/orders_10000.csv")

df.show()

df.write.mode("overwrite").saveAsTable("orders_table")

