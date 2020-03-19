# Syslog of JournalD

https://www.loggly.com/ultimate-guide/centralizing-with-syslog/

:pushpin: Monitoring et gestion de log : 

- [ ] Filebeat
- [ ] Logstash
* AWS
    - [x] Cloudwatch
    - [x] SNS
- [ ] Grafana
- [ ] Prometheus

# Windows Server Logs

https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_eventlogs?view=powershell-5.1


```
PS > Get-EventLog -List

  Max(K) Retain OverflowAction        Entries Log
  ------ ------ --------------        ------- ---
  20,480      0 OverwriteAsNeeded      22,691 Application
  20,480      0 OverwriteAsNeeded           0 HardwareEvents
     512      7 OverwriteOlder              0 Internet Explorer
  20,480      0 OverwriteAsNeeded           0 Key Management Service
  20,480      0 OverwriteAsNeeded      15,396 Security
  20,480      0 OverwriteAsNeeded       5,820 System
  15,360      0 OverwriteAsNeeded       5,670 Windows PowerShell
```

```
$  Get-EventLog -LogName "Security"
```
