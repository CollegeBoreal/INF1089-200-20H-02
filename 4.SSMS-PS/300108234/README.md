## Backup

### 📌 Copy a backup file into the container
#### :one: create a backup folder

```
$ winpty docker exec -it some-mysqlds mkdir data
```
#### :two: Capture the current $PWD directory and place it in the $SRC variable.
```
PS> $SRC = (pwd).Path | Foreach-Object {$_ -replace '\\','/'}
```
#### :three: create a volume
```
> docker container run --name some-mssql `
>>            --env "ACCEPT_EULA=Y" `
>>            --env "SA_PASSWORD=Password123" `
>>            --env "ATTACH_DBS=[{'dbName':'world_x','dbFiles':['c:\\DATA\\world_x.mdf','c:\\DATA\\world_x_log.ldf']}]" `
```

#### :four: downloads the backup file as wwi.bak
```
> curl -OutFile "wwi.bak" "https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak"
```
#### :five: copy the backup file into the container in the Data directory
```
$ docker cp wwi.bak some-mysqlds:/data
```
### 📌 Restore Database
#### :one: Connect to sqlcmd
```
sqlcmd -U sa -p
```
#### :two: Execute the following scripts
```
1> RESTORE FILELISTONLY FROM DISK = 'C:\data\wwi.bak'
2> go
```

```
1> RESTORE DATABASE WideWorldImporters FROM DISK = 'C:\data\wwi.bak' WITH MOVE 'WW
I_Primary' TO 'C:\data\WideWorldImporters.mdf', MOVE 'WWI_UserData' TO 'C:\data\Wi
deWorldImporters_userdata.ndf', MOVE 'WWI_Log' TO 'C:\data\WideWorldImporters.ldf'
, MOVE 'WWI_InMemory_Data_1' TO 'C:\data\WideWorldImporters_InMemory_Data_1'

2> go
```

```
1> BACKUP DATABASE [WideWorldImporters] TO DISK = 'C:\data\wwi_2.bak' WITH NOFORMA
T, NOINIT, NAME = 'WideWorldImporters-full', SKIP, NOREWIND, NOUNLOAD, STATS = 10

2> go
```

```
1> --volume C:/Users/Administrator/Developer/INF1089-200-20H-02/4.SSMS-PS/30009895
7/DATA:C:/Program Files/Microsoft SQL Server/MSSQL14.MSSQLSERVER/MSSQL/DATA `

2> go
```
✔
