Odpalenie:
`snort -c local.rules -A full -l . -r mx-3.pcap` - odpalenie pliku pcap z pełnym opisem i zasadami w pliku local.rules, output jako alert w tym folderze w którym jestem

`snort -v -r snort.log.1759749716 -n 64` wyświetlenie danych z logu (64 pakiety)

`snort -r snort.log.1759750447 -X -n 10` parametr -X daje pełną informację z pakietu w hex

## Przykłady FTP

```
#alert tcp any any <> any 21 (msg:"BLOCK TCP"; sid:1;rev:1;)
#alert tcp any any <> any 21 (msg:"Filed FTP LOGIN";content:"430"; sid:2;rev:1;)
#alert tcp any any <> any 21 (msg:"SUCCESS FTP LOGIN";content:"230"; sid:3;rev:1;)
#alert tcp any any <> any 21 (msg:"FTP LOGIN VALID UNAME NO PASSWORD";content:"331"; sid:4;rev:1;)
#alert tcp any any <> any 21 (msg:"FTP LOGIN ATTEMPT ADMINISTRATOR";content:"331 Password required for Administrator"; sid:5;rev:1;)
```