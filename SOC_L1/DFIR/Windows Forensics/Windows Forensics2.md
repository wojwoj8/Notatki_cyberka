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