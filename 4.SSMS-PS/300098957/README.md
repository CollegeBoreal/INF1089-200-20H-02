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
                       --publish 1433:1433 --detach `
                       --volume c:\users\administrator\developer\inf1089-200-20h-02\4.ssms-ps\300098957\data:c:\program files\microsoft sql server\mssql14.mssqlserver\mssql\data `
                       mssql-server-windows-developer-fti
```


```
PS> docker container run --name some-mssql --env "ACCEPT_EULA=Y" --env "SA_PASSWORD=Password123" --publish 1433:1433 --detach --volume "C:\Users\Administrator\Developer\INF1089-200-20H-02\4.SSMS-PS\300098957\DATA":"C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA" mssql-server-windows-developer-fti
```
