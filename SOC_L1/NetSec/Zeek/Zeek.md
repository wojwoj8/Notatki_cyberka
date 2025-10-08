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

[Cheet sheet do logów](corelight-cheatsheet-poster.pdf) 

`zeek-cut nazwa_kolumny nazwa_kolejnej` - narzędzie pozwalające wyciąć konkretne kolumny z logów

Przykład
`cat conn.log | zeek-cut uid proto id.orig_h id.orig_p id.resp_h id.resp_p`

## Przydatne polecenia do przeglądania logów

BEZ TYCH `\` to jest bug jakiś bo tego tam nie ma

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |               |                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                | Command Purpose and Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Category      | Command Purpose and Usage                                                                                                                                                                                                                                                                                                                       |
| Basics                  | View the command history:  <br>`ubuntu@ubuntu$ history`  <br><br>Execute the 10th command in history:  <br>`ubuntu@ubuntu$ !10`<br><br>Execute the previous command:  <br>`ubuntu@ubuntu$ !!`                                                                                                                                                                                                                                                                                                                                                                                                                                   | Read **File** | Read sample.txt file:  <br>`ubuntu@ubuntu$ cat sample.txt`<br><br>Read the first 10 lines of the file:  <br>`ubuntu@ubuntu$ head sample.txt`  <br><br>Read the last 10 lines of the file:  <br>`ubuntu@ubuntu$ tail sample.txt`                                                                                                                 |
| Find  <br>&  <br>Filter | Cut the 1st field:  <br>`ubuntu@ubuntu$ cat test.txt \| cut -f 1`  <br><br>Cut the 1st column:  <br>`ubuntu@ubuntu$ cat test.txt \| cut -c1`  <br><br>Filter specific keywords:  <br>`ubuntu@ubuntu$ cat test.txt \| grep 'keywords'`  <br><br>Sort outputs alphabetically:  <br>`ubuntu@ubuntu$ cat test.txt \| sort`<br><br>Sort outputs numerically:  <br>`ubuntu@ubuntu$ cat test.txt \| sort -n`<br><br>Eliminate duplicate lines:  <br>`ubuntu@ubuntu$ cat test.txt \| uniq`  <br><br>Count line numbers:  <br>`ubuntu@ubuntu$ cat test.txt \| wc -l`  <br><br>Show line numbers  <br>`ubuntu@ubuntu$ cat test.txt \| nl` | Advanced      | Print line 11:  <br>`ubuntu@ubuntu$ cat test.txt \| sed -n '11p'`  <br><br>Print lines between 10-15:  <br>`ubuntu@ubuntu$ cat test.txt \| sed -n '10,15p'`<br><br>Print lines below 11:  <br>`ubuntu@ubuntu$ cat test.txt \| awk 'NR < 11 {print $0}'`  <br><br>Print line 11:  <br>`ubuntu@ubuntu$ cat test.txt \| awk 'NR == 11 {print $0}'` |

|             |                                                                                                                   |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| **Special** | Filter specific fields of Zeek logs:<br><br>`ubuntu@ubuntu$ cat signatures.log \| zeek-cut uid src_addr dst_addr` |

|                                                  |                                                                                                  |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| **Use Case**                                     | **Description**                                                                                  |
| `sort \| uniq`                                   | Remove duplicate values.                                                                         |
| `sort \| uniq -c`                                | Remove duplicates and count the number of occurrences for each value.                            |
| `sort -nr`                                       | Sort values numerically and recursively.                                                         |
| `rev`                                            | Reverse string characters.                                                                       |
| `cut -f 1`                                       | Cut field 1.                                                                                     |
| `cut -d '.' -f 1-2`                              | Split the string on every dot and print keep the first two fields.                               |
| `grep -v 'test'`                                 | Display lines that  don't match the "test" string.                                               |
| `grep -v -e 'test1' -e 'test2'`                  | Display lines that don't match one or both "test1" and "test2" strings.                          |
| `file`                                           | View file information.                                                                           |
| `grep -rin Testvalue1 * \| column -t \| less -S` | Search the "Testvalue1" string everywhere, organise column spaces and view the output with less. |
## Zeek signatures

|   |   |
|---|---|
|**Signature id**|**Unique** signature name.|
|**Conditions**|**Header:** Filtering the packet headers for specific source and destination addresses, protocol and port numbers.<br><br>**<br><br>**Content:** Filtering the packet payload for specific value/pattern.<br><br>**|
|**Action**|**Default action:** Create the "signatures.log" file in case of a signature match.<br><br>**Additional action:** Trigger a Zeek script.|

Najczęstsze filtry i warunki

|   |   |
|---|---|
|Condition Field|Available Filters|
|Header|src-ip: Source IP.<br><br>dst-ip: Destination IP.<br><br>src-port: Source port.<br><br>dst-port: Destination port.<br><br>ip-proto: Target protocol. Supported protocols; TCP, UDP, ICMP, ICMP6, IP, IP6|
|Content|**payload:** Packet payload.  <br>**http-request:** Decoded HTTP requests.  <br>**http-request-header:** Client-side HTTP headers.  <br>**http-request-body:** Client-side HTTP request bodys.  <br>**http-reply-header:** Server-side HTTP headers.  <br>**http-reply-body:** Server-side HTTP request bodys.  <br>**ftp:** Command line input of FTP sessions.|
|**Context**|**same-ip:** Filtering the source and destination addresses for duplication.|
|Action|**event:** Signature match message.|
|**Comparison  <br>Operators**|**==**, **!=**, **<**, **<=**, **>**, **>=**|
|**NOTE!**|Filters accept string, numeric and regex values.|

Odpalenie z sygnaturami `zeek -C -r sample.pcap -s sample.sig`

Przykład sygnatury sprawdzającej w tekście jawnym w http czy jest fraza password
```
signature http-password {
    ip-proto == tcp
    dst-port == 80
    payload /.*password.*/
    event "Cleartext password found!"
}
# signature: Signature name.
# ip-proto: Filtering TCP connection.
# dst-port: Filtering destination port 80.
# payload: Filtering the "password" phrase. REGEX
# event: Signature match message.
```

Po wywołaniu `zeek -C -r http.pcap -s http-password.sig` dostajemy kilka plików .log, te dotyczące sygnatury to notice.log i signatures.log. 

Można w jednym pliku mieć kilka sygnatur.

## Zeek scripts

Zeek ma własny język skryptowy

|   |   |
|---|---|
|Zeek has base scripts installed by default, and these are not intended to be modified.|These scripts are located in "/opt/zeek/share/zeek/base".|
|User-generated or modified scripts should be located in a specific path.|These scripts are located in  <br>**"/opt/zeek/share/zeek/site".**|
|Policy scripts are located in a specific path.|These scripts are located in **"/opt/zeek/share/zeek/policy"**.|
|Like Snort, to automatically load/use a script in live sniffing mode, you must identify the script in the Zeek configuration file. You can also use a script for a single run, just like the signatures.|The configuration file is located in "/opt/zeek/share/zeek/site/local.zeek".|
- Zeek scripts use the ".zeek" extension.  
- Do not modify anything under the "zeek/base" directory. User-generated and modified scripts should be in the "zeek/site" directory.
- You can call scripts in live monitoring mode by loading them with the command `load @/script/path` or `load @script-name` in local.zeek file.   
- Zeek is event-oriented, not packet-oriented! We need to use/write scripts to handle the event of interest.

Odpalanie skryptu
`zeek -C -r smallFlows.pcap dhcp-hostname.zeek`

## Pisanie skryptów zeek

```
event zeek_init()
    {
     print ("Started Zeek!");
    }
event zeek_done()
    {
    print ("Stopped Zeek!");
    }
# zeek_init: Do actions once Zeek starts its process. 
# zeek_done: Do activities once Zeek finishes its process. 
# print: Prompt a message on the terminal.
```

Wywołanie da te printy

```
event new_connection(c: connection)
{
	print c;
}
```

Wywołanie da full info o każdym połączeniu.

```
event new_connection(c: connection)
{
	print ("###########################################################");
	print ("");
	print ("New Connection Found!");
	print ("");
	print fmt ("Source Host: %s # %s --->", c$id$orig_h, c$id$orig_p);
	print fmt ("Destination Host: resp: %s # %s <---", c$id$resp_h, c$id$resp_p);
	print ("");
}
```

Wypisze info o konkretnych polach z połączenia.

```
event signature_match (state: signature_state, msg: string, data: string)
{
if (state$sig_id == "ftp-admin")
    {
    print ("Signature hit! --> #FTP-Admin ");
    }
}
```

Można łączyć z sygnaturami

Domyślnie skrypty są w `/opt/zeek/share/zeek/base`, odpalenie ich jest za pomocą `zeek -C -r ftp.pcap local`, gdzie local zadziała jako ten path.

Odpalenie jednego konkretnego z local to już trzeba path podać:
`zeek -C -r ftp.pcap /opt/zeek/share/zeek/policy/protocols/ftp/detect-bruteforcing.zeek`

Odpalanie jednocześnie skryptu i sygnatury na pcap 
`zeek -C -r ftp.pcap -s ftp-admin.sig 201.zeek`

## Zeek scripts frameworks

Zeek ma 15+ frameworków.

Wywołanie frameworka w skrypcie `load @ $PATH/base/frameworks/framework-name`

## Zeek package manager

Ten package manager jest wywoływany jako `zkg`, użycie:

|   |   |
|---|---|
|**Command**|**Description**|
|`zkg install package_path`|Install a package. Example (zkg install zeek/j-gras/zeek-af_packet-plugin).|
|`zkg install git_url`|Install package. Example (zkg install https://github.com/corelight/ztest).|
|`zkg list`|List installed package.|
|`zkg remove`|Remove installed package.|
|`zkg refresh`|Check version updates for installed packages.|
|`zkg upgrade`|Update installed packages.|
Użycie tych paczek:

```
### Calling with script 
ubuntu@ubuntu$ zeek -Cr http.pcap sniff-demo.zeek 

### View script contents 
ubuntu@ubuntu$ cat sniff-demo.zeek 
@load /opt/zeek/share/zeek/site/zeek-sniffpass 

### Calling from path 
ubuntu@ubuntu$ zeek -Cr http.pcap /opt/zeek/share/zeek/site/zeek-sniffpass 

### Calling with package name 
ubuntu@ubuntu$ zeek -Cr http.pcap zeek-sniffpass
```