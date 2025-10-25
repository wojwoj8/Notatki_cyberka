Splunk posiada trzy główne komponenty - Frowarder, indexer i Search Head.

### Splunk Forwarder

Agent instalowany na endpoincie który ma być monitorowany, zbiera i wysyła dane do Splunka. Nie wpływa na wydajność endpointa. Przykłady zbieranych danych:

- Web server generating web traffic.
- Windows machine generating Windows Event Logs, PowerShell, and Sysmon data.
- Linux host generating host-centric logs.
- Database generating DB connection requests, responses, and errors.

### Splunk Indexer

Zbiera dane i normalizuje je do field-value pairs. Określa typ danych danych i przechowuje je jako zdarzenia.

### Search Head

Wyszukiwarka zdarzeń - korzysta z języka Splunk Search Processing Language. Pozwala też na wizualizację danych.

Przydatne źródła logów

|   |   |
|---|---|
|**Log Sources  <br>**|**Details  <br>**|
|**wineventlog**|It contains Windows Event logs|
|**winRegistry**|It contains the logs related to registry creation / modification / deletion etc.|
|**XmlWinEventLog**|It contains the sysmon event logs. It is a very important log source from an investigation point of view.|
|**fortigate_utm  <br>**|It contains Fortinet Firewall logs|
|**iis  <br>**|It contains IIS web server logs|
|**Nessus:scan  <br>**|It contains the results from the Nessus vulnerability scanner.|
|**Suricata  <br>**|It contains the details of the alerts from the Suricata IDS. This log source shows which alert was triggered and what caused the alert to get triggered— a very important log source for the Investigation.|
|**stream:http  <br>**|It contains the network flow related to http traffic.|
|**stream: DNS  <br>**|It contains the network flow related to DNS traffic.|
|**stream:icmp  <br>**|It contains the network flow related to icmp traffic.|

Sysmon jest w logach jako "XmlWinEventLog"

[Robtex](https://www.robtex.com/) is a Threat Intel site that provides information about IP addresses, domain names, etc.

**OSINT sites**

- Virustotal
- ThreatMiner
- Hybrid-Analysis