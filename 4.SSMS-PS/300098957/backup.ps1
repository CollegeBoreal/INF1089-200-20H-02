RESTORE FILELISTONLY FROM DISK = 'C:\data\wwi.bak'
RESTORE DATABASE WideWorldImporters FROM DISK = 'C:\data\wwi.bak' WITH MOVE 'WWI_Primary' TO 'C:\data\WideWorldImporters.mdf', MOVE 'WWI_UserData' TO 'C:\data\WideWorldImporters_userdata.ndf', MOVE 'WWI_Log' TO 'C:\data\WideWorldImporters.ldf', MOVE 'WWI_InMemory_Data_1' TO 'C:\data\WideWorldImporters_InMemory_Data_1'
BACKUP DATABASE [WideWorldImporters] TO DISK = 'C:\data\wwi_2.bak' WITH NOFORMAT, NOINIT, NAME = 'WideWorldImporters-full', SKIP, NOREWIND, NOUNLOAD, STATS = 10
