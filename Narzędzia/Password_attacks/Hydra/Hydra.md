Bruteforce atak na hasła, działa na protokołach jak FTP, POP3, IMAP, SMTP, SSH, and all methods related to HTTP

Syntax:
`hydra -l username -P wordlist.txt server service`
- -l username - nazwa użytkownika, L - słownik z nazwami
- -P wodlist.txt - słownik z hasłami, p - to pojedyncze hasło nie z pliku
- server - ip albo nazwa celu
- service - usługa
- -s PORT - niestandardowy port
- -V lub -vV - pokazuje progres i wypisuje w terminalu kolejne próby
- -t n - działanie na n wątkach
- -d deugowanie, przydatne żeby zobaczyć czy np. hydra próbuje połączyć się z zamkniętym portem

# Zapobieganie atakom na hasła

- polityka haseł
- blokowanie jak za dużo nieudanych prób
- opóźnienie odpowiedzi przy podaniu niepoprawnego hasła
- captcha
- 2FA