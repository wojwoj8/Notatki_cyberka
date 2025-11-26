
### Login/logout events

Można szukać po session opened, session closed, to samo logowanie sudo i cron

```bash
cat /var/log/auth.log | grep -E 'session opened|session closed'
```

Dla ssh jeszcze daemon loguje udane i nie udane próby.

```bash
cat /var/log/auth.log | grep "sshd" | grep -E 'Accepted|Failed'
```

### Różne

Różne polecenia np dodania usera to normalnie można szukać grepem po tym poleceniu.

```bash
cat /var/log/auth.log | grep -E '(passwd|useradd|usermod|userdel)\['
```

Jeszcze może być po sudo

```bash
cat /var/log/auth.log | grep -E 'COMMAND=
```

### Logi systemowe

- `/var/log/kern.log`: Kernel messages and errors, useful for more advanced investigations
- `/var/log/syslog (or /var/log/messages)`: A consolidated stream of various Linux events
- `/var/log/dpkg.log (or /var/log/apt)`: Package manager logs on Debian-based systems
- `/var/log/dnf.log (or /var/log/yum.log)`: Package manager logs on RHEL-based systems

### Logi aplikacji

W zależności od aplikacji mogą być logi baz danych czy serwerów webowych jak np. Nginx

```shell-session
cat /var/log/nginx/access.log
```

### Bash History

`history`

Historia poleceń w bashu czy innej powłoce to inna nazwa ale są w katalogu domowym pod `~./.bash_history` czy np. `~./.zsh_history`. Te logi jednak nie są takie usefull bo da się wykonać polecenia bez rejestrowania polecenia albo polecenia inicjowane przez OS, cron jobs czy web serwery nie są rejestrowane. 

```bash
# Attackers can simply add a leading space to the command to avoid being logged
ubuntu@thm-vm:~$  echo "You will never see me in logs!"

# Attackers can paste their commands in a script to hide them from Bash history
ubuntu@thm-vm:~$ nano legit.sh && ./legit.sh
 
# Attackers can use other shells like /bin/sh that don't save the history like Bash
ubuntu@thm-vm:~$ sh
$ echo "I am no longer tracked by Bash!"
```

### System calls

Jak dowolny program się wykonuje albo np. korzysta z kamery czy robi inne rzeczy to wykonywany jest syscall do kernela w celu wykonania tego zadania. Syscalli nie da się ominąć także warto je monitorować.

![](Attatchments/Pasted%20image%2020251125215635.png)

### Audit Deamon

"Auditd (Audit Daemon) is a built-in auditing solution often used by the SOC team for runtime monitoring." Instructions located in `/etc/audit/rules.d/` that define which system calls to monitor and which filters to apply

![](Attatchments/Pasted%20image%2020251125215907.png)

Można te logi zobaczyć real-time w `/var/log/audit/audit.log`, ale łatwiej przez `ausearch`. Przykład:

```
root@thm-vm:~$ ausearch -i -k proc_wget 
---- type=PROCTITLE msg=audit(08/12/25 12:48:19.093:2219) : proctitle=wget https://files.tryhackme.thm/report.zip type=CWD msg=audit(08/12/25 12:48:19.093:2219) : cwd=/root type=EXECVE msg=audit(08/12/25 12:48:19.093:2219) : argc=2 a0=wget a1=https://files.tryhackme.thm/report.zip type=SYSCALL msg=audit(08/12/25 12:48:19.093:2219) : arch=x86_64 syscall=execve [...] ppid=3752 pid=3888 auid=ubuntu uid=root tty=pts1 exe=/usr/bin/wget key=proc_wget
```

### Alternatywy dla Auditd

- [Sysmon for Linux](https://github.com/microsoft/SysmonForLinux): A perfect choice if you already work with Sysmon and love XML
- [Falco](https://falco.org/): A modern, open-source solution, ideal for monitoring containerized systems
- [Osquery](https://osquery.io/): An interesting tool that can be broadly used for various security purposes
- [EDRs](https://tryhackme.com/room/introductiontoedr): Most EDR solutions can track and monitor various Linux runtime events


