Paczka narzędzi windows-based obejmująca:
- File and Disk Utilities
- Networking Utilities
- Process Utilities
- Security Utilities
- System Information
- Miscellaneous

[dokumentacja](https://learn.microsoft.com/en-us/sysinternals/downloads/) (fajne te narzędzia)

sigcheck - sprawdza wersję pliku,  timestamp, certyfikat i status na virusTotal pliku.

streams - pozwala zobaczyć inne strumienie danych, te streams Alternate Data Streams (ADS) - pozwalają na zawieranie dodatkowych danych w plikach i window explorer nie wyświetla ich.

czytanie ads - `more < path:stream`

SDelete - pozwala na usuwanie plików i folderów 

TCPView - pokazuje połączenia TCP i UDP, to samo jest już w windows pod `resmon` w cmd. 

Autoruns - bardzo dokładnie info o autostatcie aplikacji jak rejestry, path. sterowniki itp.

ProcDump - cli tool do monitorowania zużycia CPU przez aplikacje i następnie oceny czemu jest spike.


**Process Explorer** - było już wcześniej - można zamiast task managera używać


ProcessMonitor - "Process Monitor is an advanced monitoring tool for Windows that shows real-time file system, Registry and process/thread activity. It combines the features of two legacy Sysinternals utilities, Filemon and Regmon, and adds an extensive list of enhancements including rich and non-destructive filtering, comprehensive event properties such as session IDs and user names, reliable process information, full thread stacks with integrated symbol support for each operation, simultaneous logging to a file, and much more. Its uniquely powerful features will make Process Monitor a core utility in your system troubleshooting and malware hunting toolkit."

PsExec - narzędzie zastępujące telnet - pozwala na wykonywanie procesów na innych komputerach.

Sysmon - sytem monitor - zbiera informacje o systemie i wydarzeniach. 

WinObj - "**WinObj** is a 32-bit Windows NT program that uses the native Windows NT API (provided by NTDLL.DLL) to access and display information on the NT Object Manager's name space."

BgInfo - wyświetla informacje o systemie i rzeczach jak ip, nazwa komputera itp - robi to na tapecie, dobre do zarządzania wieloma systemami.

RegJump - odpala edytor rejestrów z terminala do explorera