# Databricks notebook source
# MAGIC %md
# MAGIC ## Doing transformation and Ingestion from Bronze to Silver Container

# COMMAND ----------

# DBTITLE 1,Imports
import delta
import pyspark.sql.functions as F
from pyspark.sql.functions import col, lit, concat
import os
import sys
from delta.tables import *
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType

# COMMAND ----------

# DBTITLE 1,Classes and Functions
class IngestionSilver:

    def __init__(self, table, sourcePath, isDelta):
        self.table = table
        self.sourcePath = sourcePath
        self.isDelta = isDelta
        self.spark = spark
        self.output_path = f'/mnt/silver/Sales/{self.table}/'
        self.idField = "BusinessEntityID"

    def read(self):
        df = spark.read.format('parquet').load(self.sourcePath)
        return df
    
    def transform(self, df):
        df.createOrReplaceTempView(self.table)
        df_transform = spark.sql(f"select * from {self.table}")
        return df_transform

    def save(self, df):
        (df.write
           .mode("overwrite")
           .format("delta")
           .option("overwriteSchema", "true")
           .save(self.output_path)
           )
    
    def upsert(self, df):
        delta_table = DeltaTable.forPath(self.spark, self.output_path)
        
        delta_table.alias("d").merge(df.alias("n"), f"d.{self.idField} = n.{self.idField}").whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
        
    def auto(self):
        df = self.read()
        df_transform = self.transform(df)

        if self.isDelta == 'Y':
            self.upsert(df_transform)
        else:
            self.save(df_transform)

    


# COMMAND ----------

# DBTITLE 1,Getting all tables in the container
table_name = []
print(table)
for i in dbutils.fs.ls("/mnt/bronze/Sales/"):
    table_name.append(i.name.split('/')[0])
table_name


# COMMAND ----------

# DBTITLE 1,Transformation and Ingestion from Bronze Container to Silver
from datetime import datetime

date_path = datetime.today().strftime('%Y-%m-%d')
isFirstLoad = True

for i in table_name:
    sourcePath = '/mnt/bronze/Sales/' + i + '/delta/' + date_path + '/' + i + '*'

    if i == 'Store':
        isDelta = 'Y'
    else:
        isDelta = 'N'
    
    try:  
        ingestion = IngestionSilver(i, sourcePath, isDelta)
        ingestion.auto()
        print(f"Loading data from path: {sourcePath}")
    except Exception as e:
        print(f"Path does not exist: {sourcePath}")
