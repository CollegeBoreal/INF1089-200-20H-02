# Laboratoire : Création d’un plan de maintenance MSSQL

## :a: Création du container MSSQL

:pushpin: Aller dans le repertoire de son :id: et creer un repertoire `backup`

```
PS> mkdir backup
PS> echo $null >> backup\.gitkeep
```

:pushpin: Capturer le répertoire courant `$PWD` et le placer dans la variable `$SRC`

```
PS> $SRC = (pwd).Path | Foreach-Object {$_ -replace '\\','/'}
```

:m: Lancer le conteneur avec une gestion d'état `--volume`

:bulb: Le paramètre Docker `--volume` représente l'état à capturer et prend une source et une destination

```
PS> docker container run --name some-mssql `
           --env "ACCEPT_EULA=Y" `
           --env "SA_PASSWORD=Password123" `
           --volume ${SRC}:C:/DATA `
           --publish 1433:1433 --detach `
           mssql-server-windows-developer-fti
```



```
PS C:\DATA> Stop-Service -Name 'MSSQLSERVER'
PS C:\DATA> cp 'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\world_x*' .
PS C:\DATA> gci


    Directory: C:\DATA


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2/13/2020   3:59 PM              2 .gitkeep
-a----        2/14/2020   4:30 PM        8388608 world_x.mdf
-a----        2/14/2020   4:30 PM        8388608 world_x_log.ldf
```


PS C:\DATA> Start-Service -Name 'MSSQLSERVER'


## :b: Restore Database

:one: Aller dans son répertoire de travail


```
PS > Set-Location -Path $HOME\Developer\INF1089-200-20H-02\4.SSMS-PS\300098957
```

```
PS > curl -OutFile "data\wwi.bak" "https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak"
```

```
1> RESTORE FILELISTONLY FROM DISK = 'C:\data\wwi.bak'
2> GO
```

```
1> RESTORE DATABASE WideWorldImporters FROM DISK = 'C:\data\wwi.bak' WITH MOVE 'WWI_Primary' TO 'C:\data\WideWorldImporters.mdf', MOVE 'WWI_UserData' TO 'C:\data\WideWorldImporters_userdata.ndf', MOVE 'WWI_Log' TO 'C:\data\WideWorldImporters.ldf', MOVE 'WWI_InMemory_Data_1' TO 'C:\data\WideWorldImporters_InMemory_Data_1'
2> GO
```


```
1> BACKUP DATABASE [WideWorldImporters] TO DISK = 'C:\data\wwi_2.bak' WITH NOFORMAT, NOINIT, NAME = 'WideWorldImporters-full', SKIP, NOREWIND, NOUNLOAD, STATS = 10

2> GO
```






:x: ?craser le r/pertoire par d/faut de MS-SQL ne marche pas (mais le chemin est correct)

```
        --volume C:/Users/Administrator/Developer/INF1089-200-20H-02/4.SSMS-PS/300098957/DATA:C:/Program Files/Microsoft SQL Server/MSSQL14.MSSQLSERVER/MSSQL/DATA `
```
