# Databricks notebook source
# MAGIC %md
# MAGIC ## Doing transformation and Ingestion from Bronze to Silver Container

# COMMAND ----------

# DBTITLE 1,Getting all tables in the container
import os
import sys
sys.path.append(os.path.abspath("/data-lakehouse/y-alencar@hotmail.com/data-lakehouse/lib/ingestion"))

table_name = []
print(table)
for i in dbutils.fs.ls("/mnt/bronze/Sales/"):
    table_name.append(i.name.split('/')[0])
table_name

# COMMAND ----------

from datetime import datetime

date_path = datetime.today().strftime('%Y-%m-%d')

for i in table_name:
    sourcePath = '/mnt/bronze/Sales/' + i + '/delta/' + date_path + '/*'
    try:  
        ingestion = FullIngestionSilver(i, sourcePath)
        ingestion.auto()
        print(f"Loading data from path: {sourcePath}")
    except Exception as e:
        print(f"Path does not exist: {sourcePath}")

