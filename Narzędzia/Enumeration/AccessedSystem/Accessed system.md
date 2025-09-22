Po zdobyciu dostępu do systemu warto wykonać następującą enumerację:

## hostname
Polecenie `hostname` zwróci nazwę hosta 
```
wade7363
```

## uname -a 
Wypisze informacje o systemie takie jak kernel

```
Linux wade7363 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
```

## /proc/version

Informacje o wersji kernela, informacje np jaki compiler jest zainstalowany
```
Linux version 3.13.0-24-generic (buildd@panlong) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014
```

## /etc/issue

Pokazuje nazwę systemu ale może być zmienione.
```
Ubuntu 14.04 LTS \n \l
```

## polecenie ps

Wypisuje procesy na komputerze, output zawiera informaje jak:
- PID - id procesu
- TTY - typ terminalu użytego przez użytkownika
- Time - czas poświęcony przez procesor na proces (NIE JEST TO CZAS DZIAŁANIA PROCESU)
- CMD - polecenie lub działający program (executable) (NIE WYŚWIETLI PARAMETRÓW CLI)
Można wyświetlić wszystkie procesy `ps -A` albo drzewo procesów `ps axjf`

Jeszcze `ps aux` wyświetli procesy wszystkich użytkowników (a), użytkownika który odpalił proces (u) i pokaże procesy które nie są przypisane do terminala (x)

## env
Wszystkie zmienne środowiskowe
```
XDG_SESSION_ID=1
SHELL=/bin/sh
TERM=xterm-256color
SSH_CLIENT=10.21.251.149 42478 22
SSH_TTY=/dev/pts/4
USER=karen
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
MAIL=/var/mail/karen
QT_QPA_PLATFORMTHEME=appmenu-qt5
PWD=/
LANG=en_US.UTF-8
SHLVL=1
HOME=/home/karen
LOGNAME=karen
SSH_CONNECTION=10.21.251.149 42478 10.10.63.104 22
XDG_RUNTIME_DIR=/run/user/1001
_=/usr/bin/env
```

Zmienna PATH może mieć kompiler albo język skryptowy jak python który może odpalać kod na systemie i prowadzić do privilege escalation.

## sudo -l

System może mieć konfigurację pozwalającą uźytkownikowi na odpalanie z pozwoleniami root, polecenie sudo -l można wykorzystać żeby zobaczyć wszystkie polecenia działające jako sudo dla użytkownika

## ls

Wyświetlanie plików w folderze, `ls -la` pokazuje wszystko i dostęp do plików.

# id
Pokazuje poziom uprawnień i członkostwo grup, można sprawdzić innych użytkowników za pomocą `id nazwa_innego_usera`
```
uid=1001(karen) gid=1001(karen) groups=1001(karen)
```

## /etc/passwd

Pokazuje uzytkowników systemu, warto użyć `grep` do filtrowania, z reguły użytkownicy będą mieli folder domowy `/home` i powłokę `/bin/bash` albo inną

## history
Historia wykonanych poleceń na systemie

## ifconfig

Informacje o sieci

## netstat

Wyświetla istniejące połączenia sieciowe, warto korzystać z:
- `netstat -a`: wszystkie nasłuchujące porty ustalonych połączeń
- `netstat -at` albo `netstat -au` wszystkie protokoły TCP i kolejno UDP
- `netstat -l`: wszystkie porty w stanie "listening", gotowe do akceptacji nadchodzących połączeń, można z parametrem `t` żeby pokazać same TCP
- `netstat -s`: statystyki zużycia sieci przez protokoły, `-t` TCP, `-u` UDP
- `netstat -tp` wszystkie połączenia z nazwą serwisu i PID, dodanie `l` pokaże nasłuchujące porty, jak proces innego użytkownika to nie widać tego PID/ Program Name, root może zobaczyć wszystko
- `netstat -i`: pokazuje statystyki dla interfejsów, np. eth0, tun0
- ### `netstat -ano` **BARDZO POPULARNE W CTF**:
	- -a - wyświetla wszystkie sockety
	- -n do not resolve names (pewnie chodzi o to że nie zmienia ip na nazwy dns)
	- -o wyświetla timer

## find

Polecenie find wyszukuje pliki, foldery, z pozwoleniami, treścią itp. Przykłady:
- `find . -name flag1.txt`: find the file named “flag1.txt” in the current directory
- `find /home -name flag1.txt`: find the file names “flag1.txt” in the /home directory
- `find / -type d -name config`: find the directory named config under “/”
- `find / -type f -perm 0777`: find files with the 777 permissions (files readable, writable, and executable by all users)
- `find / -perm a=x`: find executable files
- `find /home -user frank`: find all files for user “frank” under “/home”
- `find / -mtime 10`: find files that were modified in the last 10 days
- `find / -atime 10`: find files that were accessed in the last 10 day
- `find / -cmin -60`: find files changed within the last hour (60 minutes)
- `find / -amin -60`: find files accesses within the last hour (60 minutes)
- `find / -size 50M`: find files with a 50 MB size
-size można dać + i - do szukania więcej/mniej czyli np `find / -size +20M`

PRZEKIEROWANIE BŁĘDÓW NP PERMISSION DENIED ŻEBY NIE WYŚWIETLAŁY SIĘ:
- `find coś tam coś tam 2>/dev/null`

Foldery i pliki do których można zapisywać albo wykonywać z nich executables:
- `find / -writable -type d 2>/dev/null` : Find world-writeable folders
- `find / -perm -222 -type d 2>/dev/null`: Find world-writeable folders
- `find / -perm -o w -type d 2>/dev/null`: Find world-writeable folders
- `find / -perm -o x -type d 2>/dev/null` : Find world-executable folders

Znalezienie narzędzi deweloperskich i wspieranych języków (programowania)
- `find / -name perl*`
- `find / -name python*`
- `find / -name gcc*`

Znalezienie konkretnych pozwoleń plików:

Znalezienie plików z bitem SUID - pliki które można wykonywać z pozwoleniami użytkownika który ten bit ustawił `find / -perm -u=s -type f 2>/dev/null`

# Inne przydatne polecenia
- `locate` - szuka plików po nazwie
- `grep` 
- `cut`
- `sort`
