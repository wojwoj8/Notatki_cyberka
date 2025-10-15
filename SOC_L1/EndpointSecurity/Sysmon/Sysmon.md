Sysmon to usługa windows i sterownik który zbiera logi z aktywności systemu.

Eventy sysmona są w  `Event Viewer Applications and Services Logs/Microsoft/Windows/Sysmon/Operational`

Sysmona trzeba skonfigurować i podać własne zasady co ma być logowane, często więcej jest wyjatków logowania żeby sysmon nie zapisywał codziennej aktywności.

[SwiftOnSecurity sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) - polecany konfig sysmona

Sysmon jest w sysinternals - pobieranie przez PS `Download-SysInternalsTools C:\Sysinternals`

Odpalenie sysmona z tym Swift configiem: `Sysmon.exe -accepteula -i ..\Configurations\swift.xml`

Można użyć `Get-WinEvent` albo `wevutil.exe` do filtrowania logów.

[Porty z malware](https://docs.google.com/spreadsheets/d/17pSTDNpa0sf6pHeRhusvWG6rThciE8CsXTSlDUAZDyo/edit?gid=0#gid=0) 

Mimkatz - narzędzie do dumpowania credentialsów z ramu wraz z innymi winodws post-exploitation activities. Mimikatz is mainly known for dumping LSASS

Jak LSASS is accessed przez process inny niż svchost.exe to jest to sus.