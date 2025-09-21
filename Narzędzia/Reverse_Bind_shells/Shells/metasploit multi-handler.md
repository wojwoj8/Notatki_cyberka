metasploit multi/handler - dobre narzędzie do łapania reverse shell, szczególnie jak chce się korzystać z meterpreter shells i staged payloads.

## Użycie
1. `msfconsole`
2. `use multi/handler`

Dalej wpisuje się `options` i tam jest konfiguracja payload, lhost i lport. Te opcje to to samo co w msfvenom.

Odpalenie listenera `exploit -j` - to spowoduje odpalenie exploitu w tle. Jak sesja jest w tle to informacje o niej są pod poleceniem `sessions`