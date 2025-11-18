
### Techniki i wskaźniki ataków

| Techniques                        | Examples                                                                                                                                                                                                    | Indicator of Attack & where to look                                                                                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Network-based**                 | HTTP/HTTPS uploads to S3/Azure Blob/webmail, FTP/SFTP/SCP, DNS tunnelling, ICMP/covert protocols, custom TCP/UDP.                                                                                           | Proxy/web gateway logs (large POSTs, uploads to cloud endpoints), firewall/NGFW flows (high bytes to single IP/ASN), netflow (spikes/outbound flows), DNS logs (long hostnames, TXT queries). |
| **Host-based**                    | Powershell/Invoke-WebRequest, rclone, awscli, curl/wget, archive creation (zip/rar), use of removable USBs, ADS/hidden streams.                                                                             | Sysmon/EDR (Process Create, Network Connect, File Create events), Windows Security (4663/4656 object access), auditd/shell history on Linux, and removable-media events.                      |
| **Cloud exfiltration**            | S3 PutObject / multipart upload, Azure Blob uploads, Google Cloud Storage objects. Insert, Drive/SharePoint external sharing.                                                                               | CloudTrail / Azure Activity / GCP Audit, cloud storage access logs, unusual service-account or IP activity.                                                                                   |
| **Covert & encoding**             | DNS tunnelling, base64 or chunked encoding, steganography into images/audio, splitting files into many small requests (low-and-slow).                                                                       | DNS logs, proxy logs with many small POSTs, correlation of intermittent uploads + suspicious process activity.                                                                                |
| **Insider & collaboration tools** | Slack/Teams/Dropbox/Google Drive/Box uploads or sharing to external users; compromised employee accounts.                                                                                                   | Audit logs (share events, file downloads), and mail logs.                                                                                                                                     |
| **General IoAs & triage signals** | A large outbound volume to external IPs/domains, unknown destination domains, suspicious processes/command lines, many file read events followed by an outbound connection, and multipart/streamed uploads. | Correlate: Proxy/Firewall/Netflow, DNS, Sysmon/EDR (EventID 1/3/11), mail server logs.                                                                                                        |

### Wskaźniki ataku dns tunneling

- Many DNS queries are sent to a single external domain, especially with very high counts compared to the baseline.
- Long subdomain labels or unusually long full query names (> 60–100 characters).
- High entropy or Base32/Base64-like patterns in the query name (lots of mixed case letters, digits, `-`, `=` signs for base64).
- Rare record types (TXT, NULL) or many large TXT responses.
- Unusual response behavior: frequent NXDOMAIN (if attacker uses exfil-by-query without answering), or TCP/large UDP fragments for DNS.
- Queries at regular intervals (beaconing behaviour).

### IoA FTP

- `USER` and `PASS` commands (cleartext credentials).
- `STOR` (upload) and `RETR` (download) commands: repeated or large transfers.
- Large data connections to unusual external IPs, especially outside business hours.
- Data channel openings on ephemeral ports (PASV) paired with large payloads.


### Wykorzystanie HTTP przez hackerów

- **POST uploads to external servers**: Bulk data is sent to attacker-controlled hosts or cloud storage in POST request bodies.
- **GET requests with encoded data**: Attacker squeezes small chunks into query strings or path segments (useful for low-and-slow exfiltration).
- **Use of common services / CDN**: Exfiltration disguised as uploads to popular services or attacker-controlled subdomains under reputable domains.
- **Custom headers**: Data placed in headers (e.g., `X-Data: <base64>`) may bypass some string-based DLP.
- **Chunked transfer / multipart**: Large payloads split into multiple requests to avoid size thresholds.
- **HTTPS/TLS tunneling**: The encrypted channel hides the payload; detection requires TLS inspection, SNI analysis, or metadata-based detection.
- **Staging via cloud services**: The attacker uploads to Dropbox/GitHub/Gist and then fetches externally.

### HTTP IoA

- Unusually large HTTP POST requests to external/unexpected hosts.
- HTTP requests to domains with low reputation / rarely seen in baseline traffic.
- Frequent small requests (beaconing) to the same host, followed by large uploads.
- Chunked or multipart transfers where multiple requests compose a larger file.

### Exfiltracja przez ICMP

- ICMP echo (type 8) / reply (type 0) tunneling: attackers place encoded (base64, hex) chunks of files inside ICMP payloads. The remote server collects and decodes them.
- Custom ICMP types/codes: using uncommon ICMP types or non-zero codes to avoid signature-based detections.
- Fragmentation and reassembly: large payloads are split across multiple packets.
- Encryption/obfuscation: Encrypting or encrypting payloads (base64 is common) to look like random data.

### ICMP IoA

- Persistent ICMP sessions to an external host not used for legitimate monitoring.
- Unusually large ICMP payloads or frequent ICMP with payload > typical ping size (ping jest około 74 bajtów).
- ICMP payloads that contain high-entropy data or patterns consistent with base64/hex.
- Bursts of ICMP are immediately followed by no other legitimate application traffic from the same host.