Skanowanie portów na atakowanym/testowanym urządzeniu.

`nmap -Pn -p- --min-rate 2000 -sC -sV -oN nmap_scan.txt IP`

-pn - bez icmp (ping)
-p- - wszystkie 65535 porty
--min-rate 2000 - 2000 pakietów na sekundę
-sC - odpala domyślne skrypty nmapa (podatności, misconfiguration)
-sV - pokazuje wersje skanowanych serwisów 
-oN - zapisuje output do pliku