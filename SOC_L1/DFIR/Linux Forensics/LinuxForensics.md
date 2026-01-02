### OS

Info o OS w `/etc/os-release`

### User accounts, groups

`/etc/passwd`, `/etc/shadow`, `/home`, `/etc/group`

### User accounts

Użytkownicy z prawami sudo w `/etc/sudoers`

### Login information

W `/var/log` są rózne pliki jak wtmp, btmp. The `btmp` file saves information about failed logins, while the `wtmp` keeps historical data of logins. Je można wyczytać poleceniem `last -f plik`

### Authentication logs

Uwierzytelnianie userów na systemie. W `/var/log/auth.log`

### Active network connections

Są pod `netstat`, np. `netstat -natp`

### Running processes

`ps -aux`

### DNS

`/etc/hosts`
The information about DNS servers that a Linux host talks to for DNS resolution is stored in the resolv.conf file. Its location is `/etc/resolv.conf`.

### Persistance mechanisms

Oznacza, że program będzie działał po restarcie systemu.

#### Cron jobs

Polecenia które mają się wykonywać co określony czas `/etc/crontab`

#### Service startup

Programy działające w tle po starcie systemu  - folder=`/etc/init.d`

#### .Bashrc

System-wide settings are stored in `/etc/bash.bashrc` and `/etc/profile` files

### Evidence of execution

#### Sudo execution history

Są w `/var/log/auth.log*` bo trzeba się uwierzytelniać do użycia sudo.
Przykład `cat /var/log/auth.log* |grep -i COMMAND|tail`

#### Bash history

Historia poleceń, czasami hasła mogą tam być - `cat ~/.bash_history`

#### Files accessed using vim

`cat ~/.viminfo`

### Log files

#### Syslog

Contains messages that are recorded by the host about system activity. The detail which is recorded in these messages is configurable through the logging level.

##### Third-party logs

W `/var/log`, logi różnych aplikacji.

- `/var/log/messages` - a general log for Linux systems
- `/var/log/auth.log` - a log file that lists all authentication attempts (Debian-based systems)
- `/var/log/secure` - a log file that lists all authentication attempts (Red Hat and Fedora-based systems)
- `/var/log/utmp` - an access log that contains information regarding users that are currently logged into the system
- `/var/log/wtmp` - an access log that contains information for all users that have logged in and out of the system
- `/var/log/kern.log` - a log file containing messages from the kernel
- `/var/log/boot.log` - a log file that contains start-up messages and boot information