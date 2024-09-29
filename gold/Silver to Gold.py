# Databricks notebook source
# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Doing transformation and Ingestion from Silver to Gold Container

# COMMAND ----------

# DBTITLE 1,Import Libs
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace

# COMMAND ----------

# DBTITLE 1,Getting all tables in the container
table_name = []
print(table)
for i in dbutils.fs.ls("/mnt/silver/Sales/"):
    table_name.append(i.name.split('/')[0])
table_name

# COMMAND ----------

# DBTITLE 1,Transformation

for name in table_name:
	path = f'/mnt/silver/Sales/{name}/'
	df = spark.read.format('delta').load(path)

	column_names = df.columns

	for old_col_name in column_names:
		#convert column name from ColumnName to Column_Name format
		new_col_name = "".join(["_" + char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")

		df = df.withColumnRenamed(old_col_name, new_col_name)

	output_path = f'/mnt/gold/Sales/{name}'
	df.write.format('delta').mode("overwrite").save(output_path)

# COMMAND ----------

# DBTITLE 1,Checking result for last table
display(df)
