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


### Uwierzytelnianie

|**Event ID**|**Purpose**|**Logging**|**Limitations**|
|---|---|---|---|
|**4624  <br>**(Successful Logon)|Detect suspicious RDP/network logins and identify the attack starting point|Logged on the target machine, the one you are trying to access|**Noisy**. You will see hundreds of logon events per minute on loaded servers|
|**4625  <br>**(Failed Logon)|Detect brute force, password spraying, or vulnerability scanning|Logged on the target machine, the one you are trying to access|**Inconsistent**. The logs have lots of caveats that may trick you into the wrong understanding of the event|


### User Management

| **Event ID**                   | **Description**                                                | **Malicious Usage**                                                                                                                                                                                        |
| ------------------------------ | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **4720** / **4722** / **4738** | A user account was  <br>created / enabled / changed            | Attackers might create a backdoor account or even enable an old one to avoid detection                                                                                                                     |
| **4725** / **4726**            | A user account was  <br>disabled / deleted                     | In some advanced cases, threat actors may disable privileged SOC accounts to slow down their actions                                                                                                       |
| **4723** / **4724**            | A user changed their password /  <br>User's password was reset | Given enough permissions, threat actors might reset the password and then access the required user                                                                                                         |
| **4732** / **4733**            | A user was added to /  <br>removed from a security group       | Attackers often add their backdoor accounts to privileged groups like "[Administrators](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#administrators)" |

### Process monitoring

|**Event Code**|**Purpose**|**Limitations**|
|---|---|---|
|**4688  <br>**(Security Log: Process Creation)|Log an event every time a new process is launched, including its command line and parent process details|Disabled by default, you need to enable it by following the [official documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing)|
|**1  <br>**(Sysmon: Process Creation)|Replace 4688 event code and provide more advanced fields like process hash and its signature|Sysmon is an external tool not installed by default. Check out the [Sysmon official page](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)|

### Pliki i sieć

|**Event ID**|**Security Log Alternative**|**Event Purpose**|
|---|---|---|
|**11 / 13  <br>**(File Create / Registry Value Set)|**4656** for file changes and **4657** for registry changes, both disabled by default|Detect files dropped by malware or its changes to the registry (e.g. for persistence)|
|**3 / 22  <br>**(Network Connection / DNS Query)|No direct alternative, requires additional firewall and DNS configuration|Detect traffic from untrusted processes or to known malicious destinations|

### Powershell logging commands


#### Powershell history

```plaintext
C:\Users\<USER>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```