Można wyświetlić pod domeny, które nie są dostępne publicznie w DNS. Odkryć je można za pomocą fuzzingu narzędziem takim jak ffuf.

``` zsh
ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://MACHINE_IP
```

To zwróci listę pod domen dopasowanych i niedopasowanych. Żeby pozbyć się tych niedopasowanych można zrobić tak:

``` zsh
ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://MACHINE_IP -fs {size}
```

zamiast size trzeba podać długość tego niedopasowanego, żeby się nie wyświetlało.