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