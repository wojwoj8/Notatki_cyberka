Cyber Threat Intelligence skupia się na tym który z wielu logów jest niebezpieczny bazując na 3 pytaniach:
1. Kto lub co jest po drugiej stronie tego indykatora (logu?)
2. Jak wcześniej się to zachowywało
3. Jak inne organizacje na to reagowały i co powinno się z tym zrobić

W information security skupia się na 3 filarach z surowych danych:

| Layer            | Definition                                  | Alert-queue example                                         | SOC L1 action         |
| ---------------- | ------------------------------------------- | ----------------------------------------------------------- | --------------------- |
| **Data**         | An unprocessed observable                   | `45.155.205.3 :443`                                         | Capture the artefact. |
| **Information**  | Data plus factual annotation                | _IP registered to Hetzner, first seen 2023-07-14_           | Record attributes.    |
| **Intelligence** | Analysed information that answers _so-what_ | _IP belongs to the current BumbleBee C2; block immediately_ | Escalate or suppress. |
Podczas wyciągania dodatkowych inforamcji jeszcze są 3 ważne pojęcia:
- **Indicator of Compromise (IOC)**: Evidence of a breach, such as a C2 address in the logs.
- **Indicator of Attack (IOA)**: A malicious action, such as PowerShell launching an unknown service, is underway.
- **Tactics, Techniques, and Procedures (TTP)**: An adversary's detailed methodologies expressed in MITRE ATT&CK IDs and descriptions.

Typy indykatorów kluczowe na soc-l1:

| Indicator          | Example                                | First Resources                                                                       | Associated IOA or TTP Examples                               |
| ------------------ | -------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **IPv4 / IPv6**    | `45.155.205.3`                         | • WHOIS (ASN, allocation date) · VirusTotal Relations· Shodan banner scan             | IOA: Repeated SSH failures TTP: `T1110.003`Password Guessing |
| **Domain / FQDN**  | `malicious-updates[.]net`              | • WHOIS age · RiskIQ or SecurityTrails passive-DNS · urlscan.io                       | IOA: surge of DNS queries to a 24-hour-old domain            |
| **URL**            | `hxxp://malicious-updates[.]net/login` | • URLhaus reputation · urlscan.io behaviour graph · Any.Run dynamic run (network off) | IOA: Browser POST to /gateway.php with payload               |
| **File hash**      | `e99a18c428cb38d5…`                    | • VirusTotal static & dynamic · Hybrid-Analysis · MalShare corpus                     | TTP: T1055 Process Injection into regsvr32.exe               |
| **E-mail address** | `billing@evil-corp.com`                | • MXToolbox header analysis • Have I Been Pwned                                       | IOA: SPF failure plus recent domain registration             |
| **Local artefact** | `HKCU\Software\Run\updater.exe`        | • Sigma rules · EDR prevalence query · Vendor knowledge bas                           | TTP: T1060.001 Registry Run Keys                             |

Feed - określony strunień indykatorów zazwyczaj dostarczony w CSV czy JSON.
Platform - Ustrukturyzowane repo które prezchowuje indykatory, mapuje relacje itp. Przykładami są OpenCTI i MISP.

Źródła CTI:
- **Internal telemetry:** SIEM logs, EDR detections, phishing-mailbox submissions provide the highest immediate relevance.
- **Commercial services:** Vendor premium feeds, paid sandboxes and closed-source analytics. These provide high fidelity, but may have export and sharing limits based on licensing.
- **Open-source intelligence (OSINT):** AbuseIPDB, URLhaus, public blogs with IOCs, and academic research. Before applying, information from these sources will need to be cross-confirmed.
- **Communities & ISACs:** Sector-specific lists marked with labels and rich context (e.g., FS-ISAC)

## Threat intelligence Classifications

Threat intelligence jest bardziej stworzone do zrozumienia relacji między moim systemem (chronionym) a hackerem. Można podzielić ten threat intel na:
- Strategic intel - wysokopoziomowa analiza która skupia się na organizacji i mapuje miejsca ryzyka, patterny albo powstające zagrożenia które mogą wpłynąć na business. Przykładem jest coroczny raport o ransomware.
- Tactical intel - Ocena zachowań hackerów, TTP.
- Operational intel - Szczegółowe informacje dotyczące konkretnej kampanii, motywów i zamiarów przeprowadzenia ataku. Jest to przydatne do zrozumienia, jakie kluczowe zasoby organizacji (ludzie, procesy i technologie) mogą stać się celem ataku.
- Technical Intel - atomiczne wskaźniki i artefakty jak ip i hashe związane z atakiem.

CTI skupia się na przetwarzaniu surowych danych w dane połączone z kontekstem ataku, celu.

## Traffic Light Protocol (TLP)—A Primer for Proper Sharing
Jest to czworo-kolorowy schemat etykietowania który zarządza jak szeroko wywiad może zostać dzielony (shared)

| TLP label      | Sharing boundary                                                   | Typical SOC L1 behaviour                                                           |
| -------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| **TLP: CLEAR** | No restriction                                                     | Post to the internal wiki or platform.                                             |
| **TLP: GREEN** | Share with peer community but not publicly                         | Upload to MISP/Slack workspace restricted to partner SOCs.                         |
| **TLP: AMBER** | Organisation-wide, external sharing only with need-to-know clients | Keep within the company CTI platform; reference, do not copy, in tickets.          |
| **TLP: RED**   | Named recipients only                                              | Store in an encrypted note; do not post to the ticketing system without clearance. |
![](Attachments/{C004358B-F61B-44EB-A83A-419A7B548A24}.png)

## CTI standards and frameworks:

MITRE D3FEND, MITRE ATT&CK, Cyber Kill Chain
CVEs, CVSS, and the NVD:
- **CVE (Common Vulnerabilities and Exposures)** — provides a catalogue number for discovered vulnerabilities, e.g., _CVE-2023-4863_.
- **CVSS (Common Vulnerability Scoring System)** — a 0–10 severity scale with temporal and environmental modifiers for vulnerabilities.
- **NVD (National Vulnerability Database)** — the canonical repository that links CVE numbers to CVSS scores, exploits, and affected products.

## Sharing and Processing Intel
- **STIX**: the structured JSON schema for describing threat information.
- **TAXII**: The Trusted Automated eXchange of Indicator Information is a set of secure APIs used to exchange threat intelligence in near real-time for detection, prevention, and mitigation of threats. It supports two sharing models: **Collection**, which ensures threat intel is collected and hosted by a producer, and **Channel**, which publishes threat intel to users from a central server.