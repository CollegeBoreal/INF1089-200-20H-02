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

