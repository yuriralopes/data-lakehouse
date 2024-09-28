# Databricks notebook source
dbutils.fs.ls('/mnt/silver/Sales/')

# COMMAND ----------

from pyspark.sql.functions import col
input_path = '/mnt/silver/Sales/Store/'

df = spark.read.format('delta').load(input_path)

display(df.where(col("BusinessEntityID") == 292))
