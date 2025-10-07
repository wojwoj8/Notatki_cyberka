Zekk (wcześniej Bro) to open-source i commercial network monitoring tool (traffic analyser) - jest to IDS/NIDS jak snort ale trochę się różni bo jeszcze jest Network Security Monitoring (NSM)

|   |   |   |
|---|---|---|
|**Tool**|**Zeek**|**Snort**|
|**Capabilities**|NSM and IDS framework. It is heavily focused on network analysis. It is more focused on specific threats to trigger alerts. The detection mechanism is focused on events.|An IDS/IPS system. It is heavily focused on signatures to detect vulnerabilities. The detection mechanism is focused on signature patterns and packets.|
|**Cons**|Hard to use.<br><br>The analysis is done out of the Zeek, manually or by automation.|Hard to detect complex threats.|
|**Pros**|It provides in-depth traffic visibility.<br><br>Useful for threat hunting.<br><br>Ability to detect complex threats.<br><br>It has a scripting language and supports event correlation. <br><br>Easy to read logs.|Easy to write rules.<br><br>Cisco supported rules.<br><br>Community support.|
|**Common Use Case**|Network monitoring.  <br>In-depth traffic investigation.  <br>Intrusion detecting in chained events.|Intrusion detection and prevention.  <br>Stop known attacks/threats.|

Zeek automatycznie zacznie skanować ruch sieciowy albo pcap. Logi są w `/opt/zeek/logs/`

## Zeek as a service

Trzeba użyć modułu ZeekControl `zeekctl` - trzeba odpalić jako sudo albo root. Ma 3 plecenia:
- `zeekctl status`
- `zeekctl start` 
- `zeekctl stop`

## Zeek

Odpalenie pliku `zeek -C -r sample.pcap`

|   |   |
|---|---|
|**Parameter**|**Description**|
|**-r**|Reading option, read/process a pcap file.|
|**-C**|Ignoring checksum errors.|
|**-v**|Version information.|

[Cheet sheet do logów](remote-cyberka/SOC_L1/NetSec/Zeek/corelight-cheatsheet-poster.pdf) 