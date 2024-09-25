# Data Lakehouse Project
## About

This project was inspired by the Trampar-de-Lakehouse (https://github.com/TeoMeWhy/trampar-de-lakehouse/blob/main/lib/ingestors.py) project, but with some differences, such as the data source and architecture.


![image](https://github.com/user-attachments/assets/c3b1a398-3413-488d-a4fa-ac3b9e6195a3)

## Stages
### Source System
The data is generated in real-time in a SQL Server database. The tables have a column with a timestamp that contains the date and time of insertion or update. 

An user called "datalakehouse" was created in SQL server. You can find the script in lib/createlogin.sql

### Azure
#### Resouce Group
For this project, a resource group "datalakehouse_project" was created on Azure Portal.

##### Key Vault
Azure Key Vault is a cloud service for securely storing and accessing secrets. It was named as KVdatalakehouseyu2. For the DB connection, two secrets were created: one for psw and other for username.

#### Azure Data Factory
An Azure Data Factory Resource was deployed to be used as an ETL tool in our architecture. Since the data source (SQL Server) is on a local machine, a Self-Hosted Integration Runtime will be used.

>> Pipeline: ADF_SalesData_Delta

### Azure Data Lake Gen2
A Data Lake will be the target for ours pipelines. Raw data will be extracted from source and placed in a bronze layer in data lake container. It will be called: dldatalakehouse.

There will be three containers: Bronze, Silver and Gold.
