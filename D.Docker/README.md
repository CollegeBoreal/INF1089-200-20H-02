

# :a: Install Docker on Windows Server 

:pushpin: Dans @PowerShell

:one: Installer le module `DockerMsftProvider`

```
PS > Install-Module -Name DockerMsftProvider -Repository PSGallery -Force
```

:two: Installer le package `Docker`

```
PS > Install-Package -Name docker -ProviderName DockerMsftProvider
```

:three: Redémarrer le serveur

```
PS > Restart-Computer -Force
```

# :b: Check Docker on Windows Server 

* Vérifiez la version installée avec 

```
PS > Get-Package -Name Docker -ProviderName DockerMsftProvider
```

* Rechercher la version actuelle avec 

```
PS > Find-Package -Name Docker -ProviderName DockerMsftProvider
```

* Tester que le service Docker tourne

```
PS >  Get-Service Docker

Status   Name               DisplayName
------   ----               -----------
Running  Docker             Docker Engine
```

:bulb: Quand vous êtes prêt, effectuez une mise à niveau avec  (Maintenance)

```
PS > Install-Package -Name Docker -ProviderName DockerMsftProvider -Update -Force
```

* suivi de 

```
PS > Start-Service Docker
```


# :ab: Test Docker

```
PS > docker container run hello-world:nanoserver
```

```
PS > [environment]::OSVersion

Platform ServicePack Version      VersionString
-------- ----------- -------      -------------
 Win32NT             10.0.17763.0 Microsoft Windows NT 10.0.17763.0
```

```
PS > $winver = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\'
PS > $releasetag = "$($winver.releaseid)"
```


```
PS > docker container run `
                      --interactive --tty --rm `
                      mcr.microsoft.com/windows/nanoserver:$releasetag `
                      powershell.exe
```



https://hub.docker.com/_/microsoft-windows-nanoserver


# References

https://docs.microsoft.com/fr-fr/virtualization/windowscontainers/quick-start/set-up-environment?redirectedfrom=MSDN&tabs=Windows-Server

https://blogs.technet.microsoft.com/virtualization/2018/06/27/insider-preview-windows-container-image/
