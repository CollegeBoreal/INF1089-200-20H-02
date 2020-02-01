

:pushpin: mcr.microsoft.com/mssql/server:2019-GA-ubuntu-16.04

-e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=yourStrong(!)Password' -e 'MSSQL_PID=Express'

```
PS > docker container run --name some-mssql `
                        --env "SA_PASSWORD=Password123" `
                        --env "ACCEPT_EULA=Y" `
                        --env "MSSQL_PID=Express" `
                        --publish 1433:1433 --detach `
                        mcr.microsoft.com/mssql/server:2019-GA-ubuntu-16.04
```

# References


https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15&pivots=cs1-powershell



## :warning: Erreurs possible

```
PS > docker container ls --all
CONTAINER ID        IMAGE                                                 COMMAND                  CREATED
   STATUS                      PORTS               NAMES
0fe68511b9fe        mcr.microsoft.com/mssql/server:2019-GA-ubuntu-16.04   "/opt/mssql/bin/perm…"   17 seconds ago
   Exited (1) 11 seconds ago                       some-mssql
```

```
PS > docker logs some-mssql
SQL Server 2019 will run as non-root by default.
This container is running as user mssql.
To learn more visit https://go.microsoft.com/fwlink/?linkid=2099216.
sqlservr: This program requires a machine with at least 2000 megabytes of memory.
/opt/mssql/bin/sqlservr: This program requires a machine with at least 2000 megabytes of memory.
```

```
PS >  docker logs some-mssql
SQL Server 2019 will run as non-root by default.
This container is running as user mssql.
To learn more visit https://go.microsoft.com/fwlink/?linkid=2099216.
The SQL Server End-User License Agreement (EULA) must be accepted before SQL
Server can start. The license terms for this product can be downloaded from
http://go.microsoft.com/fwlink/?LinkId=746388.

You can accept the EULA by specifying the --accept-eula command line option,
setting the ACCEPT_EULA environment variable, or using the mssql-conf tool.
```
