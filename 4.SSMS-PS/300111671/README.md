
# Powershell SQL Backup and restore script 


##  Création du container MSSQL

👁 Aller dans le repertoire de son :id: et creer un répertoire `backup` et y mettre le fichier `.gitkeep`

```
PS> mkdir backup
PS> echo $null >> backup\.gitkeep
```

😎 Capturer le répertoire courant `$PWD` et le placer dans la variable d'environnement `$SRC`

```
PS> $SRC = (pwd).Path | Foreach-Object {$_ -replace '\\','/'}
```

🚓 Lancer le conteneur avec une gestion d'état `--volume`

🆗 Le paramètre Docker `--volume` représente l'état à capturer et prend une source et une destination

```
PS> docker container run --name some-mssql `
           --env "ACCEPT_EULA=Y" `
           --env "SA_PASSWORD=Password123" `
           --volume C:\Users\Administrator\INF1089-200-20H-02\4.SSMS-PS\300111671\backup:C:/DATA `
           --publish 1433:1433 --detach `
           mssql-server-windows-developer-fti
```

<<<<<<< HEAD
💥 Restore Database
=======
#### :b: Downloads the backup file as wwi.bak
```
> curl -OutFile "wwi.bak" "https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak"
```
## :c: Restore Database


>>>>>>> 69e6def1ecf68b3ff5525f17d1e975cb51e714e3

🕠 Dans son répertoire de travail (i.e. :id: )

* Lancer son script de restauration

```
PS > .\restore.ps1
``` 
![](images/RESTO.png)

👉 Vérification dans `SSMS` 

* La base de donnees `WorldWideImporters` a été importée

<img src="sql.JPG" width="204" heidth="477"></img>

🤷‍♀️ Backup Database

:pushpin: Dans son répertoire de travail (i.e. :id: )

* Lancer son script de backup

```
PS > .\backup.ps1
```

🤦‍♂️ Vérification

```
PS > gci backup
```

![](images/bak.png)

* le fichier `wwwi_2.bak` doit ètre présent 
![](images/baki2.png)
