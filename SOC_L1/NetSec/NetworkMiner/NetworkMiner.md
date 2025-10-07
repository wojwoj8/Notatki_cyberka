"NetworkMiner is an open source Network Forensic Analysis Tool (NFAT) for Windows (but also works in Linux / Mac OS X / FreeBSD). NetworkMiner can be used as a passive network sniffer/packet capturing tool to detect operating systems, sessions, hostnames, open ports etc. without putting any traffic on the network. NetworkMiner can also parse PCAP files for off-line analysis and to regenerate/reassemble transmitted files and certificates from PCAP files.

Może skanować:
- ruch sieciowy aktywnie
- przechwycony ruch sieciowy
- logi

|   |   |
|---|---|
|**Capability**|**Description**|
|Traffic sniffing|It can intercept the traffic, sniff it, and collect and log packets that pass through the network.|
|Parsing PCAP files|It can parse pcap files and show the content of the packets in detail.|
|Protocol analysis|It can identify the used protocols from the parsed pcap file.|
|OS fingerprinting|It can identify the used OS by reading the pcap file. This feature strongly relies on [Satori](https://github.com/xnih/satori/) and [p0f](https://lcamtuf.coredump.cx/p0f3/).|
|File Extraction|It can extract images, HTML files and emails from the parsed pcap file.|
|Credential grabbing|It can extract credentials from the parsed pcap file.|
|Clear text keyword parsing|It can extract cleartext keywords and strings from the parsed pcap file.|
Jako sniffer działa tylko na windowsie.