Przykład metryk w SoC

|Metric|Common SLA|Description|
|---|---|---|
|SOC Team Availability|24/7|Working schedule of the SOC team, often Monday-Friday (8/5) or 24/7 mode|
|Mean Time to Detect (MTTD)|5 minutes|Average time between the attack and its detection by SOC tools|
|Mean Time to Acknowledge (MTTA)|10 minutes|Average time for L1 analysts to start triage of the new alert|
|Mean Time to Respond (MTTR)|60 minutes|Average time taken by SOC to actually stop the breach from spreading|
![](Attatchments/Pasted%20image%2020251109153432.png)

### Problemy z metrykami alertów

| Issue                                     | Recommendations                                                                                                                                                                                                                                              |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| False Positive Rate  <br>over 80%         | **Your team receives too much noise in the alerts. Try to:**  <br>  <br>1. Exclude trusted activities like system updates from your EDR or SIEM detection rules  <br>2. Consider automating alert triage for most common alerts using SOAR or custom scripts |
| Mean Time to Detect  <br>over 30 min      | **Your team detects a threat with a high delay. Try to:**  <br>  <br>1. Contact SOC engineers to make the detection rules run faster or with a higher rate  <br>2. Check if SIEM logs are collected in real-time, without a 10-minute delay                  |
| Mean Time to Acknowledge  <br>over 30 min | **L1 analysts start alert triage with a high delay. Try to:**  <br>  <br>1. Ensure the analysts are notified in real-time when a new alert appears  <br>2. Try to evenly distribute alerts in the queue between the analysts on shift                        |
| Mean Time to Respond  <br>over 4 hours    | **SOC team can't stop the breach in time. Try to:**  <br>  <br>1. As L1, make everything possible to quickly escalate the threats to L2  <br>2. Ensure your team has documented what to do during different attack scenarios                                 |