# Databricks notebook source
# MAGIC %md
# MAGIC ## Doing transformation for all tables in Scope

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls("/mnt/bronze/Sales/"):
    table_name.append(i.name)

table_name
