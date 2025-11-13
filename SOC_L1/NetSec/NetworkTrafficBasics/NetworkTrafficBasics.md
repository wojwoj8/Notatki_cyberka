Przy analizowaniu pakietu TCP/IP

![](Attatchments/Pasted%20image%2020251113125504.png)

W warstwie aplikacji sus jest np. plik załączony w zapytaniu http

W Transportowej może być niepoprawny numer Seq połączenia 3-way handshake

W internetu do ominięcia IDS może być wykorzystane fragmentation attack - jak segment jest za duży na MTU to jest podzielony. Można też wykorzystać w ten sposób overlapping, na fragment segmentu jest nakładany kolejny.

W link może być arp poisoning albo arp spoofing.