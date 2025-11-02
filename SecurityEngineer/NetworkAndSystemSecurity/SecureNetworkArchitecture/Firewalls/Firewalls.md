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