USE [AdventureWorks2022]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[updateHSEntry]
    @name_table [nvarchar](255), 
    @last_execution_date [nvarchar](8),
    @low_last_execution_time [nvarchar](14),
	@high_last_execution_time [nvarchar](14),
    @name_Schema [nvarchar](255)
WITH EXECUTE AS CALLER
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        UPDATE [dbo].[HandshakingDB] 
        SET [last_execution_date] = @last_execution_date 
            ,[low_last_execution_time] = @low_last_execution_time 
            ,[high_last_execution_time] = @high_last_execution_time 
        WHERE [name_Schema] = @name_Schema AND [name_table] = @name_table;
    END TRY
    BEGIN CATCH
        EXECUTE [dbo].[uspLogError];
    END CATCH;
END;
GO



