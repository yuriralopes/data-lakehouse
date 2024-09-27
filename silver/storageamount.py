# Databricks notebook source
# DBTITLE 1,Mounting Azure Data Lake - Bronze
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "5d49f494-8b9f-429b-95f0-2d60f9a4f4ea",
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="datalakehouse",key="ADLS-DATABRICKS-KEY"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/d1c90e28-32cb-41ac-b3eb-5dced487b30a/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://bronze@dldatalakehouse.dfs.core.windows.net/",
  mount_point = "/mnt/bronze/",
  extra_configs = configs)

#checking if the mount point is working
dbutils.fs.ls("/mnt/bronze/Sales/")

# COMMAND ----------

# DBTITLE 1,Mounting Azure Data Lake - Silver
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "5d49f494-8b9f-429b-95f0-2d60f9a4f4ea",
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="datalakehouse",key="ADLS-DATABRICKS-KEY"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/d1c90e28-32cb-41ac-b3eb-5dced487b30a/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://bronze@dldatalakehouse.dfs.core.windows.net/",
  mount_point = "/mnt/silver/",
  extra_configs = configs)

dbutils.fs.ls("/mnt/silver/")

# COMMAND ----------

# DBTITLE 1,Mounting Azure Data Lake - Gold
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "5d49f494-8b9f-429b-95f0-2d60f9a4f4ea",
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="datalakehouse",key="ADLS-DATABRICKS-KEY"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/d1c90e28-32cb-41ac-b3eb-5dced487b30a/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://bronze@dldatalakehouse.dfs.core.windows.net/",
  mount_point = "/mnt/gold/",
  extra_configs = configs)

dbutils.fs.ls("/mnt/gold/")
