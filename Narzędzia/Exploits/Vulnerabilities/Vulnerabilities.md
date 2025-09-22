Główne kategorie

|                             |                                                                                                                                                                                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vulnerability**           | **Description**                                                                                                                                                                                                                                    |
| Operating System            | These types of vulnerabilities are found within Operating Systems (OSs) and often result in privilege escalation.                                                                                                                                  |
| (Mis)Configuration-based    | These types of vulnerability stem from an incorrectly configured application or service. For example, a website exposing customer details.                                                                                                         |
| Weak or Default Credentials | Applications and services that have an element of authentication will come with default credentials when installed. For example, an administrator dashboard may have the username and password of "admin". These are easy to guess by an attacker. |
| Application Logic           | These vulnerabilities are a result of poorly designed applications. For example, poorly implemented authentication mechanisms that may result in an attacker being able to impersonate a user.                                                     |
| Human-Factor                | Human-Factor vulnerabilities are vulnerabilities that leverage human behaviour. For example, phishing emails are designed to trick humans into believing they are legitimate.                                                                      |

# Ocena podatności

CVSS - Common Vulnerability Scoring System, open-source
[Kalkulator CVSS](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)

|   |   |
|---|---|
|**Advantages of CVSS**|**Disadvantages of CVSS**|
|CVSS has been around for a long time.|CVSS was never designed to help prioritise vulnerabilities, instead, just assign a value of severity.|
|CVSS is popular in organisations.|CVSS heavily assesses vulnerabilities on an exploit being available. However, only 20% of all vulnerabilities have an exploit available ([Tenable., 2020](https://www.tenable.com/research)) .|
|CVSS is a free framework to adopt and recommended by organisations such as NIST.|Vulnerabilities rarely change scoring after assessment despite the fact that new developments such as exploits may be found.|


VPR - Vulnerability Priority Rating 

|   |   |
|---|---|
|**Advantages of VPR**|**Disadvantages of VPR**|
|VPR is a modern framework that is real-world.|VPR is not open-source like some other vulnerability management frameworks.|
|VPR considers over 150 factors when calculating risk.|VPR can only be adopted apart of a commercial platform.|
|VPR is risk-driven and used by organisations to help prioritise patching vulnerabilities.|VPR does not consider the CIA triad to the extent that CVSS does; meaning that risk to the confidentiality, integrity and availability of data does not play a large factor in scoring vulnerabilities when using VPR.|
|Scorings are not final and are very dynamic, meaning the priority a vulnerability should be given can change as the vulnerability ages.|_Intentionally left blank._|

# Bazy danych podatności

[NVD (National Vulnerability Database)](https://nvd.nist.gov/vuln) - zawiera wszystkie CVE (Common Vulnerabilities and Exposures)
[Exploit-DB](http://exploit-db.com/) - zawiera exploity danych podatności

# Wyszukiwanie podatności

Może być automatyczne i manualne

## Automatyczne

Nessus - jest darmowy w wersji community oraz płatny. Płatny jest bardzo drogi i raczej wykorzystywany przez organizacje zapewniające testy penetracyjne albo audyty.

Wady i zalety

|   |   |
|---|---|
|**Advantage**|**Disadvantage**|
|Automated scans are easy to repeat, and the results can be shared within a team with ease.|People can often become reliant on these tools.|
|These scanners are quick and can test numerous applications efficiently.|They are extremely "loud" and produce a lot of traffic and logging. This is not good if you are trying to bypass firewalls and the likes.|
|Open-source solutions exist.|Open-source solutions are often basic and require expensive licenses to have useful features.|
|Automated scanners cover a wide range of different vulnerabilities that may be hard to manually search for.|They often do not find every vulnerability on an application.|

## Manualne

Bazy jak [Rapid7](https://www.rapid7.com/db/), exploitdb, github, searchsploit (kopia offline exploit-db)