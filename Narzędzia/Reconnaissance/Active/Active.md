Aktywny rekonesans polega na bezpośrednim ingerowaniu w cel, np. :
- łączenie się na firmowe serwery jak FTP, HTTP
- dzwonienie do pracowników firmy w celu zdobycia informacji
- wchodzenie na teren firmy podając się np. za hydraulika.

# Przeglądarka

Z reguły porty 80 i 443, można wykorzystać dev toolsy, dodatkowo:
- foxyproxy - zmiana serwera proxy
- User-Agent Switcher and Manager - możliwość zmiany user-agenta
- Wappalyser - Daje informacje o technologiach wykorzystywanych przez daną stronę.

# Ping

Wysyła pakiet do systemu a on zwraca odpowiedź, jak system odpowie to znaczy że nie jest zablokowany przez firewalla.

# Traceroute

Pokazuje trasę pakietu od hosta do celu. Na linux jest to `traceroute ip` a na windows `tracert ip` Na linuxie traceroute wysyła datagram udp z ttl=1 i kiedy dojdzie do pierwszego routera to ttl=0 i  ten router wysyła ICMP TTL exceeded do hosta, tak wiadomo jakie IP ma ten router, następnie wysyła ttl=2 i tak dalej.

# Telnet

Działa na porcie TCP/23, podobne do ssh ale starsze i nie szyfruje komunikacji. Można użyć do zdobycia baneru `telnet ip port` Można tym się podłączyć pod każdy serwis TCP dopóki nie wykorzystuje on szyfrowania.

# Netcat

`nc` - wspiera udp i tcp, może działać jak klient który łączy się na nasłuchujący port albo działać jako serwer nasłuchujący na wybranym porcie.
Połączenie - `nc ip port` i podobnie jak telnet
Nasłuchiwanie `nc -lvnp port` 