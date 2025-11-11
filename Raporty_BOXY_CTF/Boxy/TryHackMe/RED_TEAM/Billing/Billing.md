# **Nmap Results**
```text
# Nmap 7.95 scan initiated Tue Nov 11 19:25:11 2025 as: /usr/lib/nmap/nmap --privileged -Pn -sV --min-rate=2000 -p- -sC -oN nmap_scan.txt 10.10.29.38
Nmap scan report for 10.10.29.38
Host is up (0.042s latency).
Not shown: 65531 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 9.2p1 Debian 2+deb12u6 (protocol 2.0)
| ssh-hostkey: 
|   256 60:66:ec:17:a2:e1:ce:da:8e:b8:f3:b8:bd:0f:8e:6b (ECDSA)
|_  256 7d:09:8c:6b:99:40:5d:23:e3:00:c7:cd:60:18:a2:c0 (ED25519)
80/tcp   open  http     Apache httpd 2.4.62 ((Debian))
| http-title:             MagnusBilling        
|_Requested resource was http://10.10.29.38/mbilling/
| http-robots.txt: 1 disallowed entry 
|_/mbilling/
|_http-server-header: Apache/2.4.62 (Debian)
3306/tcp open  mysql    MariaDB 10.3.23 or earlier (unauthorized)
5038/tcp open  asterisk Asterisk Call Manager 2.10.6
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Nov 11 19:25:49 2025 -- 1 IP address (1 host up) scanned in 38.39 seconds
```

# **Service Enumeration**

## **TCP/22**
SSH

## **TCP/80**
Na porcie 80 znajduje się aplikacja internetowa na serwerze Apache/2.4.62(Debian). Ta aplikacja to MagnusBilling - "Voip sistem to Asterisk."

![](Attatchments/Pasted%20image%2020251111192830.png)
W pliku `robots.txt` nie ma nic ciekawego

```
User-agent: *
Disallow: /mbilling/
```

W pliku `README.md` można się dowiedziećm że jest to aplikacja w wersji 7

![](Attatchments/Pasted%20image%2020251111201113.png)

## **TCP/3306**
Na tym porcie znajduje się baza danych MariaDB w wersji 10.3.23 lub wcześniejsza. Do zalogowania potrzebne jest hasło.

![](Attatchments/Pasted%20image%2020251111193401.png)


## **TCP/5038**
Na tym porcie jest Asterisk Call Manager 2.10.6. Jest to interfejs który umożliwia zdalne zarządzanie systemem telefonicznym Asterisk. Pozwala na automatyzację i zdalną kontrolę nad systemem. Usługa umozliwiająca integrację systemu telefonicznego z innymi zewnętrznymi usługami i systemami. Obsługuje protoków AMI, dzięki temu API można obsługiwać z języków PHP, Python, Java, Ruby i inne.


# **Exploit**

Szukając na metasploit exploit na Asterisk znalazłem [exploit](https://nvd.nist.gov/vuln/detail/CVE-2023-30258) do tej aplikacji internetowej. Ten exploit pozwala na conmand injection w wersjach 6.x, 7.x tej aplikacji co umożliwia wykonywanie poleceń przez nieuwierzytelnione zapytania HTTP. Wszystko przez kod w bibliotece `lib/icepay/icepay.php`, która odnosi się do funkcji `exec()` w php. Parametr exec() zawiera parametr GET „democ”, który jest kontrolowany przez użytkownika i nie jest odpowiednio sanitowany/escapowany. Po pomyślnym wykorzystaniu luki nieautoryzowany użytkownik może wykonać dowolne polecenia.

![](Attatchments/Pasted%20image%2020251111201953.png)

# **Post-Exploit Enumeration**
## **Operating Environment**
### OS & Kernel

```text
  - "uname -a" 
Linux ip-10-10-29-38 6.1.0-37-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.140-1 (2025-05-22) x86_64 GNU/Linux
  - "cat /etc/os-release" 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

- "env"
      
PWD=/var
SYSTEMD_EXEC_PID=854
APACHE_LOG_DIR=/var/log/apache2
LANG=C
INVOCATION_ID=24432921784f42a197cbf96fe2bf2c50
APACHE_PID_FILE=/var/run/apache2/apache2.pid
TERM=xterm
APACHE_RUN_GROUP=www-data
APACHE_LOCK_DIR=/var/lock/apache2
SHLVL=1
LC_CTYPE=C.UTF-8
APACHE_RUN_DIR=/var/run/apache2
JOURNAL_STREAM=8:15179
APACHE_RUN_USER=www-data
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
_=/usr/bin/env
OLDPWD=/var/lib

```


### User Asterisk

```text
  - "id" uid=1001(asterisk) gid=1001(asterisk) groups=1001(asterisk)
  - "sudo -l" 
    Matching Defaults entries for asterisk on ip-10-10-29-38:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

Runas and Command-specific defaults for asterisk:
    Defaults!/usr/bin/fail2ban-client !requiretty

User asterisk may run the following commands on ip-10-10-29-38:
    (ALL) NOPASSWD: /usr/bin/fail2ban-client
```


### /var/lib/asterisk/astdb.sqlite3

Zawartość bazy danych (tabeli astdb) astdb.sqlite3
```
/pbx/UUID|b6b87109-7097-4d85-ae26-9a33d60482bb
/dundi/secret|JY3GLK+W8Qrs6uJyPIleHw==;vpL+GIWz4CeTkfwD8P8SdA==
/dundi/secretexpiry|1762892511
```


# **Privilege Escalation**  

Polecenie `sudo -l` zwraca informację o tym, że można odpalić z prawami roota aplikację `fail2ban-client` na koncie asterisk.

```
User asterisk may run the following commands on ip-10-10-29-38:
    (ALL) NOPASSWD: /usr/bin/fail2ban-client
```

Korzystając z https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/fail2ban-command/ udało mi się zdobyć konto roota. Należało dodać akcję do "jail" na metodzie ban i wykonać ją. Tą akcją było `chmod +s /bin/bash`. To dało dostęp do roota.

![](Attatchments/Pasted%20image%2020251111214745.png)

# **Flags**

Pierwsza flaga znajduje się w folderze `/home/magnus`

![](Attatchments/Pasted%20image%2020251111202217.png)

### User

```text
THM{4a6831d5f124b25eefb1e92e0f0da4ca}
```


![](Attatchments/Pasted%20image%2020251111214959.png)

### Root

```text
THM{33ad5b530e71a172648f424ec23fae60}
```


<br>
<br>
