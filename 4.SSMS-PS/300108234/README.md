## Backup

### Copy a backup file into the container
#### :one: create a backup folder

```
$ winpty docker exec -it some-mysqlds mkdir Data
```
#### :two: downloads the backup file as wwi.bak
```
$ curl -L -o wwi.bak 'https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak'
```
#### :three: copy the backup file into the container in the Data directory
```
$ docker cp wwi.bak some-mysqlds:Data
```
