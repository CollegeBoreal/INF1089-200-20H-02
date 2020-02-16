# Laboratoire : Création d’un plan de maintenance MSSQL

## Création du container MSSQL

```
PS> docker container run --name some-mssql `
                       --env "ACCEPT_EULA=Y" `
                       --env "SA_PASSWORD=Password123" `
                       --publish 1433:1433 --detach `
                       --volume SOURCE:DESTINATION `
                       mssql-server-windows-developer-fti
```

```
PS> docker container run --name some-mssql `
           --env "ACCEPT_EULA=Y" `
           --env "SA_PASSWORD=Password123" `
           --env "ATTACH_DBS=[{'dbName':'world_x','dbFiles':['c:\\DATA\\world_x.mdf','c:\\DATA\\world_x_log.ldf']}]" `
           --volume (Get-Location).Path:C:/DATA `
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


```
PS> docker C:/DATA/world_x.mdf
PS> docker C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\world_x_log.ldf
```


:x: ?craser le r/pertoire par d/faut de MS-SQL ne marche pas (mais le chemin est correct)

```
        --volume C:/Users/Administrator/Developer/INF1089-200-20H-02/4.SSMS-PS/300098957/DATA:C:/Program Files/Microsoft SQL Server/MSSQL14.MSSQLSERVER/MSSQL/DATA `
```

