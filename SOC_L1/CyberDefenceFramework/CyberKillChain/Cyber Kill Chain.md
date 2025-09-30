Cyber Kill Chain opisuje fazy ataku na cel. Obejmuje on:
- Reconnaissance
- Weaponization
- Delivery
- Exploitation
- Installation
- Command & Control
- Actions on Objectives

## 1. Reconnaissance
Jest to odkrywanie informacji o celu. Obejmuje między innymi OSINT.
Przydatne źródła:
- [theHarvester](https://github.com/laramies/theHarvester) - other than gathering emails, this tool is also capable of gathering names, subdomains, IPs, and URLs using multiple public data sources 
- [Hunter.io](https://hunter.io/) - this is  an email hunting tool that will let you obtain contact information associated with the domain
- [OSINT Framework](https://osintframework.com/) - OSINT Framework provides the collection of OSINT tools based on various categories
## 2. Weaponization

W tej fazie po wstępnym rozpoznaniu celu przygotowuje się malware, backdor albo inny exploit, payload do w celu ataku.

## 3. Delivery
Ta faza polega na dostarczeniu tego malware. Może to być przez email, zainfekowany USB, czy Wattering hole attack - przejęcie strony internetowej z której korzysta cel a następnie przekierowanie z niej do własnej strony z której może zostać wgrany malware.

## 4. Exploitation
Uruchomienie malware na celu po dostarczenu.

## 5. Installation
Instalacja backdoora na systemie, reverse shell, web-shell.

## 6. Command & Control
Ustalenie komunikacji z celem w celu zarządzania systemem.

## 7. Actions on Objectives
Wykonanie celu jak wykradnięcie danych, zbieranie informacji o celu, przechodzenie na inne systemy w sieci itp.