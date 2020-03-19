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
PS > Get-EventLog -LogName Security -Newest 5

   Index Time          EntryType   Source                 InstanceID Message
   ----- ----          ---------   ------                 ---------- -------
   15396 Mar 19 15:28  SuccessA... Microsoft-Windows...         4634 An account was logged off....
   15395 Mar 19 15:28  SuccessA... Microsoft-Windows...         4634 An account was logged off....
   15394 Mar 19 15:28  SuccessA... Microsoft-Windows...         4672 Special privileges assigned to new logon....
   15393 Mar 19 15:28  SuccessA... Microsoft-Windows...         4624 An account was successfully logged on....
   15392 Mar 19 15:28  SuccessA... Microsoft-Windows...         4672 Special privileges assigned to new logon....
```

```
PS > $A = Get-EventLog -LogName Security -Newest 2
PS > $A | Select-Object -Property *


EventID            : 4634
MachineName        : WIN-DO3JKCENK11
Data               : {}
Index              : 15396
Category           : (12545)
CategoryNumber     : 12545
EntryType          : SuccessAudit
Message            : An account was logged off.

                     Subject:
                        Security ID:            S-1-5-96-0-5
                        Account Name:           UMFD-5
                        Account Domain:         Font Driver Host
                        Logon ID:               0x1ea8da036

                     Logon Type:                        2

                     This event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are
                     only unique between reboots on the same computer.
Source             : Microsoft-Windows-Security-Auditing
ReplacementStrings : {S-1-5-96-0-5, UMFD-5, Font Driver Host, 0x1ea8da036...}
InstanceId         : 4634
TimeGenerated      : 3/19/2020 3:28:26 PM
TimeWritten        : 3/19/2020 3:28:26 PM
UserName           :
Site               :
Container          :

EventID            : 4634
MachineName        : WIN-DO3JKCENK11
Data               : {}
Index              : 15395
Category           : (12545)
CategoryNumber     : 12545
EntryType          : SuccessAudit
Message            : An account was logged off.

                     Subject:
                        Security ID:            S-1-5-21-2824105513-3625184561-1594800028-1000
                        Account Name:           Brice
                        Account Domain:         WIN-DO3JKCENK11
                        Logon ID:               0x1ea8ffb55

                     Logon Type:                        10

                     This event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are
                     only unique between reboots on the same computer.
Source             : Microsoft-Windows-Security-Auditing
ReplacementStrings : {S-1-5-21-2824105513-3625184561-1594800028-1000, Brice, WIN-DO3JKCENK11, 0x1ea8ffb55...}
```
