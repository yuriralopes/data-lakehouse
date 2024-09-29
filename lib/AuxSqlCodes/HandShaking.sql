CREATE TABLE [dbo].[HandshakingDB] (
	
    [table_id] [int] NOT NULL, 
	[name_Schema] [nvarchar](255) NOT NULL,
	[name_table] [nvarchar](255) NOT NULL, 
    [last_execution_date] [nvarchar](8) NOT NULL,
    [low_last_execution_time] [nvarchar](14) NOT NULL,
	[high_last_execution_time] [nvarchar](14) NOT NULL,
	PRIMARY KEY ([table_id], [name_Schema],  [name_table])

	
	)

   INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (1,'Sales','SalesTaxRate','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (2,'Sales','PersonCreditCard','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (3,'Sales','SalesTerritory','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (4,'Sales','SalesTerritoryHistory','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (5,'Sales','ShoppingCartItem','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (6,'Sales','SpecialOffer','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (7,'Sales','SpecialOfferProduct','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (8,'Sales','Store','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (9,'Sales','CountryRegionCurrency','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (10,'Sales','CreditCard','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (11,'Sales','Currency','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (12,'Sales','CurrencyRate','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (13,'Sales','Customer','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (14,'Sales','SalesOrderDetail','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (15,'Sales','SalesOrderHeader','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (16,'Sales','SalesOrderHeaderSalesReason','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (17,'Sales','SalesPerson','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (18,'Sales','SalesPersonQuotaHistory','20240928','20240928000000','20240928000000');
INSERT INTO [dbo].[HandshakingDB]([table_id],[name_Schema],[name_table],[last_execution_date],[low_last_execution_time],[high_last_execution_time]) VALUES (19,'Sales','SalesReason','20240928','20240928000000','20240928000000');
