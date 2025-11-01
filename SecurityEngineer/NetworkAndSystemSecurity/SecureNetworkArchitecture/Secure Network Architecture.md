


![](Attatchments/Pasted%20image%2020251101122517.png)

Vlany dodają tag to ramki. Tag 802.1q albo dot1q wyznacza sieć VLAN z której pochodzi ruch. Ten 802.1q to standard i routery cisco i np. mikrotik będą się widzieć.

Native vlan jest do trasowania każdego ruchu, który nie jest tagowany i idzie przez switch. Do skonfigurowania trzeba wiedzieć jaki tag i interfejs im przypisać.

Router na patyku - rozwiązuje problem fizycznego podłączania routera i switcha do poszczególnego vlan. W nim sieci vlan są skonfigurowane tak żeby konfigurowały się z routerem przez jeden port na switchu (switchport). Połaczenie między switchem a routerem jest w trunku (tagowane). Sieci VLAN są kierowane przez port przełącznika, co wymaga tylko jednego łącza/połączenia między przełącznikiem a routerem.

|                          |                                                                                                                                                  |                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| **Zone  <br>**           | **Explanation  <br>**                                                                                                                            | **Examples**                              |
| External                 | All devices and entities outside of our network or asset control.                                                                                | Devices connecting to a web server        |
| DMZ (demilitarized zone) | Separates untrusted networks or devices from internal resources.                                                                                 | BYOD, remote users/guests, public servers |
| Trusted                  | Internal networks or devices. A device may be placed in the trusted zone if there is no confidential or sensitive information.                   | Workstations, B2B                         |
| Restricted               | Any high-risk servers or databases.                                                                                                              | Domain controllers, client information    |
| Management               | Any devices or services dedicated to network or other device management. This zone is less commonly seen and can be grouped with the audit zone. | Virtualization management, backup servers |
| Audit                    | Any devices or services dedicated to security or monitoring. This zone is less commonly seen and can be grouped with management.                 | SIEM, telemetry                           |

ACL - access list - lista dostępu, wprowadzanie zasad, że np. wpuszczamy tylko ruch przychodzący z ip takiego i idądy do ip takiego. Zasady w ACL to ACE. Poprawne zastosowanie ACL spowoduje, że routrer będzie odrzucał lub akceptował pakiety.

Firewall - są stateless i stateful. ACL w routerach są stateless - nie patrzą na połączenie i go nie analizują. Stateful są bardziej wymagające i śledzą połączenie.

### Zone-pairs

**Zone-pairs** are a direction-based and stateful policy that will enforce the traffic in single directions per each VLAN, hence, zone-pair. For example, **DMZ → LAN** or **LAN → DMZ.**
Każda strefa w danej topologii musi mieć inną parę stref dla każdej innej strefy w topologii i w każdym możliwym kierunku. Takie podejście zapewnia największą widoczność z poziomu firewalla i znacznie poprawia możliwości filtrowania.

Trzeba zrobić każde możliwe połączenie stref ze sobą w obie strony i ewentualnie dodać/zmienić zasady.

### SSL/TLS inspection

SSL/TLS inspection uses an **SSL proxy** to intercept protocols, including HTTP, POP3, SMTP, or other SSL/TLS encrypted traffic. Once intercepted, the proxy will decrypt the traffic and send it to be processed by a **UTM** (**U**nified **T**hreat **M**anagement) platform. UTM solutions will employ deep SSL inspection, feeding the decrypted traffic from the proxy into other UTM services, including but not limited to web filters or **IPS** (**Intrusion Prevention System**), to process the information.

To rozwiązanie spowoduje MiTM pomiędzy urządzeniem a światem zewnętrzym co może spowodować wyciek poufnych danych w plain-text.

### DHCP Snooping

[Cisco](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst6500/ios/12-2SXF/native/configuration/guide/swcg/snoodhcp.pdf) defines **DHCP snooping** as "a security feature that acts like a firewall between untrusted hosts and trusted DHCP servers."

To rozwiązanie wprowadzono żeby zwalczyć wrogie serwery DHCP; to waliduje i ustala rate-limit na ruch dhcp. Mimo że dhcp to protokół warstwy 3 to dhcp snooping działa na warstwie 2. The switch will store untrusted hosts with leased IP addresses in a **DHCP Binding Database**. The database is used to validate traffic and can be used by other protocols, such as dynamic ARP inspection. List of conditions the protocol will inspect to determine if a DHCP packet should be dropped:
- Any DHCP packet is received from outside of the network.
- The source MAC address and DHCP client hardware address do not match.
- A `DHCPRELEASE` or `DHCPDECLINE` packet is received on an untrusted interface that does not match an interface that the source address already has registered.
- A DHCP packet that includes a relay agent address that is not `0.0.0.0`

### Dynamic ARP Inspection

[Cisco](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/dynarp.html) defines **ARP inspection** as "a security feature that validates **A**ddress **R**esolution **P**rotocol (**ARP**) packets in a network."

DHCP binding database provides the expected MAC and IP address pair of untrusted hosts; ARP inspection will compare the source IP address and MAC address to the binding pair; if they are mismatched, it will drop the packet.