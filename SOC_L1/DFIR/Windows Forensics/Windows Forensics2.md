### The File Allocation Table (FAT)

FAT wspiera następujące struktury danych:

Clusters - podstwatowa jednostka pamięci. Każdy plik przechowywany na urządzeniu pamięci masowej można traktować jako grupę klastrów zawierających fragmenty informacji.

Directory - Katalog zawiera informacje dotyczące identyfikacji plików, takie jak nazwa pliku, początkowy klaster i długość nazwy pliku.

File Allocation Table - jest linked list wszystkich klastrów. Zawiera ona status klastra oraz wskaźnik do następnego klastra w łańcuchu.

|   |   |   |   |
|---|---|---|---|
|**Attribute**|**FAT12**|**FAT16**|**FAT32**|
|**Addressable bits**|12|16|28|
|**Max number of clusters**|4,096|65,536|268,435,456|
|**Supported size of clusters**|512B - 8KB|2KB - 32KB|4KB - 32KB|
|**Maximum Volume size**|32MB|2GB|2TB|
Z fat32 jest tak, że windows ogranicza do 32GB ale jak się zrobi partycję na innym systemie z większą wartością niż 32GB to windows nie ma problemu. Na fat32 max file size to 4gb

The exFAT file system supports a cluster size of 4KB to 32MB. It has a maximum file size and a maximum volume size of 128PB (Petabytes). It also reduces some of the overheads of the FAT file system to make it lighter and more efficient. It can have a maximum of 2,796,202 files per directory.

### NTFS file system

Journaling - NTFS śledzi zmiany w metadanych partycji, są one w `$LOGFILE`
Access Control - W przeciwieństwie do FAT - NTFS posiada kontrolę dostępu do plików i folderów dla każdego usera (coś jak na linux)

Volume Shadow Copy - Można restore plików zrobić bo jest shadow copy, jak dysk przepiąłem z windowsa do linuxa to były tam pod $coś usunięte pliki.

Alternate Data Streams - A file is a stream of data organized in a file system. Alternate data streams (ADS) is a feature in NTFS that allows files to have multiple streams of data stored in a single file. Internet Explorer and other browsers use Alternate Data Streams to identify files downloaded from the internet (using the ADS Zone Identifier). Malware has also been observed to hide their code in ADS. 

Master File Table - Fat to file allocation table a to ma master file table, jest bardziej rozległe niż fat. Jest to ustrukturyzowana baza danych śledząca zmiany na partycji. Tam z punktu widzenia informatyki śledczej są ciekawe dane.

$MFT - pierwszy wpis na partycji, Volume Boot Record (VBR) wskazuje na cluster gdzie jest zlokalizowany. $MFT stores information about the clusters where all other objects present on the volume are located. This file contains a directory of all the files present on the volume.

$LOGFILE - The $LOGFILE stores the transactional logging of the file system. It helps maintain the integrity of the file system in the event of a crash.

$UsnFrnl -c It stands for the Update Sequence Number (USN) Journal. It is present in the $Extend record. It contains information about all the files that were changed in the file system and the reason for the change. It is also called the change journal.

### MFT Explorer

Narzędzie od Eric Zimmerman do ekploracji plików MFT. Wyciąga dane MFT z dysku np. do pliku CSV. MFTECmd.exe doesn't support $Logfile.

`MFTECmd.exe -f <path-to-$MFT-file> --csv <path-to-save-results-in-csv>`

Dalej output można w EZviewer

### Deleted files and data recovery

Można wykorzystać autopsy.

### Windows Prefetch files

Jak windows odpali program to zapisuje sobie informacje o nim, żeby szybciej odpalić następnym razem, To info jest w `C:\Windows\Prefetch`. Pliki tam mają rozszerzenie `.pf`  Prefetch files contain the last run times of the application, the number of times the application was run, and any files and device handles used by the file.

Program do tego PECmd.exe od Eric Zimmerman.

### Windows 10 Timeline

Windows 10 stores recently used applications and files in an SQLite database called the Windows 10 Timeline. This data can be a source of information about the last executed programs. It contains the application that was executed and the focus time of the application. 
`C:\Users\<username>\AppData\Local\ConnectedDevicesPlatform\{randomfolder}\ActivitiesCache.db`

Do tego WxTCmd.exe

### Windows Jump Lists

Windows introduced jump lists to help users go directly to their recently used files from the taskbar. We can view jumplists by right-clicking an application's icon in the taskbar, and it will show us the recently opened files in that application. Jumplists include information about the applications executed, first time of execution, and last time of execution of the application against an AppID.
`C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations`

Do tego JLECmd.exe

### Shortcut Files

Windows creates a shortcut file for each file opened either locally or remotely. The shortcut files contain information about the first and last opened times of the file and the path of the opened file, along with some other data. Shortcut files can be found in the following locations:

`C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\`

`C:\Users\<username>\AppData\Roaming\Microsoft\Office\Recent\`

Do tego LECmd.exe

### IE/Edge history

IE/Edge browsing history is that it includes files opened in the system as well, whether those files were opened using the browser or not.
`C:\Users\<username>\AppData\Local\Microsoft\Windows\WebCache\WebCacheV*.dat`
The files/folders accessed appear with a `file:///*` prefix in the IE/Edge history. Tutaj można autopsy do przeglądania webcache. W configure ingest trzeba zaznaczyć tylko recent activity.


When any new device is attached to a system, information related to the setup of that device is stored in the `setupapi.dev.log` - device serial number and the first/last times when the device was connected.

`C:\Windows\inf\setupapi.dev.log`