Działanie maili

![](Attatchments/Pasted%20image%2020251110194914.png)
1. Alexa composes an email to Billy (`billy@johndoe.com`) in her favorite email client. After she's done, she hits the send button.
2. The **SMTP** server needs to determine where to send Alexa's email. It queries **DNS** for information associated with `johndoe.com`. 
3. The **DNS** server obtains the information `johndoe.com` and sends that information to the **SMTP** server. 
4. The **SMTP** server sends Alexa's email across the Internet to Billy's mailbox at `johndoe.com`.
5. In this stage, Alexa's email passes through various **SMTP** servers and is finally relayed to the destination **SMTP** server. 
6. Alexa's email finally reached the destination **SMTP** server.
7. Alexa's email is forwarded and is now sitting in the local **POP3/IMAP** server waiting for Billy. 
8. Billy logs into his email client, which queries the local **POP3/IMAP** server for new emails in his mailbox.
9. Alexa's email is copied (**IMAP**) or downloaded (**POP3**) to Billy's email client.

### Email header


1. **X-Originating-IP** - The IP address of the email was sent from (this is known as an **[X-header](https://help.returnpath.com/hc/en-us/articles/220567127-What-are-X-headers-)**)
2. **Smtp.mailfrom**/**header.from** - The domain the email was sent from (these headers are within **Authentication-Results**)
3. **Reply-To** - This is the email address a reply email will be sent to instead of the **From** email address

### Typy phishingu

- **[Spam](https://www.proofpoint.com/us/threat-reference/spam)** - unsolicited junk emails sent out in bulk to a large number of recipients. The more malicious variant of Spam is known as **MalSpam**.
- **[Phishing](https://www.proofpoint.com/us/threat-reference/phishing)** -  emails sent to a target(s) purporting to be from a trusted entity to lure individuals into providing sensitive information. 
- **[Spear phishing](https://www.proofpoint.com/us/threat-reference/spear-phishing) -** takes phishing a step further by targeting a specific individual(s) or organization seeking sensitive information.  
- **[Whaling](https://www.rapid7.com/fundamentals/whaling-phishing-attacks/)** - is similar to spear phishing, but it's targeted specifically to C-Level high-position individuals (CEO, CFO, etc.), and the objective is the same. 
- [**Smishing**](https://www.proofpoint.com/us/threat-reference/smishing) - takes phishing to mobile devices by targeting mobile users with specially crafted text messages. 
- [**Vishing**](https://www.proofpoint.com/us/threat-reference/vishing) - is similar to smishing, but instead of using text messages for the social engineering attack, the attacks are based on voice calls.

### Często w mailach phishingowych

- The **sender email name/address** will masquerade as a trusted entity (**[email spoofing](https://www.proofpoint.com/us/threat-reference/email-spoofing)**)
- The email subject line and/or body (text) is written with a **sense of urgency** or uses certain keywords such as **Invoice**, **Suspended**, etc. 
- The email body (HTML) is designed to match a trusting entity (such as Amazon)
- The email body (HTML) is poorly formatted or written (contrary from the previous point)
- The email body uses generic content, such as Dear Sir/Madam. 
- **Hyperlinks** (oftentimes uses URL shortening services to hide its true origin)
- A [malicious attachment](https://www.proofpoint.com/us/threat-reference/malicious-email-attachments) posing as a legitimate document


### Narzędzia

Do analizy nagłówków SMTP:
- **Messageheader**: [https://toolbox.googleapps.com/apps/messageheader/analyzeheader](https://toolbox.googleapps.com/apps/messageheader/analyzeheader)
- **Message Header Analyzer**: [https://mha.azurewebsites.net/](https://mha.azurewebsites.net/)
- [mailheader.org](https://mailheader.org/)

Do analizy sender's IP: 
- IPinfo.io: [https://ipinfo.io/](https://ipinfo.io/)
- URLScan.io: [https://urlscan.io/](https://urlscan.io/) - to też url.

Reputacja strony:
- Talos Reputation Center: [https://talosintelligence.com/reputation](https://talosintelligence.com/reputation)

Wyciąganie url z body maili:
- URL Extractor: [https://www.convertcsv.com/url-extractor.htm](https://www.convertcsv.com/url-extractor.htm)
- [CyberChef](https://gchq.github.io/CyberChef/)

Warto jeszcze przeskanować root domain.

Jak w mailu są attatchmentsy to trzeba wyciągnąć hash i sprawdzić np.
- Talos File Reputation: [https://talosintelligence.com/talos_file_reputation](https://talosintelligence.com/talos_file_reputation)
- VirusTotal: [https://www.virustotal.com/gui/](https://www.virustotal.com/gui/)


### Malware sandboxes

- Any.Run: [https://app.any.run/](https://app.any.run/)
- Hybrid Analysis: [https://www.hybrid-analysis.com/](https://www.hybrid-analysis.com/)
- [https://www.joesecurity.org/](https://www.joesecurity.org/)

Dedykowane narzędzie do phishingu: [PhishTool](https://www.phishtool.com/).

