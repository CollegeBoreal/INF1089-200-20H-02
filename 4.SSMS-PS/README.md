# SSMS PowerShell

## :o: Devoir

           Le but de l'exercice est de créer un plan de maintenance permettant la sauvegarde 
           et la récupération de base de données MSSQL  dans un script Powershell

## :a: Création du container MSSQL

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



## :ab: Exemple de Backup et Restore

:pushpin: Avec Docker

https://docs.microsoft.com/en-us/sql/linux/tutorial-restore-backup-in-sql-server-container

:pushpin: Autre plus diffcile

http://www.mikefal.net/2015/10/13/a-month-of-sql-ps-backups-and-restores/


## :bulb: Volumes:

https://github.com/pulla2908/docker-mssql-server-windows-developer-fti
