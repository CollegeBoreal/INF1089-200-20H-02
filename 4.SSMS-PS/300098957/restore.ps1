

docker exec --interactive --tty some-mssql `
    sqlcmd -U sa -P "Password123" ` -i .\restore.sql