

|   |   |
|---|---|
|**Alert Report Purpose**|**Explanation**|
|Provide context for escalation|- A well-written report saves lots of time for L2 analysts<br>- Also, it helps them quickly understand what happened|
|Save findings for the records|- Raw SIEM logs are stored for 3-12 months, but alerts are kept indefinitely<br>- As a result, it's better to keep all the context inside the alert, just in case|
|Improve investigation skills|- If you can't explain it simply, you don't understand it well enough<br>- Report writing is a great way to boost L1 skills by summarising alerts|

### Jak opisywać alert

- **Who**: Which user logs in, runs the command, or downloads the file
- **What**: What exact action or event sequence was performed
- **When**: When exactly did the suspicious activity start and ended
- **Where**: Which device, IP, or website was involved in the alert
- **Why**: The most important W, the reasoning for your final verdict


SPF (sender policy framework) - metoda uwierzytelniania maila, sprawdzenia czy jest legitny, może mieć wartość:
- pass - legit
- fail - nie legit - nie uwierzytelniony
- softfail - The server is not listed, but the domain owner allows the message to pass with suspicion (often marked as spam).
- neutral

DKIM (DomainKeys Identified Mail) - coś jak SPF, to jest w DNS jako record w domenie i nagłówek DKIM jest doczepiany do każdego maila z domeny. Używa to klucza publicznego do uwierzytelniania pochodzenia maila. Prywatny klucz jest do podpisu maila. Ten DKIM w DNS to jest TXT record który jest publicznie dostępny.

### Kiedy eskalować alert

1. The alert is an indicator of a major cyberattack requiring deeper investigation or DFIR
2. Remediation actions like malware removal, host isolation, or password reset are required
3. Communication with customers, partners, management, or law enforcement agencies is required
4. You just do not fully understand the alert and need some help from more senior analysts

![](Attatchments/Pasted%20image%2020251109142324.png)

![](Attatchments/Pasted%20image%2020251109142413.png)

