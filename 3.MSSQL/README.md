# MS SQL Server

Installer MS SQL Server

```
PS > docker container run --name some-mssql `
                          --env sa_password=password --env ACCEPT_EULA=Y `
                          --publish 1433:1433 --detach `
                          microsoft/mssql-server-windows-express
```


# References

https://hub.docker.com/r/microsoft/mssql-server-windows-express
