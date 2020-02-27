# Laboratoire : Création d’un plan de maintenance MSSQL

## :a: Création du container MSSQL

:pushpin: Aller dans le repertoire de son :id: et creer un répertoire `backup` et y mettre le fichier `.gitkeep`

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

## :b: Restore Database

:pushpin: Dans son répertoire de travail (i.e. :id: )

```
PS > .\restore.ps1
```

:pushpin: Vérification dans `SSMS` 

<img src="images/WWI_SSMS.png" width="204" heidth="477"></img>

## :ab: Backup Database

:pushpin: Dans son répertoire de travail (i.e. :id: )

```
PS > .\backup.ps1
```

:pushpin: Vérification

```
PS > gci backup
```

* le fichier `wwwi_2.bak` doit ètre présent 
