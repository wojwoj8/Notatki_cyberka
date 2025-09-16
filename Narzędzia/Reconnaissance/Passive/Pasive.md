Pasywny rekonesans polega na zbieraniu informacji o np. systemie z publicznych źródeł. Jest to:
- Patrzenie na rekordy DNS
- sprawdzanie ofert pracy dotyczących danej strony
- czytanie newsów na temat danej firmy.


# WHOIS
Nasłuchuje na porcie TCP/43, zwraca informacje związane z domeną takie jak:
- przez jaki serwis została zarejestrowana domena
- informacje kontaktowe
- daty stworzenia i aktualizacji domeny


`whois nazwa_domeny` - użycie w terminalu. 

# nslookup

`nslookup` - od Name server look up, pozwala sprawdzić adres ip domeny, wywołanie podonbne do whois, `nslookup opcje nazwa_domeny server`:
- opcje - zawierają query type z tabelki poniżej
- nazwa_domeny - nazwa domeny
- server - server dns który chcemy sprawdzić. Można wybrać lokalny albo publiczny. Lista publicznych dns: https://public-dns.info

|Query type|Result|
|---|---|
|A|IPv4 Addresses|
|AAAA|IPv6 Addresses|
|CNAME|Canonical Name|
|MX|Mail Servers|
|SOA|Start of Authority|
|TXT|TXT Records|
Przykład
`nslookup -type=a tryhackme.com 1.1.1.1`

# dig
Bardziej zaawansowane narzędzie zapytań dns, nazwa od "domain information groper"
Użycie: `dig @server nazwa_domeny typ`:
- @server - serwer dns
- nazwa_domeny - nazwa domeny
- typ - to co w tabeli powyżej (query type)

# Subdomains

Wyszukiwanie subdomen można bruteforce jak ffuz czy gobuster a można też sewisy jak  [DNSDumpster](https://dnsdumpster.com/)

# Shodan.io

[Shodan.io](https://www.shodan.io/)
Informacje o sieci klienta bez aktywnego łączenia się do niej. Dodatkowo w ramach "obrony" można zobaczyć swoją firmę czy stronę w celu sprawdzenia informacji o wystawionych urządzeniach.

Shodan próbuje połączyć się z każdym dostępnym online urządzeniem tworząc sieć połączeń. Jak się połączy to zbiera informacje i zapisuje je w bazie danych.

Można w shodan pytać o ip z wcześnej zdobytych adresów z dig, nslookup itp.