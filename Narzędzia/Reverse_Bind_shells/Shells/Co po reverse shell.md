Po reverse shell najczęściej szukać kluczy ssh `/home/<user>/.ssh`, szukać haseł gdzie indziej w jakiś plikach, niektóre exploity pozwalają na założenie swojego konta, szczególnie coś jak [Dirty C0w](https://dirtycow.ninja/) albo writeable `/etc/shadow` albo `/etc/passwd` co da na prosty dostęp do ssh jeżeli jest aktywne.

Na windows jest mniej opcji, czasami hasła są w działających usługach w rejestrze. Serwery VNC często zostawiają jawnie hasła w rejestrze. Niektóre wersje FileZilla ftp zostawiają hasła w xml w `C:\Program Files\FileZilla Server\FileZilla Server.xml` albo `C:\xampp\FileZilla Server\FileZilla Server.xml`. Mogą to być hashe MD5 albo tekst jawny zależnie od systemu.

Najlepiej na windowsie by było mieć shell odpalony jako SYSTEM albo administrator żeby mieć wysokie pozwolenia. W takiej sytuacji jest możliwe po prostu dodanie swojego konta do grupy administratorów na masynie i zalogowanie przez RDP, telnet, winexe, psexec, WinRM czy inną metodą. 
Syntax na windowsie dodawanie usera:
`net user <username> <password> /add`
`net localgroup administrators <username> /add`