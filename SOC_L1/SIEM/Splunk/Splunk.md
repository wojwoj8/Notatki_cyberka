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