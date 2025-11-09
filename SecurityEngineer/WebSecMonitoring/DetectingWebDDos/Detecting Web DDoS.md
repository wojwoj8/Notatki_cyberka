
Rodzaje ataków DDoS

|DoS Attack Type|Description|
|---|---|
|Slowloris|Sending many partial HTTP requests to tie up server resources|
|HTTP Flood|Sending a large number of HTTP requests to overwhelm the server|
|Cache Bypass|Bypassing CDN edge servers and forcing the origin server to respond|
|Oversized Query|Forcing the server to process large, resource-intensive requests|
|Login/Form Abuse|Overloading authentication logic with login attempts or password resets|
|Faulty Input Validation Abuse|Exploiting poorly designed input handling|

Indykatory ataków

|Indicator|Example|Description|
|---|---|---|
|High Request Rate|`10.10.10.100` → 1000 `GET /login`|A resource-heavy page like `/login` is flooded with requests to overwhelm authentication processes. Login pages are common targets since each request may trigger password checks and database queries|
|Odd User-Agents|`curl/7.6.88` → `/index` repeatedly|Attackers spoof outdated or unusual User-Agents to blend in or bypass filters. Spotting traffic with tools like `curl` or `Python-urllib/3.x`, for example, can be a red flag for automated attacks|
|Geographic Anomalies|IP address origins dotted around the world|Legitimate traffic typically comes from a few regions where real users are located. A globally distributed botnet may utilize IP addresses from around the world|
|Burst Timestamps|50 requests in 1 second → `/search`|A sudden spike of requests packed into the same second creates an unnatural traffic pattern that points to automation|
|Server Errors ([5xx](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status#server_error_responses))|A significant spike of `503 Service Unavailable` errors|A sudden surge of server error responses (`500` - `511`) indicates resources are maxed out and the service is struggling under attack traffic|
|Logic Abuse|`GET /products?limit=999999`|Attackers craft queries that overload the server, forcing it to load huge amounts of information and slowing it down for everyone|