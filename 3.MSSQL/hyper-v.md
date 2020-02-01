

:pushpin: mcr.microsoft.com/mssql/server:2019-GA-ubuntu-16.04

```
PS > docker container run --name some-mssql `
>>                        --env "SA_PASSWORD=Password123" `
>>                        --publish 1433:1433 --detach `
>>                        mcr.microsoft.com/mssql/server:2019-GA-ubuntu-16.04
Unable to find image 'mcr.microsoft.com/mssql/server:2019-GA-ubuntu-16.04' locally
2019-GA-ubuntu-16.04: Pulling from mssql/server
59ab41dd721a: Pull complete
57da90bec92c: Pull complete
06fe57530625: Pull complete
5a6315cba1ff: Pull complete
739f58768b3f: Pull complete
fd449e8d7345: Pull complete
51d0933375e5: Pull complete
64f21ba81504: Pull complete
55b6919c0cc6: Pull complete
Digest: sha256:c8fa22553ce421b0482febcafa712b29cbb933b0d97a8671686797b31cf157a9
Status: Downloaded newer image for mcr.microsoft.com/mssql/server:2019-GA-ubuntu-16.04
0fe68511b9fe0fe81f9148d0b1bd0e399015374fc831563b94a5b8fc4e404c37
```


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
