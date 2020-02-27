# SSMS PowerShell

## :o: Devoir

           Le but de l'exercice est de créer un plan de maintenance permettant la sauvegarde de données MSSQL 
           et sa récupération dans un script Powershell

## :zero: Création du container MSSQL

:pushpin: Aller dans le repertoire de son :id: et creer un repertoire `backup`

```
PS> mkdir backup
PS> echo $null >> backup\.gitkeep
```

:pushpin: Capturer le répertoire courant `$PWD` et le placer dans la variable `$SRC`

```
PS> $SRC = (pwd).Path | Foreach-Object {$_ -replace '\\','/'}
```

:m: Lancer le conteneur avec une gestion d'état `--volume`

:bulb: Le paramètre Docker `--volume` représente l'état à capturer et prend une source et une destination

```
PS> docker container run --name some-mssql `
           --env "ACCEPT_EULA=Y" `
           --env "SA_PASSWORD=Password123" `
           --volume ${SRC}:C:/DATA `
           --publish 1433:1433 --detach `
           mssql-server-windows-developer-fti
```


## :one: Installation

https://docs.microsoft.com/en-us/sql/powershell/download-sql-server-ps-module

Installer le Module

```
PS > Install-Module -Name SqlServer
```

Lister les commandes

```
PS > Get-Module SqlServer -ListAvailable
```


:two: Utiliser SQLPS(https://docs.microsoft.com/en-us/sql/powershell/sql-server-powershell)


```
PS> Invoke-Sqlcmd "SELECT DB_NAME() AS DatabaseName"
```

:pushpin: Creer une base de donnees `TestDB`

```
PS> Invoke-Sqlcmd "CREATE DATABASE TestDB;"
```

https://www.sqlshack.com/connecting-powershell-to-sql-server/

:ab: Exemple de Backup et Restore

:pushpin: Avec Docker

https://docs.microsoft.com/en-us/sql/linux/tutorial-restore-backup-in-sql-server-container

:pushpin: Autre plus diffcile

http://www.mikefal.net/2015/10/13/a-month-of-sql-ps-backups-and-restores/


## Volumes:

https://github.com/pulla2908/docker-mssql-server-windows-developer-fti
