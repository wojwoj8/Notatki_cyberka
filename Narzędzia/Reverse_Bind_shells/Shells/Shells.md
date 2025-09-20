Najszęstsze shelle to:
- netcat - na każdym linuksie jest ale mało stabilne te rev shells
- socat - netcat na sterydach, shelle są stabilniejsze ale socat ma ciężki syntax i nie jest domyślnie zainstalowany na systemach linux
- Metasploit -- multi/handler - należy do metasploit framework, zapewnia stabilne rev shells, i inne opcje, jest jedyną metodą interakcji z meterpreter shell.
- Msfvenom - niby część metasploit i podobne do tego wyżej ale jest standalone tool, używany do generowania payloadów na bieżąco, potrafi generować inne payloady niż tylko bind shell i reverse shell.

# Źródła payloadów

[Payloads all the Things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)
[Reverse Shell Cheatsheet](https://web.archive.org/web/20200901140719/http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)

# Rodzaje

Są 2 rodzaje:
- reverse shell - zmuszenie atakowanego komputera do połączenia się z naszym, dobre żeby ominąć firewall ale problemem może być ustawienie połączenia przez internet.
- bind shell - ustawienie nasłuchiwania na atakowanym komputerze żeby można było się z nim połączyć. Problemem może być firewall, nie ma problemu z konfigurowaniem połączenia przez internet.