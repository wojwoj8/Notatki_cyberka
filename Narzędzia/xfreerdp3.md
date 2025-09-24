Narzędzie pozwalające na zdalny dostęp do komputera (z gui) za pomocą protokołu RDP. Przydatne w celu połączenia z maszyną Windows na Kali.

Przykład użycia:
```
xfreerdp3 /u:JohnDoe /p:Pwd123! /v:192.168.1.100
```

```
xfreerdp3 /dynamic-resolution +clipboard /cert:ignore /v:10.10.54.14 /u:thm-unpriv /p:'Password321'
```