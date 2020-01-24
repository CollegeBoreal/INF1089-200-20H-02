# MS SQL Server


Creer un repertoir avec comme nom votre :id:

Copier le contenu ci-dessous dans un fichier appelle Dockerfile






https://github.com/pulla2908/docker-mssql-server-windows-developer-fti


# References

https://hub.docker.com/r/microsoft/mssql-server-windows-express

Installer MS SQL Server

```
PS > docker container run --name some-mssql `
                          --env sa_password=password --env ACCEPT_EULA=Y `
                          --publish 1433:1433 --detach `
                          microsoft/mssql-server-windows-express
```
