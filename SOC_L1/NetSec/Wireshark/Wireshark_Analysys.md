## Nmap Scans

**TCP flags in a nutshell.**

|                                                                                          |                                                                                |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Notes**                                                                                | **Wireshark Filters**                                                          |
| Global search.                                                                           | - `tcp`<br><br>- `udp`                                                         |
| - Only SYN flag.<br>- SYN flag is set. The rest of the bits are not important.           | - `tcp.flags == 2`<br><br>- `tcp.flags.syn == 1`                               |
| - Only ACK flag.<br>- ACK flag is set. The rest of the bits are not important.           | - `tcp.flags == 16`<br><br>- `tcp.flags.ack == 1`                              |
| - Only SYN, ACK flags.<br>- SYN and ACK are set. The rest of the bits are not important. | - `tcp.flags == 18`<br><br>- `(tcp.flags.syn == 1) and (tcp.flags.ack == 1)`   |
| - Only RST flag.<br>- RST flag is set. The rest of the bits are not important.           | - `tcp.flags == 4`<br><br>- `tcp.flags.reset == 1`                             |
| - Only RST, ACK flags.<br>- RST and ACK are set. The rest of the bits are not important. | - `tcp.flags == 20`<br><br>- `(tcp.flags.reset == 1) and (tcp.flags.ack == 1)` |
| - Only FIN flag<br>- FIN flag is set. The rest of the bits are not important.            | - `tcp.flags == 1`<br><br>- `tcp.flags.fin == 1`                               |

### TCP Connect Scans  

**TCP Connect Scan in a nutshell:**

- Relies on the three-way handshake (needs to finish the handshake process).
- Usually conducted with `nmap -sT` command.
- Used by non-privileged users (only option for a non-root user).
- Usually has a windows size larger than 1024 bytes as the request expects some data due to the nature of the protocol.

|   |   |   |
|---|---|---|
|**Open TCP Port**|**Open TCP Port  <br>**|**Closed TCP Port**|
|- SYN --><br>- <-- SYN, ACK<br>- ACK -->|- SYN --><br>- <-- SYN, ACK<br>- ACK --><br>- RST, ACK -->|- SYN --><br>- <-- RST, ACK|
`tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size > 1024`
### TCP SYN Scan in a nutshell:

- Doesn't rely on the three-way handshake (no need to finish the handshake process).
- Usually conducted with `nmap -sS` command.
- Used by privileged users.
- Usually have a size less than or equal to 1024 bytes as the request is not finished and it doesn't expect to receive data.

|   |   |
|---|---|
|**Open TCP Port**|**Close TCP Port**|
|- SYN --><br>- <-- SYN,ACK<br>- RST-->|- SYN --><br>- <-- RST,ACK|

### UDP Scans  

UDP Scan in a nutshell:

- Doesn't require a handshake process
- No prompt for open ports
- ICMP error message for close ports
- Usually conducted with `nmap -sU` command.

|   |   |
|---|---|
|Open UDP Port|Closed UDP Port|
|- UDP packet -->|- UDP packet --><br>- ICMP Type 3, Code 3 message. (Destination unreachable, port unreachable)|
UDP close port: `icmp.type==3 and icmp.code==3`

## ARP Poisoning/Spoofing (A.K.A. Man In The Middle Attack)

**ARP analysis in a nutshell:**

- Works on the local network
- Enables the communication between MAC addresses
- Not a secure protocol
- Not a routable protocol
- It doesn't have an authentication function
- Common patterns are request & response, announcement and gratuitous packets.

|                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Notes**                                                                                                                                                                                                                                          | **Wireshark filter**                                                                                                                                                                                                                                   |
| Global search                                                                                                                                                                                                                                      | - `arp`                                                                                                                                                                                                                                                |
| "ARP" options for grabbing the low-hanging fruits:<br><br>- Opcode 1: ARP requests.<br>- Opcode 2: ARP responses.<br>- **Hunt:** Arp scanning<br>- **Hunt:** Possible ARP poisoning detection<br>- **Hunt:** Possible ARP flooding from detection: | - `arp.opcode == 1`<br><br>- `arp.opcode == 2`<br><br>- `arp.dst.hw_mac==00:00:00:00:00:00`<br><br>- `arp.duplicate-address-detected or arp.duplicate-address-frame`<br><br>- `((arp) && (arp.opcode == 1)) && (arp.src.hw_mac == target-mac-address)` |


|                                |                                                                                                                              |                                                                                                                                         |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Notes**                      | Detection Notes                                                                                                              | **Findings**                                                                                                                            |
| Possible IP address match.     | 1 IP address announced from a MAC address.                                                                                   | - MAC: 00:0c:29:e2:18:b4<br>- IP: 192.168.1.25                                                                                          |
| Possible ARP spoofing attempt. | 2 MAC addresses claimed the same IP address (192.168.1.1).  <br>The " 192.168.1.1" IP address is a possible gateway address. | - MAC1: 50:78:b3:f3:cd:f4<br>- MAC 2: 00:0c:29:e2:18:b4                                                                                 |
| Possible ARP flooding attempt. | The MAC address that ends with "b4" claims to have a different/new IP address.                                               | - MAC: 00:0c:29:e2:18:b4<br>- IP: 192.168.1.1                                                                                           |

|                                |                                                                                                                              |                                                                                                                                         |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Notes**                      | Detection Notes                                                                                                              | **Findings**                                                                                                                            |
| IP to MAC matches.             | 3  IP to MAC address matches.                                                                                                | - MAC: 00:0c:29:e2:18:b4 = IP: 192.168.1.25<br>- MAC: 50:78:b3:f3:cd:f4 = IP: 192.1681.1<br>- MAC: 00:0c:29:98:c7:a8 = IP: 192.168.1.12 |
| Attacker                       | The attacker created noise with ARP packets.                                                                                 | - MAC: 00:0c:29:e2:18:b4 = IP: 192.168.1.25                                                                                             |
| Router/gateway                 | Gateway address.                                                                                                             | - MAC: 50:78:b3:f3:cd:f4 = IP: 192.1681.1                                                                                               |
| Victim                         | The attacker sniffed all traffic of the victim.                                                                              | - MAC: 50:78:b3:f3:cd:f4 = IP: 192.1681.12                                                                                              |

##  Identifying Hosts

Protocols that can be used in Host and User identification:

- Dynamic Host Configuration Protocol (DHCP) traffic
- NetBIOS (NBNS) traffic 
- Kerberos traffic

### DHCP Analysis

**DHCP investigation in a nutshell:**

|   |   |
|---|---|
|**Notes**|**Wireshark Filter**|
|Global search.|- `dhcp` or `bootp`|
|Filtering the proper DHCP packet options is vital to finding an event of interest.   <br>  <br><br>- **"DHCP Request"** packets contain the hostname information<br>- **"DHCP ACK"** packets represent the accepted requests<br>- **"DHCP NAK"** packets represent denied requests<br><br>Due to the nature of the protocol, only "Option 53" ( request type) has predefined static values. You should filter the packet type first, and then you can filter the rest of the options by "applying as column" or use the advanced filters like "contains" and "matches".|- Request: `dhcp.option.dhcp == 3`<br><br>- ACK: `dhcp.option.dhcp == 5`<br><br>- NAK: `dhcp.option.dhcp == 6`|
|**"DHCP Request"** options for grabbing the low-hanging fruits:<br><br>- **Option 12:** Hostname.<br>- **Option 50:** Requested IP address.<br>- **Option 51:** Requested IP lease time.<br>- **Option 61:** Client's MAC address.|- `dhcp.option.hostname contains "keyword"`|
|**"DHCP ACK"** options for grabbing the low-hanging fruits:<br><br>- **Option 15:** Domain name.<br>- **Option 51:** Assigned IP lease time.|- `dhcp.option.domain_name contains "keyword"`|
|**"DHCP NAK"** options for grabbing the low-hanging fruits:<br><br>- **Option 56:** Message (rejection details/reason).|As the message could be unique according to the case/situation, It is suggested to read the message instead of filtering it. Thus, the analyst could create a more reliable hypothesis/result by understanding the event circumstances.|
### NetBIOS (NBNS) Analysis

**NetBIOS** or **Net**work **B**asic **I**nput/**O**utput **S**ystem is the technology responsible for allowing applications on different hosts to communicate with each other. 

**NBNS investigation in a nutshell:**

|                                                                                                                                                                                 |                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **Notes**                                                                                                                                                                       | **Wireshark Filter**             |
| Global search.                                                                                                                                                                  | - `nbns`                         |
| "NBNS" options for grabbing the low-hanging fruits:<br><br>- **Queries:** Query details.<br>- Query details could contain **"name, Time to live (TTL) and IP address details"** | - `nbns.name contains "keyword"` |

### Kerberos Analysis  

**Kerberos** is the default authentication service for Microsoft Windows domains. It is responsible for authenticating service requests between two or more computers over the untrusted network. The ultimate aim is to prove identity securely.  

**Kerberos investigation in a nutshell:**

|                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Notes**                                                                                                                                                                                                                                                                                                                                                                           | **Wireshark Filter**                                                                                               |
| Global search.                                                                                                                                                                                                                                                                                                                                                                      | - `kerberos`                                                                                                       |
| User account search:<br><br>- **CNameString:** The username.<br><br>**Note:** Some packets could provide hostname information in this field. To avoid this confusion, filter the **"$"** value. The values end with **"$"** are hostnames, and the ones without it are user names.                                                                                                  | - `kerberos.CNameString contains "keyword"` <br>- `kerberos.CNameString and !(kerberos.CNameString contains "$" )` |
| "Kerberos" options for grabbing the low-hanging fruits:<br><br>- **pvno:** Protocol version.<br>- **realm:** Domain name for the generated ticket.  <br>    <br>- **sname:** Service and domain name for the generated ticket.<br>- **addresses:** Client IP address and NetBIOS name.  <br>    <br><br>**Note:** the "addresses" information is only available in request packets. | - `kerberos.pvno == 5`<br><br>- `kerberos.realm contains ".org"` <br><br>- `kerberos.SNameString == "krbtg"`       |

## Tunnelling Traffic: ICMP and DNS   

Traffic tunnelling is (also known as **"port forwarding"**) transferring the data/resources in a secure method to network segments and zones. It can be used for "internet to private networks" and "private networks to internet" flow/direction. There is an encapsulation process to hide the data, so the transferred data appear natural for the case, but it contains private data packets and transfers them to the final destination securely.

### ICMP Analysis

|                                                                                                                                                                          |                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| **Notes**                                                                                                                                                                | **Wireshark filters**      |
| Global search                                                                                                                                                            | - `icmp`                   |
| "ICMP" options for grabbing the low-hanging fruits:<br><br>- Packet length.<br>- ICMP destination addresses.  <br>    <br>- Encapsulated protocol signs in ICMP payload. | - `data.len > 64 and icmp` |

## DNS Analysis

|                                                                                                                                                                                                                                                                                                                                                                                           |                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Notes**                                                                                                                                                                                                                                                                                                                                                                                 | **Wireshark Filter**                                                 |
| Global search                                                                                                                                                                                                                                                                                                                                                                             | - `dns`                                                              |
| "DNS" options for grabbing the low-hanging fruits:<br><br>- Query length.<br>- Anomalous and non-regular names in DNS addresses.<br>- Long DNS addresses with encoded subdomain addresses.<br>- Known patterns like dnscat and dns2tcp.<br>- Statistical analysis like the anomalous volume of DNS requests for a particular target.<br><br>**!mdns:** Disable local link device queries. | - `dns contains "dnscat"`<br><br>- `dns.qry.name.len > 15 and !mdns` |

## FTP Analysis   

File Transfer Protocol (FTP) is designed to transfer files with ease, so it focuses on simplicity rather than security. As a result of this, using this protocol in unsecured environments could create security issues like:

- MITM attacks
- Credential stealing and unauthorised access
- Phishing
- Malware planting
- Data exfiltration

**FTP analysis in a nutshell:**

|                                                                                                                                                                                                                                                         |                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Notes**                                                                                                                                                                                                                                               | **Wireshark Filter**                                                                                                                                                                          |
| Global search                                                                                                                                                                                                                                           | - `ftp`                                                                                                                                                                                       |
| **"FTP"** options for grabbing the low-hanging fruits:<br><br>- **x1x series:** Information request responses.<br>- **x2x series:** Connection messages.<br>- **x3x series:** Authentication messages.<br><br>**Note:** "200" means command successful. | **---**                                                                                                                                                                                       |
| "x1x" series options for grabbing the low-hanging fruits:<br><br>- **211:** System status.<br>- **212:** Directory status.<br>- **213:** File status                                                                                                    | - `ftp.response.code == 211`                                                                                                                                                                  |
| "x2x" series options for grabbing the low-hanging fruits:<br><br>- **220:** Service ready.<br>- **227:** Entering passive mode.<br>- **228:** Long passive mode.<br>- **229:** Extended passive mode.                                                   | - `ftp.response.code == 227`                                                                                                                                                                  |
| "x3x" series options for grabbing the low-hanging fruits:<br><br>- **230:** User login.<br>- **231:** User logout.<br>- **331:** Valid username.<br>- **430:** Invalid username or password<br>- **530:** No login, invalid password.                   | - `ftp.response.code == 230`                                                                                                                                                                  |
| "FTP" commands for grabbing the low-hanging fruits:<br><br>- **USER:** Username.<br>- **PASS:** Password.<br>- **CWD:** Current work directory.<br>- **LIST:** List.                                                                                    | - `ftp.request.command == "USER"`<br><br>- `ftp.request.command == "PASS"`<br><br>- `ftp.request.arg == "password"`                                                                           |
| Advanced usages examples for grabbing low-hanging fruits:<br><br>- **Bruteforce signal:** List failed login attempts.<br>- **Bruteforce signal:** List target username.<br>- **Password spray signal:** List targets for a static password.             | - `ftp.response.code == 530`<br><br>- `(ftp.response.code == 530) and (ftp.response.arg contains "username")`<br><br>- `(ftp.request.command == "PASS" ) and (ftp.request.arg == "password")` |

## HTTP Analysis

Analizą można wykryć:
- Phishing pages
- Web attacks
- Data exfiltration
- Command and control traffic (C2)

|   |   |
|---|---|
|**Notes**|**Wireshark Filter**|
|Global search<br><br>**Note:** HTTP2 is a revision of the HTTP protocol for better performance and security. It supports binary data transfer and request&response multiplexing.|- `http`<br><br>- `http2`|
|"HTTP **Request Methods"** for grabbing the low-hanging fruits:<br><br>- GET<br>- POST<br>- Request: Listing all requests|- `http.request.method == "GET"`<br><br>- `http.request.method == "POST"`<br><br>- `http.request`|
|"HTTP Response Status Codes" for grabbing the low-hanging fruits:<br><br>- **200 OK:** Request successful.<br>- **301 Moved Permanently:** Resource is moved to a new URL/path (permanently).<br>- **302 Moved Temporarily:** Resource is moved to a new URL/path (temporarily).<br>- **400 Bad Request:** Server didn't understand the request.<br>- **401 Unauthorised:** URL needs authorisation (login, etc.).<br>- **403 Forbidden:** No access to the requested URL. <br>- **404 Not Found:** Server can't find the requested URL.<br>- **405 Method Not Allowed:** Used method is not suitable or blocked.<br>- **408 Request Timeout:**  Request look longer than server wait time.<br>- **500 Internal Server Error:** Request not completed, unexpected error.<br>- **503 Service Unavailable:** Request not completed server or service is down.|- `http.response.code == 200`<br><br>- `http.response.code == 401`<br><br>- `http.response.code == 403`<br><br>- `http.response.code == 404`<br><br>- `http.response.code == 405`<br><br>- `http.response.code == 503`|
|"HTTP Parameters" for grabbing the low-hanging fruits:<br><br>- **User agent:** Browser and operating system identification to a web server application.<br>- **Request URI:** Points the requested resource from the server.  <br>    <br>- **Full *URI:** Complete URI information.<br><br>***URI:** Uniform Resource Identifier.|- `http.user_agent contains "nmap"`<br><br>- `http.request.uri contains "admin"`<br><br>- `http.request.full_uri contains "admin"`|
|"HTTP Parameters" for grabbing the low-hanging fruits:<br><br>- **Server:** Server service name.  <br>    <br>- **Host:** Hostname of the server<br>- **Connection:** Connection status.  <br>    <br>- **Line-based text data:** Cleartext data provided by the server.<br>- **HTML Form URL Encoded:** Web form information.|- `http.server contains "apache"`<br><br>- `http.host contains "keyword"`<br><br>- `http.host == "keyword"`<br><br>- `http.connection == "Keep-Alive"`<br><br>- `data-text-lines contains "keyword"`|

## User Agent Analysis

[Lista user-agentów](https://explore.whatismybrowser.com/useragents/explore/)

|                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Notes**                                                                                                                                                                                                                                                                                                                                                                                                            | **Wireshark Filter**                                                                                                                                     |
| Global search.                                                                                                                                                                                                                                                                                                                                                                                                       | - `http.user_agent`                                                                                                                                      |
| Research outcomes for grabbing the low-hanging fruits:<br><br>- Different user agent information from the same host in a short time notice.<br>- Non-standard and custom user agent info.<br>- Subtle spelling differences. **("Mozilla" is not the same as  "Mozlilla" or "Mozlila")**<br>- Audit tools info like Nmap, Nikto, Wfuzz and sqlmap in the user agent field.<br>- Payload data in the user agent field. | - `(http.user_agent contains "sqlmap") or (http.user_agent contains "Nmap") or (http.user_agent contains "Wfuzz") or (http.user_agent contains "Nikto")` |


## Log4j Analysis

|                                                                                                                                                                                               |                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Notes**                                                                                                                                                                                     | **Wireshark Filters**                                                                                                                                                                                                                        |
| **Research outcomes** for grabbing the low-hanging fruits:<br><br>- The attack starts with a "POST" request<br>- There are known cleartext patterns: "**jndi:ldap**" and "**Exploit.class**". | - `http.request.method == "POST"`<br><br>- `(ip contains "jndi") or ( ip contains "Exploit")`<br><br>- `(frame contains "jndi") or ( frame contains "Exploit")`<br><br>- `(http.user_agent contains "$") or (http.user_agent contains "==")` |

## HTTPS

|   |   |
|---|---|
|Notes|Wireshark Filter|
|"HTTPS Parameters" for grabbing the low-hanging fruits:<br><br>- **Request:** Listing all requests  <br>    <br>- **TLS:** Global TLS search<br>- TLS Client Request<br>- TLS Server response<br>- Local Simple Service Discovery Protocol (SSDP)<br><br>**Note:** SSDP is a network protocol that provides advertisement and discovery of network services.|- `http.request`<br><br>- `tls`<br><br>- `tls.handshake.type == 1`<br><br>- `tls.handshake.type == 2`<br><br>- `ssdp`|

HTTPS korzysta z TLS, które ma też "handshake". Pierwsze dwa kroki to 
- Client Hello: `(http.request or tls.handshake.type == 1) and !(ssdp)` 
- Server Hello: `(http.request or tls.handshake.type == 2) and !(ssdp)`'

Żeby analizować ruch HTTPS trzeba go odszyfrować i to robi się pobierając z przeglądarki key log file.

Dodawanie klucza do wireshark:

![](Attachments/{27DB7447-89CE-4664-B663-A4DE3BCAF3FB}.png)

Dalej ruch będzie widziany jako HTTP2 protocol.

W zakładce tools można wyciągnąć hasła

![](Attachments/{5C51E3B9-9F6D-4388-913F-40788D62234C}%201.png)

Wireshark może tworzyć zasady ACL dla:
- Netfilter (iptables)
- Cisco IOS (standard/extended)
- IP Filter (ipfilter)
- IPFirewall (ipfw)
- Packet filter (pf)
- Windows Firewall (netsh new/old format)
![](Attachments/{B1CABE12-9B1F-4774-9E9C-F44445A24523}.png)

