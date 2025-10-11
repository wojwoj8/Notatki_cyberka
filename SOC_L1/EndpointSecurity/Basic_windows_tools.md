- **TCPView** - Networking Utility tool.
- **Process Explorer** - Process Utility tool.

TCPView jest gui które pokazuje aktywne połączenia tcp i udp

Process Explorer - gui które składa się z dwóch okienek, aktywne procesy wraz z nazwą, właścicielem itp., 

Process Explorer enables you to inspect the details of a running process, such as:

- Associated services
- Invoked network traffic
- Handles such as files or directories opened
- DLLs and memory-mapped files loaded

## Windows Event Logs

Eventy są w `C:\Windows\System32\winevt\Logs
There are three main ways of accessing these event logs within a Windows system:

1. Event Viewer (GUI-based application)
2. Wevtutil.exe (command-line tool)
3. Get-WinEvent (PowerShell cmdlet)
## Sysmon

To co windows event logs ale dokładniejsze

## OSQuery

W powershellu - Można za pomocą SQL syntaxu sprawdzać endpointy, `select pid,name,path from processes where name='lsass.exe';`