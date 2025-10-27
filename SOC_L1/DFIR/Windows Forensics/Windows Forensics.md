### Rejestry windows

Jest to zbiór baz danych zawierający konfigurację systemu. Zawiera również dane aplikacji. Dostęp jest pod `regedit.exe`. Podział rejestrów nazywa się [Registry Hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)

The registry on any Windows system contains the following five root keys:

1. HKEY_CURRENT_USER
2. HKEY_USERS
3. HKEY_LOCAL_MACHINE
4. HKEY_CLASSES_ROOT
5. HKEY_CURRENT_CONFIG

|Folder/predefined key|Description|
|---|---|
|**HKEY_CURRENT_USER**|Contains the root of the configuration information for the user who is currently logged on. The user's folders, screen colors, and Control Panel settings are stored here. This information is associated with the user's profile. This key is sometimes abbreviated as HKCU.|
|**HKEY_USERS**|Contains all the actively loaded user profiles on the computer. HKEY_CURRENT_USER is a subkey of HKEY_USERS. HKEY_USERS is sometimes abbreviated as HKU.|
|**HKEY_LOCAL_MACHINE**|Contains configuration information particular to the computer (for any user). This key is sometimes abbreviated as HKLM.|
|**HKEY_CLASSES_ROOT**|Is a subkey of `HKEY_LOCAL_MACHINE\Software` . The information that is stored here makes sure that the correct program opens when you open a file by using Windows Explorer. This key is sometimes abbreviated as HKCR.<br><br>Starting with Windows 2000, this information is stored under both the HKEY_LOCAL_MACHINE and HKEY_CURRENT_USER keys. The `HKEY_LOCAL_MACHINE\Software\Classes` key contains default settings that can apply to all users on the local computer.  The `HKEY_CURRENT_USER\Software\Classes` key has settings that override the default settings and apply only to the interactive user.<br><br>The HKEY_CLASSES_ROOT key provides a view of the registry that merges the information from these two sources. HKEY_CLASSES_ROOT also provides this merged view for programs that are designed for earlier versions of Windows. To change the settings for the interactive user, changes must be made under `HKEY_CURRENT_USER\Software\Classes` instead of under HKEY_CLASSES_ROOT.<br><br>To change the default settings, changes must be made under `HKEY_LOCAL_MACHINE\Software\Classes`  .If you write keys to a key under HKEY_CLASSES_ROOT, the system stores the information under `HKEY_LOCAL_MACHINE\Software\Classes` .<br><br>If you write values to a key under HKEY_CLASSES_ROOT, and the key already exists under `HKEY_CURRENT_USER\Software\Classes` , the system will store the information there instead of under `HKEY_LOCAL_MACHINE\Software\Classes` .|
|**HKEY_CURRENT_CONFIG**|Contains information about the hardware profile that is used by the local computer at system startup.|

Jak mamy tylko dostęp do obrazu dysku to rejestry są w `C:\Windows\System32\Config` I foldery:

1. **DEFAULT** (mounted on `HKEY_USERS\DEFAULT`)
2. **SAM** (mounted on `HKEY_LOCAL_MACHINE\SAM`)
3. **SECURITY** (mounted on `HKEY_LOCAL_MACHINE\Security`)
4. **SOFTWARE** (mounted on `HKEY_LOCAL_MACHINE\Software`)
5. **SYSTEM** (mounted on `HKEY_LOCAL_MACHINE\System`)

### Dane użytkownika

Od Windows 7 `C:\Users\<username>\` where the hives are:

1. **NTUSER.DAT** (mounted on HKEY_CURRENT_USER when a user logs in)
2. **USRCLASS.DAT** (mounted on HKEY_CURRENT_USER\Software\CLASSES)

The USRCLASS.DAT hive is located in the directory `C:\Users\<username>\AppData\Local\Microsoft\Windows`.
The NTUSER.DAT hive is located in the directory `C:\Users\<username>\`.

TE DANE SĄ DOMYŚLNIE UKRYTE!!!

Jeszcze istnieje "Amcache" - informacje o programach które ostatnio zostały uruchomione. Lokalizacja: `C:\Windows\AppCompat\Programs\Amcache.hve`

### Transaction logs and backups

Trasnascion logs to logi z ostatnich zmian w tym hive, np. ostatnie zmiany w SAM hive będą w logu SAM.LOG1, LOG2 itp. tam gdzie są te hive. 
Backups z kolei to backup rejestrów przed zmianami w `C:\Windows\System32\Config\RegBack`

Data acquisition - zdobywanie danych z obrazu systemu. Problem jest że np. te registy hives w `%WINDIR%\System32\Config` są zabezpieczone przed dostępem. W takiej sytuacji można skorzystać ze specjalnych narzędzi:

### KAPE

[KAPE](https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape) is a live data acquisition and analysis tool which can be used to acquire registry data. It is primarily a command-line tool but also comes with a GUI.

### Autopsy

[Autopsy](https://www.autopsy.com/)  gives you the option to acquire data from both live systems or from a disk image. After adding your data source, navigate to the location of the files you want to extract, then right-click and select the Extract File(s) option.

### FTK Imager

[FTK Imager](https://www.exterro.com/ftk-imager)  is similar to Autopsy and allows you to extract files from a disk image or a live system by mounting the said disk image or drive in FTK Imager.

### Odczyt rejestrów

Zdobyte przez te narzędzia nie pozwalają na odczytanie tych rejestrów, do tego potrzebny jest działający system, dlatego można skorzystać z:

[AccessData's Registry Viewer](https://accessdata.com/product-download/registry-viewer-2-0-0)  has a similar user interface to the Windows Registry Editor. There are a couple of limitations, though. It only loads one hive at a time, and it can't take the transaction logs into account.

Eric Zimmerman has developed a handful of [tools](https://ericzimmerman.github.io/#!index.md) that are very useful for performing Digital Forensics and Incident Response. One of them is the Registry Explorer.

[RegRipper](https://github.com/keydet89/RegRipper3.0) is a utility that takes a registry hive as input and outputs a report that extracts data from some of the forensically important keys and values in that hive. The output report is in a text file and shows all the results in sequential order.

### System infomation and system accounts

OS Version: `SOFTWARE\Microsoft\Windows NT\CurrentVersion`

Hives które mają indo do kontrolowania startupu są w `SYSTEM\ControlSet001` i  `SYSTEM\ControlSet002` In most cases (but not always), ControlSet001 will point to the Control Set that the machine booted with, and ControlSet002 will be the `last known good`  configuration.

Podczas działania systemu Windows tworzy `HKLM\SYSTEM\CurrentControlSet` Jest on dokładniejszy niż te poprzednie.  Żeby wiedzieć jaki controlset jest używany obecnie to info jest tutaj:  `SYSTEM\Select\Current`
Similarly, the `last known good` configuration can be found using the following registry value:
`SYSTEM\Select\LastKnownGood`

It is vital to establish this information before moving forward with the analysis.

### Nazwa komputera

`SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName`

### Strefa czasowa

`SYSTEM\CurrentControlSet\Control\TimeZoneInformation`

### Network interfaces and past networks

`SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces`
Each Interface is represented with a unique identifier (GUID) subkey, which contains values relating to the interface’s TCP/IP configuration. This key will provide us with information like IP addresses, DHCP IP address and Subnet Mask, DNS Servers, and more. This information is significant because it helps you make sure that you are performing forensics on the machine that you are supposed to perform it on.

Poprzednie połączenia sieciowe są w:

`SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged`

`SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Managed`

## Autostart (Autoruns)

Programy i polecenia odpalane przy logowaniu użytkownika

`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Run`

`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\RunOnce`

`SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce`

`SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer\Run`

`SOFTWARE\Microsoft\Windows\CurrentVersion\Run`

Usługi -In this registry key, if the `start`   key is set to 0x02, this means that this service will start at boot.
`SYSTEM\CurrentControlSet\Services`

### SAM hive and user information

SAM zawiera info o koncie użytkownika, informacje logowania, info grup.

`SAM\Domains\Account\Users`