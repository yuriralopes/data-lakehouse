# Databricks notebook source
# MAGIC %md
# MAGIC ## Doing transformation for all tables in Scope

# COMMAND ----------

table_name = []
file_name = []

for i in dbutils.fs.ls("/mnt/bronze/Sales/"):
    table_name.append(i.name.split('/')[0])

table_name

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType
from datetime import datetime

date_path = datetime.today().strftime('%Y-%m-%d')

for i in table_name:
    date_path
    path = '/mnt/bronze/Sales/' + i + '/delta/' + date_path + '/'
    dbutils.fs.ls('"'+path+'"')
    #df = spark.read.format('parquet').load(path)
#df.display()
