![](Attatchments/Pasted%20image%2020251101144523.png)

![](Attatchments/Pasted%20image%2020251101144545.png)

irewalls focus on layers 3 and 4 and, to a lesser extent, layer 2. Next-generation firewalls are also designed to cover layers 5, 6, and 7. The more layers a firewall can inspect, the more sophisticated it gets and the more processing power it needs.

![](Attatchments/Pasted%20image%2020251101151749.png)

Taktyki nmap na oszukanie systemu

| Evasion Approach                              | Nmap Argument                             |
| --------------------------------------------- | ----------------------------------------- |
| Hide a scan with decoys                       | `-D DECOY1_IP1,DECOY_IP2,ME`              |
| Hide a scan with random decoys                | `-D RND,RND,ME`                           |
| Use an HTTP/SOCKS4 proxy to relay connections | `--proxies PROXY_URL`                     |
| Spoof source MAC address                      | `--spoof-mac MAC_ADDRESS`                 |
| Spoof source IP address                       | `-S IP_ADDRESS`                           |
| Use a specific source port number             | `-g PORT_NUM` or `--source-port PORT_NUM` |

| Evasion Approach                | Nmap Argument       |
| ------------------------------- | ------------------- |
| Fragment IP data into 8 bytes   | `-f`                |
| Fragment IP data into 16 bytes  | `-ff`               |
| Fragment packets with given MTU | `--mtu VALUE`       |
| Specify packet length           | `--data-length NUM` |

| Evasion Approach                           | Nmap Argument          |
| ------------------------------------------ | ---------------------- |
| Set IP time-to-live field                  | `--ttl VALUE`          |
| Send packets with specified IP options     | `--ip-options OPTIONS` |
| Send packets with a wrong TCP/UDP checksum | `--badsum`             |

### Evasion using port hopping

Polega to na tym, że aplikacja skacze po różnych portach aż nie znajdzie takiego, z którym będzie mieć stabilne połączenie. Istnieje jeszcze taki port hopping, gdzie aplikacja utrzymuje połączenie na jednym porcie a wysyła dane na innym. Po chwili tworzy nowe połączenie na innym porcie i wznawia wysyłanie danych.

### Port tunneling

We have an SMTP server listening on port 25; however, we cannot connect to the SMTP server because the firewall blocks packets from the Internet sent to destination port 25. We discover that packets sent to destination port 443 are not blocked, so we decide to take advantage of this and send our packets to port 443, and after they pass through the firewall, we forward them to port 25. Let’s say that we can run a command of our choice on one of the systems behind the firewall. We can use that system to forward our packets to the SMTP server using the following command.

Przykładowe polecenie co to wykona `ncat -lvnp 443 -c "ncat TARGET_SERVER 25"`

Next-Generation Firewall (NGFW) is designed to handle the new challenges facing modern enterprises. For instance, some of NGFW capabilities include:

- Integrate a firewall and a real-time Intrusion Prevention System (IPS). It can stop any detected threat in real-time.
- Identify users and their traffic. It can enforce the security policy per-user or per-group basis.
- Identify the applications and protocols regardless of the port number being used.
- Identify the content being transmitted. It can enforce the security policy in case any violating content is detected.
- Ability to decrypt SSL/TLS and SSH traffic. For instance, it restricts evasive techniques built around encryption to transfer malicious files.

### SSH TUNNELING

W skrócie - jest sobie port 1000 na serwerze ale blokuje mnie firewall, teraz mogę mając ssh do serwera powiedzieć od serwera, że ten port 1000 ma być forwardowany na inny serwer (np. mój z  ssh -L) i na moim localhost mogę wbić na wyznaczonym porcie na tę usługę skipując firewall.

Think of SSH port forwarding (or SSH tunneling) as creating a secure, encrypted "pipe" between your computer and a remote server. Once that pipe is built, you can shuffle network traffic through it that wouldn't normally be allowed—like bypassing a firewall or accessing a private database.

Here is the breakdown of the three main types and how they operate.

---

## 1. Local Port Forwarding (`-L`)

This is the most common type. It allows you to connect a port on your **local** machine to a port on a **remote** destination via the SSH server.

- **The Scenario:** You want to access a database sitting on a private server at work, but the database port (e.g., 5432) is blocked by a firewall. However, you _can_ SSH into a "jump box" at the office.
    
- **How it works:** You tell your computer, "Take anything sent to my local port 8080 and tunnel it through the SSH connection to the office server, which will then hand it off to the database."
    

**The Command:** `ssh -L 8080:database-server:5432 user@ssh-jump-box`

---

## 2. Remote Port Forwarding (`-R`)

This is the reverse. It allows a **remote** server to access a service running on your **local** machine.

- **The Scenario:** You are developing a website on your laptop (`localhost:3000`) and you want a client or a colleague to see it. Your laptop is behind a home router, so they can’t just browse to your IP.
    
- **How it works:** You create a tunnel where the remote SSH server listens on a specific port (e.g., 9000). Any traffic hitting that server's port 9000 is sent back through the tunnel to your laptop's port 3000.
    

**The Command:** `ssh -R 9000:localhost:3000 user@remote-server`

---

## 3. Dynamic Port Forwarding (`-D`)

This turns your SSH client into a **SOCKS proxy server**. Unlike the others, you don't specify a single destination.

- **The Scenario:** You are on sketchy public Wi-Fi and want all your web traffic to be encrypted and appear as if it's coming from your home server.
    
- **How it works:** You open a single port on your machine. Your browser (configured to use a SOCKS proxy) sends all its requests there. The SSH client wraps that traffic and sends it to the SSH server, which then acts as the middleman for _any_ website you visit.
    

**The Command:** `ssh -D 1080 user@home-server`

---

## Summary Comparison

|Type|Flag|Primary Use Case|Direction of Traffic|
|---|---|---|---|
|**Local**|`-L`|Accessing a remote service from your PC.|Local PC → SSH Server → Target|
|**Remote**|`-R`|Sharing a local service with the world.|Remote Server → SSH Server → Local PC|
|**Dynamic**|`-D`|Using the SSH server as a general proxy (VPN-lite).|Local PC → SSH Server → Anywhere|