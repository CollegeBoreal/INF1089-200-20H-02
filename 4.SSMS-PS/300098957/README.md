# Laboratoire : Création d’un plan de maintenance MSSQL

## :a: Création du container MSSQL

:one: Aller dans le repertoire de son :id: et creer un repertoire `DATA`

```
PS> mkdir DATA
PS> cd DATA
```

:two: Capturer le répertoire courant `$PWD` et le placer dans la variable `$src`


```
PS> $SRC = (pwd).Path | Foreach-Object {$_ -replace '\\','/'}
```

:three: Lancer le conteneur avec une gestion d'état `--volume`

:bulb: Le paramètre Docker `--volume` représente l'état à capturer et prend une source et une destination

```
PS> docker container run --name some-mssql `
           --env "ACCEPT_EULA=Y" `
           --env "SA_PASSWORD=Password123" `
           --env "ATTACH_DBS=[{'dbName':'world_x','dbFiles':['c:\\DATA\\world_x.mdf','c:\\DATA\\world_x_log.ldf']}]" `
           --volume ${SRC}:C:/DATA `
           --publish 1433:1433 --detach `
           mssql-server-windows-developer-fti
```


```
PS C:\DATA> Stop-Service -Name 'MSSQLSERVER'
PS C:\DATA> cp 'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\world_x*' .
PS C:\DATA> gci


    Directory: C:\DATA


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2/13/2020   3:59 PM              2 .gitkeep
-a----        2/14/2020   4:30 PM        8388608 world_x.mdf
-a----        2/14/2020   4:30 PM        8388608 world_x_log.ldf
```


PS C:\DATA> Start-Service -Name 'MSSQLSERVER'


## :b: Restore Database

:one: Aller dans son répertoire de travail


```
PS > Set-Location -Path $HOME\Developer\INF1089-200-20H-02\4.SSMS-PS\300098957\DATA\
```

```
PS > curl -OutFile "wwi.bak" "https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak"
```












:x: ?craser le r/pertoire par d/faut de MS-SQL ne marche pas (mais le chemin est correct)

```
        --volume C:/Users/Administrator/Developer/INF1089-200-20H-02/4.SSMS-PS/300098957/DATA:C:/Program Files/Microsoft SQL Server/MSSQL14.MSSQLSERVER/MSSQL/DATA `
```

