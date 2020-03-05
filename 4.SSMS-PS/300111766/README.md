        📗 Laboratoire : Création d’un plan de maintenance MSSQL
        
   Création du container MSSQL
   
   
   
   PS> mkdir backup
   PS> echo $null >> backup\.gitkeep
   
   PS> $SRC = (pwd).Path | Foreach-Object {$_ -replace '\\','/'}
Ⓜ️ Lancer le 

  PS> docker container run --name some-mssql `
           --env "ACCEPT_EULA=Y" `
           --env "SA_PASSWORD=Password123" `
           --volume ${SRC}:C:/DATA `
           --publish 1433:1433 --detach `
           mssql-server-windows-developer-fti
           
           
  PS > .\restore.ps1
  
  PS > .\backup.ps1
  
  
  PS > gci backup


