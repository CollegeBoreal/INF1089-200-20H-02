# MS SQL Server


Test Docker

```
PS > docker container run hello-world:nanoserver
```

```
PS > docker container run --interactive --tty --rm mcr.microsoft.com/windows/nanoserver:1809 powershell.exe
```

Installer MS SQL Server

```
PS > docker container run --name some-mssql `
                          --env sa_password=password --env ACCEPT_EULA=Y `
                          --publish 1433:1433 --detach `
                          microsoft/mssql-server-windows-express
```


# References

https://hub.docker.com/r/microsoft/mssql-server-windows-express
