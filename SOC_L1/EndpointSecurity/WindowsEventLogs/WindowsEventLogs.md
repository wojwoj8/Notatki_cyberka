Logi są w formacie .evt albo .evtx tutaj: `C:\Windows\System32\winevt\Logs`

### Elementy winfows event log

Są takie:
- System logs - zapisują wydarzenia związane z segmentami OS, informacje o sterownikach, hardware, zmiany systemowe itp.
- Security logs - logowanie i wylogowywanie z systemu. system audit policy określa te eventy
- Application logs - Zapisuje wydarzenia związane z aplikacjami na systemie
- Directory service event - Active directory changes and activities
- File replicaton service event - wydarzenia związane z winfows servers podczas sharowania group policies i logon scripts to domain controllers
- DNS Event logs
- Custom logs
 [dodatkowo typy eventów](https://docs.microsoft.com/en-us/windows/win32/eventlog/event-types)

Metody zobaczenia tych logów:
1. **Event Viewer** (GUI-based application) - odpalenie win +r `eventvwr.msc`
2. **Wevtutil.exe** (command-line tool)
3. **Get-WinEvent** (PowerShell cmdlet)

### wevutil.exe

"enables you to retrieve information about event logs and publishers. You can also use this command to install and uninstall event manifests, to run queries, and to export, archive, and clear logs."

## Get-WinEvent

Pozwala zagnąć logi z różnych komputerów i źródeł w jedno

Przydatne linki bo to jest upo
[The Windows Logging Cheat Sheet (Windows 7 - Windows 2012)](https://static1.squarespace.com/static/552092d5e4b0661088167e5c/t/580595db9f745688bc7477f6/1476761074992/Windows+Logging+Cheat+Sheet_ver_Oct_2016.pdf)
[Spotting the Adversary with Windows Event Log Monitoring](https://web.archive.org/web/20190115215749/https://apps.nsa.gov/iaarchive/customcf/openAttachment.cfm?FilePath=/iad/library/ia-guidance/security-configuration/applications/assets/public/upload/Spotting-the-Adversary-with-Windows-Event-Log-Monitoring.pdf&WpKes=aF6woL7fQp3dJiqyJL2LenrLxuHC7ztGtVNK3x)
[Events to Monitor](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor) (Best Practices for Securing Active Directory)
[The Windows 10 and Windows Server 2016 Security Auditing and Monitoring Reference](https://www.microsoft.com/en-us/download/confirmation.aspx?id=52630) (a comprehensive list [**over 700 pages**])


Filtrowanie w cli

Filter by Event ID: `*/System/EventID=<ID>`

Filter by XML Attribute/Name: `*/EventData/Data[@Name="<XML Attribute/Name>"]`

Filter by Event Data: `*/EventData/Data=<Data>`

Przykład: `Get-WinEvent -Path <Path to Log> -FilterXPath '*/System/EventID=3 and */EventData/Data[@Name="DestinationPort"] and */EventData/Data=4444'`