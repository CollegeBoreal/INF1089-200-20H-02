## Backup

### Copy a backup file into the container
#### :one: create a backup folder

```
$ winpty docker exec -it some-mysqlds mkdir data
```
### creer un volume
```
> docker container run --name some-mssql `
>>            --env "ACCEPT_EULA=Y" `
>>            --env "SA_PASSWORD=Password123" `
>>            --env "ATTACH_DBS=[{'dbName':'world_x','dbFiles':['c:\\DATA\\world_x.mdf','c:\\DATA\\world_x_log.ldf']}]" `
```

#### :two: downloads the backup file as wwi.bak
```
> curl -OutFile "wwi.bak" "https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak"
```
#### :three: copy the backup file into the container in the Data directory
```
$ docker cp wwi.bak some-mysqlds:data
```
