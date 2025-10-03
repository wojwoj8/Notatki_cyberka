[MISP (Malware Information Sharing Platform)](https://www.misp-project.org/) jest to platforma open-source, która ułatwia gromadzenie, przechowywanie i dystrybucję danych wywiadowczych dotyczących zagrożeń oraz wskaźników naruszenia bezpieczeństwa (IOC) związanych ze złośliwym oprogramowaniem, cyberatakami, oszustwami finansowymi lub wszelkimi informacjami wywiadowczymi

Dzielenie się informacjami działa jako model rozproszony, wspierany przez zamknięte, pół-otwarte i otwarte społeczności. Informacje mogą zostać wykorzystane w NIDS (Network Intrusion Detection System) i SIEM (Security information and event management systems).

## Wykorzystanie MISP

MISP można użyć do:
- **Malware Reverse Engineering**: Sharing of malware indicators to understand how different malware families function.
- **Security Investigations:** Searching, validating and using indicators in investigating security breaches.
- **Intelligence Analysis:** Gathering information about adversary groups and their capabilities.
- **Law Enforcement:** Using Indicators to support forensic investigations.
- **Risk Analysis:** Researching new threats, their likelihood and occurrences.
- **Fraud Analysis:** Sharing of financial indicators to detect financial fraud.

MISP zapewnia takie kluczowe funkcjonalności:
- **IOC database:** This allows for the storage of technical and non-technical information about malware samples, incidents, attackers and intelligence.
- **Automatic Correlation:** Identification of relationships between attributes and indicators from malware, attack campaigns or analysis.
- **Data Sharing:** This allows for sharing of information using different models of distributions and among different MISP instances.
- **Import & Export Features:** This allows the import and export of events in different formats to integrate other systems such as NIDS, HIDS, and OpenIOC.
- **Event Graph:** Showcases the relationships between objects and attributes identified from events.
- **API support:** Supports integration with own systems to fetch and export events and intelligence.

Korzystając z MISP używa się takiej terminologii:
- **Events:** Collection of contextually linked information.
- **Attributes:** Individual data points associated with an event, such as network or system indicators.
- **Objects:** Custom attribute compositions.
- **Object References:** Relationships between different objects.
- **Sightings:** Time-specific occurrences of a given data point or attribute detected to provide more credibility.
- **Tags:** Labels attached to events/attributes.
- **Taxonomies:** Classification libraries are used to tag, classify and organise information.
- **Galaxies:** Knowledge base items used to label events/attributes.
- **Indicators:** Pieces of information that can detect suspicious or malicious cyber activity.