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
           --volume C:/Users/Administrator/Developer/INF1089-200-20H-02/4.SSMS-PS/300098957/DATA:C:/DATA `
           --publish 1433:1433 --detach `
           mssql-server-windows-developer-fti
```


```
PS> docker C:/DATA/world_x.mdf
PS> docker C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\world_x_log.ldf
```


:x: ?craser le r/pertoire par d/faut de MS-SQL ne marche pas (mais le chemin est correct)

```
        --volume C:/Users/Administrator/Developer/INF1089-200-20H-02/4.SSMS-PS/300098957/DATA:C:/Program Files/Microsoft SQL Server/MSSQL14.MSSQLSERVER/MSSQL/DATA `
```

