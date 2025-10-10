
Ważne podczas korzystania z funkcji z wiresharka:
- Opcje działają dla wszystkich pakietów jeżeli nie ma ustawionych filtrów
- wykorzystanie poleceń da ich opis po wywołaniu: `psh` polecenie da nagłówek z odpowiedzią "Packet Hierarchy Statistics"

|   |   |
|---|---|
|**Parameter**|**Purpose**|
|--color|- Wireshark-like colourised output.<br>- `tshark --color`|
|-z|- Statistics<br>- There are multiple options available under this parameter. You can view the available filters under this parameter with:<br><br>- `tshark -z help`<br><br>- Sample usage.<br><br>- `tshark -z filter`<br><br>- Each time you filter the statistics, packets are shown first, then the statistics provided. You can suppress packets and focus on the statistics by using the `-q` parameter.|

|   |   |
|---|---|
|**Filter**|**Purpose**|
|eth|- Ethernet addresses|
|ip|- IPv4 addresses|
|ipv6|- IPv6 addresses|
|tcp|- TCP addresses<br>- Valid for both IPv4 and IPv6|
|udp|- UDP addresses<br>- Valid for both IPv4 and IPv6|
|wlan|- IEEE 802.11 addresses|

|   |   |
|---|---|
|**Filter**|**Details**|
|**Contains**|- Search a value inside packets.<br>- Case sensitive.<br>- Similar to Wireshark's "find" option.|
|**Matches**|- Search a pattern inside packets.<br>- Supports regex.<br>- Case insensitive.<br>- Complex queries have a margin of error.|

|   |   |   |
|---|---|---|
|**Main Filter**|**Target Field**|**Show Field Name**|
|-T fields|-e <field name>|-E header=y|

Filter: "contains"

|             |                                                                                                                                              |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Filter      | contains                                                                                                                                     |
| Type        | Comparison operator                                                                                                                          |
| Description | Search a value inside packets. It is case-sensitive and provides similar functionality to the "Find" option by focusing on a specific field. |
| Example     | Find all "Apache" servers.                                                                                                                   |
| Workflow    | List all HTTP packets where the "server" field contains the "Apache" keyword.                                                                |
| Usage       | `http.server contains "Apache"`                                                                                                              |

Filter: "matches"

|   |   |
|---|---|
|Filter|matches|
|Type|Comparison operator|
|Description|Search a pattern of a regular expression. It is case-insensitive, and complex queries have a margin of error.|
|Example|Find all .php and .html pages.|
|Workflow|List all HTTP packets where the "request method" field matches the keywords "GET" or "POST".|
|Usage|`http.request.method matches "(GET\|POST)"`|

|                                                                |                                                                                     |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Query**                                                      | **Purpose**                                                                         |
| `tshark -r hostnames.pcapng -T fields -e dhcp.option.hostname` | Main query.  <br>Extract the DHCP hostname value.                                   |
| `awk NF`                                                       | Remove empty lines.                                                                 |
| `sort -r`                                                      | Sort recursively before handling the values.                                        |
| `uniq -c`                                                      | Show unique values, but calculate and show the number of occurrences.               |
| `sort -r`                                                      | The final sort process.  <br>Show the output/results from high occurrences to less. |