Skanowanie portów na atakowanym/testowanym urządzeniu.

`nmap -Pn -p- --min-rate 2000 -sC -sV -oN nmap_scan.txt IP`

-pn - bez icmp (ping)
-p- - wszystkie 65535 porty
--min-rate 2000 - 2000 pakietów na sekundę (dosyć agresywnie)
-sC - odpala domyślne skrypty nmapa (podatności, misconfiguration)
-sV - pokazuje wersje skanowanych serwisów 
-oN - zapisuje output do pliku

|Scan Type|Example Command|
|---|---|
|ARP Scan|`sudo nmap -PR -sn MACHINE_IP/24`|
|ICMP Echo Scan|`sudo nmap -PE -sn MACHINE_IP/24`|
|ICMP Timestamp Scan|`sudo nmap -PP -sn MACHINE_IP/24`|
|ICMP Address Mask Scan|`sudo nmap -PM -sn MACHINE_IP/24`|
|TCP SYN Ping Scan|`sudo nmap -PS22,80,443 -sn MACHINE_IP/30`|
|TCP ACK Ping Scan|`sudo nmap -PA22,80,443 -sn MACHINE_IP/30`|
|UDP Ping Scan|`sudo nmap -PU53,161,162 -sn MACHINE_IP/30`|

Remember to add `-sn` if you are only interested in host discovery without port-scanning. Omitting `-sn` will let Nmap default to port-scanning the live hosts.

| Option | Purpose                          |
| ------ | -------------------------------- |
| `-n`   | no DNS lookup                    |
| `-R`   | reverse-DNS lookup for all hosts |
| `-sn`  | host discovery only              |

# Stany portów

1. Port otwarty
2. Port zamknięty - nie zablokowany przez firewall
3. Filtered - nie wiadomo czy zamknięty czy otwarty port bo nie jest dostępny. Z reguły firewall blokuje pakiety
4. Unfiltered - nmap nie wie czy port jest otwarty czy zamknięty ale jest dostępny, ten stan występuje przy ACK scan `-sA`
5. Open|Filtered - nmap nie wie czy port jest otwarty czy filtrowany
6. Closed|Filtered 

|Port Scan Type|Example Command|
|---|---|
|TCP Connect Scan|`nmap -sT 10.10.67.141`|
|TCP SYN Scan|`sudo nmap -sS 10.10.67.141`|
|UDP Scan|`sudo nmap -sU 10.10.67.141`|

These scan types should get you started discovering running TCP and UDP services on a target host.

|Option|Purpose|
|---|---|
|`-p-`|all ports|
|`-p1-1023`|scan ports 1 to 1023|
|`-F`|100 most common ports|
|`-r`|scan ports in consecutive order|
|`-T<0-5>`|-T0 being the slowest and T5 the fastest|
|`--max-rate 50`|rate <= 50 packets/sec|
|`--min-rate 15`|rate >= 15 packets/sec|
|`--min-parallelism 100`|at least 100 probes in parallel|