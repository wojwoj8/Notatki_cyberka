SMB - Server message block - współdzielony dostęp do plików, drukarek itp. Jest to client-server. Działa na TCP/IP (actually NetBIOS over TCP/IP as specified in RFC1001 and RFC1002) Działa na Windows

### Enumeracja

**Enum4Linux**

Enum4linux is a tool used to enumerate SMB shares on both Windows and Linux systems. It is basically a wrapper around the tools in the Samba package and makes it easy to quickly extract information from the target pertaining to SMB. It's already installed on the AttackBox, however if you need to install it on your own attacking machine, you can do so from the official [github](https://github.com/portcullislabs/enum4linux).

The syntax of Enum4Linux is nice and simple: **"enum4linux [options] ip"**

**TAG**            **FUNCTION**

-U             get userlist  
-M             get machine list  
-N             get namelist dump (different from -U and-M)  
-S             get sharelist  
-P             get password policy information  
-G             get group and member list
-a             all of the above (full basic enumeration)