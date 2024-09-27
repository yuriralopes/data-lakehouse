# Databricks notebook source
# MAGIC %md
# MAGIC ## Doing transformation for all tables in Scope

# COMMAND ----------

# DBTITLE 1,Getting all tables in the container
table_name = []
print(table)
for i in dbutils.fs.ls("/mnt/bronze/Sales/"):
    table_name.append(i.name.split('/')[0])
table_name

# COMMAND ----------

class FullIngestionSilver:

    def __init__(self, table, sourcePath):
        self.table = table
        self.sourcePath = sourcePath
        self.output_path = f"/mnt/silver/Sales/{self.table}/"

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

    def auto(self):
        df = self.read()
        df_transform = self.transform(df)
        self.save(df_transform)



# COMMAND ----------

from datetime import datetime

date_path = datetime.today().strftime('%Y-%m-%d')

for i in table_name:
   sourcePath = '/mnt/bronze/Sales/' + i + '/delta/' + date_path + '/*'
   ingestion = FullIngestionSilver(i, sourcePath)
   ingestion.auto()

