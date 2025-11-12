Diagram działania SPF (Sender policy framework)
![](Attatchments/Pasted%20image%2020251112110241.png)

|Verification Result|Intended Action|
|---|---|
|Pass, Neutral, None|Accept (Allow and process the email)|
|SoftFail, PermError|Flag (Mark as suspicious but allow)|
|Fail, TempError|Reject (Immediately discard the email)|

### SPF Record

`v=spf1 ip4:127.0.0.1 include:_spf.google.com -all`

- `v=spf1` Signifies the start of the SPF record
- `ip4:127.0.0.1` Specifies which IP can send mail (IPv4 in this case)
- `include:_spf.google.com` Specifies which domain can send mail
- `-all` Non-authorized emails will be rejected

**[SPF Surveyor](https://dmarcian.com/spf-survey/)** - pozwala na wpisanie domeny i sprawdzenie zapytań SPF.

## DKIM

**DomainKeys Identified Mail** (**[DKIM](https://dmarcian.com/what-is-dkim/)**) - used for the authentication of an email that's being sent.  A DKIM record exists in the DNS, but it is more complex than SPF. DKIM’s advantage is that it can survive forwarding.

### DKIM record

`v=DKIM1; k=rsa; p=<public_key>`

- `v=DKIM1` Specifies the version of DKIM being used (optional)
- `k=rsa` The key type. The RSA encryption algorithm is standard
- `p=` This is the public key that will be matched to the private key to verify the DKIM signature

Wystąpienie błędu permerror oznacza, że mógł być problem z niepoprawną sygnaturą, brakującym lub niepoprawnym DNS.

## **Domain-Based Message Authentication, Reporting, and Conformance**

“DMARC, an open source standard, uses a concept called alignment to tie the result of two other open source standards,  SPF (a published list of servers that are authorized to send email on behalf of a domain) and DKIM (a tamper-evident domain seal associated with a piece of email), to the content of an email.”


### DMARC Record

`v=DMARC1; p=quarantine; rua=mailto:postmaster@website.com`

- `v=DMARC1`: The version of DMARC (required)
- `p=quarantine` The DMARC policy (quarantine = move to the spam folder)
- `rua=mailto:postmaster@website.com` An optional tag. In this case, aggregate reports will be sent to the email specified

Narzędzie do sprawdzania DMACRm SPF i DKIM dla domen - [tool](https://dmarcian.com/domain-checker/)

### S/MIME

**Secure/Multipurpose Internet Mail Extensions** ([**S/MIME**](https://learn.microsoft.com/en-us/exchange/security-and-compliance/smime-exo/smime-exo)) is a standard protocol for sending digitally signed and encrypted messages.

S/MIME dzieli się na 2 główne komponenty:

Digital signatures:
- Authentication: Confirms the sender's identity through their digital certificate
- Non-repudiation: Ensures the sender cannot deny sending the message
- Data Integrity: Detects any changes to the message after it's signed

Encryption:
- Confidentiality: Keeps the content private and readable only by the intended recipient
- Data Integrity: Detects any changes during message transmission

Przykład użycia:
- If Bob wishes to use S/MIME, then he'll need a digital certificate. This digital certificate will contain his public key. 
- With this digital certificate, Bob can "sign" the email message with his private key. 
- Mary can then decrypt Bob's message with Bob's public key. 
- Mary will do the same (send her certificate to Bob) when she replies to his email, and Bob will complete the same process on his end.
- Both Bob and Mary will now have each other's certificates for future correspondence.

### Metody na obronę przed phishingiem

- [**Email Filtering**](https://www.spamhaus.org/resource-hub/ip-domain-reputation/): Provides filtering based on IP and domain reputation, allowing for blocking or quarantining of suspicious messages.
- [**Secure Email Gateways**](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/) (SEGs): Scan messages to detect impersonation attempts, spoofing, and other phishing techniques that other filters might miss.
- [**Link Rewriting**](https://learn.microsoft.com/en-us/defender-office-365/safe-links-about): Replaces suspicious or unknown URLs with safe, redirected ones, giving the system time to scan and verify the link.
- [**Sandboxing**](https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-about): Isolates and tests suspicious links or attachments in a secure, virtual environment to check for malicious behavior.