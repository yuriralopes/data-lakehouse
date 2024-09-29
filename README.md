# Data Lakehouse Project
## About

This project is a simple data architecture in Azure, using SQL Server as the data source, ADF as ETL, Azure Data Lake as the storage layer, Azure Databricks to transform the data, and finally, Power BI for reporting.

![image](https://github.com/user-attachments/assets/c3b1a398-3413-488d-a4fa-ac3b9e6195a3)

## Stages
### Source System
The data is generated in real-time in a SQL Server database. The tables have a column with a timestamp that contains the date and time of insertion or update. 

An user called "datalakehouse" was created in SQL server. You can find the script in lib/createlogin.sql

### Azure

#### Resouce Group
For this project, a resource group "datalakehouse_project" was created on Azure Portal.
*All resources used in this project has the minimal computing capacity as possible.*

##### Key Vault
Azure Key Vault is a cloud service for securely storing and accessing secrets. It was named as KVdatalakehouseyu2. For the DB connection, two secrets were created: one for psw and other for username.

##### Azure Data Factory
An Azure Data Factory Resource was deployed to be used as an ETL tool in our architecture. Since the data source (SQL Server) is on a local machine, a Self-Hosted Integration Runtime will be used.

> Pipeline: ADF_SalesData_Delta

> Raw Data: ADF will send the data from SQL Server to the bronze layer of the Data Lake. The data will be sent as it is in the table, without any changes. All tables have a "ModifiedDate" column, which will be used for delta control. All records updated since the last execution will be sent to the Data Lake. The date and time of the last execution will be saved in a table created specifically for this purpose. 

##### Azure Data Lake Gen2
A Data Lake will be the target for ours pipelines. Raw data will be extracted from source and placed in a bronze layer in data lake container. It will be called: dldatalakehouse.

There will be three containers: Bronze, Silver and Gold.

##### Azure Databricks
An Azure Databricks resource will be used to transform and move the data between containers (Bronze to Silver and Silver to Gold).

##### Power BI
Power BI will be used in the NEXT PROJECT along with AZURE SYNAPSE ANALYTICS to create interactive dashboards and reports that enable real-time data analysis, facilitating decision-making.